import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def start(self):
        self.assertTrue(TestLexer.test("2053105", "2053105,<EOF>", 100))

########################################################################## 

    def test_simple_string(self):
        """test simple string"""
        input = """ "Yanxi Palace - 2018" """
        expect = """Yanxi Palace - 2018,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 101))

########################################################################## 

    def test_complex_string(self):
        """test complex string"""
        input = """ "This is a string containing tab \t" """
        expect = """This is a string containing tab 	,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 102))

########################################################################## 

    def test_in_des(self):
        input = """number a[5] <- [1,2,3,4,5]
        number b[2,3] <- [[1,2,3],[4,5,6]]"""
        expect = """number,a,[,5,],<-,[,1,,,2,,,3,,,4,,,5,],
,number,b,[,2,,,3,],<-,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],],<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 115))

        input = """a[3 + foo(2)] <- a[b[2,3]] + 4"""
        expect = """a,[,3,+,foo,(,2,),],<-,a,[,b,[,2,,,3,],],+,4,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 116))

        input = """func foo (number a[5], string b)
        begin
            var i <- 0
            for i until i >= 5 by 1
            begin
                a[i] <- i * i + 5
            end
            return -1
        end"""
        expect = """func,foo,(,number,a,[,5,],,,string,b,),
,begin,
,var,i,<-,0,
,for,i,until,i,>=,5,by,1,
,begin,
,a,[,i,],<-,i,*,i,+,5,
,end,
,return,-,1,
,end,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 117))

        input = """aPI <- 3.14
        l[3] <- value * aPI"""
        expect = """aPI,<-,3.14,
,l,[,3,],<-,value,*,aPI,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 118))

        input = """var i<-0
        for i until i >= 10 by 1
            writeNumbe(1)"""
        expect = """var,i,<-,0,
,for,i,until,i,>=,10,by,1,
,writeNumbe,(,1,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 119))

        input = """ begin
         number r
          number s
           r <- 2.0
            number a[5]
             number b[5]
              s <- r * r * 3.14
               a[0] <- s
                end """
        expect = """begin,
,number,r,
,number,s,
,r,<-,2.0,
,number,a,[,5,],
,number,b,[,5,],
,s,<-,r,*,r,*,3.14,
,a,[,0,],<-,s,
,end,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 120))

        input = """func areDivisors (number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main()
            begin 
                var num1 <- readNumber()
                var num2 <- readNumber()
                
                if (areDivisors(num1, num2) writeString("yes"))
                else writeString("No")
            end"""
        expect = """func,areDivisors,(,number,num1,,,number,num2,),
,return,(,(,num1,%,num2,=,0,),or,(,num2,%,num1,=,0,),),
,func,main,(,),
,begin,
,var,num1,<-,readNumber,(,),
,var,num2,<-,readNumber,(,),
,
,if,(,areDivisors,(,num1,,,num2,),writeString,(,yes,),),
,else,writeString,(,No,),
,end,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 121))

        input = """func isPrime(number x)
func main()
    begin
        number x <- readNumber()
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
end
func isPrime(number x)
    begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
            if (x % i = 0) return false
        end
        return true
    end """
        expect = """func,isPrime,(,number,x,),
