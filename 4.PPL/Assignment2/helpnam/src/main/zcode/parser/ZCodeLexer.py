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
        buf.write("\u01a5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3)\3)\3*\3*\3+\6+\u0124\n+\r+\16+\u0125\3")
        buf.write("+\3+\3,\6,\u012b\n,\r,\16,\u012c\3,\3,\7,\u0131\n,\f,")
        buf.write("\16,\u0134\13,\5,\u0136\n,\3,\5,\u0139\n,\3-\3-\5-\u013d")
        buf.write("\n-\3.\3.\7.\u0141\n.\f.\16.\u0144\13.\3.\3.\3.\3/\3/")
        buf.write("\3/\3/\3/\5/\u014e\n/\3\60\3\60\3\61\3\61\3\62\3\62\5")
        buf.write("\62\u0156\n\62\3\62\6\62\u0159\n\62\r\62\16\62\u015a\3")
        buf.write("\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\5\67\u016c\n\67\38\38\39\39\3:\3")
        buf.write(":\3;\3;\3;\7;\u0177\n;\f;\16;\u017a\13;\3;\3;\3<\3<\3")
        buf.write("<\7<\u0181\n<\f<\16<\u0184\13<\3=\3=\7=\u0188\n=\f=\16")
        buf.write("=\u018b\13=\3=\3=\3=\5=\u0190\n=\3=\3=\3>\3>\7>\u0196")
        buf.write("\n>\f>\16>\u0199\13>\3>\3>\3>\3?\3?\3?\5?\u01a1\n?\3@")
        buf.write("\3@\3@\2\2A\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\2a\2c\2e\2g\2i\2k\2m\2o\2")
        buf.write("q\2s\60u\61w\62y\63{\64}\2\177\65\3\2\16\5\2\n\13\16\17")
        buf.write("\"\"\3\2$$\6\2\f\f\17\17$$^^\t\2))^^ddhhppttvv\5\2C\\")
        buf.write("aac|\3\2\62;\4\2GGgg\4\2--//\4\2\f\f\16\17\3\2\f\f\3\3")
        buf.write("\f\f\3\2\17\17\2\u01ad\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y")
        buf.write("\3\2\2\2\2{\3\2\2\2\2\177\3\2\2\2\3\u0081\3\2\2\2\5\u0086")
        buf.write("\3\2\2\2\7\u008c\3\2\2\2\t\u0093\3\2\2\2\13\u0098\3\2")
        buf.write("\2\2\r\u009f\3\2\2\2\17\u00a6\3\2\2\2\21\u00aa\3\2\2\2")
        buf.write("\23\u00b2\3\2\2\2\25\u00b7\3\2\2\2\27\u00bb\3\2\2\2\31")
        buf.write("\u00c1\3\2\2\2\33\u00c4\3\2\2\2\35\u00ca\3\2\2\2\37\u00d3")
        buf.write("\3\2\2\2!\u00d6\3\2\2\2#\u00db\3\2\2\2%\u00e0\3\2\2\2")
        buf.write("\'\u00e6\3\2\2\2)\u00ea\3\2\2\2+\u00ee\3\2\2\2-\u00f2")
        buf.write("\3\2\2\2/\u00f5\3\2\2\2\61\u00f7\3\2\2\2\63\u00f9\3\2")
        buf.write("\2\2\65\u00fb\3\2\2\2\67\u00fd\3\2\2\29\u00ff\3\2\2\2")
        buf.write(";\u0101\3\2\2\2=\u0104\3\2\2\2?\u0107\3\2\2\2A\u0109\3")
        buf.write("\2\2\2C\u010c\3\2\2\2E\u010e\3\2\2\2G\u0111\3\2\2\2I\u0115")
        buf.write("\3\2\2\2K\u0118\3\2\2\2M\u011a\3\2\2\2O\u011c\3\2\2\2")
        buf.write("Q\u011e\3\2\2\2S\u0120\3\2\2\2U\u0123\3\2\2\2W\u012a\3")
        buf.write("\2\2\2Y\u013c\3\2\2\2[\u013e\3\2\2\2]\u014d\3\2\2\2_\u014f")
        buf.write("\3\2\2\2a\u0151\3\2\2\2c\u0153\3\2\2\2e\u015c\3\2\2\2")
        buf.write("g\u015f\3\2\2\2i\u0161\3\2\2\2k\u0163\3\2\2\2m\u016b\3")
        buf.write("\2\2\2o\u016d\3\2\2\2q\u016f\3\2\2\2s\u0171\3\2\2\2u\u0173")
        buf.write("\3\2\2\2w\u017d\3\2\2\2y\u0185\3\2\2\2{\u0193\3\2\2\2")
        buf.write("}\u01a0\3\2\2\2\177\u01a2\3\2\2\2\u0081\u0082\7v\2\2\u0082")
        buf.write("\u0083\7t\2\2\u0083\u0084\7w\2\2\u0084\u0085\7g\2\2\u0085")
        buf.write("\4\3\2\2\2\u0086\u0087\7h\2\2\u0087\u0088\7c\2\2\u0088")
        buf.write("\u0089\7n\2\2\u0089\u008a\7u\2\2\u008a\u008b\7g\2\2\u008b")
        buf.write("\6\3\2\2\2\u008c\u008d\7p\2\2\u008d\u008e\7w\2\2\u008e")
        buf.write("\u008f\7o\2\2\u008f\u0090\7d\2\2\u0090\u0091\7g\2\2\u0091")
        buf.write("\u0092\7t\2\2\u0092\b\3\2\2\2\u0093\u0094\7d\2\2\u0094")
        buf.write("\u0095\7q\2\2\u0095\u0096\7q\2\2\u0096\u0097\7n\2\2\u0097")
        buf.write("\n\3\2\2\2\u0098\u0099\7u\2\2\u0099\u009a\7v\2\2\u009a")
        buf.write("\u009b\7t\2\2\u009b\u009c\7k\2\2\u009c\u009d\7p\2\2\u009d")
        buf.write("\u009e\7i\2\2\u009e\f\3\2\2\2\u009f\u00a0\7t\2\2\u00a0")
        buf.write("\u00a1\7g\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3\7w\2\2\u00a3")
        buf.write("\u00a4\7t\2\2\u00a4\u00a5\7p\2\2\u00a5\16\3\2\2\2\u00a6")
        buf.write("\u00a7\7x\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9\7t\2\2\u00a9")
        buf.write("\20\3\2\2\2\u00aa\u00ab\7f\2\2\u00ab\u00ac\7{\2\2\u00ac")
        buf.write("\u00ad\7p\2\2\u00ad\u00ae\7c\2\2\u00ae\u00af\7o\2\2\u00af")
        buf.write("\u00b0\7k\2\2\u00b0\u00b1\7e\2\2\u00b1\22\3\2\2\2\u00b2")
        buf.write("\u00b3\7h\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7p\2\2\u00b5")
        buf.write("\u00b6\7e\2\2\u00b6\24\3\2\2\2\u00b7\u00b8\7h\2\2\u00b8")
        buf.write("\u00b9\7q\2\2\u00b9\u00ba\7t\2\2\u00ba\26\3\2\2\2\u00bb")
        buf.write("\u00bc\7w\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7v\2\2\u00be")
        buf.write("\u00bf\7k\2\2\u00bf\u00c0\7n\2\2\u00c0\30\3\2\2\2\u00c1")
        buf.write("\u00c2\7d\2\2\u00c2\u00c3\7{\2\2\u00c3\32\3\2\2\2\u00c4")
        buf.write("\u00c5\7d\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7g\2\2\u00c7")
        buf.write("\u00c8\7c\2\2\u00c8\u00c9\7m\2\2\u00c9\34\3\2\2\2\u00ca")
        buf.write("\u00cb\7e\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7p\2\2\u00cd")
        buf.write("\u00ce\7v\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7p\2\2\u00d0")
        buf.write("\u00d1\7w\2\2\u00d1\u00d2\7g\2\2\u00d2\36\3\2\2\2\u00d3")
        buf.write("\u00d4\7k\2\2\u00d4\u00d5\7h\2\2\u00d5 \3\2\2\2\u00d6")
        buf.write("\u00d7\7g\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7u\2\2\u00d9")
        buf.write("\u00da\7g\2\2\u00da\"\3\2\2\2\u00db\u00dc\7g\2\2\u00dc")
        buf.write("\u00dd\7n\2\2\u00dd\u00de\7k\2\2\u00de\u00df\7h\2\2\u00df")
        buf.write("$\3\2\2\2\u00e0\u00e1\7d\2\2\u00e1\u00e2\7g\2\2\u00e2")
        buf.write("\u00e3\7i\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7p\2\2\u00e5")
        buf.write("&\3\2\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8\7p\2\2\u00e8")
        buf.write("\u00e9\7f\2\2\u00e9(\3\2\2\2\u00ea\u00eb\7p\2\2\u00eb")
        buf.write("\u00ec\7q\2\2\u00ec\u00ed\7v\2\2\u00ed*\3\2\2\2\u00ee")
        buf.write("\u00ef\7c\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1\7f\2\2\u00f1")
        buf.write(",\3\2\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7t\2\2\u00f4")
        buf.write(".\3\2\2\2\u00f5\u00f6\7-\2\2\u00f6\60\3\2\2\2\u00f7\u00f8")
        buf.write("\7/\2\2\u00f8\62\3\2\2\2\u00f9\u00fa\7,\2\2\u00fa\64\3")
        buf.write("\2\2\2\u00fb\u00fc\7\61\2\2\u00fc\66\3\2\2\2\u00fd\u00fe")
        buf.write("\7\'\2\2\u00fe8\3\2\2\2\u00ff\u0100\7?\2\2\u0100:\3\2")
        buf.write("\2\2\u0101\u0102\7>\2\2\u0102\u0103\7/\2\2\u0103<\3\2")
        buf.write("\2\2\u0104\u0105\7#\2\2\u0105\u0106\7?\2\2\u0106>\3\2")
        buf.write("\2\2\u0107\u0108\7>\2\2\u0108@\3\2\2\2\u0109\u010a\7>")
        buf.write("\2\2\u010a\u010b\7?\2\2\u010bB\3\2\2\2\u010c\u010d\7@")
        buf.write("\2\2\u010dD\3\2\2\2\u010e\u010f\7@\2\2\u010f\u0110\7?")
        buf.write("\2\2\u0110F\3\2\2\2\u0111\u0112\7\60\2\2\u0112\u0113\7")
        buf.write("\60\2\2\u0113\u0114\7\60\2\2\u0114H\3\2\2\2\u0115\u0116")
        buf.write("\7?\2\2\u0116\u0117\7?\2\2\u0117J\3\2\2\2\u0118\u0119")
        buf.write("\7*\2\2\u0119L\3\2\2\2\u011a\u011b\7+\2\2\u011bN\3\2\2")
        buf.write("\2\u011c\u011d\7]\2\2\u011dP\3\2\2\2\u011e\u011f\7_\2")
        buf.write("\2\u011fR\3\2\2\2\u0120\u0121\7.\2\2\u0121T\3\2\2\2\u0122")
        buf.write("\u0124\t\2\2\2\u0123\u0122\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\3")
        buf.write("\2\2\2\u0127\u0128\b+\2\2\u0128V\3\2\2\2\u0129\u012b\5")
        buf.write("a\61\2\u012a\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012a")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u0135\3\2\2\2\u012e")
        buf.write("\u0132\5o8\2\u012f\u0131\5a\61\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u012e\3")
        buf.write("\2\2\2\u0135\u0136\3\2\2\2\u0136\u0138\3\2\2\2\u0137\u0139")
        buf.write("\5c\62\2\u0138\u0137\3\2\2\2\u0138\u0139\3\2\2\2\u0139")
        buf.write("X\3\2\2\2\u013a\u013d\5\3\2\2\u013b\u013d\5\5\3\2\u013c")
        buf.write("\u013a\3\2\2\2\u013c\u013b\3\2\2\2\u013dZ\3\2\2\2\u013e")
        buf.write("\u0142\t\3\2\2\u013f\u0141\5]/\2\u0140\u013f\3\2\2\2\u0141")
        buf.write("\u0144\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2")
        buf.write("\u0143\u0145\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0146\t")
        buf.write("\3\2\2\u0146\u0147\b.\3\2\u0147\\\3\2\2\2\u0148\u014e")
        buf.write("\n\4\2\2\u0149\u014a\7^\2\2\u014a\u014e\t\5\2\2\u014b")
        buf.write("\u014c\7)\2\2\u014c\u014e\7$\2\2\u014d\u0148\3\2\2\2\u014d")
        buf.write("\u0149\3\2\2\2\u014d\u014b\3\2\2\2\u014e^\3\2\2\2\u014f")
        buf.write("\u0150\t\6\2\2\u0150`\3\2\2\2\u0151\u0152\t\7\2\2\u0152")
        buf.write("b\3\2\2\2\u0153\u0155\t\b\2\2\u0154\u0156\t\t\2\2\u0155")
        buf.write("\u0154\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0158\3\2\2\2")
        buf.write("\u0157\u0159\5a\61\2\u0158\u0157\3\2\2\2\u0159\u015a\3")
        buf.write("\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015bd")
        buf.write("\3\2\2\2\u015c\u015d\7^\2\2\u015d\u015e\t\5\2\2\u015e")
        buf.write("f\3\2\2\2\u015f\u0160\n\n\2\2\u0160h\3\2\2\2\u0161\u0162")
        buf.write("\7)\2\2\u0162j\3\2\2\2\u0163\u0164\7$\2\2\u0164l\3\2\2")
        buf.write("\2\u0165\u016c\5e\63\2\u0166\u016c\5g\64\2\u0167\u0168")
        buf.write("\5i\65\2\u0168\u0169\5k\66\2\u0169\u016c\3\2\2\2\u016a")
        buf.write("\u016c\n\3\2\2\u016b\u0165\3\2\2\2\u016b\u0166\3\2\2\2")
        buf.write("\u016b\u0167\3\2\2\2\u016b\u016a\3\2\2\2\u016cn\3\2\2")
        buf.write("\2\u016d\u016e\7\60\2\2\u016ep\3\2\2\2\u016f\u0170\7%")
        buf.write("\2\2\u0170r\3\2\2\2\u0171\u0172\t\13\2\2\u0172t\3\2\2")
        buf.write("\2\u0173\u0174\5q9\2\u0174\u0178\5q9\2\u0175\u0177\5g")
        buf.write("\64\2\u0176\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017b\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017b\u017c\b;\2\2\u017cv\3\2\2\2\u017d")
        buf.write("\u0182\5_\60\2\u017e\u0181\5_\60\2\u017f\u0181\5a\61\2")
        buf.write("\u0180\u017e\3\2\2\2\u0180\u017f\3\2\2\2\u0181\u0184\3")
        buf.write("\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183x")
        buf.write("\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0189\t\3\2\2\u0186")
        buf.write("\u0188\5]/\2\u0187\u0186\3\2\2\2\u0188\u018b\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018f\3\2\2\2")
        buf.write("\u018b\u0189\3\2\2\2\u018c\u018d\7\17\2\2\u018d\u0190")
        buf.write("\7\f\2\2\u018e\u0190\t\f\2\2\u018f\u018c\3\2\2\2\u018f")
        buf.write("\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0192\b=\4\2")
        buf.write("\u0192z\3\2\2\2\u0193\u0197\t\3\2\2\u0194\u0196\5]/\2")
        buf.write("\u0195\u0194\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3")
        buf.write("\2\2\2\u0197\u0198\3\2\2\2\u0198\u019a\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u019a\u019b\5}?\2\u019b\u019c\b>\5\2\u019c|\3")
        buf.write("\2\2\2\u019d\u01a1\t\r\2\2\u019e\u019f\7^\2\2\u019f\u01a1")
        buf.write("\n\5\2\2\u01a0\u019d\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1")
        buf.write("~\3\2\2\2\u01a2\u01a3\13\2\2\2\u01a3\u01a4\b@\6\2\u01a4")
        buf.write("\u0080\3\2\2\2\25\2\u0125\u012c\u0132\u0135\u0138\u013c")
        buf.write("\u0142\u014d\u0155\u015a\u016b\u0178\u0180\u0182\u0189")
        buf.write("\u018f\u0197\u01a0\7\b\2\2\3.\2\3=\3\3>\4\3@\5")
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
    ASSIGN = 29
    NEQ = 30
    LT = 31
    LTE = 32
    GT = 33
    GTE = 34
    CONCAT = 35
    COMPARE = 36
    LPAREN = 37
    RPAREN = 38
    LBRACK = 39
    RBRACK = 40
    COMMA = 41
    WS = 42
    NUMLIT = 43
    BOOLIT = 44
    STRLIT = 45
    NEWLINE = 46
    CMT = 47
    ID = 48
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
            "SUB", "MUL", "DIV", "MOD", "EQ", "ASSIGN", "NEQ", "LT", "LTE", 
            "GT", "GTE", "CONCAT", "COMPARE", "LPAREN", "RPAREN", "LBRACK", 
            "RBRACK", "COMMA", "WS", "NUMLIT", "BOOLIT", "STRLIT", "NEWLINE", 
            "CMT", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
                  "ASSIGN", "NEQ", "LT", "LTE", "GT", "GTE", "CONCAT", "COMPARE", 
                  "LPAREN", "RPAREN", "LBRACK", "RBRACK", "COMMA", "WS", 
                  "NUMLIT", "BOOLIT", "STRLIT", "VALIDSTRING", "LETTER", 
                  "DIGIT", "EXPONENT", "ESC_SEQ", "NOT_EOL", "SQUOTE", "DQUOTE", 
                  "CHARACTER", "DOT", "HASTAG", "NEWLINE", "CMT", "ID", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ILLEGAL", "ERROR_CHAR" ]

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
            actions[44] = self.STRLIT_action 
            actions[59] = self.UNCLOSE_STRING_action 
            actions[60] = self.ILLEGAL_ESCAPE_action 
            actions[62] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
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
     


