# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\2\7\2\23\n\2\f\2\16\2\26\13\2\3\2\7\2\31\n")
        buf.write("\2\f\2\16\2\34\13\2\3\2\7\2\37\n\2\f\2\16\2\"\13\2\3\2")
        buf.write("\5\2%\n\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\6\6\60\n")
        buf.write("\6\r\6\16\6\61\3\6\3\6\3\7\3\7\3\7\2\2\b\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\3\2\6\3\2\63;\3\2\62;\4\2\62;aa\5\2\13\f\17")
        buf.write("\17\"\"\2<\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3$\3\2\2\2\5&\3\2\2\2\7")
        buf.write("(\3\2\2\2\t*\3\2\2\2\13/\3\2\2\2\r\65\3\2\2\2\17%\7\62")
        buf.write("\2\2\20\24\t\2\2\2\21\23\t\3\2\2\22\21\3\2\2\2\23\26\3")
        buf.write("\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25\32\3\2\2\2\26\24")
        buf.write("\3\2\2\2\27\31\t\4\2\2\30\27\3\2\2\2\31\34\3\2\2\2\32")
        buf.write("\30\3\2\2\2\32\33\3\2\2\2\33 \3\2\2\2\34\32\3\2\2\2\35")
        buf.write("\37\t\3\2\2\36\35\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3")
        buf.write("\2\2\2!#\3\2\2\2\" \3\2\2\2#%\b\2\2\2$\17\3\2\2\2$\20")
        buf.write("\3\2\2\2%\4\3\2\2\2&\'\7=\2\2\'\6\3\2\2\2()\7<\2\2)\b")
        buf.write("\3\2\2\2*+\7X\2\2+,\7c\2\2,-\7t\2\2-\n\3\2\2\2.\60\t\5")
        buf.write("\2\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2")
        buf.write("\62\63\3\2\2\2\63\64\b\6\3\2\64\f\3\2\2\2\65\66\13\2\2")
        buf.write("\2\66\67\b\7\4\2\67\16\3\2\2\2\b\2\24\32 $\61\5\3\2\2")
        buf.write("\b\2\2\3\7\3")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PHPINT = 1
    SEMI = 2
    COLON = 3
    VAR = 4
    WS = 5
    ERROR_CHAR = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>",
            "PHPINT", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR" ]

    ruleNames = [ "PHPINT", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.PHPINT_action 
            actions[5] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def PHPINT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     