,func,main,(,),
,begin,
,number,x,<-,readNumber,(,),
,if,(,isPrime,(,x,),),writeString,(,Yes,),
,else,writeString,(,No,),
,end,
,func,isPrime,(,number,x,),
,begin,
,if,(,x,<=,1,),return,false,
,var,i,<-,2,
,for,i,until,i,>,x,/,2,by,1,
,begin,
,if,(,x,%,i,=,0,),return,false,
,end,
,return,true,
,end,<EOF>"""

        self.assertTrue(TestLexer.test(input, expect, 122))

        input = """ """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 123))

########################################################################## 

    def test_keyword(self):
        input = """true"""
        expect = "true,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 124))

        input = """false"""
        expect = "false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 125))

        input = """number"""
        expect = "number,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 126))

        input = """bool"""
        expect = "bool,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 127))

        input = """string"""
        expect = "string,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 128))

        input = """return"""
        expect = "return,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 129))

        input = """var"""
        expect = "var,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 130))

        input = """dynamic"""
        expect = "dynamic,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 131))

        input = """func"""
        expect = "func,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 132))

        input = """for"""
        expect = "for,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 133))

        input = """until"""
        expect = "until,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 134))

        input = """by"""
        expect = "by,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 135))

        input = """break"""
        expect = "break,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 136))

        input = """continue"""
        expect = "continue,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 137))

        input = """if"""
        expect = "if,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 138))

        input = """else"""
        expect = "else,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 139))

        input = """elif"""
        expect = "elif,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 140))

        input = """begin"""
        expect = "begin,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 141))

        input = """end"""
        expect = "end,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 142))

        input = """not"""
        expect = "not,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 143))

        input = """and"""
        expect = "and,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 144))

        input = """or"""
        expect = "or,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 145))

        input = """true false number bool string return var dynamic func for until by break continue if else elif begin end not and or"""
        expect = "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,<EOF>";
        self.assertTrue(TestLexer.test(input, expect, 103))

########################################################################## 

    def test_operators(self):
        input = """+"""
        expect = "+,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 146))

        input = """-"""
        expect = "-,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 147))

        input = """*"""
        expect = "*,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 148))

        input = """/"""
        expect = "/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 149))

        input = """%"""
        expect = "%,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))

        input = """=="""
        expect = "==,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))

        input = """<"""
        expect = "<,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 152))

        input = """<="""
        expect = "<=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 153))

        input = """>"""
        expect = ">,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 154))

        input = """>="""
        expect = ">=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 155))

        input = """..."""
        expect = "...,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 156))

        input = """<-"""
        expect = "<-,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 157))

        input = """!="""
        expect = "!=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 158))

        input = "+-*/%= <- != < <= > >= ... =="
        expect = "+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 104))

########################################################################## 

    def test_seperators(self):
        input = "[(,,)]"
        expect = "[,(,,,,,),],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 105))

########################################################################## 
        
    def test_id(self):
        input = 'A_bcdefgh'
        expect = "A_bcdefgh,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 106))

        input = """variable"""
        expect = "variable,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 159))

        input = """Var123"""
        expect = "Var123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 160))

        input = """_underscore"""
        expect = "_underscore,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))

        input = """mixed_Case"""
        expect = "mixed_Case,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 162))

        input = """Identifier_123"""
        expect = "Identifier_123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 163))

        input = """_"""
        expect = "_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 164))

        input = """var_123"""
        expect = "var_123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 165))

        input = """UpperCase"""
        expect = "UpperCase,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 166))

        input = """camelCaseIdentifier"""
        expect = "camelCaseIdentifier,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 167))

        input = """__double_underscore__"""
        expect = "__double_underscore__,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 168))

        input = """123Variable"""
        expect = "123,Variable,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 169))

        input = """!NotIdentifier"""
        expect = "Error Token !"
        self.assertTrue(TestLexer.test(input, expect, 170))

        input = """-Invalid"""
        expect = "-,Invalid,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 171))

        input = """no spaces"""
        expect = "no,spaces,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 172))

        input = """special@character"""
        expect = "special,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 173))

        input = """empty"""
        expect = "empty,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 174))

        input = """space between"""
        expect = "space,between,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))

        input = """mixedCase-"""
        expect = "mixedCase,-,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))

        input = """under_score_"""
        expect = "under_score_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 177))

        input = """@symbol"""
        expect = "Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 178))

########################################################################## 

    def test_number_literal(self):
        input = '123123123'
        expect = "123123123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 107))

        input = '0.1212'
        expect = "0.1212,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 108))

########################################################################## 

    def test_string_literal(self):
        input = """ "hahaha" """
        expect = "hahaha,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 109))

        input = """ "Khanh dep trai \t \t" """
        expect = "Khanh dep trai 	 	,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 110))

        input = """ "\\b \\f \\r \\n \\t \\\\ \\b \\f \\r \\n \\t \\\\ \\b \\f \\r \\n \\t \\\\" """
        expect = "\\b \\f \\r \\n \\t \\\\ \\b \\f \\r \\n \\t \\\\ \\b \\f \\r \\n \\t \\\\,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,111))

        input = """ "Valid String" """
        expect = "Valid String,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 179))

        input = """ "Escaped '" Quote" """
        expect = """Escaped '" Quote,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 180))

        input = """ "New\nLine" """
        expect = "Unclosed String: New"
        self.assertTrue(TestLexer.test(input, expect, 181))

        input = """ "Tab\tCharacter" """
        expect = "Tab	Character,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 182))

        input = """ "Carriage\rReturn" """
        expect = """Illegal Escape In String: Carriage
