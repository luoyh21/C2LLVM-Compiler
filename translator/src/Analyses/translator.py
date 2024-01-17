from antlr4 import *
from antlr.clongParser import clongParser
from antlr.clongVisitor import clongVisitor
from antlr.clongLexer import clongLexer
from Analyses.config import *
import os
from llvmlite import ir
from Analyses.symbol_table import SymbolTable

class Visitor(clongVisitor):
    # 进行语义分析，并转换为目标语言(LLVM)
    def __init__(self):
        super(clongVisitor, self).__init__()
        self.Module=ir.Module("clong prog")
        self.Module.triple = "x86_64-pc-linux-gnu"
        self.Module.data_layout = "e-m:o-i64:64-f80:128-n8:16:32:64-S128"
        
        # 语句块
        self.Blocks: list[ir.Block] = []

        # 生成栈
        self.Builders: list[ir.IRBuilder] = []

        # 函数列表
        self.Functions = dict()

        # 符号栈
        self.SymbolTable = SymbolTable()

        # 条件结束块
        self.EndIfBlock = None

        # 常量索引
        self.ConstantIndex = 0
        
    def visitProg(self,ctx:clongParser.ProgContext):
        '''
        语法：prog:head main;
        作用：处理prog（全代码）
        '''
        # 不支持引用库文件
        print("正在分析prog")
        self.visitMain(ctx.main())
        print("分析完成!")
        
    def visitMain(self,ctx:clongParser.MainContext):
        '''
        语法：main:('int'|'void') 'main''()''{' body '}';
        描述：处理main函数
        '''
        #LLVM函数定义
        print("正在分析main")
        IRType=ir.FunctionType(int32,[])
        IRFunc=ir.Function(self.Module,IRType,"main")
        
        #LLVM函数块
        mainBlock=IRFunc.append_basic_block("main.entry")
        mainBuilder=ir.IRBuilder(mainBlock)

        #LLVM函数块入栈
        self.Blocks.append(mainBlock)
        self.Builders.append(mainBuilder)
        self.SymbolTable.push()
        
        #处理main函数体
        self.visitBody(ctx.body())

        #LLVM函数块出栈
        self.Blocks.pop()
        self.Builders.pop()
        self.SymbolTable.pop()
        
        return
    
    def visitBody(self,ctx:clongParser.BodyContext):
        '''
        语法：body:(func';'|block)*;
        描述：处理函数体
        '''
        print(ctx.getText())
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))
            if self.Blocks[-1].is_terminated:
                break
        return

    def visitFunc(self,ctx:clongParser.FuncContext):
        '''
        语法：func:(printf|gets|strlen|returnFunc);
        描述：处理单行函数调用
        '''
        return self.visit(ctx.getChild(0))
        
    def visitStrlen(self, ctx: clongParser.StrlenContext):
        """
        语法：strlen:'strlen''('paramName')';
        描述：处理strlen函数调用
        """
        # 检测函数是否已经定义
        if 'strlen' in self.Functions:
            strlenFunc = self.Module.globals['strlen']
        else:
            strlenType = ir.FunctionType(int32, [int8.as_pointer()])
            strlenFunc = ir.Function(self.Module, strlenType, 'strlen')
            self.Functions['strlen'] = strlenFunc

        currentBuilder = self.Builders[-1]

        strName = self.visit(ctx.paramName())
        strPtr = self.SymbolTable.getItem(strName)[1]

        Argument = currentBuilder.gep(strPtr, [int32(0), int32(0)])
        strlen = currentBuilder.call(strlenFunc, [Argument])

        return strlen
        
    def visitPrintf(self, ctx: clongParser.PrintfContext):
        """
        语法：printf: 'printf' '(' ((stringm | paramName) (',' exp)*) ')';
        描述：处理printf函数调用
        """
        if 'printf' in self.Functions:
            printfFunc = self.Module.globals['printf']
        else:
            printfType = ir.FunctionType(int32, [ir.PointerType(int8)], var_arg=True)
            printfFunc = ir.Function(self.Module, printfType, 'printf')
            self.Functions['printf'] = printfFunc

        currentBuilder = self.Builders[-1]
        zero = ir.Constant(int32, 0)

        # 处理字符串
        if isinstance(ctx.getChild(2), clongParser.StringmContext):
            strPtr = self.visit(ctx.getChild(2))
            strPtr = currentBuilder.gep(strPtr, [zero, zero], inbounds=True)
        # 处理变量  
        else:
            strName = self.visit(ctx.getChild(2))
            strPtr = self.SymbolTable.getItem(strName)[1]

        # 处理参数
        Arguments = [strPtr]
        length = ctx.getChildCount()
        currentNumber = 4
        while currentNumber < length - 1:
            Arguments.append(self.visit(ctx.getChild(currentNumber)))
            currentNumber += 2

        rtn = currentBuilder.call(printfFunc, Arguments)

        return rtn


    def visitGets(self, ctx: clongParser.GetsContext):
        """
        语法：gets:'gets''('paramName')';
        描述：处理gets函数调用
        """
        if 'gets' in self.Functions:
            getsFunc = self.Module.globals['gets']
        else:
            getsType = ir.FunctionType(int8.as_pointer(), [int8.as_pointer()])
            getsFunc = ir.Function(self.Module, getsType, 'gets')
            self.Functions['gets'] = getsFunc

        currentBuilder = self.Builders[-1]
        zero = ir.Constant(int32, 0)

        strName = self.visit(ctx.paramName())
        strPtr = self.SymbolTable.getItem(strName)[1]
        Arguments = [currentBuilder.gep(strPtr, [zero, zero], inbounds=True)]

        rtn = currentBuilder.call(getsFunc, Arguments)
        return rtn
        
    def visitReturnFunc(self, ctx: clongParser.ReturnFuncContext):
        """
        语法：returnFunc:'return'(intm)?;
        描述：处理return退出
        """
        currentBuilder = self.Builders[-1]
        if ctx.getChildCount() > 1:
            ret = self.visit(ctx.getChild(1))
            currentBuilder.ret(ret)
        else:
            currentBuilder.ret_void()
    
    def visitBlock(self, ctx: clongParser.BlockContext):
        """
        语法：block:ifElse|whileFunc|forFunc|initParam|initArray|assign;
        描述：处理语句块
        """
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        
    def visitIfElse(self, ctx: clongParser.IfElseContext):
        """
        语法：ifElse:ifFunc(elseif)*(elseFunc)?;
        描述：处理整个if-elseif-else语句块
        """
        # 当前整个块的Builder
        IfBuilder = self.Builders[-1]  
        # 给这个块加两个分支，分别是各种条件和结束 
        IfBlock = IfBuilder.append_basic_block()
        EndIfBlock = IfBuilder.append_basic_block()
        # 切换到IfBlock
        IfBuilder.branch(IfBlock)

        # 把之前的块出栈
        self.Blocks.pop()
        self.Builders.pop()

        # 把新的块入栈
        self.Blocks.append(IfBlock)
        self.Builders.append(ir.IRBuilder(IfBlock))

        # 处理if部分
        # 暂存下一个
        temp = self.EndIfBlock
        self.EndIfBlock = EndIfBlock
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        # 恢复
        self.EndIfBlock = temp

        # 导向endif
        blockTemp = self.Blocks.pop()
        builderTemp = self.Builders.pop()
        if not blockTemp.is_terminated:
            builderTemp.branch(EndIfBlock)

        self.Blocks.append(EndIfBlock)
        self.Builders.append(ir.IRBuilder(EndIfBlock))

        
    def visitIfFunc(self, ctx: clongParser.IfFuncContext):
        """
        语法：ifFunc:'if' '('condition')''{'body'}';
        描述：处理if部分
        """
        self.SymbolTable.push()
        currentBuilder = self.Builders[-1]
        TrueBlock = currentBuilder.append_basic_block("if.true")
        FalseBlock = currentBuilder.append_basic_block("if.false")

        result = self.visit(ctx.condition())
        currentBuilder.cbranch(result, TrueBlock, FalseBlock)

        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(TrueBlock)
        self.Builders.append(ir.IRBuilder(TrueBlock))
        self.visit(ctx.body())

        if not self.Blocks[-1].is_terminated:
            self.Builders[-1].branch(self.EndIfBlock)

        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(FalseBlock)
        self.Builders.append(ir.IRBuilder(FalseBlock))
        
        self.SymbolTable.pop()

        
    def visitElseif(self, ctx: clongParser.ElseifContext):
        """
        语法：elseif:'else''if''('condition')''{'body'}';
        描述：处理elseif部分
        """
        self.SymbolTable.push()
        currentBuilder = self.Builders[-1]
        TrueBlock = currentBuilder.append_basic_block()
        FalseBlock = currentBuilder.append_basic_block()

        result = self.visit(ctx.condition())
        currentBuilder.cbranch(result, TrueBlock, FalseBlock)

        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(TrueBlock)
        self.Builders.append(ir.IRBuilder(TrueBlock))
        self.visit(ctx.body())

        if not self.Blocks[-1].is_terminated:
            self.Builders[-1].branch(self.EndIfBlock)

        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(FalseBlock)
        self.Builders.append(ir.IRBuilder(FalseBlock))
        self.SymbolTable.pop()

        
    def visitElseFunc(self, ctx: clongParser.ElseFuncContext):
        """
        语法：elseFunc:'else''{'body'}';
        描述：处理else部分
        """
        self.SymbolTable.push()
        self.visit(ctx.body())
        self.SymbolTable.pop()
    
    def visitWhileFunc(self, ctx: clongParser.WhileFuncContext):
        """
        语法：whileFunc:'while''('exp')''{'body'}';
        描述：处理while语句块
        """
        self.SymbolTable.push()
        currentBuilder = self.Builders[-1]
        WhileConditionBlock = currentBuilder.append_basic_block()
        WhileBodyBlock = currentBuilder.append_basic_block()
        WhileEndBlock = currentBuilder.append_basic_block()

        currentBuilder.branch(WhileConditionBlock)
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(WhileConditionBlock)
        self.Builders.append(ir.IRBuilder(WhileConditionBlock))

        result = self.visit(ctx.condition())
        self.Builders[-1].cbranch(result, WhileBodyBlock, WhileEndBlock)

        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(WhileBodyBlock)
        self.Builders.append(ir.IRBuilder(WhileBodyBlock))
        self.visit(ctx.body())
        currentBuilder.branch(WhileConditionBlock)

        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(WhileEndBlock)
        self.Builders.append(ir.IRBuilder(WhileEndBlock))
        self.SymbolTable.pop()

        
    def visitForFunc(self, ctx: clongParser.ForFuncContext):
        """
        语法：forFunc:'for''('initFunc';'exp';'assignFunc')''{'body'}';
        描述：处理整个for语句块
        """
        self.SymbolTable.push()
        # 初始化
        self.visit(ctx.initFunc())

        currentBuilder = self.Builders[-1]
        ForConditionBlock = currentBuilder.append_basic_block()
        ForBodyBlock = currentBuilder.append_basic_block()
        ForEndBlock = currentBuilder.append_basic_block()

        currentBuilder.branch(ForConditionBlock)
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(ForConditionBlock)
        self.Builders.append(ir.IRBuilder(ForConditionBlock))

        result = self.visit(ctx.condition())
        self.Builders[-1].cbranch(result, ForBodyBlock, ForEndBlock)
        
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(ForBodyBlock)
        self.Builders.append(ir.IRBuilder(ForBodyBlock))
        self.visit(ctx.body())
        self.visit(ctx.assignFunc())
        self.Builders[-1].branch(ForConditionBlock)

        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(ForEndBlock)
        self.Builders.append(ir.IRBuilder(ForEndBlock))
        self.SymbolTable.pop()
        
        
    def visitInitFunc(self, ctx: clongParser.InitFuncContext):
        """
        语法：initFunc: (typeParam)? paramName ('=' exp)?(','initFunc)?|;
        描述：处理for循环中的初始化部分
        """
        if ctx.getChildCount() > 0:
            # 如果有类型
            child = ctx.getChild(0)
            if isinstance(child, clongParser.TypeParamContext):
                typeParam = self.visit(child)
                paramName = self.visit(ctx.getChild(1))
                # 创建变量
                ptr = self.Builders[-1].alloca(typeParam, name=paramName)
                self.SymbolTable.addItem(paramName, (typeParam, ptr))
                # 如果有赋值
                if ctx.getText().find('=') != -1:
                    val = self.visit(ctx.getChild(3))
                    self.Builders[-1].store(val, ptr)
                else:
                    # 初始化为0
                    self.Builders[-1].store(int32(0), ptr)
            else:
                # 如果没有类型
                paramName = self.visit(ctx.getChild(0))
                ptr = self.SymbolTable.getItem(paramName)[1]
                # 如果有赋值
                if ctx.getText().find('=') != -1:
                    val = self.visit(ctx.getChild(2))
                    self.Builders[-1].store(val, ptr)
                else:
                    # 初始化为0
                    self.Builders[-1].store(int32(0), ptr)
            # 如果有下一个
            if ctx.getText().find(',') != -1:
                self.visit(ctx.getChild(ctx.getChildCount() - 1))
        
    def visitAssignFunc(self, ctx: clongParser.AssignFuncContext):
        """
        语法：assignFunc:paramName '=' exp(','assignFunc)?|;
        描述：处理for循环中的赋值部分
        """
        paramName = self.visit(ctx.getChild(0))
        ptr = self.SymbolTable.getItem(paramName)[1]
        val = self.visit(ctx.getChild(2))
        self.Builders[-1].store(val, ptr)

        if ctx.getText().find(',') != -1:
            self.visit(ctx.getChild(ctx.getChildCount() - 1))
        
    def visitInitParam(self, ctx: clongParser.InitParamContext):
        """
        语法：initParam:typeParam paramName ('=' exp)?(','paramName ('=' exp)?)*';';
        描述：处理变量初始化
        """
        paramType = self.visit(ctx.typeParam()) 
        
        length = ctx.getChildCount()

        currentNumber = 1
        while currentNumber < length:
            paramName = self.visit(ctx.getChild(currentNumber))
            currentBuilder = self.Builders[-1]
            ptr = currentBuilder.alloca(paramType)
            self.SymbolTable.addItem(paramName, (paramType, ptr))

            if ctx.getChild(currentNumber + 1).getText() == '=':
                val = self.visit(ctx.getChild(currentNumber + 2))
                currentBuilder.store(val, ptr)
                currentNumber += 4
            else:
                # 储存对应的类型的0
                if paramType == int32:
                    currentBuilder.store(int32(0), ptr)
                elif paramType == int8:
                    currentBuilder.store(int8(0), ptr)
                elif paramType == double:
                    currentBuilder.store(double(0), ptr)
                elif paramType == int8.as_pointer():
                    currentBuilder.store(int8.as_pointer()(0), ptr) 
                elif paramType == int32.as_pointer():
                    currentBuilder.store(int32.as_pointer()(0), ptr)
                elif paramType == double.as_pointer():
                    currentBuilder.store(double.as_pointer()(0), ptr)
                currentNumber += 2
        
    def visitInitArray(self, ctx: clongParser.InitArrayContext):
        """
        语法：initArray:typeParam paramName '[' intm ']'';';
        描述：处理数组初始化
        """
        paramType = self.visit(ctx.typeParam())
        paramName = self.visit(ctx.paramName())
        length = int(ctx.intm().getText())

        currentBuilder = self.Builders[-1]
        ptr = currentBuilder.alloca(ir.ArrayType(paramType, length), name=paramName)
        self.SymbolTable.addItem(paramName, (ir.ArrayType(paramType, length), ptr))

        
    def visitAssign(self, ctx: clongParser.AssignContext):
        """
        语法：assign:(((paramName|array)'=')+exp)';';
        描述：处理变量和数组赋值
        """
        currentBuilder = self.Builders[-1]
        length = ctx.getChildCount()
        currentNumber = 0
        exptr = self.visit(ctx.getChild(length - 2))
        while currentNumber < length - 2:
            child = ctx.getChild(currentNumber)
            if isinstance(child, clongParser.ParamNameContext):
                paramName = self.visit(child)
                ptr = self.SymbolTable.getItem(paramName)[1]
                currentBuilder.store(exptr, ptr)
            elif isinstance(child, clongParser.ArrayContext):
                ptr = self.visit(child)
                print(type(ptr))
                currentBuilder.store(exptr, ptr)
            currentNumber += 2

        
    def visitExp(self, ctx: clongParser.ExpContext):
        """
        语法：exp:
            charm
            | stringm
            | paramName
            | (op = '-')? (intm | doublem)
            | array
            | func
            | '(' exp ')'
            | exp op = ('+' | '-' | '*' | '/' | '%') exp;
        描述：处理表达式，用于计算出一个值
        """
        currentBuilder = self.Builders[-1]
        if ctx.getChildCount() == 1:
            child = ctx.getChild(0)
            if isinstance(child, clongParser.ParamNameContext):
                paramName = self.visit(child)
                ptr = self.SymbolTable.getItem(paramName)[1]
                return currentBuilder.load(ptr)
            elif isinstance(child, clongParser.ArrayContext):
                ptr = self.visit(child)
                return currentBuilder.load(ptr)
            elif isinstance(child, clongParser.FuncContext):
                return self.visit(child)
            elif isinstance(child, clongParser.IntmContext):
                return self.visit(child)
            elif isinstance(child, clongParser.DoublemContext):
                return self.visit(child)
            elif isinstance(child, clongParser.CharmContext):
                return self.visit(child)
            elif isinstance(child, clongParser.StringmContext):
                return self.visit(child)
        elif ctx.getChildCount() == 2:
            child = ctx.getChild(0)
            if child.getText() == '-':
                num = ctx.getChild(1)
                if isinstance(num, clongParser.IntmContext):
                    return int32(-int(num.getText()))
                elif isinstance(num, clongParser.DoublemContext):
                    return double(-float(num.getText()))
                else:
                    return None
        elif ctx.getChildCount() == 3:
            midChild = ctx.getChild(1)
            if isinstance(midChild, clongParser.ExpContext):
                return self.visit(midChild)
            else:
                # 处理二元比较运算符
                left = self.visit(ctx.getChild(0))
                right = self.visit(ctx.getChild(2))
                left_32 = currentBuilder.zext(left, int32)
                right_32 = currentBuilder.zext(right, int32)
                
                op = midChild.getText()
                if op == '+':
                    return currentBuilder.add(left_32, right_32)
                elif op == '-':
                    return currentBuilder.sub(left_32, right_32)
                elif op == '*':
                    return currentBuilder.mul(left_32, right_32)
                elif op == '/':
                    return currentBuilder.sdiv(left_32, right_32)
                elif op == '%':
                    return currentBuilder.srem(left_32, right_32)

    def visitCondition(self, ctx: clongParser.ConditionContext):
        """
        语法：condition:
            exp
            | '(' condition ')'
            | exp op = ('>' | '<' | '>=' | '<=' | '==' | '!=') exp
            | '!' condition
            | condition op = ( '&&' | '||') condition;
        描述：处理条件表达式
        """
        currentBuilder = self.Builders[-1]
        if ctx.getChildCount() == 1:
            child = ctx.getChild(0)
            if isinstance(child, clongParser.ExpContext):
                val = self.visit(child)
                return currentBuilder.icmp_signed('!=', val, int32(0))
        elif ctx.getChildCount() == 2:
            child = ctx.getChild(0)
            if child.getText() == '!':
                condition = self.visit(ctx.getChild(1))
                return currentBuilder.not_(condition)
        elif ctx.getChildCount() == 3:
            if isinstance(ctx.getChild(0), clongParser.ExpContext):
                left = self.visit(ctx.getChild(0))
                right = self.visit(ctx.getChild(2))
                left_32 = currentBuilder.zext(left, int32)
                right_32 = currentBuilder.zext(right, int32)
                op = ctx.getChild(1).getText()
                return currentBuilder.icmp_signed(op, left_32, right_32)
            elif isinstance(ctx.getChild(0), clongParser.ConditionContext):
                left = self.visit(ctx.getChild(0))
                right = self.visit(ctx.getChild(2))
                op = ctx.getChild(1).getText()
                if op == '&&':
                    return currentBuilder.and_(left, right)
                elif op == '||':
                    return currentBuilder.or_(left, right)
        else:
            return self.visit(ctx.getChild(1))
        
    def visitTypeParam(self, ctx: clongParser.TypeParamContext):
        """
        语法：typeParam:'int'|'char'|'double';
        描述：处理变量类型
        """
        if ctx.getText() == 'int':
            return int32
        elif ctx.getText() == 'char':
            return int8
        elif ctx.getText() == 'double':
            return double
        else:
            return None
        
    def visitArray(self, ctx: clongParser.ArrayContext):
        """
        语法：array:paramName'['exp']';
        描述：处理数组元素
        """
        paramName = self.visit(ctx.paramName())
        ptr = self.SymbolTable.getItem(paramName)[1]
        index = self.visit(ctx.exp())
        currentBuilder = self.Builders[-1]
        zero = ir.Constant(int32, 0)
        ptr = currentBuilder.gep(ptr, [zero, index], inbounds=True)
        print(type(ptr))
        return ptr
        
    def visitLibrary(self, ctx: clongParser.LibraryContext):
        """
        语法：library:PAR '.h'?;
        描述：处理库函数（调用不到，空置）
        """
        return
        
    def visitParamName(self, ctx: clongParser.ParamNameContext):
        """
        语法：paramName:PAR;
        描述：处理变量名
        """
        return ctx.getText()
        
    def visitIntm(self, ctx: clongParser.IntmContext):
        """
        语法：intm:INT;
        描述：处理整数
        """
        return ir.Constant(int32, int(ctx.getText()))
    
    def visitDoublem(self, ctx: clongParser.DoublemContext):
        """
        语法：doublem:DOUBLE;
        描述：处理浮点数
        """
        return double(float(ctx.getText()))
        
    def visitStringm(self, ctx: clongParser.StringmContext):
        """
        语法：stringm:STRING;
        描述：处理字符串
        """
        index = self.ConstantIndex
        self.ConstantIndex += 1
        str = ctx.getText()[1:-1]
        str = str.replace('\\n', '\n')
        str += '\0'
        length = len(bytearray(str, 'utf-8'))
        val = ir.GlobalVariable(self.Module, ir.ArrayType(int8, length), ".str%d" % index)
        val.global_constant = True
        val.initializer = ir.Constant(ir.ArrayType(int8, length), bytearray(str, 'utf-8'))
        return val
        
        
    def visitCharm(self, ctx: clongParser.CharmContext):
        """
        语法：charm:CHAR;
        描述：处理字符
        """
        return int8(ord(ctx.getText()[1]))
        
    
    def save(self,filename):
        with open(filename,'w') as f:
            f.write(str(self.Module))

def analyse(filename):
    """
    将输入的文件进行词法分析，得到token流
    Args:
        filename: 输入的文件名
    """
    lexer = clongLexer(FileStream(filename))
    stream = CommonTokenStream(lexer)
    parser=clongParser(stream)
    tree = parser.prog()
    translator=Visitor()
    translator.visit(tree)
    dirname, basename = os.path.split(filename)
    base, _ = os.path.splitext(basename)
    new_filename = os.path.join(dirname, base + '.ll')
    
    translator.save(new_filename)