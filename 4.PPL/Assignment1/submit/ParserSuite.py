import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))

    def test_in_des(self):
        input = """
            number a[5] <- [1,2,3,4,5]
            number b[2,3] <- [[1,2,3],[4,5,6]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

        input = """
        func main ()
        begin
            a[3 + foo(2)] <- a[b[2,3]] + 4
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

        input = """
        func foo (number a[5], string b)
        begin
            var i <- 0
            for i until i >= 5 by 1
            begin
                a[i] <- i * i + 5
            end
            return -1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

        input = """
        number aPI <- 3.14
        number l[3] <- value * aPI
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

        input = """
        var i<-0
        func main ()
        begin
            for i until i >= 10 by 1
            writeNumbe(1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

        input = """ 
        func main ()
        begin
         number r
          number s
           r <- 2.0
            number a[5]
             number b[5]
              s <- r * r * 3.14
               a[0] <- s
                end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

        input = """
        func areDivisors (number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main()
            begin 
                var num1 <- readNumber()
                var num2 <- readNumber()
                
                if (areDivisors(num1, num2)) writeString("yes")
                else writeString("No")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

        input = """
        func isPrime(number x)
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
    end
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

########################################################################## 

    def test_variable(self):
        input = """func main()
        begin
            number i <- 0
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 209))

        input = """func main()
        begin
            bool i <- 0
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 210))

        input = """func main()
        begin
            string i <- 0
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 211))

        input = """func main()
        begin
            var i <- 0
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 212))

        input = """func main()
        begin
            dynamic i <- 0
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 213))

        input = """func main()
        begin
            number a 
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 214))

        input = """func main()
        begin
            string a
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 215))

        input = """func main()
        begin
            bool c
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 216))

        input = """func main()
        begin
            var abc <- 10
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 217))

        input = """func main()
        begin
            dynamic ccc <- 100.0
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 218))

        input = """func main()
        begin
            bool A <- true
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 219))

        input = """func main()
        begin
            bool d <- false
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 220))

########################################################################## 

    def test_func(self):
        input = """func main()
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 221))

        input = """func main(number haha)
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 222))

        input = """func main(number c [2,3,4])
        begin
            string i <- 0
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 223))

        input = """func main() return 3
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 224))

        input = """func main()
        begin
            dynamic i <- 0
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 225))

        input = """func main(number a, bool b, string c)
        begin
            number a 
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 226))

        input = """func main(number a, number b[1,2,3,4])
        begin
            string a
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 227))

        input = """func main(number a[1,2,32,3,4,9])
        begin
            bool c
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 228))

        input = """func main(number b [2,3])
        begin
            var abc <- 10
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 229))

        input = """func main(string ccc)
        begin
            dynamic ccc <- 100.0
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 230))

        input = """func main()
        begin
            bool A <- true
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 231))

        input = """func main()
        ##comment
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 232))

######################################################################### 

    def test_stmt(self):
        input = """func main()
        begin
            aPI <- 3.14
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 233))

        input = """func main()
        begin
            l[3] <- value * aPi
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 234))

        input = """func main()
        begin
            if (1 + 1 == 2)
                aPI <- 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 235))

        input = """func main()
        begin
            if (1 + 1 == 2)
                aPI <- 1
            elif (2 + 2 == 4)
                aPI <- 4
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 236))

        input = """func main()
        begin
            if (1 + 1 == 2)
                aPI <- 1
            elif (2 + 2 == 4)
                aPI <- 4
            elif (2 + 2 == 4)
                aPI <- 4
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 237))

        input = """func main()
        begin
            if (1 + 1 == 2)
                aPI <- 1
            elif (2 + 2 == 4)
                aPI <- 4
            elif (2 + 2 == 4)
                aPI <- 4
            elif (2 + 2 == 4)
                aPI <- 4
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 238))

        input = """func main()
        begin
            if (1 + 1 == 2)
                aPI <- 1
            else
                aPI <- 15
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 239))

        input = """func main()
        begin
            if (1 + 1 == 2)
                aPI <- 1
            elif (2 + 2 == 4)
                aPI <- 4    
            else
                aPI <- 15
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 240))

        input = """func main()
        begin
            if (1 + 1 == 2)
                aPI <- 1
            elif (2 + 2 == 4)
                aPI <- 4   
            elif (2 + 2 == 4)
                aPI <- 4   
            else
                aPI <- 15
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 241))

        input = """func main()
        begin
            if (1 + 1 == 2)
                aPI <- 1
            elif (2 + 2 == 4)
                aPI <- 4   
            elif (2 + 2 == 4)
                aPI <- 4   
            elif (2 + 2 == 4)
                aPI <- 4  
            else
                aPI <- 15
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 242))

        input = """func main()
        begin
            if (1 + 1 == 2)
                aPI <- 1
            elif (2 + 2 == 4)
                aPI <- 4   
            elif (2 + 2 == 4)
                aPI <- 4   
            elif (2 + 2 == 4)
                aPI <- 4  
            elif (2 + 2 == 4)
                aPI <- 4  
            else
                aPI <- 15
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 243))

        input = """func main()
        begin
            if (1 + 1 == 2)
                aPI <- 1
            elif (2 + 2 == 4)
                aPI <- 4   
            elif (2 + 2 == 4)
                aPI <- 4   
            elif (2 + 2 == 4)
                aPI <- 4  
            elif (2 + 2 == 4)
                aPI <- 4  
            elif (2 + 2 == 4)
                aPI <- 4  
            else
                aPI <- 15
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 244))
        