"""
        self.assertTrue(TestLexer.test(input, expect, 183))

        input = """ "Backslash \\ Escape" """
        expect = """Illegal Escape In String: Backslash \ """
        self.assertTrue(TestLexer.test(input, expect, 184))

        input = """ "Mixed \' Escape" """
        expect = '''Illegal Escape In String: Mixed ' '''
        self.assertTrue(TestLexer.test(input, expect, 185))

        input = """ "Multiple \' \\ \" Escapes" """
        expect = '''Illegal Escape In String: Multiple ' '''
        self.assertTrue(TestLexer.test(input, expect, 186))

        input = """ "Empty String" """
        expect = "Empty String,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 187))

        input = """ "Special Characters !@#%^&*()" """
        expect = "Special Characters !@#%^&*(),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 188))

        input = """ Unclosed "Quote """
        expect = "Unclosed,Unclosed String: Quote "
        self.assertTrue(TestLexer.test(input, expect, 189))

        input = """ Unterminated \' Escape """
        expect = """Unterminated,Error Token '"""
        self.assertTrue(TestLexer.test(input, expect, 190))

        input = """ Newline
        in String """
        expect = """Newline,
,in,String,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 191))

        input = """ Unescaped ' Quote """
        expect = "Unescaped,Error Token '"
        self.assertTrue(TestLexer.test(input, expect, 192))

        input = """ Invalid Escape Sequence \X """
        expect = '''Invalid,Escape,Sequence,Error Token \\'''
        self.assertTrue(TestLexer.test(input, expect, 193))

        input = """ Unescaped End Quote " """
        expect = "Unescaped,End,Quote,Unclosed String:  "
        self.assertTrue(TestLexer.test(input, expect, 194))

        input = """ Invalid Escape Sequence \\x """
        expect = """Invalid,Escape,Sequence,Error Token \\"""
        self.assertTrue(TestLexer.test(input, expect, 195))

        input = """ Trailing Backslash \ """
        expect = "Trailing,Backslash,Error Token \\"
        self.assertTrue(TestLexer.test(input, expect, 196))

        input = """ Mixed ' and " Quotes """
        expect = "Mixed,Error Token '"
        self.assertTrue(TestLexer.test(input, expect, 197))

        input = """ Unterminated ' Quote """
        expect = "Unterminated,Error Token '"
        self.assertTrue(TestLexer.test(input, expect, 198))

        input = """ Multiple \\' \\' \\' Escapes """
        expect = "Multiple,Error Token \\"
        self.assertTrue(TestLexer.test(input, expect, 199))

########################################################################## 

    def test_unclosed_string(self):
        input = """ "Khanh dep trai \t \t """
        expect = "Unclosed String: Khanh dep trai 	 	 "
        self.assertTrue(TestLexer.test(input, expect, 112))

########################################################################## 
    
    def test_illegal_escape(self):
        input = """ "Khanh dep trai \f"""
        expect = "Illegal Escape In String: Khanh dep trai "
        self.assertTrue(TestLexer.test(input, expect, 113))

########################################################################## 
        
    def test_comment(self):
        input = """ ##this is a single comment.
        a <- 5 """
        expect = """
,a,<-,5,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 114))