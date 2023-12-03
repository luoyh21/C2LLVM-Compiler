# Generated from clong.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .clongParser import clongParser
else:
    from clongParser import clongParser

# This class defines a complete listener for a parse tree produced by clongParser.
class clongListener(ParseTreeListener):

    # Enter a parse tree produced by clongParser#prog.
    def enterProg(self, ctx:clongParser.ProgContext):
        pass

    # Exit a parse tree produced by clongParser#prog.
    def exitProg(self, ctx:clongParser.ProgContext):
        pass


    # Enter a parse tree produced by clongParser#head.
    def enterHead(self, ctx:clongParser.HeadContext):
        pass

    # Exit a parse tree produced by clongParser#head.
    def exitHead(self, ctx:clongParser.HeadContext):
        pass


    # Enter a parse tree produced by clongParser#include.
    def enterInclude(self, ctx:clongParser.IncludeContext):
        pass

    # Exit a parse tree produced by clongParser#include.
    def exitInclude(self, ctx:clongParser.IncludeContext):
        pass


    # Enter a parse tree produced by clongParser#main.
    def enterMain(self, ctx:clongParser.MainContext):
        pass

    # Exit a parse tree produced by clongParser#main.
    def exitMain(self, ctx:clongParser.MainContext):
        pass


    # Enter a parse tree produced by clongParser#body.
    def enterBody(self, ctx:clongParser.BodyContext):
        pass

    # Exit a parse tree produced by clongParser#body.
    def exitBody(self, ctx:clongParser.BodyContext):
        pass


    # Enter a parse tree produced by clongParser#func.
    def enterFunc(self, ctx:clongParser.FuncContext):
        pass

    # Exit a parse tree produced by clongParser#func.
    def exitFunc(self, ctx:clongParser.FuncContext):
        pass


    # Enter a parse tree produced by clongParser#block.
    def enterBlock(self, ctx:clongParser.BlockContext):
        pass

    # Exit a parse tree produced by clongParser#block.
    def exitBlock(self, ctx:clongParser.BlockContext):
        pass


    # Enter a parse tree produced by clongParser#printf.
    def enterPrintf(self, ctx:clongParser.PrintfContext):
        pass

    # Exit a parse tree produced by clongParser#printf.
    def exitPrintf(self, ctx:clongParser.PrintfContext):
        pass


    # Enter a parse tree produced by clongParser#gets.
    def enterGets(self, ctx:clongParser.GetsContext):
        pass

    # Exit a parse tree produced by clongParser#gets.
    def exitGets(self, ctx:clongParser.GetsContext):
        pass


    # Enter a parse tree produced by clongParser#strlen.
    def enterStrlen(self, ctx:clongParser.StrlenContext):
        pass

    # Exit a parse tree produced by clongParser#strlen.
    def exitStrlen(self, ctx:clongParser.StrlenContext):
        pass


    # Enter a parse tree produced by clongParser#returnFunc.
    def enterReturnFunc(self, ctx:clongParser.ReturnFuncContext):
        pass

    # Exit a parse tree produced by clongParser#returnFunc.
    def exitReturnFunc(self, ctx:clongParser.ReturnFuncContext):
        pass


    # Enter a parse tree produced by clongParser#ifElse.
    def enterIfElse(self, ctx:clongParser.IfElseContext):
        pass

    # Exit a parse tree produced by clongParser#ifElse.
    def exitIfElse(self, ctx:clongParser.IfElseContext):
        pass


    # Enter a parse tree produced by clongParser#ifFunc.
    def enterIfFunc(self, ctx:clongParser.IfFuncContext):
        pass

    # Exit a parse tree produced by clongParser#ifFunc.
    def exitIfFunc(self, ctx:clongParser.IfFuncContext):
        pass


    # Enter a parse tree produced by clongParser#elseif.
    def enterElseif(self, ctx:clongParser.ElseifContext):
        pass

    # Exit a parse tree produced by clongParser#elseif.
    def exitElseif(self, ctx:clongParser.ElseifContext):
        pass


    # Enter a parse tree produced by clongParser#elseFunc.
    def enterElseFunc(self, ctx:clongParser.ElseFuncContext):
        pass

    # Exit a parse tree produced by clongParser#elseFunc.
    def exitElseFunc(self, ctx:clongParser.ElseFuncContext):
        pass


    # Enter a parse tree produced by clongParser#whileFunc.
    def enterWhileFunc(self, ctx:clongParser.WhileFuncContext):
        pass

    # Exit a parse tree produced by clongParser#whileFunc.
    def exitWhileFunc(self, ctx:clongParser.WhileFuncContext):
        pass


    # Enter a parse tree produced by clongParser#forFunc.
    def enterForFunc(self, ctx:clongParser.ForFuncContext):
        pass

    # Exit a parse tree produced by clongParser#forFunc.
    def exitForFunc(self, ctx:clongParser.ForFuncContext):
        pass


    # Enter a parse tree produced by clongParser#initFunc.
    def enterInitFunc(self, ctx:clongParser.InitFuncContext):
        pass

    # Exit a parse tree produced by clongParser#initFunc.
    def exitInitFunc(self, ctx:clongParser.InitFuncContext):
        pass


    # Enter a parse tree produced by clongParser#assignFunc.
    def enterAssignFunc(self, ctx:clongParser.AssignFuncContext):
        pass

    # Exit a parse tree produced by clongParser#assignFunc.
    def exitAssignFunc(self, ctx:clongParser.AssignFuncContext):
        pass


    # Enter a parse tree produced by clongParser#initParam.
    def enterInitParam(self, ctx:clongParser.InitParamContext):
        pass

    # Exit a parse tree produced by clongParser#initParam.
    def exitInitParam(self, ctx:clongParser.InitParamContext):
        pass


    # Enter a parse tree produced by clongParser#initArray.
    def enterInitArray(self, ctx:clongParser.InitArrayContext):
        pass

    # Exit a parse tree produced by clongParser#initArray.
    def exitInitArray(self, ctx:clongParser.InitArrayContext):
        pass


    # Enter a parse tree produced by clongParser#assign.
    def enterAssign(self, ctx:clongParser.AssignContext):
        pass

    # Exit a parse tree produced by clongParser#assign.
    def exitAssign(self, ctx:clongParser.AssignContext):
        pass


    # Enter a parse tree produced by clongParser#exp.
    def enterExp(self, ctx:clongParser.ExpContext):
        pass

    # Exit a parse tree produced by clongParser#exp.
    def exitExp(self, ctx:clongParser.ExpContext):
        pass


    # Enter a parse tree produced by clongParser#typeParam.
    def enterTypeParam(self, ctx:clongParser.TypeParamContext):
        pass

    # Exit a parse tree produced by clongParser#typeParam.
    def exitTypeParam(self, ctx:clongParser.TypeParamContext):
        pass


    # Enter a parse tree produced by clongParser#array.
    def enterArray(self, ctx:clongParser.ArrayContext):
        pass

    # Exit a parse tree produced by clongParser#array.
    def exitArray(self, ctx:clongParser.ArrayContext):
        pass


    # Enter a parse tree produced by clongParser#paramName.
    def enterParamName(self, ctx:clongParser.ParamNameContext):
        pass

    # Exit a parse tree produced by clongParser#paramName.
    def exitParamName(self, ctx:clongParser.ParamNameContext):
        pass


    # Enter a parse tree produced by clongParser#intm.
    def enterIntm(self, ctx:clongParser.IntmContext):
        pass

    # Exit a parse tree produced by clongParser#intm.
    def exitIntm(self, ctx:clongParser.IntmContext):
        pass


    # Enter a parse tree produced by clongParser#doublem.
    def enterDoublem(self, ctx:clongParser.DoublemContext):
        pass

    # Exit a parse tree produced by clongParser#doublem.
    def exitDoublem(self, ctx:clongParser.DoublemContext):
        pass


    # Enter a parse tree produced by clongParser#charm.
    def enterCharm(self, ctx:clongParser.CharmContext):
        pass

    # Exit a parse tree produced by clongParser#charm.
    def exitCharm(self, ctx:clongParser.CharmContext):
        pass


    # Enter a parse tree produced by clongParser#stringm.
    def enterStringm(self, ctx:clongParser.StringmContext):
        pass

    # Exit a parse tree produced by clongParser#stringm.
    def exitStringm(self, ctx:clongParser.StringmContext):
        pass