######################################################################### 

    def test_stmt(self):
        input = """func main()
        begin
            for aPI until a < 2 by a = a + 1
                aPI <- 3
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 245))

        input = """func main()
        begin
            var i <- 0
            for i until i >= 10 by 1
                writeNumbe(i)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 246))

        input = """func main()
        begin
            for i until i == 10 by 2
                i <- 200
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 247))

        input = """func main()
        begin

        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 248))

        input = """func main()
        begin
            for i until i == 10 by 2
                break
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 249))

        input = """func main()
        begin
            for i until i == 10 by 2
                continue
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 250))

        input = """func main()
        begin
            for i until i == 10 by 2
                return true
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 251))

        input = """func main()
        begin
            for i until i == 10 by 2
                return false
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 252))

        input = """func main()
        begin
            for i until i == 10 by 2
                i <- 10
                break
            return
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 253))

        input = """func main()
        begin
            for i until i == 10 by 2
                    i <- 30
                    continue
            return
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 254))

######################################################################### 
    
    def test_stmt2(self):
        input = """func main()
        begin
            foo()
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 255))

        input = """func main()
        begin
            foo(one)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 256))
        
        input = """func main()
        begin
            foo(one, two)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 257))
        
        input = """func main()
        begin
            foo(one, two, three)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 258))
        
        input = """func main()
        begin
            number r
            number s
            r <- 2.0
            number a[5]
            number b[5]
            s <- r * r * 3.14
            a[0] <- s
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 259))

        input = """func main()
        begin
            readNumber()
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 260))
        
        input = """func main()
        begin
            writeNumber(anArg)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 261))
        
        input = """func main()
        begin
            readBool()
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 262))

        input = """func main()
        begin
            writeBool(anArg)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 263))
        
        input = """func main()
        begin
            readString()
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 264))

        input = """func main()
        begin
            writeString(anArg)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 265))

######################################################################### 
    
    def test_expr(self):
        input = """func main()
        begin
            haha <- -1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 266))

        input = """func main()
        begin
            haha <- 1 + 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 267))
        input = """func main()
        begin
            haha <- 1 - 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 268))

        input = """func main()
        begin
            haha <- 1 * 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 269))

        input = """func main()
        begin
            haha <- 1 / 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 270))

        input = """func main()
        begin
            haha <- 1 % 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 271))

        input = """func main()
        begin
            haha <- not 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 272))

        input = """func main()
        begin
            haha <- 1 and 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 273))
        input = """func main()
        begin
            haha <- 1 or 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 274))

        input = """func main()
        begin
            haha <- 1 and not 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 275))

        input = """func main()
        begin
            haha <- hahahaha ... hahahahah
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 276))

        input = """func main()
        begin
            haha <- 1 + 2 - 2 * 3 / 4 and 7
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 277))
        input = """func main()
        begin
            haha <- (string1 ... string2) ... string3
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 278))
        input = """func main()
        begin
            haha <- 1 = 2 
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 279))
        input = """func main()
        begin
            haha <- 1 != 2
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 280))
        input = """func main()
        begin
            haha <- 1 < 2
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 281))
        input = """func main()
        begin
            haha <- 1 > 2
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 282))
        input = """func main()
        begin
            haha <- 1 <= 2
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 283))
        input = """func main()
        begin
            haha <- 1 >= 2
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 284))
        input = """func main()
        begin
            haha <- 1 == 2
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 285))

        input = """func main()
        begin
            haha <- string1 == string2
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 286))
        input = """func main()
        begin
            haha <- string1 == string2
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 287))
        input = """func main()
        begin
            a[3 + foo(2)] <- a[b[2, 3]] + 4
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 288))
        input = """func main()
        begin
            a[3 + foo(2)] <- 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 289))
        input = """func main()
        begin
            haha <-  a[3 + foo(2)]
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 290))
        input = """func main()
        begin
            haha <- a[3]
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 291))
        input = """func main()
        begin
            haha <- a[3,4,5]
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 292))
        input = """func main()
        begin
            haha <- foo()
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 293))
        input = """func main()
        begin
            haha <- foo(15, 20)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 294))
        input = """func main()
        begin
            haha <- a[foo(string1, string2)]
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 295))

        input = """func main()
        begin
            haha <- numb1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 296))

        input = """func main()
        begin
            haha <- numb1 ... numb2 and numb3
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 297))

        input = """func main()
        begin
            if (exp1) 
                return true
            return false
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 298))

        input = """func main()
        begin
            for i until i < 10 by 1
                i <- i + 1
            print(i)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 299))