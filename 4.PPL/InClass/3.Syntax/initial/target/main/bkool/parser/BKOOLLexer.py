# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("h\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\6\fJ\n\f\r\f\16\fK\3")
        buf.write("\r\6\rO\n\r\r\r\16\rP\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\20\3\20\3\21\3\21\3\22\3\22\3\23\6\23`\n\23\r\23\16\23")
        buf.write("a\3\23\3\23\3\24\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25\3\2\5\4\2C\\c|\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\2j\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2\5-\3\2\2\2\7")
        buf.write("\63\3\2\2\2\t\65\3\2\2\2\13\67\3\2\2\2\r9\3\2\2\2\17@")
        buf.write("\3\2\2\2\21B\3\2\2\2\23D\3\2\2\2\25F\3\2\2\2\27I\3\2\2")
        buf.write("\2\31N\3\2\2\2\33R\3\2\2\2\35V\3\2\2\2\37X\3\2\2\2!Z\3")
        buf.write("\2\2\2#\\\3\2\2\2%_\3\2\2\2\'e\3\2\2\2)*\7k\2\2*+\7p\2")
        buf.write("\2+,\7v\2\2,\4\3\2\2\2-.\7h\2\2./\7n\2\2/\60\7q\2\2\60")
        buf.write("\61\7c\2\2\61\62\7v\2\2\62\6\3\2\2\2\63\64\7}\2\2\64\b")
        buf.write("\3\2\2\2\65\66\7\177\2\2\66\n\3\2\2\2\678\7?\2\28\f\3")
        buf.write("\2\2\29:\7t\2\2:;\7g\2\2;<\7v\2\2<=\7w\2\2=>\7t\2\2>?")
        buf.write("\7p\2\2?\16\3\2\2\2@A\7-\2\2A\20\3\2\2\2BC\7/\2\2C\22")
        buf.write("\3\2\2\2DE\7,\2\2E\24\3\2\2\2FG\7\61\2\2G\26\3\2\2\2H")
        buf.write("J\t\2\2\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2L\30")
        buf.write("\3\2\2\2MO\t\3\2\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2")
        buf.write("\2\2Q\32\3\2\2\2RS\5\31\r\2ST\7\60\2\2TU\5\31\r\2U\34")
        buf.write("\3\2\2\2VW\7=\2\2W\36\3\2\2\2XY\7.\2\2Y \3\2\2\2Z[\7*")
        buf.write("\2\2[\"\3\2\2\2\\]\7+\2\2]$\3\2\2\2^`\t\4\2\2_^\3\2\2")
        buf.write("\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2bc\3\2\2\2cd\b\23\2\2")
        buf.write("d&\3\2\2\2ef\13\2\2\2fg\b\24\3\2g(\3\2\2\2\6\2KPa\4\b")
        buf.write("\2\2\3\24\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    ID = 11
    INTLIT = 12
    FLOATLIT = 13
    SM = 14
    CM = 15
    LB = 16
    RB = 17
    WS = 18
    ERROR_CHAR = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'{'", "'}'", "'='", "'return'", "'+'", 
            "'-'", "'*'", "'/'", "';'", "','", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INTLIT", "FLOATLIT", "SM", "CM", "LB", "RB", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "ID", "INTLIT", "FLOATLIT", "SM", 
                  "CM", "LB", "RB", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[18] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


