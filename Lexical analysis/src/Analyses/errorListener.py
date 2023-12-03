from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *

class fewerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, row, column, msg, e):
        if offendingSymbol.text == "<EOF>":
            return
        exception = "(row:" + str(row) + ",column:" + str(column) + ") " + msg
        print('SyntaxError: ' + exception)