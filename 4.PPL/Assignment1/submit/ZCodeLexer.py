# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0180\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\5+\u0117\n")
        buf.write("+\3+\5+\u011a\n+\3,\6,\u011d\n,\r,\16,\u011e\3-\3-\7-")
        buf.write("\u0123\n-\f-\16-\u0126\13-\3.\3.\5.\u012a\n.\3.\6.\u012d")
        buf.write("\n.\r.\16.\u012e\3/\3/\5/\u0133\n/\3\60\3\60\7\60\u0137")
        buf.write("\n\60\f\60\16\60\u013a\13\60\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\5\61\u0144\n\61\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\63\7\63\u014c\n\63\f\63\16\63\u014f\13\63\3\63\3")
        buf.write("\63\3\64\3\64\7\64\u0155\n\64\f\64\16\64\u0158\13\64\3")
        buf.write("\65\6\65\u015b\n\65\r\65\16\65\u015c\3\65\3\65\3\66\3")
        buf.write("\66\7\66\u0163\n\66\f\66\16\66\u0166\13\66\3\66\3\66\3")
        buf.write("\66\5\66\u016b\n\66\3\66\3\66\3\67\3\67\7\67\u0171\n\67")
        buf.write("\f\67\16\67\u0174\13\67\3\67\3\67\3\67\38\38\38\58\u017c")
        buf.write("\n8\39\39\39\2\2:\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W\2Y\2[\2]-_.a\2c/e\60g\61i\62")
        buf.write("k\63m\64o\2q\65\3\2\17\3\2\62;\4\2GGgg\4\2--//\3\2$$\6")
        buf.write("\2\f\f\17\17$$^^\t\2))^^ddhhppttvv\3\2\f\f\4\2\f\f\16")
        buf.write("\17\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\13\16\17\"\"\3\3\f")
        buf.write("\f\3\2\17\17\2\u018b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2")
        buf.write("\2\2m\3\2\2\2\2q\3\2\2\2\3s\3\2\2\2\5x\3\2\2\2\7~\3\2")
        buf.write("\2\2\t\u0085\3\2\2\2\13\u008a\3\2\2\2\r\u0091\3\2\2\2")
        buf.write("\17\u0098\3\2\2\2\21\u009c\3\2\2\2\23\u00a4\3\2\2\2\25")
        buf.write("\u00a9\3\2\2\2\27\u00ad\3\2\2\2\31\u00b3\3\2\2\2\33\u00b6")
        buf.write("\3\2\2\2\35\u00bc\3\2\2\2\37\u00c5\3\2\2\2!\u00c8\3\2")
        buf.write("\2\2#\u00cd\3\2\2\2%\u00d2\3\2\2\2\'\u00d8\3\2\2\2)\u00dc")
        buf.write("\3\2\2\2+\u00e0\3\2\2\2-\u00e4\3\2\2\2/\u00e7\3\2\2\2")
        buf.write("\61\u00e9\3\2\2\2\63\u00eb\3\2\2\2\65\u00ed\3\2\2\2\67")
        buf.write("\u00ef\3\2\2\29\u00f1\3\2\2\2;\u00f3\3\2\2\2=\u00f6\3")
        buf.write("\2\2\2?\u00f9\3\2\2\2A\u00fb\3\2\2\2C\u00fe\3\2\2\2E\u0100")
        buf.write("\3\2\2\2G\u0103\3\2\2\2I\u0107\3\2\2\2K\u010a\3\2\2\2")
        buf.write("M\u010c\3\2\2\2O\u010e\3\2\2\2Q\u0110\3\2\2\2S\u0112\3")
        buf.write("\2\2\2U\u0114\3\2\2\2W\u011c\3\2\2\2Y\u0120\3\2\2\2[\u0127")
        buf.write("\3\2\2\2]\u0132\3\2\2\2_\u0134\3\2\2\2a\u0143\3\2\2\2")
        buf.write("c\u0145\3\2\2\2e\u0147\3\2\2\2g\u0152\3\2\2\2i\u015a\3")
        buf.write("\2\2\2k\u0160\3\2\2\2m\u016e\3\2\2\2o\u017b\3\2\2\2q\u017d")
        buf.write("\3\2\2\2st\7v\2\2tu\7t\2\2uv\7w\2\2vw\7g\2\2w\4\3\2\2")
        buf.write("\2xy\7h\2\2yz\7c\2\2z{\7n\2\2{|\7u\2\2|}\7g\2\2}\6\3\2")
        buf.write("\2\2~\177\7p\2\2\177\u0080\7w\2\2\u0080\u0081\7o\2\2\u0081")
        buf.write("\u0082\7d\2\2\u0082\u0083\7g\2\2\u0083\u0084\7t\2\2\u0084")
        buf.write("\b\3\2\2\2\u0085\u0086\7d\2\2\u0086\u0087\7q\2\2\u0087")
        buf.write("\u0088\7q\2\2\u0088\u0089\7n\2\2\u0089\n\3\2\2\2\u008a")
        buf.write("\u008b\7u\2\2\u008b\u008c\7v\2\2\u008c\u008d\7t\2\2\u008d")
        buf.write("\u008e\7k\2\2\u008e\u008f\7p\2\2\u008f\u0090\7i\2\2\u0090")
        buf.write("\f\3\2\2\2\u0091\u0092\7t\2\2\u0092\u0093\7g\2\2\u0093")
        buf.write("\u0094\7v\2\2\u0094\u0095\7w\2\2\u0095\u0096\7t\2\2\u0096")
        buf.write("\u0097\7p\2\2\u0097\16\3\2\2\2\u0098\u0099\7x\2\2\u0099")
        buf.write("\u009a\7c\2\2\u009a\u009b\7t\2\2\u009b\20\3\2\2\2\u009c")
        buf.write("\u009d\7f\2\2\u009d\u009e\7{\2\2\u009e\u009f\7p\2\2\u009f")
        buf.write("\u00a0\7c\2\2\u00a0\u00a1\7o\2\2\u00a1\u00a2\7k\2\2\u00a2")
        buf.write("\u00a3\7e\2\2\u00a3\22\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5")
        buf.write("\u00a6\7w\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7e\2\2\u00a8")
        buf.write("\24\3\2\2\2\u00a9\u00aa\7h\2\2\u00aa\u00ab\7q\2\2\u00ab")
        buf.write("\u00ac\7t\2\2\u00ac\26\3\2\2\2\u00ad\u00ae\7w\2\2\u00ae")
        buf.write("\u00af\7p\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7k\2\2\u00b1")
        buf.write("\u00b2\7n\2\2\u00b2\30\3\2\2\2\u00b3\u00b4\7d\2\2\u00b4")
        buf.write("\u00b5\7{\2\2\u00b5\32\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7")
        buf.write("\u00b8\7t\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7c\2\2\u00ba")
        buf.write("\u00bb\7m\2\2\u00bb\34\3\2\2\2\u00bc\u00bd\7e\2\2\u00bd")
        buf.write("\u00be\7q\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7v\2\2\u00c0")
        buf.write("\u00c1\7k\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3\7w\2\2\u00c3")
        buf.write("\u00c4\7g\2\2\u00c4\36\3\2\2\2\u00c5\u00c6\7k\2\2\u00c6")
        buf.write("\u00c7\7h\2\2\u00c7 \3\2\2\2\u00c8\u00c9\7g\2\2\u00c9")
        buf.write("\u00ca\7n\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7g\2\2\u00cc")
        buf.write("\"\3\2\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7n\2\2\u00cf")
        buf.write("\u00d0\7k\2\2\u00d0\u00d1\7h\2\2\u00d1$\3\2\2\2\u00d2")
        buf.write("\u00d3\7d\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5\7i\2\2\u00d5")
        buf.write("\u00d6\7k\2\2\u00d6\u00d7\7p\2\2\u00d7&\3\2\2\2\u00d8")
        buf.write("\u00d9\7g\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7f\2\2\u00db")
        buf.write("(\3\2\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7q\2\2\u00de")
        buf.write("\u00df\7v\2\2\u00df*\3\2\2\2\u00e0\u00e1\7c\2\2\u00e1")
        buf.write("\u00e2\7p\2\2\u00e2\u00e3\7f\2\2\u00e3,\3\2\2\2\u00e4")
        buf.write("\u00e5\7q\2\2\u00e5\u00e6\7t\2\2\u00e6.\3\2\2\2\u00e7")
        buf.write("\u00e8\7-\2\2\u00e8\60\3\2\2\2\u00e9\u00ea\7/\2\2\u00ea")
        buf.write("\62\3\2\2\2\u00eb\u00ec\7,\2\2\u00ec\64\3\2\2\2\u00ed")
        buf.write("\u00ee\7\61\2\2\u00ee\66\3\2\2\2\u00ef\u00f0\7\'\2\2\u00f0")
        buf.write("8\3\2\2\2\u00f1\u00f2\7?\2\2\u00f2:\3\2\2\2\u00f3\u00f4")
        buf.write("\7>\2\2\u00f4\u00f5\7/\2\2\u00f5<\3\2\2\2\u00f6\u00f7")
        buf.write("\7#\2\2\u00f7\u00f8\7?\2\2\u00f8>\3\2\2\2\u00f9\u00fa")
        buf.write("\7>\2\2\u00fa@\3\2\2\2\u00fb\u00fc\7>\2\2\u00fc\u00fd")
        buf.write("\7?\2\2\u00fdB\3\2\2\2\u00fe\u00ff\7@\2\2\u00ffD\3\2\2")
        buf.write("\2\u0100\u0101\7@\2\2\u0101\u0102\7?\2\2\u0102F\3\2\2")
        buf.write("\2\u0103\u0104\7\60\2\2\u0104\u0105\7\60\2\2\u0105\u0106")
        buf.write("\7\60\2\2\u0106H\3\2\2\2\u0107\u0108\7?\2\2\u0108\u0109")
        buf.write("\7?\2\2\u0109J\3\2\2\2\u010a\u010b\7*\2\2\u010bL\3\2\2")
        buf.write("\2\u010c\u010d\7+\2\2\u010dN\3\2\2\2\u010e\u010f\7]\2")
        buf.write("\2\u010fP\3\2\2\2\u0110\u0111\7_\2\2\u0111R\3\2\2\2\u0112")
        buf.write("\u0113\7.\2\2\u0113T\3\2\2\2\u0114\u0116\5W,\2\u0115\u0117")
        buf.write("\5Y-\2\u0116\u0115\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0119")
        buf.write("\3\2\2\2\u0118\u011a\5[.\2\u0119\u0118\3\2\2\2\u0119\u011a")
        buf.write("\3\2\2\2\u011aV\3\2\2\2\u011b\u011d\t\2\2\2\u011c\u011b")
        buf.write("\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011c\3\2\2\2\u011e")
        buf.write("\u011f\3\2\2\2\u011fX\3\2\2\2\u0120\u0124\7\60\2\2\u0121")
        buf.write("\u0123\t\2\2\2\u0122\u0121\3\2\2\2\u0123\u0126\3\2\2\2")
        buf.write("\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125Z\3\2\2")
        buf.write("\2\u0126\u0124\3\2\2\2\u0127\u0129\t\3\2\2\u0128\u012a")
        buf.write("\t\4\2\2\u0129\u0128\3\2\2\2\u0129\u012a\3\2\2\2\u012a")
        buf.write("\u012c\3\2\2\2\u012b\u012d\t\2\2\2\u012c\u012b\3\2\2\2")
        buf.write("\u012d\u012e\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3")
        buf.write("\2\2\2\u012f\\\3\2\2\2\u0130\u0133\5\3\2\2\u0131\u0133")
        buf.write("\5\5\3\2\u0132\u0130\3\2\2\2\u0132\u0131\3\2\2\2\u0133")
        buf.write("^\3\2\2\2\u0134\u0138\t\5\2\2\u0135\u0137\5a\61\2\u0136")
        buf.write("\u0135\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2")
        buf.write("\u0138\u0139\3\2\2\2\u0139\u013b\3\2\2\2\u013a\u0138\3")
        buf.write("\2\2\2\u013b\u013c\t\5\2\2\u013c\u013d\b\60\2\2\u013d")
        buf.write("`\3\2\2\2\u013e\u0144\n\6\2\2\u013f\u0140\7^\2\2\u0140")
        buf.write("\u0144\t\7\2\2\u0141\u0142\7)\2\2\u0142\u0144\7$\2\2\u0143")
        buf.write("\u013e\3\2\2\2\u0143\u013f\3\2\2\2\u0143\u0141\3\2\2\2")
        buf.write("\u0144b\3\2\2\2\u0145\u0146\t\b\2\2\u0146d\3\2\2\2\u0147")
        buf.write("\u0148\7%\2\2\u0148\u0149\7%\2\2\u0149\u014d\3\2\2\2\u014a")
        buf.write("\u014c\n\t\2\2\u014b\u014a\3\2\2\2\u014c\u014f\3\2\2\2")
        buf.write("\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0150\3")
        buf.write("\2\2\2\u014f\u014d\3\2\2\2\u0150\u0151\b\63\3\2\u0151")
        buf.write("f\3\2\2\2\u0152\u0156\t\n\2\2\u0153\u0155\t\13\2\2\u0154")
        buf.write("\u0153\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3\2\2\2")
        buf.write("\u0156\u0157\3\2\2\2\u0157h\3\2\2\2\u0158\u0156\3\2\2")
        buf.write("\2\u0159\u015b\t\f\2\2\u015a\u0159\3\2\2\2\u015b\u015c")
        buf.write("\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015e\u015f\b\65\3\2\u015fj\3\2\2\2\u0160")
        buf.write("\u0164\t\5\2\2\u0161\u0163\5a\61\2\u0162\u0161\3\2\2\2")
        buf.write("\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165\u016a\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168")
        buf.write("\7\17\2\2\u0168\u016b\7\f\2\2\u0169\u016b\t\r\2\2\u016a")
        buf.write("\u0167\3\2\2\2\u016a\u0169\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u016d\b\66\4\2\u016dl\3\2\2\2\u016e\u0172\t\5\2")
        buf.write("\2\u016f\u0171\5a\61\2\u0170\u016f\3\2\2\2\u0171\u0174")
        buf.write("\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u0175\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0176\5o8\2\u0176")
        buf.write("\u0177\b\67\5\2\u0177n\3\2\2\2\u0178\u017c\t\16\2\2\u0179")
        buf.write("\u017a\7^\2\2\u017a\u017c\n\7\2\2\u017b\u0178\3\2\2\2")
        buf.write("\u017b\u0179\3\2\2\2\u017cp\3\2\2\2\u017d\u017e\13\2\2")
        buf.write("\2\u017e\u017f\b9\6\2\u017fr\3\2\2\2\23\2\u0116\u0119")
        buf.write("\u011e\u0124\u0129\u012e\u0132\u0138\u0143\u014d\u0156")
        buf.write("\u015c\u0164\u016a\u0172\u017b\7\3\60\2\b\2\2\3\66\3\3")
        buf.write("\67\4\39\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQ = 28
    ASSIGNINIT = 29
    DIF = 30
    LT = 31
    LTE = 32
    GT = 33
    GTE = 34
    CONCAT = 35
    SAME = 36
    LB = 37
    RB = 38
    LSB = 39
    RSB = 40
    CM = 41
    NUMBER_LIT = 42
    BOOLEAN_LIT = 43
    STRING_LIT = 44
    NEWLINE = 45
    COMMENTS = 46
    ID = 47
    WS = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQ", "ASSIGNINIT", "DIF", "LT", 
            "LTE", "GT", "GTE", "CONCAT", "SAME", "LB", "RB", "LSB", "RSB", 
            "CM", "NUMBER_LIT", "BOOLEAN_LIT", "STRING_LIT", "NEWLINE", 
            "COMMENTS", "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
                  "ASSIGNINIT", "DIF", "LT", "LTE", "GT", "GTE", "CONCAT", 
                  "SAME", "LB", "RB", "LSB", "RSB", "CM", "NUMBER_LIT", 
                  "INTPART", "DECPART", "EXPPART", "BOOLEAN_LIT", "STRING_LIT", 
                  "VALIDSTRING", "NEWLINE", "COMMENTS", "ID", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ILLEGAL", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[46] = self.STRING_LIT_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
            actions[55] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                if self.text[-1] == '\n' and self.text[-2] == '\r':
                    raise UncloseString(self.text[1:-2])
                elif self.text[-1] == '\n':
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


