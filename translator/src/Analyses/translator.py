from antlr4 import *
from antlr.clongParser import clongParser
from antlr.clongVisitor import clongVisitor
from antlr.clongLexer import clongLexer
from Analyses.config import *
import os
from llvmlite import ir

class Visitor(clongVisitor):
    def __init__(self):
        super(clongVisitor, self).__init__()
        self.IR=ir.Module()
        self.IR.triple = "x86_64-pc-linux-gnu"
        self.IR.data_layout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
        #输入语句块列表
        self.InputBlocks=[]
        #输出语句块列表
        self.OutputBlocks=[]
        
    def visitProg(self,ctx:clongParser.ProgContext):
        '''
        语法：prog:head main;
        作用：处理prog（全代码）
        '''
        self.visit(ctx.main())
        
    def visitMain(self,ctx:clongParser.MainContext):
        '''
        语法：main:('int'|'void') 'main''()''{' body '}';
        描述：处理main函数
        '''
        #LLVM函数定义
        IRType=ir.FunctionType(int32,[])
        IRFunc=ir.Function(self.IR,IRType,"main")
        
        #LLVM函数块
        InputBlock=IRFunc.append_basic_block("entry")
        OutputBlock=ir.IRBuilder(InputBlock)
        self.InputBlocks.append(InputBlock)
        self.OutputBlocks.append(OutputBlock)
        
        #处理main函数体
        self.visit(ctx.body())
        
        self.InputBlocks.pop()
        self.OutputBlocks.pop()
        return;
    
    def visitBody(self,ctx:clongParser.BodyContext):
        '''
        语法：body:(func';'|block)*;
        描述：处理函数体
        '''
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))
            if self.InputBlocks[-1].is_terminated:
                break
        return

    def visitFunc(self,ctx:clongParser.FuncContext):
        '''
        语法：func:(printf|gets|strlen|returnFunc);
        描述：处理单行函数调用
        '''
        
    def visitStrlen(self, ctx: clongParser.StrlenContext):
        """
        语法：strlen:'strlen''('paramName')';
        描述：处理strlen函数调用
        """
        
    def visitPrintf(self, ctx: clongParser.PrintfContext):
        """
        语法：printf:'printf''('((stringm(','exp)*) |paramName)')';
        描述：处理printf函数调用
        """
    
    def visitGets(self, ctx: clongParser.GetsContext):
        """
        语法：gets:'gets''('paramName')';
        描述：处理gets函数调用
        """
        
    def visitReturnFunc(self, ctx: clongParser.ReturnFuncContext):
        """
        语法：returnFunc:'return'(intm)?;
        描述：处理return退出
        """
        
    
    def visitBlock(self, ctx: clongParser.BlockContext):
        """
        语法：block:ifElse|whileFunc|forFunc|initParam|initArray|assign;
        描述：处理语句块
        """
        
    def visitIfElse(self, ctx: clongParser.IfElseContext):
        """
        语法：ifElse:ifFunc(elseif)*(elseFunc)?;
        描述：处理整个if-elseif-else语句块
        """
        
    def visitIfFunc(self, ctx: clongParser.IfFuncContext):
        """
        语法：ifFunc:'if' '('exp')''{'body'}';
        描述：处理if部分
        """
        
    def visitElseif(self, ctx: clongParser.ElseifContext):
        """
        语法：elseif:'else''if''('exp')''{'body'}';
        描述：处理elseif部分
        """
        
    def visitElseFunc(self, ctx: clongParser.ElseFuncContext):
        """
        语法：elseFunc:'else''{'body'}';
        描述：处理else部分
        """
    
    def visitWhileFunc(self, ctx: clongParser.WhileFuncContext):
        """
        语法：whileFunc:'while''('exp')''{'body'}';
        描述：处理while语句块
        """
        
    def visitForFunc(self, ctx: clongParser.ForFuncContext):
        """
        语法：forFunc:'for''('initFunc';'exp';'assignFunc')''{'body'}';
        描述：处理整个for语句块
        """
        
    def visitInitFunc(self, ctx: clongParser.InitFuncContext):
        """
        语法：initFunc: (typeParam)? paramName ('=' exp)?(','initFunc)?|;
        描述：处理for循环中的初始化部分
        """
        
    def visitAssignFunc(self, ctx: clongParser.AssignFuncContext):
        """
        语法：assignFunc:paramName '=' exp(','assignFunc)?|;
        描述：处理for循环中的赋值部分
        """
        
    def visitInitParam(self, ctx: clongParser.InitParamContext):
        """
        语法：initParam:typeParam paramName ('=' exp)?(','paramName ('=' exp)?)*';';
        描述：处理变量初始化
        """
        
    def visitInitArray(self, ctx: clongParser.InitArrayContext):
        """
        语法：initArray:typeParam paramName '[' intm ']'';';
        描述：处理数组初始化
        """
        
    def visitAssign(self, ctx: clongParser.AssignContext):
        """
        语法：assign:(((paramName|array)'=')+exp)';';
        描述：处理变量和数组赋值
        """
        
    def visitExp(self, ctx: clongParser.ExpContext):
        """
        语法：exp:charm|stringm|paramName|(op='-')?(intm|doublem)|array|func|'('exp')'
            |exp op=('+'|'-'|'*'|'/'|'%'|'>'|'<'|'>='|'<='|'=='|'!='|'&&'|'||') exp
            |op='!'exp;
        描述：处理表达式，用于计算出一个值
        """
        
    def visitTypeParam(self, ctx: clongParser.TypeParamContext):
        """
        语法：typeParam:'int'|'char'|'double';
        描述：处理变量类型
        """
        
    def visitArray(self, ctx: clongParser.ArrayContext):
        """
        语法：array:paramName'['exp']';
        描述：处理数组元素
        """
        
    def visitLibrary(self, ctx: clongParser.LibraryContext):
        """
        语法：library:PAR '.h'?;
        描述：处理库函数（调用不到，空置）
        """
        
    def visitParamName(self, ctx: clongParser.ParamNameContext):
        """
        语法：paramName:PAR;
        描述：处理变量名
        """
        
    def visitIntm(self, ctx: clongParser.IntmContext):
        """
        语法：intm:INT;
        描述：处理整数
        """
    
    def visitDoublem(self, ctx: clongParser.DoublemContext):
        """
        语法：doublem:DOUBLE;
        描述：处理浮点数
        """
        
    def visitStringm(self, ctx: clongParser.StringmContext):
        """
        语法：stringm:STRING;
        描述：处理字符串
        """
        
    def visitCharm(self, ctx: clongParser.CharmContext):
        """
        语法：charm:CHAR;
        描述：处理字符
        """
        
    
    def save(self,filename):
        with open(filename,'w') as f:
            f.write(str(self.IR))

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