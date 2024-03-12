# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0187\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\7\2X\n\2\f\2\16")
        buf.write("\2[\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3d\n\3\3\4\3\4")
        buf.write("\3\4\3\4\5\4j\n\4\3\5\3\5\3\5\5\5o\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7{\n\7\3\7\5\7~\n\7\3\b\3\b")
        buf.write("\3\b\5\b\u0083\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u008c")
        buf.write("\n\n\3\13\6\13\u008f\n\13\r\13\16\13\u0090\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u0098\n\f\3\f\3\f\3\f\5\f\u009d\n\f\3\f\3")
        buf.write("\f\5\f\u00a1\n\f\3\f\5\f\u00a4\n\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00ab\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00b4\n\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\5\20\u00bd")
        buf.write("\n\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u00c6\n")
        buf.write("\22\3\23\3\23\3\23\3\23\3\23\5\23\u00cd\n\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\7\24\u00d5\n\24\f\24\16\24\u00d8")
        buf.write("\13\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00e0\n\25\f")
        buf.write("\25\16\25\u00e3\13\25\3\26\3\26\3\26\3\26\3\26\3\26\7")
        buf.write("\26\u00eb\n\26\f\26\16\26\u00ee\13\26\3\27\3\27\3\27\5")
        buf.write("\27\u00f3\n\27\3\30\3\30\3\30\5\30\u00f8\n\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u00ff\n\31\3\32\3\32\3\32\3\32\3")
        buf.write("\33\3\33\5\33\u0107\n\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\5\34\u0110\n\34\3\34\3\34\3\35\3\35\3\35\3\35\3")
        buf.write("\36\3\36\3\36\3\36\3\36\5\36\u011d\n\36\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u0123\n\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \5 \u0130\n \3!\3!\3!\3!\3!\5!\u0137\n!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\5\"\u0142\n\"\3\"\3\"\3\"\3#\3#\3#")
        buf.write("\3#\3#\5#\u014c\n#\3$\3$\3$\3$\3$\5$\u0153\n$\3$\3$\3")
        buf.write("%\3%\5%\u0159\n%\3%\3%\3&\3&\3&\3&\3&\3&\3&\5&\u0164\n")
        buf.write("&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\5)\u0171\n)\3)\3")
        buf.write(")\3*\3*\3*\3*\5*\u0179\n*\3*\3*\3*\3+\3+\3+\3+\5+\u0182")
        buf.write("\n+\3+\3+\3+\3+\2\5&(*,\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRT\2\7\3\2")
        buf.write("\5\7\5\2\36\36 $&&\3\2\27\30\3\2\31\32\3\2\33\35\2\u0192")
        buf.write("\2Y\3\2\2\2\4c\3\2\2\2\6i\3\2\2\2\bn\3\2\2\2\np\3\2\2")
        buf.write("\2\ft\3\2\2\2\16\177\3\2\2\2\20\u0084\3\2\2\2\22\u008b")
        buf.write("\3\2\2\2\24\u008e\3\2\2\2\26\u0092\3\2\2\2\30\u00aa\3")
        buf.write("\2\2\2\32\u00ac\3\2\2\2\34\u00b5\3\2\2\2\36\u00bc\3\2")
        buf.write("\2\2 \u00be\3\2\2\2\"\u00c5\3\2\2\2$\u00cc\3\2\2\2&\u00ce")
        buf.write("\3\2\2\2(\u00d9\3\2\2\2*\u00e4\3\2\2\2,\u00f2\3\2\2\2")
        buf.write(".\u00f7\3\2\2\2\60\u00fe\3\2\2\2\62\u0100\3\2\2\2\64\u0106")
        buf.write("\3\2\2\2\66\u010c\3\2\2\28\u0113\3\2\2\2:\u011c\3\2\2")
        buf.write("\2<\u0122\3\2\2\2>\u012f\3\2\2\2@\u0131\3\2\2\2B\u013c")
        buf.write("\3\2\2\2D\u014b\3\2\2\2F\u014d\3\2\2\2H\u0156\3\2\2\2")
        buf.write("J\u015c\3\2\2\2L\u0167\3\2\2\2N\u016a\3\2\2\2P\u016d\3")
        buf.write("\2\2\2R\u0174\3\2\2\2T\u017d\3\2\2\2VX\7\60\2\2WV\3\2")
        buf.write("\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2")
        buf.write("\2\\]\5\4\3\2]^\7\2\2\3^\3\3\2\2\2_`\5\6\4\2`a\5\4\3\2")
        buf.write("ad\3\2\2\2bd\5\6\4\2c_\3\2\2\2cb\3\2\2\2d\5\3\2\2\2ef")
        buf.write("\5\b\5\2fg\5\24\13\2gj\3\2\2\2hj\5\26\f\2ie\3\2\2\2ih")
        buf.write("\3\2\2\2j\7\3\2\2\2ko\5\n\6\2lo\5\f\7\2mo\5\16\b\2nk\3")
        buf.write("\2\2\2nl\3\2\2\2nm\3\2\2\2o\t\3\2\2\2pq\7\t\2\2qr\7\62")
        buf.write("\2\2rs\5\20\t\2s\13\3\2\2\2tu\5\34\17\2uz\7\62\2\2vw\7")
        buf.write(")\2\2wx\5\22\n\2xy\7*\2\2y{\3\2\2\2zv\3\2\2\2z{\3\2\2")
        buf.write("\2{}\3\2\2\2|~\5\20\t\2}|\3\2\2\2}~\3\2\2\2~\r\3\2\2\2")
        buf.write("\177\u0080\7\n\2\2\u0080\u0082\7\62\2\2\u0081\u0083\5")
        buf.write("\20\t\2\u0082\u0081\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\17\3\2\2\2\u0084\u0085\7\37\2\2\u0085\u0086\5 \21\2\u0086")
        buf.write("\21\3\2\2\2\u0087\u0088\7-\2\2\u0088\u0089\7+\2\2\u0089")
        buf.write("\u008c\5\22\n\2\u008a\u008c\7-\2\2\u008b\u0087\3\2\2\2")
        buf.write("\u008b\u008a\3\2\2\2\u008c\23\3\2\2\2\u008d\u008f\7\60")
        buf.write("\2\2\u008e\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u008e")
        buf.write("\3\2\2\2\u0090\u0091\3\2\2\2\u0091\25\3\2\2\2\u0092\u0093")
        buf.write("\7\13\2\2\u0093\u0094\7\62\2\2\u0094\u0097\7\'\2\2\u0095")
        buf.write("\u0098\5\30\r\2\u0096\u0098\3\2\2\2\u0097\u0095\3\2\2")
        buf.write("\2\u0097\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u00a3")
        buf.write("\7(\2\2\u009a\u00a4\5\24\13\2\u009b\u009d\5\24\13\2\u009c")
        buf.write("\u009b\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\u00a4\5T+\2\u009f\u00a1\5\24\13\2\u00a0\u009f\3")
        buf.write("\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4")
        buf.write("\5P)\2\u00a3\u009a\3\2\2\2\u00a3\u009c\3\2\2\2\u00a3\u00a0")
        buf.write("\3\2\2\2\u00a4\27\3\2\2\2\u00a5\u00a6\5\32\16\2\u00a6")
        buf.write("\u00a7\7+\2\2\u00a7\u00a8\5\30\r\2\u00a8\u00ab\3\2\2\2")
        buf.write("\u00a9\u00ab\5\32\16\2\u00aa\u00a5\3\2\2\2\u00aa\u00a9")
        buf.write("\3\2\2\2\u00ab\31\3\2\2\2\u00ac\u00ad\5\34\17\2\u00ad")
        buf.write("\u00b3\7\62\2\2\u00ae\u00af\7)\2\2\u00af\u00b0\5\22\n")
        buf.write("\2\u00b0\u00b1\7*\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b4")
        buf.write("\3\2\2\2\u00b3\u00ae\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4")
        buf.write("\33\3\2\2\2\u00b5\u00b6\t\2\2\2\u00b6\35\3\2\2\2\u00b7")
        buf.write("\u00b8\5 \21\2\u00b8\u00b9\7+\2\2\u00b9\u00ba\5\36\20")
        buf.write("\2\u00ba\u00bd\3\2\2\2\u00bb\u00bd\5 \21\2\u00bc\u00b7")
        buf.write("\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\37\3\2\2\2\u00be\u00bf")
        buf.write("\5\"\22\2\u00bf!\3\2\2\2\u00c0\u00c1\5$\23\2\u00c1\u00c2")
        buf.write("\7%\2\2\u00c2\u00c3\5$\23\2\u00c3\u00c6\3\2\2\2\u00c4")
        buf.write("\u00c6\5$\23\2\u00c5\u00c0\3\2\2\2\u00c5\u00c4\3\2\2\2")
        buf.write("\u00c6#\3\2\2\2\u00c7\u00c8\5&\24\2\u00c8\u00c9\t\3\2")
        buf.write("\2\u00c9\u00ca\5&\24\2\u00ca\u00cd\3\2\2\2\u00cb\u00cd")
        buf.write("\5&\24\2\u00cc\u00c7\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd")
        buf.write("%\3\2\2\2\u00ce\u00cf\b\24\1\2\u00cf\u00d0\5(\25\2\u00d0")
        buf.write("\u00d6\3\2\2\2\u00d1\u00d2\f\4\2\2\u00d2\u00d3\t\4\2\2")
        buf.write("\u00d3\u00d5\5(\25\2\u00d4\u00d1\3\2\2\2\u00d5\u00d8\3")
        buf.write("\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\'")
        buf.write("\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00da\b\25\1\2\u00da")
        buf.write("\u00db\5*\26\2\u00db\u00e1\3\2\2\2\u00dc\u00dd\f\4\2\2")
        buf.write("\u00dd\u00de\t\5\2\2\u00de\u00e0\5*\26\2\u00df\u00dc\3")
        buf.write("\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2")
        buf.write("\3\2\2\2\u00e2)\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5")
        buf.write("\b\26\1\2\u00e5\u00e6\5,\27\2\u00e6\u00ec\3\2\2\2\u00e7")
        buf.write("\u00e8\f\4\2\2\u00e8\u00e9\t\6\2\2\u00e9\u00eb\5,\27\2")
        buf.write("\u00ea\u00e7\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3")
        buf.write("\2\2\2\u00ec\u00ed\3\2\2\2\u00ed+\3\2\2\2\u00ee\u00ec")
        buf.write("\3\2\2\2\u00ef\u00f0\7\26\2\2\u00f0\u00f3\5,\27\2\u00f1")
        buf.write("\u00f3\5.\30\2\u00f2\u00ef\3\2\2\2\u00f2\u00f1\3\2\2\2")
        buf.write("\u00f3-\3\2\2\2\u00f4\u00f5\t\5\2\2\u00f5\u00f8\5.\30")
        buf.write("\2\u00f6\u00f8\5\60\31\2\u00f7\u00f4\3\2\2\2\u00f7\u00f6")
        buf.write("\3\2\2\2\u00f8/\3\2\2\2\u00f9\u00ff\5\62\32\2\u00fa\u00ff")
        buf.write("\5\64\33\2\u00fb\u00ff\5\66\34\2\u00fc\u00ff\7\62\2\2")
        buf.write("\u00fd\u00ff\5:\36\2\u00fe\u00f9\3\2\2\2\u00fe\u00fa\3")
        buf.write("\2\2\2\u00fe\u00fb\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd")
        buf.write("\3\2\2\2\u00ff\61\3\2\2\2\u0100\u0101\7\'\2\2\u0101\u0102")
        buf.write("\5 \21\2\u0102\u0103\7(\2\2\u0103\63\3\2\2\2\u0104\u0107")
        buf.write("\7\62\2\2\u0105\u0107\5\66\34\2\u0106\u0104\3\2\2\2\u0106")
        buf.write("\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\7)\2\2")
        buf.write("\u0109\u010a\5\36\20\2\u010a\u010b\7*\2\2\u010b\65\3\2")
        buf.write("\2\2\u010c\u010d\7\62\2\2\u010d\u010f\7\'\2\2\u010e\u0110")
        buf.write("\5\36\20\2\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u0112\7(\2\2\u0112\67\3\2\2\2\u0113")
        buf.write("\u0114\7)\2\2\u0114\u0115\5\36\20\2\u0115\u0116\7*\2\2")
        buf.write("\u01169\3\2\2\2\u0117\u011d\7-\2\2\u0118\u011d\7\3\2\2")
        buf.write("\u0119\u011d\7\4\2\2\u011a\u011d\7/\2\2\u011b\u011d\5")
        buf.write("8\35\2\u011c\u0117\3\2\2\2\u011c\u0118\3\2\2\2\u011c\u0119")
        buf.write("\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011b\3\2\2\2\u011d")
        buf.write(";\3\2\2\2\u011e\u011f\5> \2\u011f\u0120\5<\37\2\u0120")
        buf.write("\u0123\3\2\2\2\u0121\u0123\5> \2\u0122\u011e\3\2\2\2\u0122")
        buf.write("\u0121\3\2\2\2\u0123=\3\2\2\2\u0124\u0125\5\b\5\2\u0125")
        buf.write("\u0126\5\24\13\2\u0126\u0130\3\2\2\2\u0127\u0130\5@!\2")
        buf.write("\u0128\u0130\5B\"\2\u0129\u0130\5J&\2\u012a\u0130\5L\'")
        buf.write("\2\u012b\u0130\5N(\2\u012c\u0130\5P)\2\u012d\u0130\5R")
        buf.write("*\2\u012e\u0130\5T+\2\u012f\u0124\3\2\2\2\u012f\u0127")
        buf.write("\3\2\2\2\u012f\u0128\3\2\2\2\u012f\u0129\3\2\2\2\u012f")
        buf.write("\u012a\3\2\2\2\u012f\u012b\3\2\2\2\u012f\u012c\3\2\2\2")
        buf.write("\u012f\u012d\3\2\2\2\u012f\u012e\3\2\2\2\u0130?\3\2\2")
        buf.write("\2\u0131\u0136\7\62\2\2\u0132\u0133\7)\2\2\u0133\u0134")
        buf.write("\5\36\20\2\u0134\u0135\7*\2\2\u0135\u0137\3\2\2\2\u0136")
        buf.write("\u0132\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\u0139\7\37\2\2\u0139\u013a\5 \21\2\u013a\u013b")
        buf.write("\5\24\13\2\u013bA\3\2\2\2\u013c\u013d\7\21\2\2\u013d\u013e")
        buf.write("\7\'\2\2\u013e\u013f\5 \21\2\u013f\u0141\7(\2\2\u0140")
        buf.write("\u0142\5\24\13\2\u0141\u0140\3\2\2\2\u0141\u0142\3\2\2")
        buf.write("\2\u0142\u0143\3\2\2\2\u0143\u0144\5> \2\u0144\u0145\5")
        buf.write("D#\2\u0145C\3\2\2\2\u0146\u0147\5F$\2\u0147\u0148\5D#")
        buf.write("\2\u0148\u014c\3\2\2\2\u0149\u014c\5H%\2\u014a\u014c\3")
        buf.write("\2\2\2\u014b\u0146\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014a")
        buf.write("\3\2\2\2\u014cE\3\2\2\2\u014d\u014e\7\23\2\2\u014e\u014f")
        buf.write("\7\'\2\2\u014f\u0150\5 \21\2\u0150\u0152\7(\2\2\u0151")
        buf.write("\u0153\5\24\13\2\u0152\u0151\3\2\2\2\u0152\u0153\3\2\2")
        buf.write("\2\u0153\u0154\3\2\2\2\u0154\u0155\5> \2\u0155G\3\2\2")
        buf.write("\2\u0156\u0158\7\22\2\2\u0157\u0159\5\24\13\2\u0158\u0157")
        buf.write("\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("\u015b\5> \2\u015bI\3\2\2\2\u015c\u015d\7\f\2\2\u015d")
        buf.write("\u015e\7\62\2\2\u015e\u015f\7\r\2\2\u015f\u0160\5 \21")
        buf.write("\2\u0160\u0161\7\16\2\2\u0161\u0163\5 \21\2\u0162\u0164")
        buf.write("\5\24\13\2\u0163\u0162\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("\u0165\3\2\2\2\u0165\u0166\5> \2\u0166K\3\2\2\2\u0167")
        buf.write("\u0168\7\17\2\2\u0168\u0169\5\24\13\2\u0169M\3\2\2\2\u016a")
        buf.write("\u016b\7\20\2\2\u016b\u016c\5\24\13\2\u016cO\3\2\2\2\u016d")
        buf.write("\u0170\7\b\2\2\u016e\u0171\5 \21\2\u016f\u0171\3\2\2\2")
        buf.write("\u0170\u016e\3\2\2\2\u0170\u016f\3\2\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172\u0173\5\24\13\2\u0173Q\3\2\2\2\u0174\u0175")
        buf.write("\7\62\2\2\u0175\u0178\7\'\2\2\u0176\u0179\5\36\20\2\u0177")
        buf.write("\u0179\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2")
        buf.write("\u0179\u017a\3\2\2\2\u017a\u017b\7(\2\2\u017b\u017c\5")
        buf.write("\24\13\2\u017cS\3\2\2\2\u017d\u017e\7\24\2\2\u017e\u0181")
        buf.write("\5\24\13\2\u017f\u0182\5<\37\2\u0180\u0182\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0181\u0180\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183\u0184\7\25\2\2\u0184\u0185\5\24\13\2\u0185U\3\2")
        buf.write("\2\2(Ycinz}\u0082\u008b\u0090\u0097\u009c\u00a0\u00a3")
        buf.write("\u00aa\u00b3\u00bc\u00c5\u00cc\u00d6\u00e1\u00ec\u00f2")
        buf.write("\u00f7\u00fe\u0106\u010f\u011c\u0122\u012f\u0136\u0141")
        buf.write("\u014b\u0152\u0158\u0163\u0170\u0178\u0181")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQ", "ASSIGN", "NEQ", "LT", "LTE", "GT", "GTE", 
                      "CONCAT", "COMPARE", "LPAREN", "RPAREN", "LBRACK", 
                      "RBRACK", "COMMA", "WS", "NUMLIT", "BOOLIT", "STRLIT", 
                      "NEWLINE", "CMT", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declLst = 1
    RULE_decl = 2
    RULE_varDecl = 3
    RULE_varDeclCase1 = 4
    RULE_varDeclCase2 = 5
    RULE_varDeclCase3 = 6
    RULE_declare = 7
    RULE_dimenslist = 8
    RULE_ignore = 9
    RULE_funDecl = 10
    RULE_paramLst = 11
    RULE_paramDecl = 12
    RULE_dataType = 13
    RULE_exprLst = 14
    RULE_expr = 15
    RULE_expr1 = 16
    RULE_expr2 = 17
    RULE_expr3 = 18
    RULE_expr4 = 19
    RULE_expr5 = 20
    RULE_expr6 = 21
    RULE_expr7 = 22
    RULE_operand = 23
    RULE_subexpr = 24
    RULE_arrayEle = 25
    RULE_funccall = 26
    RULE_arrayLit = 27
    RULE_literal = 28
    RULE_stmtLst = 29
    RULE_stmt = 30
    RULE_assignmentStmt = 31
    RULE_ifStmt = 32
    RULE_elifLst = 33
    RULE_elifEle = 34
    RULE_elseClause = 35
    RULE_forStmt = 36
    RULE_breakStmt = 37
    RULE_continueStmt = 38
    RULE_returnStmt = 39
    RULE_funCallStmt = 40
    RULE_blockStmt = 41

    ruleNames =  [ "program", "declLst", "decl", "varDecl", "varDeclCase1", 
                   "varDeclCase2", "varDeclCase3", "declare", "dimenslist", 
                   "ignore", "funDecl", "paramLst", "paramDecl", "dataType", 
                   "exprLst", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "operand", "subexpr", "arrayEle", 
                   "funccall", "arrayLit", "literal", "stmtLst", "stmt", 
                   "assignmentStmt", "ifStmt", "elifLst", "elifEle", "elseClause", 
                   "forStmt", "breakStmt", "continueStmt", "returnStmt", 
                   "funCallStmt", "blockStmt" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    EQ=28
    ASSIGN=29
    NEQ=30
    LT=31
    LTE=32
    GT=33
    GTE=34
    CONCAT=35
    COMPARE=36
    LPAREN=37
    RPAREN=38
    LBRACK=39
    RBRACK=40
    COMMA=41
    WS=42
    NUMLIT=43
    BOOLIT=44
    STRLIT=45
    NEWLINE=46
    CMT=47
    ID=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declLst(self):
            return self.getTypedRuleContext(ZCodeParser.DeclLstContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 84
                self.match(ZCodeParser.NEWLINE)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.declLst()
            self.state = 91
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def declLst(self):
            return self.getTypedRuleContext(ZCodeParser.DeclLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclLst" ):
                return visitor.visitDeclLst(self)
            else:
                return visitor.visitChildren(self)




    def declLst(self):

        localctx = ZCodeParser.DeclLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declLst)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.decl()
                self.state = 94
                self.declLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(ZCodeParser.VarDeclContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def funDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.varDecl()
                self.state = 100
                self.ignore()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.funDecl()
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


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclCase1(self):
            return self.getTypedRuleContext(ZCodeParser.VarDeclCase1Context,0)


        def varDeclCase2(self):
            return self.getTypedRuleContext(ZCodeParser.VarDeclCase2Context,0)


        def varDeclCase3(self):
            return self.getTypedRuleContext(ZCodeParser.VarDeclCase3Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = ZCodeParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDecl)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.varDeclCase1()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.varDeclCase2()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.varDeclCase3()
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


    class VarDeclCase1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def declare(self):
            return self.getTypedRuleContext(ZCodeParser.DeclareContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varDeclCase1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclCase1" ):
                return visitor.visitVarDeclCase1(self)
            else:
                return visitor.visitChildren(self)




    def varDeclCase1(self):

        localctx = ZCodeParser.VarDeclCase1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDeclCase1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(ZCodeParser.VAR)
            self.state = 111
            self.match(ZCodeParser.ID)
            self.state = 112
            self.declare()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclCase2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataType(self):
            return self.getTypedRuleContext(ZCodeParser.DataTypeContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def dimenslist(self):
            return self.getTypedRuleContext(ZCodeParser.DimenslistContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def declare(self):
            return self.getTypedRuleContext(ZCodeParser.DeclareContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varDeclCase2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclCase2" ):
                return visitor.visitVarDeclCase2(self)
            else:
                return visitor.visitChildren(self)




    def varDeclCase2(self):

        localctx = ZCodeParser.VarDeclCase2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDeclCase2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.dataType()
            self.state = 115
            self.match(ZCodeParser.ID)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LBRACK:
                self.state = 116
                self.match(ZCodeParser.LBRACK)
                self.state = 117
                self.dimenslist()
                self.state = 118
                self.match(ZCodeParser.RBRACK)


            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 122
                self.declare()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclCase3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def declare(self):
            return self.getTypedRuleContext(ZCodeParser.DeclareContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varDeclCase3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclCase3" ):
                return visitor.visitVarDeclCase3(self)
            else:
                return visitor.visitChildren(self)




    def varDeclCase3(self):

        localctx = ZCodeParser.VarDeclCase3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_varDeclCase3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(ZCodeParser.DYNAMIC)
            self.state = 126
            self.match(ZCodeParser.ID)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 127
                self.declare()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare" ):
                return visitor.visitDeclare(self)
            else:
                return visitor.visitChildren(self)




    def declare(self):

        localctx = ZCodeParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ZCodeParser.ASSIGN)
            self.state = 131
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimenslistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def dimenslist(self):
            return self.getTypedRuleContext(ZCodeParser.DimenslistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dimenslist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimenslist" ):
                return visitor.visitDimenslist(self)
            else:
                return visitor.visitChildren(self)




    def dimenslist(self):

        localctx = ZCodeParser.DimenslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dimenslist)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(ZCodeParser.NUMLIT)
                self.state = 134
                self.match(ZCodeParser.COMMA)
                self.state = 135
                self.dimenslist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(ZCodeParser.NUMLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 139
                self.match(ZCodeParser.NEWLINE)
                self.state = 142 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def paramLst(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunDecl" ):
                return visitor.visitFunDecl(self)
            else:
                return visitor.visitChildren(self)




    def funDecl(self):

        localctx = ZCodeParser.FunDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ZCodeParser.FUNC)
            self.state = 145
            self.match(ZCodeParser.ID)
            self.state = 146
            self.match(ZCodeParser.LPAREN)
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 147
                self.paramLst()
                pass
            elif token in [ZCodeParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 151
            self.match(ZCodeParser.RPAREN)
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 152
                self.ignore()
                pass

            elif la_ == 2:
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 153
                    self.ignore()


                self.state = 156
                self.blockStmt()
                pass

            elif la_ == 3:
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 157
                    self.ignore()


                self.state = 160
                self.returnStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramDecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramLst(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamLst" ):
                return visitor.visitParamLst(self)
            else:
                return visitor.visitChildren(self)




    def paramLst(self):

        localctx = ZCodeParser.ParamLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paramLst)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.paramDecl()
                self.state = 164
                self.match(ZCodeParser.COMMA)
                self.state = 165
                self.paramLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.paramDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataType(self):
            return self.getTypedRuleContext(ZCodeParser.DataTypeContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def dimenslist(self):
            return self.getTypedRuleContext(ZCodeParser.DimenslistContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paramDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDecl" ):
                return visitor.visitParamDecl(self)
            else:
                return visitor.visitChildren(self)




    def paramDecl(self):

        localctx = ZCodeParser.ParamDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paramDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.dataType()
            self.state = 171
            self.match(ZCodeParser.ID)
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LBRACK]:
                self.state = 172
                self.match(ZCodeParser.LBRACK)
                self.state = 173
                self.dimenslist()
                self.state = 174
                self.match(ZCodeParser.RBRACK)
                pass
            elif token in [ZCodeParser.RPAREN, ZCodeParser.COMMA]:
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


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_dataType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = ZCodeParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
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


    class ExprLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def exprLst(self):
            return self.getTypedRuleContext(ZCodeParser.ExprLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLst" ):
                return visitor.visitExprLst(self)
            else:
                return visitor.visitChildren(self)




    def exprLst(self):

        localctx = ZCodeParser.ExprLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exprLst)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.expr()
                self.state = 182
                self.match(ZCodeParser.COMMA)
                self.state = 183
                self.exprLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(ZCodeParser.Expr1Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.expr1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr1)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.expr2()
                self.state = 191
                self.match(ZCodeParser.CONCAT)
                self.state = 192
                self.expr2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.expr2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr3Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr3Context,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def COMPARE(self):
            return self.getToken(ZCodeParser.COMPARE, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LTE(self):
            return self.getToken(ZCodeParser.LTE, 0)

        def GTE(self):
            return self.getToken(ZCodeParser.GTE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)




    def expr2(self):

        localctx = ZCodeParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr2)
        self._la = 0 # Token type
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.expr3(0)
                self.state = 198
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ) | (1 << ZCodeParser.NEQ) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LTE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GTE) | (1 << ZCodeParser.COMPARE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 199
                self.expr3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.expr3(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 207
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 208
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 209
                    self.expr4(0) 
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 218
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 219
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 220
                    self.expr5(0) 
                self.state = 225
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 229
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 230
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 231
                    self.expr6() 
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr6)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(ZCodeParser.NOT)
                self.state = 238
                self.expr6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.LPAREN, ZCodeParser.LBRACK, ZCodeParser.NUMLIT, ZCodeParser.STRLIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.expr7()
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ADD, ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 243
                self.expr7()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LPAREN, ZCodeParser.LBRACK, ZCodeParser.NUMLIT, ZCodeParser.STRLIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.operand()
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


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subexpr(self):
            return self.getTypedRuleContext(ZCodeParser.SubexprContext,0)


        def arrayEle(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayEleContext,0)


        def funccall(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_operand)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.subexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.arrayEle()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.funccall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 250
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 251
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = ZCodeParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(ZCodeParser.LPAREN)
            self.state = 255
            self.expr()
            self.state = 256
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayEleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def exprLst(self):
            return self.getTypedRuleContext(ZCodeParser.ExprLstContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def funccall(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayEle

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayEle" ):
                return visitor.visitArrayEle(self)
            else:
                return visitor.visitChildren(self)




    def arrayEle(self):

        localctx = ZCodeParser.ArrayEleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arrayEle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 258
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 259
                self.funccall()
                pass


            self.state = 262
            self.match(ZCodeParser.LBRACK)
            self.state = 263
            self.exprLst()
            self.state = 264
            self.match(ZCodeParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def exprLst(self):
            return self.getTypedRuleContext(ZCodeParser.ExprLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = ZCodeParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(ZCodeParser.ID)
            self.state = 267
            self.match(ZCodeParser.LPAREN)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.LBRACK) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.STRLIT) | (1 << ZCodeParser.ID))) != 0):
                self.state = 268
                self.exprLst()


            self.state = 271
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def exprLst(self):
            return self.getTypedRuleContext(ZCodeParser.ExprLstContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLit" ):
                return visitor.visitArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def arrayLit(self):

        localctx = ZCodeParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(ZCodeParser.LBRACK)
            self.state = 274
            self.exprLst()
            self.state = 275
            self.match(ZCodeParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def STRLIT(self):
            return self.getToken(ZCodeParser.STRLIT, 0)

        def arrayLit(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayLitContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_literal)
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 279
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.STRLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.match(ZCodeParser.STRLIT)
                pass
            elif token in [ZCodeParser.LBRACK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 281
                self.arrayLit()
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


    class StmtLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def stmtLst(self):
            return self.getTypedRuleContext(ZCodeParser.StmtLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtLst" ):
                return visitor.visitStmtLst(self)
            else:
                return visitor.visitChildren(self)




    def stmtLst(self):

        localctx = ZCodeParser.StmtLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmtLst)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.stmt()
                self.state = 285
                self.stmtLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(ZCodeParser.VarDeclContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def assignmentStmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignmentStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnStmtContext,0)


        def funCallStmt(self):
            return self.getTypedRuleContext(ZCodeParser.FunCallStmtContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_stmt)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.varDecl()
                self.state = 291
                self.ignore()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.assignmentStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                self.ifStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 295
                self.forStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 296
                self.breakStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 297
                self.continueStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 298
                self.returnStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 299
                self.funCallStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 300
                self.blockStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def exprLst(self):
            return self.getTypedRuleContext(ZCodeParser.ExprLstContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignmentStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStmt" ):
                return visitor.visitAssignmentStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStmt(self):

        localctx = ZCodeParser.AssignmentStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assignmentStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.ID)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LBRACK:
                self.state = 304
                self.match(ZCodeParser.LBRACK)
                self.state = 305
                self.exprLst()
                self.state = 306
                self.match(ZCodeParser.RBRACK)


            self.state = 310
            self.match(ZCodeParser.ASSIGN)
            self.state = 311
            self.expr()
            self.state = 312
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elifLst(self):
            return self.getTypedRuleContext(ZCodeParser.ElifLstContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = ZCodeParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(ZCodeParser.IF)
            self.state = 315
            self.match(ZCodeParser.LPAREN)
            self.state = 316
            self.expr()
            self.state = 317
            self.match(ZCodeParser.RPAREN)
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 318
                self.ignore()


            self.state = 321
            self.stmt()
            self.state = 322
            self.elifLst()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifEle(self):
            return self.getTypedRuleContext(ZCodeParser.ElifEleContext,0)


        def elifLst(self):
            return self.getTypedRuleContext(ZCodeParser.ElifLstContext,0)


        def elseClause(self):
            return self.getTypedRuleContext(ZCodeParser.ElseClauseContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifLst" ):
                return visitor.visitElifLst(self)
            else:
                return visitor.visitChildren(self)




    def elifLst(self):

        localctx = ZCodeParser.ElifLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_elifLst)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.elifEle()
                self.state = 325
                self.elifLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.elseClause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifEleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifEle

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifEle" ):
                return visitor.visitElifEle(self)
            else:
                return visitor.visitChildren(self)




    def elifEle(self):

        localctx = ZCodeParser.ElifEleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elifEle)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(ZCodeParser.ELIF)
            self.state = 332
            self.match(ZCodeParser.LPAREN)
            self.state = 333
            self.expr()
            self.state = 334
            self.match(ZCodeParser.RPAREN)
            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 335
                self.ignore()


            self.state = 338
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elseClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseClause" ):
                return visitor.visitElseClause(self)
            else:
                return visitor.visitChildren(self)




    def elseClause(self):

        localctx = ZCodeParser.ElseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(ZCodeParser.ELSE)
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 341
                self.ignore()


            self.state = 344
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = ZCodeParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(ZCodeParser.FOR)
            self.state = 347
            self.match(ZCodeParser.ID)
            self.state = 348
            self.match(ZCodeParser.UNTIL)
            self.state = 349
            self.expr()
            self.state = 350
            self.match(ZCodeParser.BY)
            self.state = 351
            self.expr()
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 352
                self.ignore()


            self.state = 355
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = ZCodeParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(ZCodeParser.BREAK)
            self.state = 358
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continueStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = ZCodeParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(ZCodeParser.CONTINUE)
            self.state = 361
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = ZCodeParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(ZCodeParser.RETURN)
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.LPAREN, ZCodeParser.LBRACK, ZCodeParser.NUMLIT, ZCodeParser.STRLIT, ZCodeParser.ID]:
                self.state = 364
                self.expr()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 368
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunCallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def exprLst(self):
            return self.getTypedRuleContext(ZCodeParser.ExprLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funCallStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunCallStmt" ):
                return visitor.visitFunCallStmt(self)
            else:
                return visitor.visitChildren(self)




    def funCallStmt(self):

        localctx = ZCodeParser.FunCallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_funCallStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(ZCodeParser.ID)
            self.state = 371
            self.match(ZCodeParser.LPAREN)
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.LPAREN, ZCodeParser.LBRACK, ZCodeParser.NUMLIT, ZCodeParser.STRLIT, ZCodeParser.ID]:
                self.state = 372
                self.exprLst()
                pass
            elif token in [ZCodeParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 376
            self.match(ZCodeParser.RPAREN)
            self.state = 377
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def stmtLst(self):
            return self.getTypedRuleContext(ZCodeParser.StmtLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)




    def blockStmt(self):

        localctx = ZCodeParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_blockStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(ZCodeParser.BEGIN)
            self.state = 380
            self.ignore()
            self.state = 383
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.state = 381
                self.stmtLst()
                pass
            elif token in [ZCodeParser.END]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 385
            self.match(ZCodeParser.END)
            self.state = 386
            self.ignore()
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
        self._predicates[18] = self.expr3_sempred
        self._predicates[19] = self.expr4_sempred
        self._predicates[20] = self.expr5_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




