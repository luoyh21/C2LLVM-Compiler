# Generated from clong.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,47,324,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,1,
        1,5,1,69,8,1,10,1,12,1,72,9,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,90,8,4,10,4,12,4,93,9,4,1,5,1,
        5,1,5,1,5,3,5,99,8,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,107,8,6,1,7,1,7,
        1,7,1,7,3,7,113,8,7,1,7,1,7,5,7,117,8,7,10,7,12,7,120,9,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,3,10,136,8,10,
        1,11,1,11,5,11,140,8,11,10,11,12,11,143,9,11,1,11,3,11,146,8,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,17,3,17,191,8,17,1,17,1,17,1,17,3,17,196,8,17,1,
        17,1,17,3,17,200,8,17,1,17,3,17,203,8,17,1,18,1,18,1,18,1,18,1,18,
        3,18,210,8,18,1,18,3,18,213,8,18,1,19,1,19,1,19,1,19,3,19,219,8,
        19,1,19,1,19,1,19,1,19,3,19,225,8,19,5,19,227,8,19,10,19,12,19,230,
        9,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,3,21,
        243,8,21,1,21,1,21,4,21,247,8,21,11,21,12,21,248,1,21,1,21,1,21,
        1,21,1,22,1,22,1,22,1,22,1,22,3,22,260,8,22,1,22,1,22,3,22,264,8,
        22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,272,8,22,1,22,1,22,1,22,5,
        22,277,8,22,10,22,12,22,280,9,22,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,3,23,293,8,23,1,23,1,23,1,23,5,23,298,8,23,
        10,23,12,23,301,9,23,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,
        3,26,312,8,26,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,31,1,31,
        1,31,0,2,44,46,32,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,0,5,1,0,4,5,1,0,25,
        29,2,0,2,3,30,33,1,0,35,36,2,0,4,4,37,38,331,0,64,1,0,0,0,2,70,1,
        0,0,0,4,73,1,0,0,0,6,78,1,0,0,0,8,91,1,0,0,0,10,98,1,0,0,0,12,106,
        1,0,0,0,14,108,1,0,0,0,16,123,1,0,0,0,18,128,1,0,0,0,20,133,1,0,
        0,0,22,137,1,0,0,0,24,147,1,0,0,0,26,155,1,0,0,0,28,164,1,0,0,0,
        30,169,1,0,0,0,32,177,1,0,0,0,34,202,1,0,0,0,36,212,1,0,0,0,38,214,
        1,0,0,0,40,233,1,0,0,0,42,246,1,0,0,0,44,271,1,0,0,0,46,292,1,0,
        0,0,48,302,1,0,0,0,50,304,1,0,0,0,52,309,1,0,0,0,54,313,1,0,0,0,
        56,315,1,0,0,0,58,317,1,0,0,0,60,319,1,0,0,0,62,321,1,0,0,0,64,65,
        3,2,1,0,65,66,3,6,3,0,66,1,1,0,0,0,67,69,3,4,2,0,68,67,1,0,0,0,69,
        72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,3,1,0,0,0,72,70,1,0,0,
        0,73,74,5,1,0,0,74,75,5,2,0,0,75,76,3,52,26,0,76,77,5,3,0,0,77,5,
        1,0,0,0,78,79,7,0,0,0,79,80,5,6,0,0,80,81,5,7,0,0,81,82,5,8,0,0,
        82,83,3,8,4,0,83,84,5,9,0,0,84,7,1,0,0,0,85,86,3,10,5,0,86,87,5,
        10,0,0,87,90,1,0,0,0,88,90,3,12,6,0,89,85,1,0,0,0,89,88,1,0,0,0,
        90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,9,1,0,0,0,93,91,1,0,
        0,0,94,99,3,14,7,0,95,99,3,16,8,0,96,99,3,18,9,0,97,99,3,20,10,0,
        98,94,1,0,0,0,98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,0,99,11,1,
        0,0,0,100,107,3,22,11,0,101,107,3,30,15,0,102,107,3,32,16,0,103,
        107,3,38,19,0,104,107,3,40,20,0,105,107,3,42,21,0,106,100,1,0,0,
        0,106,101,1,0,0,0,106,102,1,0,0,0,106,103,1,0,0,0,106,104,1,0,0,
        0,106,105,1,0,0,0,107,13,1,0,0,0,108,109,5,11,0,0,109,112,5,12,0,
        0,110,113,3,62,31,0,111,113,3,54,27,0,112,110,1,0,0,0,112,111,1,
        0,0,0,113,118,1,0,0,0,114,115,5,13,0,0,115,117,3,44,22,0,116,114,
        1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,121,
        1,0,0,0,120,118,1,0,0,0,121,122,5,14,0,0,122,15,1,0,0,0,123,124,
        5,15,0,0,124,125,5,12,0,0,125,126,3,54,27,0,126,127,5,14,0,0,127,
        17,1,0,0,0,128,129,5,16,0,0,129,130,5,12,0,0,130,131,3,54,27,0,131,
        132,5,14,0,0,132,19,1,0,0,0,133,135,5,17,0,0,134,136,3,56,28,0,135,
        134,1,0,0,0,135,136,1,0,0,0,136,21,1,0,0,0,137,141,3,24,12,0,138,
        140,3,26,13,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,
        142,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,144,146,3,28,14,0,145,
        144,1,0,0,0,145,146,1,0,0,0,146,23,1,0,0,0,147,148,5,18,0,0,148,
        149,5,12,0,0,149,150,3,46,23,0,150,151,5,14,0,0,151,152,5,8,0,0,
        152,153,3,8,4,0,153,154,5,9,0,0,154,25,1,0,0,0,155,156,5,19,0,0,
        156,157,5,18,0,0,157,158,5,12,0,0,158,159,3,46,23,0,159,160,5,14,
        0,0,160,161,5,8,0,0,161,162,3,8,4,0,162,163,5,9,0,0,163,27,1,0,0,
        0,164,165,5,19,0,0,165,166,5,8,0,0,166,167,3,8,4,0,167,168,5,9,0,
        0,168,29,1,0,0,0,169,170,5,20,0,0,170,171,5,12,0,0,171,172,3,46,
        23,0,172,173,5,14,0,0,173,174,5,8,0,0,174,175,3,8,4,0,175,176,5,
        9,0,0,176,31,1,0,0,0,177,178,5,21,0,0,178,179,5,12,0,0,179,180,3,
        34,17,0,180,181,5,10,0,0,181,182,3,46,23,0,182,183,5,10,0,0,183,
        184,3,36,18,0,184,185,5,14,0,0,185,186,5,8,0,0,186,187,3,8,4,0,187,
        188,5,9,0,0,188,33,1,0,0,0,189,191,3,48,24,0,190,189,1,0,0,0,190,
        191,1,0,0,0,191,192,1,0,0,0,192,195,3,54,27,0,193,194,5,22,0,0,194,
        196,3,44,22,0,195,193,1,0,0,0,195,196,1,0,0,0,196,199,1,0,0,0,197,
        198,5,13,0,0,198,200,3,34,17,0,199,197,1,0,0,0,199,200,1,0,0,0,200,
        203,1,0,0,0,201,203,1,0,0,0,202,190,1,0,0,0,202,201,1,0,0,0,203,
        35,1,0,0,0,204,205,3,54,27,0,205,206,5,22,0,0,206,209,3,44,22,0,
        207,208,5,13,0,0,208,210,3,36,18,0,209,207,1,0,0,0,209,210,1,0,0,
        0,210,213,1,0,0,0,211,213,1,0,0,0,212,204,1,0,0,0,212,211,1,0,0,
        0,213,37,1,0,0,0,214,215,3,48,24,0,215,218,3,54,27,0,216,217,5,22,
        0,0,217,219,3,44,22,0,218,216,1,0,0,0,218,219,1,0,0,0,219,228,1,
        0,0,0,220,221,5,13,0,0,221,224,3,54,27,0,222,223,5,22,0,0,223,225,
        3,44,22,0,224,222,1,0,0,0,224,225,1,0,0,0,225,227,1,0,0,0,226,220,
        1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,231,
        1,0,0,0,230,228,1,0,0,0,231,232,5,10,0,0,232,39,1,0,0,0,233,234,
        3,48,24,0,234,235,3,54,27,0,235,236,5,23,0,0,236,237,3,56,28,0,237,
        238,5,24,0,0,238,239,5,10,0,0,239,41,1,0,0,0,240,243,3,54,27,0,241,
        243,3,50,25,0,242,240,1,0,0,0,242,241,1,0,0,0,243,244,1,0,0,0,244,
        245,5,22,0,0,245,247,1,0,0,0,246,242,1,0,0,0,247,248,1,0,0,0,248,
        246,1,0,0,0,248,249,1,0,0,0,249,250,1,0,0,0,250,251,3,44,22,0,251,
        252,1,0,0,0,252,253,5,10,0,0,253,43,1,0,0,0,254,255,6,22,-1,0,255,
        272,3,60,30,0,256,272,3,62,31,0,257,272,3,54,27,0,258,260,5,25,0,
        0,259,258,1,0,0,0,259,260,1,0,0,0,260,263,1,0,0,0,261,264,3,56,28,
        0,262,264,3,58,29,0,263,261,1,0,0,0,263,262,1,0,0,0,264,272,1,0,
        0,0,265,272,3,50,25,0,266,272,3,10,5,0,267,268,5,12,0,0,268,269,
        3,44,22,0,269,270,5,14,0,0,270,272,1,0,0,0,271,254,1,0,0,0,271,256,
        1,0,0,0,271,257,1,0,0,0,271,259,1,0,0,0,271,265,1,0,0,0,271,266,
        1,0,0,0,271,267,1,0,0,0,272,278,1,0,0,0,273,274,10,1,0,0,274,275,
        7,1,0,0,275,277,3,44,22,2,276,273,1,0,0,0,277,280,1,0,0,0,278,276,
        1,0,0,0,278,279,1,0,0,0,279,45,1,0,0,0,280,278,1,0,0,0,281,282,6,
        23,-1,0,282,283,5,12,0,0,283,284,3,46,23,0,284,285,5,14,0,0,285,
        293,1,0,0,0,286,287,3,44,22,0,287,288,7,2,0,0,288,289,3,44,22,0,
        289,293,1,0,0,0,290,291,5,34,0,0,291,293,3,46,23,2,292,281,1,0,0,
        0,292,286,1,0,0,0,292,290,1,0,0,0,293,299,1,0,0,0,294,295,10,1,0,
        0,295,296,7,3,0,0,296,298,3,46,23,2,297,294,1,0,0,0,298,301,1,0,
        0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,47,1,0,0,0,301,299,1,0,0,
        0,302,303,7,4,0,0,303,49,1,0,0,0,304,305,3,54,27,0,305,306,5,23,
        0,0,306,307,3,44,22,0,307,308,5,24,0,0,308,51,1,0,0,0,309,311,5,
        40,0,0,310,312,5,39,0,0,311,310,1,0,0,0,311,312,1,0,0,0,312,53,1,
        0,0,0,313,314,5,40,0,0,314,55,1,0,0,0,315,316,5,41,0,0,316,57,1,
        0,0,0,317,318,5,42,0,0,318,59,1,0,0,0,319,320,5,43,0,0,320,61,1,
        0,0,0,321,322,5,44,0,0,322,63,1,0,0,0,28,70,89,91,98,106,112,118,
        135,141,145,190,195,199,202,209,212,218,224,228,242,248,259,263,
        271,278,292,299,311
    ]

