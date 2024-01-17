# Generated from clong.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .clongParser import clongParser
else:
    from clongParser import clongParser

# This class defines a complete generic visitor for a parse tree produced by clongParser.

class clongVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by clongParser#prog.
    def visitProg(self, ctx:clongParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#head.
    def visitHead(self, ctx:clongParser.HeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#include.
    def visitInclude(self, ctx:clongParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#main.
    def visitMain(self, ctx:clongParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#body.
    def visitBody(self, ctx:clongParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#func.
    def visitFunc(self, ctx:clongParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#block.
    def visitBlock(self, ctx:clongParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#printf.
    def visitPrintf(self, ctx:clongParser.PrintfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#gets.
    def visitGets(self, ctx:clongParser.GetsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#strlen.
    def visitStrlen(self, ctx:clongParser.StrlenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#returnFunc.
    def visitReturnFunc(self, ctx:clongParser.ReturnFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#ifElse.
    def visitIfElse(self, ctx:clongParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#ifFunc.
    def visitIfFunc(self, ctx:clongParser.IfFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#elseif.
    def visitElseif(self, ctx:clongParser.ElseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#elseFunc.
    def visitElseFunc(self, ctx:clongParser.ElseFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#whileFunc.
    def visitWhileFunc(self, ctx:clongParser.WhileFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#forFunc.
    def visitForFunc(self, ctx:clongParser.ForFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#initFunc.
    def visitInitFunc(self, ctx:clongParser.InitFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#assignFunc.
    def visitAssignFunc(self, ctx:clongParser.AssignFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#initParam.
    def visitInitParam(self, ctx:clongParser.InitParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#initArray.
    def visitInitArray(self, ctx:clongParser.InitArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#assign.
    def visitAssign(self, ctx:clongParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#exp.
    def visitExp(self, ctx:clongParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#typeParam.
    def visitTypeParam(self, ctx:clongParser.TypeParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#array.
    def visitArray(self, ctx:clongParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#library.
    def visitLibrary(self, ctx:clongParser.LibraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#paramName.
    def visitParamName(self, ctx:clongParser.ParamNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#intm.
    def visitIntm(self, ctx:clongParser.IntmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#doublem.
    def visitDoublem(self, ctx:clongParser.DoublemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#charm.
    def visitCharm(self, ctx:clongParser.CharmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clongParser#stringm.
    def visitStringm(self, ctx:clongParser.StringmContext):
        return self.visitChildren(ctx)



del clongParser