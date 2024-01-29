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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u018e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\6*\u0114\n*\r*\16*\u0115")
        buf.write("\3+\3+\6+\u011a\n+\r+\16+\u011b\3,\3,\5,\u0120\n,\3,\6")
        buf.write(",\u0123\n,\r,\16,\u0124\3-\3-\5-\u0129\n-\3-\5-\u012c")
        buf.write("\n-\3.\3.\5.\u0130\n.\3/\3/\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\5\60\u0146\n\60\3\61\3\61\3\61\3\61\5\61\u014c")
        buf.write("\n\61\3\62\3\62\3\62\7\62\u0151\n\62\f\62\16\62\u0154")
        buf.write("\13\62\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\64\7")
        buf.write("\64\u015f\n\64\f\64\16\64\u0162\13\64\3\64\3\64\3\65\3")
        buf.write("\65\7\65\u0168\n\65\f\65\16\65\u016b\13\65\3\66\6\66\u016e")
        buf.write("\n\66\r\66\16\66\u016f\3\66\3\66\3\67\3\67\3\67\7\67\u0177")
        buf.write("\n\67\f\67\16\67\u017a\13\67\3\67\5\67\u017d\n\67\3\67")
        buf.write("\3\67\38\38\38\78\u0184\n8\f8\168\u0187\138\38\38\38\3")
        buf.write("9\39\39\2\2:\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S\2U\2W\2Y+[,]\2_\2a\2c-e.g/i\60k\61m\62")
        buf.write("o\63q\64\3\2\16\3\2\62;\4\2GGgg\4\2--//\5\2\f\f$$^^\b")
        buf.write("\2^^ddhhppttvv\3\2$$\3\2\f\f\4\2\f\f\16\17\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\5\2\13\13\17\17\"\"\3\3\f\f\2\u01a0\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2Y\3\2\2")
        buf.write("\2\2[\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2")
        buf.write("\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\3s\3")
        buf.write("\2\2\2\5x\3\2\2\2\7~\3\2\2\2\t\u0085\3\2\2\2\13\u008a")
        buf.write("\3\2\2\2\r\u0091\3\2\2\2\17\u0098\3\2\2\2\21\u009c\3\2")
        buf.write("\2\2\23\u00a4\3\2\2\2\25\u00a9\3\2\2\2\27\u00ad\3\2\2")
        buf.write("\2\31\u00b3\3\2\2\2\33\u00b6\3\2\2\2\35\u00bc\3\2\2\2")
        buf.write("\37\u00c5\3\2\2\2!\u00c8\3\2\2\2#\u00cd\3\2\2\2%\u00d2")
        buf.write("\3\2\2\2\'\u00d8\3\2\2\2)\u00dc\3\2\2\2+\u00e0\3\2\2\2")
        buf.write("-\u00e4\3\2\2\2/\u00e7\3\2\2\2\61\u00e9\3\2\2\2\63\u00eb")
        buf.write("\3\2\2\2\65\u00ed\3\2\2\2\67\u00ef\3\2\2\29\u00f1\3\2")
        buf.write("\2\2;\u00f3\3\2\2\2=\u00f6\3\2\2\2?\u00f9\3\2\2\2A\u00fb")
        buf.write("\3\2\2\2C\u00fe\3\2\2\2E\u0100\3\2\2\2G\u0103\3\2\2\2")
        buf.write("I\u0107\3\2\2\2K\u010a\3\2\2\2M\u010c\3\2\2\2O\u010e\3")
        buf.write("\2\2\2Q\u0110\3\2\2\2S\u0113\3\2\2\2U\u0117\3\2\2\2W\u011d")
        buf.write("\3\2\2\2Y\u0126\3\2\2\2[\u012f\3\2\2\2]\u0131\3\2\2\2")
        buf.write("_\u0145\3\2\2\2a\u014b\3\2\2\2c\u014d\3\2\2\2e\u0158\3")
        buf.write("\2\2\2g\u015a\3\2\2\2i\u0165\3\2\2\2k\u016d\3\2\2\2m\u0173")
        buf.write("\3\2\2\2o\u0180\3\2\2\2q\u018b\3\2\2\2st\7v\2\2tu\7t\2")
        buf.write("\2uv\7w\2\2vw\7g\2\2w\4\3\2\2\2xy\7h\2\2yz\7c\2\2z{\7")
        buf.write("n\2\2{|\7u\2\2|}\7g\2\2}\6\3\2\2\2~\177\7p\2\2\177\u0080")
        buf.write("\7w\2\2\u0080\u0081\7o\2\2\u0081\u0082\7d\2\2\u0082\u0083")
        buf.write("\7g\2\2\u0083\u0084\7t\2\2\u0084\b\3\2\2\2\u0085\u0086")
        buf.write("\7d\2\2\u0086\u0087\7q\2\2\u0087\u0088\7q\2\2\u0088\u0089")
        buf.write("\7n\2\2\u0089\n\3\2\2\2\u008a\u008b\7u\2\2\u008b\u008c")
        buf.write("\7v\2\2\u008c\u008d\7t\2\2\u008d\u008e\7k\2\2\u008e\u008f")
        buf.write("\7p\2\2\u008f\u0090\7i\2\2\u0090\f\3\2\2\2\u0091\u0092")
        buf.write("\7t\2\2\u0092\u0093\7g\2\2\u0093\u0094\7v\2\2\u0094\u0095")
        buf.write("\7w\2\2\u0095\u0096\7t\2\2\u0096\u0097\7p\2\2\u0097\16")
        buf.write("\3\2\2\2\u0098\u0099\7x\2\2\u0099\u009a\7c\2\2\u009a\u009b")
        buf.write("\7t\2\2\u009b\20\3\2\2\2\u009c\u009d\7f\2\2\u009d\u009e")
        buf.write("\7{\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1")
        buf.write("\7o\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3\7e\2\2\u00a3\22")
        buf.write("\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\u00a8\7e\2\2\u00a8\24\3\2\2\2\u00a9\u00aa")
        buf.write("\7h\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7t\2\2\u00ac\26")
        buf.write("\3\2\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af\7p\2\2\u00af\u00b0")
        buf.write("\7v\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2\7n\2\2\u00b2\30")
        buf.write("\3\2\2\2\u00b3\u00b4\7d\2\2\u00b4\u00b5\7{\2\2\u00b5\32")
        buf.write("\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9")
        buf.write("\7g\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7m\2\2\u00bb\34")
        buf.write("\3\2\2\2\u00bc\u00bd\7e\2\2\u00bd\u00be\7q\2\2\u00be\u00bf")
        buf.write("\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4\7g\2\2\u00c4\36")
        buf.write("\3\2\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7h\2\2\u00c7 ")
        buf.write("\3\2\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb")
        buf.write("\7u\2\2\u00cb\u00cc\7g\2\2\u00cc\"\3\2\2\2\u00cd\u00ce")
        buf.write("\7g\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1")
        buf.write("\7h\2\2\u00d1$\3\2\2\2\u00d2\u00d3\7d\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\u00d5\7i\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7")
        buf.write("\7p\2\2\u00d7&\3\2\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da")
        buf.write("\7p\2\2\u00da\u00db\7f\2\2\u00db(\3\2\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7v\2\2\u00df*\3")
        buf.write("\2\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3")
        buf.write("\7f\2\2\u00e3,\3\2\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6.\3\2\2\2\u00e7\u00e8\7-\2\2\u00e8\60\3\2")
        buf.write("\2\2\u00e9\u00ea\7/\2\2\u00ea\62\3\2\2\2\u00eb\u00ec\7")
        buf.write(",\2\2\u00ec\64\3\2\2\2\u00ed\u00ee\7\61\2\2\u00ee\66\3")
        buf.write("\2\2\2\u00ef\u00f0\7\'\2\2\u00f08\3\2\2\2\u00f1\u00f2")
        buf.write("\7?\2\2\u00f2:\3\2\2\2\u00f3\u00f4\7>\2\2\u00f4\u00f5")
        buf.write("\7/\2\2\u00f5<\3\2\2\2\u00f6\u00f7\7#\2\2\u00f7\u00f8")
        buf.write("\7?\2\2\u00f8>\3\2\2\2\u00f9\u00fa\7>\2\2\u00fa@\3\2\2")
        buf.write("\2\u00fb\u00fc\7>\2\2\u00fc\u00fd\7?\2\2\u00fdB\3\2\2")
        buf.write("\2\u00fe\u00ff\7@\2\2\u00ffD\3\2\2\2\u0100\u0101\7@\2")
        buf.write("\2\u0101\u0102\7?\2\2\u0102F\3\2\2\2\u0103\u0104\7\60")
        buf.write("\2\2\u0104\u0105\7\60\2\2\u0105\u0106\7\60\2\2\u0106H")
        buf.write("\3\2\2\2\u0107\u0108\7?\2\2\u0108\u0109\7?\2\2\u0109J")
        buf.write("\3\2\2\2\u010a\u010b\7]\2\2\u010bL\3\2\2\2\u010c\u010d")
        buf.write("\7_\2\2\u010dN\3\2\2\2\u010e\u010f\7*\2\2\u010fP\3\2\2")
        buf.write("\2\u0110\u0111\7+\2\2\u0111R\3\2\2\2\u0112\u0114\t\2\2")
        buf.write("\2\u0113\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0113")
        buf.write("\3\2\2\2\u0115\u0116\3\2\2\2\u0116T\3\2\2\2\u0117\u0119")
        buf.write("\7\60\2\2\u0118\u011a\t\2\2\2\u0119\u0118\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011cV\3\2\2\2\u011d\u011f\t\3\2\2\u011e\u0120\t\4\2")
        buf.write("\2\u011f\u011e\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0122")
        buf.write("\3\2\2\2\u0121\u0123\t\2\2\2\u0122\u0121\3\2\2\2\u0123")
        buf.write("\u0124\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125X\3\2\2\2\u0126\u0128\5S*\2\u0127\u0129\5U+\2\u0128")
        buf.write("\u0127\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012b\3\2\2\2")
        buf.write("\u012a\u012c\5W,\2\u012b\u012a\3\2\2\2\u012b\u012c\3\2")
        buf.write("\2\2\u012cZ\3\2\2\2\u012d\u0130\5\3\2\2\u012e\u0130\5")
        buf.write("\5\3\2\u012f\u012d\3\2\2\2\u012f\u012e\3\2\2\2\u0130\\")
        buf.write("\3\2\2\2\u0131\u0132\n\5\2\2\u0132^\3\2\2\2\u0133\u0134")
        buf.write("\7^\2\2\u0134\u0146\7d\2\2\u0135\u0136\7^\2\2\u0136\u0146")
        buf.write("\7h\2\2\u0137\u0138\7^\2\2\u0138\u0146\7t\2\2\u0139\u013a")
        buf.write("\7^\2\2\u013a\u0146\7p\2\2\u013b\u013c\7^\2\2\u013c\u0146")
        buf.write("\7v\2\2\u013d\u013e\7^\2\2\u013e\u0146\7)\2\2\u013f\u0140")
        buf.write("\7^\2\2\u0140\u0146\7^\2\2\u0141\u0142\7)\2\2\u0142\u0146")
        buf.write("\7$\2\2\u0143\u0144\7^\2\2\u0144\u0146\7$\2\2\u0145\u0133")
        buf.write("\3\2\2\2\u0145\u0135\3\2\2\2\u0145\u0137\3\2\2\2\u0145")
        buf.write("\u0139\3\2\2\2\u0145\u013b\3\2\2\2\u0145\u013d\3\2\2\2")
        buf.write("\u0145\u013f\3\2\2\2\u0145\u0141\3\2\2\2\u0145\u0143\3")
        buf.write("\2\2\2\u0146`\3\2\2\2\u0147\u0148\7^\2\2\u0148\u014c\n")
        buf.write("\6\2\2\u0149\u014a\7)\2\2\u014a\u014c\n\7\2\2\u014b\u0147")
        buf.write("\3\2\2\2\u014b\u0149\3\2\2\2\u014cb\3\2\2\2\u014d\u0152")
        buf.write("\7$\2\2\u014e\u0151\5]/\2\u014f\u0151\5_\60\2\u0150\u014e")
        buf.write("\3\2\2\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0155\3\2\2\2")
        buf.write("\u0154\u0152\3\2\2\2\u0155\u0156\7$\2\2\u0156\u0157\b")
        buf.write("\62\2\2\u0157d\3\2\2\2\u0158\u0159\t\b\2\2\u0159f\3\2")
        buf.write("\2\2\u015a\u015b\7%\2\2\u015b\u015c\7%\2\2\u015c\u0160")
        buf.write("\3\2\2\2\u015d\u015f\n\t\2\2\u015e\u015d\3\2\2\2\u015f")
        buf.write("\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2")
        buf.write("\u0161\u0163\3\2\2\2\u0162\u0160\3\2\2\2\u0163\u0164\b")
        buf.write("\64\3\2\u0164h\3\2\2\2\u0165\u0169\t\n\2\2\u0166\u0168")
        buf.write("\t\13\2\2\u0167\u0166\3\2\2\2\u0168\u016b\3\2\2\2\u0169")
        buf.write("\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016aj\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u016e\t\f\2\2\u016d\u016c\3\2\2\2")
        buf.write("\u016e\u016f\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3")
        buf.write("\2\2\2\u0170\u0171\3\2\2\2\u0171\u0172\b\66\3\2\u0172")
        buf.write("l\3\2\2\2\u0173\u0178\7$\2\2\u0174\u0177\5]/\2\u0175\u0177")
        buf.write("\5_\60\2\u0176\u0174\3\2\2\2\u0176\u0175\3\2\2\2\u0177")
        buf.write("\u017a\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017d\t")
        buf.write("\r\2\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f")
        buf.write("\b\67\4\2\u017fn\3\2\2\2\u0180\u0185\7$\2\2\u0181\u0184")
        buf.write("\5]/\2\u0182\u0184\5_\60\2\u0183\u0181\3\2\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0183\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186\u0188\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0188\u0189\5a\61\2\u0189\u018a\b8\5\2\u018ap\3\2\2\2")
        buf.write("\u018b\u018c\13\2\2\2\u018c\u018d\b9\6\2\u018dr\3\2\2")
        buf.write("\2\26\2\u0115\u011b\u011f\u0124\u0128\u012b\u012f\u0145")
        buf.write("\u014b\u0150\u0152\u0160\u0169\u016f\u0176\u0178\u017c")
        buf.write("\u0183\u0185\7\3\62\2\b\2\2\3\67\3\38\4\39\5")
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
    DOTS = 35
    SAME = 36
    LB = 37
    RB = 38
    LP = 39
    RP = 40
    NUMBER_LIT = 41
    BOOLEAN_LIT = 42
    STRINGLIT = 43
    NEWLINE = 44
    COMMENTS = 45
    ID = 46
    WS = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'['", "']'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQ", "ASSIGNINIT", "DIF", "LT", 
            "LTE", "GT", "GTE", "DOTS", "SAME", "LB", "RB", "LP", "RP", 
            "NUMBER_LIT", "BOOLEAN_LIT", "STRINGLIT", "NEWLINE", "COMMENTS", 
            "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
                  "ASSIGNINIT", "DIF", "LT", "LTE", "GT", "GTE", "DOTS", 
                  "SAME", "LB", "RB", "LP", "RP", "Integer_part", "Decimal_part", 
                  "Exponent_part", "NUMBER_LIT", "BOOLEAN_LIT", "STRING_CHAR", 
                  "ESCAPE", "ESCERROR", "STRINGLIT", "NEWLINE", "COMMENTS", 
                  "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[48] = self.STRINGLIT_action 
            actions[53] = self.UNCLOSE_STRING_action 
            actions[54] = self.ILLEGAL_ESCAPE_action 
            actions[55] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	content = str(self.text) 
            	self.text = content[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	content = str(self.text)
            	esc = '\n'
            	if content[-1] in esc:
            		raise UncloseString(content[1:-1])
            	else:
            		raise UncloseString(content[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	content = str(self.text) 
            	raise IllegalEscape(content[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


