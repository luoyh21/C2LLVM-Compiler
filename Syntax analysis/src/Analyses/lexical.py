from antlr4 import *
from antlr.clongParser import clongParser
from antlr.clongVisitor import clongVisitor
from antlr.clongLexer import clongLexer
from Analyses.errorListener import fewerErrorListener

def analyse(filename):
    """
    将输入的文件进行词法分析，得到token流
    Args:
        filename: 输入的文件名
    """
    lexer = clongLexer(FileStream(filename))
    stream = CommonTokenStream(lexer)
    parser=clongParser(stream)
    parser.removeErrorListeners()
    errorListener = fewerErrorListener()
    parser.addErrorListener(errorListener)
    tree = parser.prog()
    