class clongParser ( Parser ):

    grammarFileName = "clong.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#include'", "'<'", "'>'", "'int'", "'void'", 
                     "'main'", "'()'", "'{'", "'}'", "';'", "'printf'", 
                     "'('", "','", "')'", "'gets'", "'strlen'", "'return'", 
                     "'if'", "'else'", "'while'", "'for'", "'='", "'['", 
                     "']'", "'-'", "'+'", "'*'", "'/'", "'%'", "'>='", "'<='", 
                     "'=='", "'!='", "'!'", "'&&'", "'||'", "'char'", "'double'", 
                     "'.h'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "PAR", "INT", "DOUBLE", "CHAR", "STRING", "LineComment", 
                      "BlockComment", "DELIMITER" ]

    RULE_prog = 0
    RULE_head = 1
    RULE_include = 2
    RULE_main = 3
    RULE_body = 4
    RULE_func = 5
    RULE_block = 6
    RULE_printf = 7
    RULE_gets = 8
    RULE_strlen = 9
    RULE_returnFunc = 10
    RULE_ifElse = 11
    RULE_ifFunc = 12
    RULE_elseif = 13
    RULE_elseFunc = 14
    RULE_whileFunc = 15
    RULE_forFunc = 16
    RULE_initFunc = 17
    RULE_assignFunc = 18
    RULE_initParam = 19
    RULE_initArray = 20
    RULE_assign = 21
    RULE_exp = 22
    RULE_condition = 23
    RULE_typeParam = 24
    RULE_array = 25
    RULE_library = 26
    RULE_paramName = 27
    RULE_intm = 28
    RULE_doublem = 29
    RULE_charm = 30
    RULE_stringm = 31

    ruleNames =  [ "prog", "head", "include", "main", "body", "func", "block", 
                   "printf", "gets", "strlen", "returnFunc", "ifElse", "ifFunc", 
                   "elseif", "elseFunc", "whileFunc", "forFunc", "initFunc", 
                   "assignFunc", "initParam", "initArray", "assign", "exp", 
                   "condition", "typeParam", "array", "library", "paramName", 
                   "intm", "doublem", "charm", "stringm" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    PAR=40
    INT=41
    DOUBLE=42
    CHAR=43
    STRING=44
    LineComment=45
    BlockComment=46
    DELIMITER=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def head(self):
            return self.getTypedRuleContext(clongParser.HeadContext,0)


        def main(self):
            return self.getTypedRuleContext(clongParser.MainContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = clongParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.head()
            self.state = 65
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def include(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clongParser.IncludeContext)
            else:
                return self.getTypedRuleContext(clongParser.IncludeContext,i)


        def getRuleIndex(self):
            return clongParser.RULE_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHead" ):
                listener.enterHead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHead" ):
                listener.exitHead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHead" ):
                return visitor.visitHead(self)
            else:
                return visitor.visitChildren(self)




    def head(self):

        localctx = clongParser.HeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_head)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 67
                self.include()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def library(self):
            return self.getTypedRuleContext(clongParser.LibraryContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_include

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclude" ):
                listener.enterInclude(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclude" ):
                listener.exitInclude(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude" ):
                return visitor.visitInclude(self)
            else:
                return visitor.visitChildren(self)




    def include(self):

        localctx = clongParser.IncludeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(clongParser.T__0)
            self.state = 74
            self.match(clongParser.T__1)
            self.state = 75
            self.library()
            self.state = 76
            self.match(clongParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(clongParser.BodyContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = clongParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 79
            self.match(clongParser.T__5)
            self.state = 80
            self.match(clongParser.T__6)
            self.state = 81
            self.match(clongParser.T__7)
            self.state = 82
            self.body()
            self.state = 83
            self.match(clongParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clongParser.FuncContext)
            else:
                return self.getTypedRuleContext(clongParser.FuncContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clongParser.BlockContext)
            else:
                return self.getTypedRuleContext(clongParser.BlockContext,i)


        def getRuleIndex(self):
            return clongParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = clongParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1511832127504) != 0):
                self.state = 89
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 15, 16, 17]:
                    self.state = 85
                    self.func()
                    self.state = 86
                    self.match(clongParser.T__9)
                    pass
                elif token in [4, 18, 20, 21, 37, 38, 40]:
                    self.state = 88
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printf(self):
            return self.getTypedRuleContext(clongParser.PrintfContext,0)


        def gets(self):
            return self.getTypedRuleContext(clongParser.GetsContext,0)


        def strlen(self):
            return self.getTypedRuleContext(clongParser.StrlenContext,0)


        def returnFunc(self):
            return self.getTypedRuleContext(clongParser.ReturnFuncContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = clongParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 94
                self.printf()
                pass
            elif token in [15]:
                self.state = 95
                self.gets()
                pass
            elif token in [16]:
                self.state = 96
                self.strlen()
                pass
            elif token in [17]:
                self.state = 97
                self.returnFunc()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifElse(self):
            return self.getTypedRuleContext(clongParser.IfElseContext,0)


        def whileFunc(self):
            return self.getTypedRuleContext(clongParser.WhileFuncContext,0)


        def forFunc(self):
            return self.getTypedRuleContext(clongParser.ForFuncContext,0)


        def initParam(self):
            return self.getTypedRuleContext(clongParser.InitParamContext,0)


        def initArray(self):
            return self.getTypedRuleContext(clongParser.InitArrayContext,0)


        def assign(self):
            return self.getTypedRuleContext(clongParser.AssignContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = clongParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.ifElse()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.whileFunc()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
                self.forFunc()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 103
                self.initParam()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 104
                self.initArray()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 105
                self.assign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stringm(self):
            return self.getTypedRuleContext(clongParser.StringmContext,0)


        def paramName(self):
            return self.getTypedRuleContext(clongParser.ParamNameContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clongParser.ExpContext)
            else:
                return self.getTypedRuleContext(clongParser.ExpContext,i)


        def getRuleIndex(self):
            return clongParser.RULE_printf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintf" ):
                listener.enterPrintf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintf" ):
                listener.exitPrintf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintf" ):
                return visitor.visitPrintf(self)
            else:
                return visitor.visitChildren(self)




    def printf(self):

        localctx = clongParser.PrintfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_printf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(clongParser.T__10)
            self.state = 109
            self.match(clongParser.T__11)

            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.state = 110
                self.stringm()
                pass
            elif token in [40]:
                self.state = 111
                self.paramName()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 114
                self.match(clongParser.T__12)
                self.state = 115
                self.exp(0)
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
            self.match(clongParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramName(self):
            return self.getTypedRuleContext(clongParser.ParamNameContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_gets

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGets" ):
                listener.enterGets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGets" ):
                listener.exitGets(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGets" ):
                return visitor.visitGets(self)
            else:
                return visitor.visitChildren(self)




    def gets(self):

        localctx = clongParser.GetsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_gets)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(clongParser.T__14)
            self.state = 124
            self.match(clongParser.T__11)
            self.state = 125
            self.paramName()
            self.state = 126
            self.match(clongParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrlenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramName(self):
            return self.getTypedRuleContext(clongParser.ParamNameContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_strlen

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrlen" ):
                listener.enterStrlen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrlen" ):
                listener.exitStrlen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrlen" ):
                return visitor.visitStrlen(self)
            else:
                return visitor.visitChildren(self)




    def strlen(self):

        localctx = clongParser.StrlenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_strlen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(clongParser.T__15)
            self.state = 129
            self.match(clongParser.T__11)
            self.state = 130
            self.paramName()
            self.state = 131
            self.match(clongParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intm(self):
            return self.getTypedRuleContext(clongParser.IntmContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_returnFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnFunc" ):
                listener.enterReturnFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnFunc" ):
                listener.exitReturnFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnFunc" ):
                return visitor.visitReturnFunc(self)
            else:
                return visitor.visitChildren(self)




    def returnFunc(self):

        localctx = clongParser.ReturnFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(clongParser.T__16)
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 134
                self.intm()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifFunc(self):
            return self.getTypedRuleContext(clongParser.IfFuncContext,0)


        def elseif(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clongParser.ElseifContext)
            else:
                return self.getTypedRuleContext(clongParser.ElseifContext,i)


        def elseFunc(self):
            return self.getTypedRuleContext(clongParser.ElseFuncContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_ifElse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)




    def ifElse(self):

        localctx = clongParser.IfElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifElse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.ifFunc()
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 138
                    self.elseif() 
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 144
                self.elseFunc()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(clongParser.ConditionContext,0)


        def body(self):
            return self.getTypedRuleContext(clongParser.BodyContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_ifFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfFunc" ):
                listener.enterIfFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfFunc" ):
                listener.exitIfFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfFunc" ):
                return visitor.visitIfFunc(self)
            else:
                return visitor.visitChildren(self)




    def ifFunc(self):

        localctx = clongParser.IfFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(clongParser.T__17)
            self.state = 148
            self.match(clongParser.T__11)
            self.state = 149
            self.condition(0)
            self.state = 150
            self.match(clongParser.T__13)
            self.state = 151
            self.match(clongParser.T__7)
            self.state = 152
            self.body()
            self.state = 153
            self.match(clongParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(clongParser.ConditionContext,0)


        def body(self):
            return self.getTypedRuleContext(clongParser.BodyContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_elseif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseif" ):
                listener.enterElseif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseif" ):
                listener.exitElseif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif" ):
                return visitor.visitElseif(self)
            else:
                return visitor.visitChildren(self)




    def elseif(self):

        localctx = clongParser.ElseifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elseif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(clongParser.T__18)
            self.state = 156
            self.match(clongParser.T__17)
            self.state = 157
            self.match(clongParser.T__11)
            self.state = 158
            self.condition(0)
            self.state = 159
            self.match(clongParser.T__13)
            self.state = 160
            self.match(clongParser.T__7)
            self.state = 161
            self.body()
            self.state = 162
            self.match(clongParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(clongParser.BodyContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_elseFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseFunc" ):
                listener.enterElseFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseFunc" ):
                listener.exitElseFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseFunc" ):
                return visitor.visitElseFunc(self)
            else:
                return visitor.visitChildren(self)




    def elseFunc(self):

        localctx = clongParser.ElseFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_elseFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(clongParser.T__18)
            self.state = 165
            self.match(clongParser.T__7)
            self.state = 166
            self.body()
            self.state = 167
            self.match(clongParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(clongParser.ConditionContext,0)


        def body(self):
            return self.getTypedRuleContext(clongParser.BodyContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_whileFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileFunc" ):
                listener.enterWhileFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileFunc" ):
                listener.exitWhileFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileFunc" ):
                return visitor.visitWhileFunc(self)
            else:
                return visitor.visitChildren(self)




    def whileFunc(self):

        localctx = clongParser.WhileFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_whileFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(clongParser.T__19)
            self.state = 170
            self.match(clongParser.T__11)
            self.state = 171
            self.condition(0)
            self.state = 172
            self.match(clongParser.T__13)
            self.state = 173
            self.match(clongParser.T__7)
            self.state = 174
            self.body()
            self.state = 175
            self.match(clongParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initFunc(self):
            return self.getTypedRuleContext(clongParser.InitFuncContext,0)


        def condition(self):
            return self.getTypedRuleContext(clongParser.ConditionContext,0)


        def assignFunc(self):
            return self.getTypedRuleContext(clongParser.AssignFuncContext,0)


        def body(self):
            return self.getTypedRuleContext(clongParser.BodyContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_forFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForFunc" ):
                listener.enterForFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForFunc" ):
                listener.exitForFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForFunc" ):
                return visitor.visitForFunc(self)
            else:
                return visitor.visitChildren(self)




    def forFunc(self):

        localctx = clongParser.ForFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(clongParser.T__20)
            self.state = 178
            self.match(clongParser.T__11)
            self.state = 179
            self.initFunc()
            self.state = 180
            self.match(clongParser.T__9)
            self.state = 181
            self.condition(0)
            self.state = 182
            self.match(clongParser.T__9)
            self.state = 183
            self.assignFunc()
            self.state = 184
            self.match(clongParser.T__13)
            self.state = 185
            self.match(clongParser.T__7)
            self.state = 186
            self.body()
            self.state = 187
            self.match(clongParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramName(self):
            return self.getTypedRuleContext(clongParser.ParamNameContext,0)


        def typeParam(self):
            return self.getTypedRuleContext(clongParser.TypeParamContext,0)


        def exp(self):
            return self.getTypedRuleContext(clongParser.ExpContext,0)


        def initFunc(self):
            return self.getTypedRuleContext(clongParser.InitFuncContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_initFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitFunc" ):
                listener.enterInitFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitFunc" ):
                listener.exitInitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitFunc" ):
                return visitor.visitInitFunc(self)
            else:
                return visitor.visitChildren(self)




    def initFunc(self):

        localctx = clongParser.InitFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_initFunc)
        self._la = 0 # Token type
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 37, 38, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 412316860432) != 0):
                    self.state = 189
                    self.typeParam()


                self.state = 192
                self.paramName()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 193
                    self.match(clongParser.T__21)
                    self.state = 194
                    self.exp(0)


                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 197
                    self.match(clongParser.T__12)
                    self.state = 198
                    self.initFunc()


                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramName(self):
            return self.getTypedRuleContext(clongParser.ParamNameContext,0)


        def exp(self):
            return self.getTypedRuleContext(clongParser.ExpContext,0)


        def assignFunc(self):
            return self.getTypedRuleContext(clongParser.AssignFuncContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_assignFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignFunc" ):
                listener.enterAssignFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignFunc" ):
                listener.exitAssignFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignFunc" ):
                return visitor.visitAssignFunc(self)
            else:
                return visitor.visitChildren(self)




    def assignFunc(self):

        localctx = clongParser.AssignFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignFunc)
        self._la = 0 # Token type
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.paramName()
                self.state = 205
                self.match(clongParser.T__21)
                self.state = 206
                self.exp(0)
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 207
                    self.match(clongParser.T__12)
                    self.state = 208
                    self.assignFunc()


                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeParam(self):
            return self.getTypedRuleContext(clongParser.TypeParamContext,0)


        def paramName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clongParser.ParamNameContext)
            else:
                return self.getTypedRuleContext(clongParser.ParamNameContext,i)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clongParser.ExpContext)
            else:
                return self.getTypedRuleContext(clongParser.ExpContext,i)


        def getRuleIndex(self):
            return clongParser.RULE_initParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitParam" ):
                listener.enterInitParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitParam" ):
                listener.exitInitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitParam" ):
                return visitor.visitInitParam(self)
            else:
                return visitor.visitChildren(self)




    def initParam(self):

        localctx = clongParser.InitParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_initParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.typeParam()
            self.state = 215
            self.paramName()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 216
                self.match(clongParser.T__21)
                self.state = 217
                self.exp(0)


            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 220
                self.match(clongParser.T__12)
                self.state = 221
                self.paramName()
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 222
                    self.match(clongParser.T__21)
                    self.state = 223
                    self.exp(0)


                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 231
            self.match(clongParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeParam(self):
            return self.getTypedRuleContext(clongParser.TypeParamContext,0)


        def paramName(self):
            return self.getTypedRuleContext(clongParser.ParamNameContext,0)


        def intm(self):
            return self.getTypedRuleContext(clongParser.IntmContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_initArray

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitArray" ):
                listener.enterInitArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitArray" ):
                listener.exitInitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitArray" ):
                return visitor.visitInitArray(self)
            else:
                return visitor.visitChildren(self)




    def initArray(self):

        localctx = clongParser.InitArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_initArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.typeParam()
            self.state = 234
            self.paramName()
            self.state = 235
            self.match(clongParser.T__22)
            self.state = 236
            self.intm()
            self.state = 237
            self.match(clongParser.T__23)
            self.state = 238
            self.match(clongParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(clongParser.ExpContext,0)


        def paramName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clongParser.ParamNameContext)
            else:
                return self.getTypedRuleContext(clongParser.ParamNameContext,i)


        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clongParser.ArrayContext)
            else:
                return self.getTypedRuleContext(clongParser.ArrayContext,i)


        def getRuleIndex(self):
            return clongParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = clongParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 242
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        self.state = 240
                        self.paramName()
                        pass

                    elif la_ == 2:
                        self.state = 241
                        self.array()
                        pass


                    self.state = 244
                    self.match(clongParser.T__21)

                else:
                    raise NoViableAltException(self)
                self.state = 248 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 250
            self.exp(0)
            self.state = 252
            self.match(clongParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def charm(self):
            return self.getTypedRuleContext(clongParser.CharmContext,0)


        def stringm(self):
            return self.getTypedRuleContext(clongParser.StringmContext,0)


        def paramName(self):
            return self.getTypedRuleContext(clongParser.ParamNameContext,0)


        def intm(self):
            return self.getTypedRuleContext(clongParser.IntmContext,0)


        def doublem(self):
            return self.getTypedRuleContext(clongParser.DoublemContext,0)


        def array(self):
            return self.getTypedRuleContext(clongParser.ArrayContext,0)


        def func(self):
            return self.getTypedRuleContext(clongParser.FuncContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clongParser.ExpContext)
            else:
                return self.getTypedRuleContext(clongParser.ExpContext,i)


        def getRuleIndex(self):
            return clongParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = clongParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 255
                self.charm()
                pass

            elif la_ == 2:
                self.state = 256
                self.stringm()
                pass

            elif la_ == 3:
                self.state = 257
                self.paramName()
                pass

            elif la_ == 4:
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 258
                    localctx.op = self.match(clongParser.T__24)


                self.state = 263
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [41]:
                    self.state = 261
                    self.intm()
                    pass
                elif token in [42]:
                    self.state = 262
                    self.doublem()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 5:
                self.state = 265
                self.array()
                pass

            elif la_ == 6:
                self.state = 266
                self.func()
                pass

            elif la_ == 7:
                self.state = 267
                self.match(clongParser.T__11)
                self.state = 268
                self.exp(0)
                self.state = 269
                self.match(clongParser.T__13)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = clongParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 273
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 274
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1040187392) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 275
                    self.exp(2) 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clongParser.ConditionContext)
            else:
                return self.getTypedRuleContext(clongParser.ConditionContext,i)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clongParser.ExpContext)
            else:
                return self.getTypedRuleContext(clongParser.ExpContext,i)


        def getRuleIndex(self):
            return clongParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = clongParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_condition, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 282
                self.match(clongParser.T__11)
                self.state = 283
                self.condition(0)
                self.state = 284
                self.match(clongParser.T__13)
                pass

            elif la_ == 2:
                self.state = 286
                self.exp(0)
                self.state = 287
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127372) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 288
                self.exp(0)
                pass

            elif la_ == 3:
                self.state = 290
                self.match(clongParser.T__33)
                self.state = 291
                self.condition(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 299
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = clongParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 294
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 295
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==35 or _la==36):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 296
                    self.condition(2) 
                self.state = 301
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return clongParser.RULE_typeParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeParam" ):
                listener.enterTypeParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeParam" ):
                listener.exitTypeParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeParam" ):
                return visitor.visitTypeParam(self)
            else:
                return visitor.visitChildren(self)




    def typeParam(self):

        localctx = clongParser.TypeParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typeParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 412316860432) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramName(self):
            return self.getTypedRuleContext(clongParser.ParamNameContext,0)


        def exp(self):
            return self.getTypedRuleContext(clongParser.ExpContext,0)


        def getRuleIndex(self):
            return clongParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = clongParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.paramName()
            self.state = 305
            self.match(clongParser.T__22)
            self.state = 306
            self.exp(0)
            self.state = 307
            self.match(clongParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LibraryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAR(self):
            return self.getToken(clongParser.PAR, 0)

        def getRuleIndex(self):
            return clongParser.RULE_library

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLibrary" ):
                listener.enterLibrary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLibrary" ):
                listener.exitLibrary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLibrary" ):
                return visitor.visitLibrary(self)
            else:
                return visitor.visitChildren(self)




    def library(self):

        localctx = clongParser.LibraryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_library)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(clongParser.PAR)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 310
                self.match(clongParser.T__38)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAR(self):
            return self.getToken(clongParser.PAR, 0)

        def getRuleIndex(self):
            return clongParser.RULE_paramName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamName" ):
                listener.enterParamName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamName" ):
                listener.exitParamName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamName" ):
                return visitor.visitParamName(self)
            else:
                return visitor.visitChildren(self)




    def paramName(self):

        localctx = clongParser.ParamNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_paramName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(clongParser.PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(clongParser.INT, 0)

        def getRuleIndex(self):
            return clongParser.RULE_intm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntm" ):
                listener.enterIntm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntm" ):
                listener.exitIntm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntm" ):
                return visitor.visitIntm(self)
            else:
                return visitor.visitChildren(self)




    def intm(self):

        localctx = clongParser.IntmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_intm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(clongParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoublemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE(self):
            return self.getToken(clongParser.DOUBLE, 0)

        def getRuleIndex(self):
            return clongParser.RULE_doublem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoublem" ):
                listener.enterDoublem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoublem" ):
                listener.exitDoublem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoublem" ):
                return visitor.visitDoublem(self)
            else:
                return visitor.visitChildren(self)




    def doublem(self):

        localctx = clongParser.DoublemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_doublem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(clongParser.DOUBLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(clongParser.CHAR, 0)

        def getRuleIndex(self):
            return clongParser.RULE_charm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharm" ):
                listener.enterCharm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharm" ):
                listener.exitCharm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharm" ):
                return visitor.visitCharm(self)
            else:
                return visitor.visitChildren(self)




    def charm(self):

        localctx = clongParser.CharmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_charm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(clongParser.CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(clongParser.STRING, 0)

        def getRuleIndex(self):
            return clongParser.RULE_stringm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringm" ):
                listener.enterStringm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringm" ):
                listener.exitStringm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringm" ):
                return visitor.visitStringm(self)
            else:
                return visitor.visitChildren(self)




    def stringm(self):

        localctx = clongParser.StringmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_stringm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(clongParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.exp_sempred
        self._predicates[23] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




