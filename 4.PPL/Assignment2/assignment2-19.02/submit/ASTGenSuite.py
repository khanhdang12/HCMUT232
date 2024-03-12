import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def testcase(self):
		input = '''
number var2 <- 99.19
bool test <- 62.34
bool x[52.6,72.42,92.01]
bool a
'''
		expect = '''Program([VarDecl(Id(var2), NumberType, None, NumLit(99.19)), VarDecl(Id(test), BoolType, None, NumLit(62.34)), VarDecl(Id(x), ArrayType([52.6, 72.42, 92.01], BoolType), None, None), VarDecl(Id(a), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 300))

		input = '''
bool d <- function(pizza((- - 8.99)))["test", 6.52]
func variable ()	begin
	end

bool d[33.87,94.09] <- false
func x (bool healthy, bool var1[96.39,43.04,70.65], string func1[48.83,79.19,68.35])
	begin
	end

func y (bool b)	begin
		for func1 until function by false
			continue
	end

'''
		expect = '''Program([VarDecl(Id(d), BoolType, None, ArrayCell(CallExpr(Id(function), [CallExpr(Id(pizza), [UnaryOp(-, UnaryOp(-, NumLit(8.99)))])]), [StringLit(test), NumLit(6.52)])), FuncDecl(Id(variable), [], Block([])), VarDecl(Id(d), ArrayType([33.87, 94.09], BoolType), None, BooleanLit(False)), FuncDecl(Id(x), [VarDecl(Id(healthy), BoolType, None, None), VarDecl(Id(var1), ArrayType([96.39, 43.04, 70.65], BoolType), None, None), VarDecl(Id(func1), ArrayType([48.83, 79.19, 68.35], StringType), None, None)], Block([])), FuncDecl(Id(y), [VarDecl(Id(b), BoolType, None, None)], Block([For(Id(func1), Id(function), BooleanLit(False), Continue)]))])'''
		self.assertTrue(TestAST.test(input, expect, 301))

		input = '''
string func1
func d (string func2, number c)	begin
		continue
		break
	end
func var1 (number z, number y, string pizza)
	return 90.29

number var1[98.91]
'''
		expect = '''Program([VarDecl(Id(func1), StringType, None, None), FuncDecl(Id(d), [VarDecl(Id(func2), StringType, None, None), VarDecl(Id(c), NumberType, None, None)], Block([Continue, Break])), FuncDecl(Id(var1), [VarDecl(Id(z), NumberType, None, None), VarDecl(Id(y), NumberType, None, None), VarDecl(Id(pizza), StringType, None, None)], Return(NumLit(90.29))), VarDecl(Id(var1), ArrayType([98.91], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 302))

		input = '''
number a[22.58,44.12,12.2] <- "b"
func func2 ()	return
func b ()
	return false

string var2[86.15] <- "abc"
func def (bool a, string c, bool var2[55.85])
	begin
		z()
	end
'''
		expect = '''Program([VarDecl(Id(a), ArrayType([22.58, 44.12, 12.2], NumberType), None, StringLit(b)), FuncDecl(Id(func2), [], Return()), FuncDecl(Id(b), [], Return(BooleanLit(False))), VarDecl(Id(var2), ArrayType([86.15], StringType), None, StringLit(abc)), FuncDecl(Id(def), [VarDecl(Id(a), BoolType, None, None), VarDecl(Id(c), StringType, None, None), VarDecl(Id(var2), ArrayType([55.85], BoolType), None, None)], Block([CallStmt(Id(z), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 303))

		input = '''
bool function
var func1 <- variable
func asm2 ()
	return 89.23

string y[67.54]
dynamic healthy
'''
		expect = '''Program([VarDecl(Id(function), BoolType, None, None), VarDecl(Id(func1), None, var, Id(variable)), FuncDecl(Id(asm2), [], Return(NumLit(89.23))), VarDecl(Id(y), ArrayType([67.54], StringType), None, None), VarDecl(Id(healthy), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 304))

		input = '''
string z[36.38] <- true
func a (number asm2[51.81,15.02,56.86], bool asm2[71.29])
	return "function"

func y (number foo[26.96,32.34], string a[59.03,51.02,81.61], string abc)	begin
		func1 <- "d"
	end
'''
		expect = '''Program([VarDecl(Id(z), ArrayType([36.38], StringType), None, BooleanLit(True)), FuncDecl(Id(a), [VarDecl(Id(asm2), ArrayType([51.81, 15.02, 56.86], NumberType), None, None), VarDecl(Id(asm2), ArrayType([71.29], BoolType), None, None)], Return(StringLit(function))), FuncDecl(Id(y), [VarDecl(Id(foo), ArrayType([26.96, 32.34], NumberType), None, None), VarDecl(Id(a), ArrayType([59.03, 51.02, 81.61], StringType), None, None), VarDecl(Id(abc), StringType, None, None)], Block([AssignStmt(Id(func1), StringLit(d))]))])'''
		self.assertTrue(TestAST.test(input, expect, 305))

		input = '''
func d (number func1)	return "abc"

func y (bool function[53.65,90.2], bool asm2)
	return

'''
		expect = '''Program([FuncDecl(Id(d), [VarDecl(Id(func1), NumberType, None, None)], Return(StringLit(abc))), FuncDecl(Id(y), [VarDecl(Id(function), ArrayType([53.65, 90.2], BoolType), None, None), VarDecl(Id(asm2), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 306))

		input = '''
func asm2 (bool function[87.63], bool func1)	return
func test (number z)
	return false
'''
		expect = '''Program([FuncDecl(Id(asm2), [VarDecl(Id(function), ArrayType([87.63], BoolType), None, None), VarDecl(Id(func1), BoolType, None, None)], Return()), FuncDecl(Id(test), [VarDecl(Id(z), NumberType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 307))

		input = '''
func test (number x)
	begin
		c[true, foo, false] <- "b"
	end

func c (bool x)	return y
bool function
number x[0.55,91.09]
string b[50.27,34.6]
'''
		expect = '''Program([FuncDecl(Id(test), [VarDecl(Id(x), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(c), [BooleanLit(True), Id(foo), BooleanLit(False)]), StringLit(b))])), FuncDecl(Id(c), [VarDecl(Id(x), BoolType, None, None)], Return(Id(y))), VarDecl(Id(function), BoolType, None, None), VarDecl(Id(x), ArrayType([0.55, 91.09], NumberType), None, None), VarDecl(Id(b), ArrayType([50.27, 34.6], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 308))

		input = '''
func c (number z)	return 11.94

func var2 (bool def[67.48])
	return
'''
		expect = '''Program([FuncDecl(Id(c), [VarDecl(Id(z), NumberType, None, None)], Return(NumLit(11.94))), FuncDecl(Id(var2), [VarDecl(Id(def), ArrayType([67.48], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 309))

		input = '''
func var1 (bool pizza[80.94,84.78])
	return "function"

string pizza <- false
'''
		expect = '''Program([FuncDecl(Id(var1), [VarDecl(Id(pizza), ArrayType([80.94, 84.78], BoolType), None, None)], Return(StringLit(function))), VarDecl(Id(pizza), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 310))

		input = '''
func func2 (number y[20.94,80.19], bool z)
	return
number foo[94.96]
'''
		expect = '''Program([FuncDecl(Id(func2), [VarDecl(Id(y), ArrayType([20.94, 80.19], NumberType), None, None), VarDecl(Id(z), BoolType, None, None)], Return()), VarDecl(Id(foo), ArrayType([94.96], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 311))

		input = '''
number foo[48.48,22.0,14.71] <- false
func a (number func2, bool foo)
	return 86.86
func y (string test, string a)	return z

number var2[29.21,82.96]
'''
		expect = '''Program([VarDecl(Id(foo), ArrayType([48.48, 22.0, 14.71], NumberType), None, BooleanLit(False)), FuncDecl(Id(a), [VarDecl(Id(func2), NumberType, None, None), VarDecl(Id(foo), BoolType, None, None)], Return(NumLit(86.86))), FuncDecl(Id(y), [VarDecl(Id(test), StringType, None, None), VarDecl(Id(a), StringType, None, None)], Return(Id(z))), VarDecl(Id(var2), ArrayType([29.21, 82.96], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 312))

		input = '''
string y[79.97] <- d
func var2 (number a, string function[51.72,24.44,78.71])	return

string var2
string z[89.81,64.55,74.36]
'''
		expect = '''Program([VarDecl(Id(y), ArrayType([79.97], StringType), None, Id(d)), FuncDecl(Id(var2), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(function), ArrayType([51.72, 24.44, 78.71], StringType), None, None)], Return()), VarDecl(Id(var2), StringType, None, None), VarDecl(Id(z), ArrayType([89.81, 64.55, 74.36], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 313))

		input = '''
func asm2 (bool z[42.16,92.31,38.49], number test)
	begin
		for variable until "test" by "b"
			variable <- foo
		if ("x")
		return 31.19
		elif ("x")
		c()
		elif (99.11) for x until c by true
			for function until def by true
				begin
				end
		elif (43.08) for pizza until 52.1 by true
			continue
	end
func z (string b[94.66,38.14,76.57], string y[51.26], bool y)
	begin
		if (41.07) if (func2) for z until false by true
			d("c", "func2", 70.92)
		elif ("func")
		bool var1 <- var1
		elif (c) continue
		elif (false)
		continue
		elif ("var2")
		begin
			begin
				bool b[33.15,25.68] <- c
				begin
					continue
					var asm2 <- true
				end
				begin
				end
			end
		end
		elif ("healthy")
		return
		else for y until def by 76.93
			continue
	end
func x (number b)	return true
'''
		expect = '''Program([FuncDecl(Id(asm2), [VarDecl(Id(z), ArrayType([42.16, 92.31, 38.49], BoolType), None, None), VarDecl(Id(test), NumberType, None, None)], Block([For(Id(variable), StringLit(test), StringLit(b), AssignStmt(Id(variable), Id(foo))), If((StringLit(x), Return(NumLit(31.19))), [(StringLit(x), CallStmt(Id(c), [])), (NumLit(99.11), For(Id(x), Id(c), BooleanLit(True), For(Id(function), Id(def), BooleanLit(True), Block([])))), (NumLit(43.08), For(Id(pizza), NumLit(52.1), BooleanLit(True), Continue))], None)])), FuncDecl(Id(z), [VarDecl(Id(b), ArrayType([94.66, 38.14, 76.57], StringType), None, None), VarDecl(Id(y), ArrayType([51.26], StringType), None, None), VarDecl(Id(y), BoolType, None, None)], Block([If((NumLit(41.07), If((Id(func2), For(Id(z), BooleanLit(False), BooleanLit(True), CallStmt(Id(d), [StringLit(c), StringLit(func2), NumLit(70.92)]))), [(StringLit(func), VarDecl(Id(var1), BoolType, None, Id(var1))), (Id(c), Continue), (BooleanLit(False), Continue), (StringLit(var2), Block([Block([VarDecl(Id(b), ArrayType([33.15, 25.68], BoolType), None, Id(c)), Block([Continue, VarDecl(Id(asm2), None, var, BooleanLit(True))]), Block([])])])), (StringLit(healthy), Return())], For(Id(y), Id(def), NumLit(76.93), Continue))), [], None)])), FuncDecl(Id(x), [VarDecl(Id(b), NumberType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 314))

		input = '''
bool a <- 60.15
bool foo[45.08] <- c
'''
		expect = '''Program([VarDecl(Id(a), BoolType, None, NumLit(60.15)), VarDecl(Id(foo), ArrayType([45.08], BoolType), None, Id(c))])'''
		self.assertTrue(TestAST.test(input, expect, 315))

		input = '''
func func2 (string abc[98.12,0.78,24.14], string a[54.58,90.03,2.62])	return
func def ()	return
string func2
'''
		expect = '''Program([FuncDecl(Id(func2), [VarDecl(Id(abc), ArrayType([98.12, 0.78, 24.14], StringType), None, None), VarDecl(Id(a), ArrayType([54.58, 90.03, 2.62], StringType), None, None)], Return()), FuncDecl(Id(def), [], Return()), VarDecl(Id(func2), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 316))

		input = '''
func var1 (number b[48.87], string b[63.96,62.8], number a[74.22,66.96])
	begin
		return false
		if (true)
		variable["y", true] <- "abc"
	end

var foo <- abc
func pizza ()	return

func z ()	return

'''
		expect = '''Program([FuncDecl(Id(var1), [VarDecl(Id(b), ArrayType([48.87], NumberType), None, None), VarDecl(Id(b), ArrayType([63.96, 62.8], StringType), None, None), VarDecl(Id(a), ArrayType([74.22, 66.96], NumberType), None, None)], Block([Return(BooleanLit(False)), If((BooleanLit(True), AssignStmt(ArrayCell(Id(variable), [StringLit(y), BooleanLit(True)]), StringLit(abc))), [], None)])), VarDecl(Id(foo), None, var, Id(abc)), FuncDecl(Id(pizza), [], Return()), FuncDecl(Id(z), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 317))

		input = '''
dynamic c
string d[73.51,50.79]
func b (string a, bool foo, number function)	return 75.41
func var2 (bool def, number func2[91.93,93.16,88.92], string var2[13.79])
	begin
	end

func var1 ()
	begin
		if (true)
		function <- var2
		else continue
		number x <- 13.37
	end

'''
		expect = '''Program([VarDecl(Id(c), None, dynamic, None), VarDecl(Id(d), ArrayType([73.51, 50.79], StringType), None, None), FuncDecl(Id(b), [VarDecl(Id(a), StringType, None, None), VarDecl(Id(foo), BoolType, None, None), VarDecl(Id(function), NumberType, None, None)], Return(NumLit(75.41))), FuncDecl(Id(var2), [VarDecl(Id(def), BoolType, None, None), VarDecl(Id(func2), ArrayType([91.93, 93.16, 88.92], NumberType), None, None), VarDecl(Id(var2), ArrayType([13.79], StringType), None, None)], Block([])), FuncDecl(Id(var1), [], Block([If((BooleanLit(True), AssignStmt(Id(function), Id(var2))), [], Continue), VarDecl(Id(x), NumberType, None, NumLit(13.37))]))])'''
		self.assertTrue(TestAST.test(input, expect, 318))

		input = '''
func pizza ()
	return
number x[60.33,63.5,0.63]
func z (number test[72.2,97.64], string b, string function[76.94,83.86,1.77])	return
dynamic d
'''
		expect = '''Program([FuncDecl(Id(pizza), [], Return()), VarDecl(Id(x), ArrayType([60.33, 63.5, 0.63], NumberType), None, None), FuncDecl(Id(z), [VarDecl(Id(test), ArrayType([72.2, 97.64], NumberType), None, None), VarDecl(Id(b), StringType, None, None), VarDecl(Id(function), ArrayType([76.94, 83.86, 1.77], StringType), None, None)], Return()), VarDecl(Id(d), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 319))

		input = '''
func x (number y[6.14,36.81,55.0])	begin
		for c until func2 by 58.69
			continue
		begin
			continue
			if (false)
			if (d) for def until 71.47 by true
				if (73.39) continue
				elif (false)
				return
				elif ("function")
				asm2 <- "a"
				else for function until "variable" by "func"
					if (38.43) return "func1"
					elif ("var2") bool a <- false
					elif (4.03)
					asm2["func1"] <- func1
					elif (true) var1 <- false
					elif (7.03)
					for c until y by true
						continue
					elif (func2)
					return
			elif (foo) number b[21.85]
			elif (true)
			begin
			end
			elif (19.54) for func1 until func1 by "z"
				begin
				end
			elif (test) return
			elif (12.65)
			bool var2[42.71]
		end
	end
string y[94.18,15.89] <- false
string abc
'''
		expect = '''Program([FuncDecl(Id(x), [VarDecl(Id(y), ArrayType([6.14, 36.81, 55.0], NumberType), None, None)], Block([For(Id(c), Id(func2), NumLit(58.69), Continue), Block([Continue, If((BooleanLit(False), If((Id(d), For(Id(def), NumLit(71.47), BooleanLit(True), If((NumLit(73.39), Continue), [(BooleanLit(False), Return()), (StringLit(function), AssignStmt(Id(asm2), StringLit(a)))], For(Id(function), StringLit(variable), StringLit(func), If((NumLit(38.43), Return(StringLit(func1))), [(StringLit(var2), VarDecl(Id(a), BoolType, None, BooleanLit(False))), (NumLit(4.03), AssignStmt(ArrayCell(Id(asm2), [StringLit(func1)]), Id(func1))), (BooleanLit(True), AssignStmt(Id(var1), BooleanLit(False))), (NumLit(7.03), For(Id(c), Id(y), BooleanLit(True), Continue)), (Id(func2), Return()), (Id(foo), VarDecl(Id(b), ArrayType([21.85], NumberType), None, None)), (BooleanLit(True), Block([])), (NumLit(19.54), For(Id(func1), Id(func1), StringLit(z), Block([]))), (Id(test), Return()), (NumLit(12.65), VarDecl(Id(var2), ArrayType([42.71], BoolType), None, None))], None))))), [], None)), [], None)])])), VarDecl(Id(y), ArrayType([94.18, 15.89], StringType), None, BooleanLit(False)), VarDecl(Id(abc), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 320))

		input = '''
number healthy
func var2 (string d)
	return foo
func var2 (number d[40.56,17.41], number abc[41.22,41.27,87.95])
	return
func var1 (string function[44.19,75.93,71.41], bool x, bool x[53.15,41.86])
	return

func d ()	return

'''
		expect = '''Program([VarDecl(Id(healthy), NumberType, None, None), FuncDecl(Id(var2), [VarDecl(Id(d), StringType, None, None)], Return(Id(foo))), FuncDecl(Id(var2), [VarDecl(Id(d), ArrayType([40.56, 17.41], NumberType), None, None), VarDecl(Id(abc), ArrayType([41.22, 41.27, 87.95], NumberType), None, None)], Return()), FuncDecl(Id(var1), [VarDecl(Id(function), ArrayType([44.19, 75.93, 71.41], StringType), None, None), VarDecl(Id(x), BoolType, None, None), VarDecl(Id(x), ArrayType([53.15, 41.86], BoolType), None, None)], Return()), FuncDecl(Id(d), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 321))

		input = '''
dynamic func2 <- y
string var2
'''
		expect = '''Program([VarDecl(Id(func2), None, dynamic, Id(y)), VarDecl(Id(var2), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 322))

		input = '''
string def
'''
		expect = '''Program([VarDecl(Id(def), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 323))

		input = '''
func var1 (string foo)
	begin
		break
		if (true) for healthy until b by asm2
			return
		elif (6.91)
		dynamic healthy
		elif (true)
		x[c, false, foo] <- "foo"
	end
func b (string function[65.47,17.66,79.77])	return
func a ()
	return abc

'''
		expect = '''Program([FuncDecl(Id(var1), [VarDecl(Id(foo), StringType, None, None)], Block([Break, If((BooleanLit(True), For(Id(healthy), Id(b), Id(asm2), Return())), [(NumLit(6.91), VarDecl(Id(healthy), None, dynamic, None)), (BooleanLit(True), AssignStmt(ArrayCell(Id(x), [Id(c), BooleanLit(False), Id(foo)]), StringLit(foo)))], None)])), FuncDecl(Id(b), [VarDecl(Id(function), ArrayType([65.47, 17.66, 79.77], StringType), None, None)], Return()), FuncDecl(Id(a), [], Return(Id(abc)))])'''
		self.assertTrue(TestAST.test(input, expect, 324))

		input = '''
bool func2[4.82]
func test (string foo, string func1[60.56])
	return "func2"

func function (bool test[26.36,25.42], number x, bool func1[55.05,25.78,3.59])
	begin
		for def until false by false
			break
		continue
		return
	end

'''
		expect = '''Program([VarDecl(Id(func2), ArrayType([4.82], BoolType), None, None), FuncDecl(Id(test), [VarDecl(Id(foo), StringType, None, None), VarDecl(Id(func1), ArrayType([60.56], StringType), None, None)], Return(StringLit(func2))), FuncDecl(Id(function), [VarDecl(Id(test), ArrayType([26.36, 25.42], BoolType), None, None), VarDecl(Id(x), NumberType, None, None), VarDecl(Id(func1), ArrayType([55.05, 25.78, 3.59], BoolType), None, None)], Block([For(Id(def), BooleanLit(False), BooleanLit(False), Break), Continue, Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 325))

		input = '''
bool pizza[42.1,60.53] <- "func"
'''
		expect = '''Program([VarDecl(Id(pizza), ArrayType([42.1, 60.53], BoolType), None, StringLit(func))])'''
		self.assertTrue(TestAST.test(input, expect, 326))

		input = '''
string function <- false
bool abc
var variable <- 41.55
func a (bool x, string func1)
	begin
	end

string healthy
'''
		expect = '''Program([VarDecl(Id(function), StringType, None, BooleanLit(False)), VarDecl(Id(abc), BoolType, None, None), VarDecl(Id(variable), None, var, NumLit(41.55)), FuncDecl(Id(a), [VarDecl(Id(x), BoolType, None, None), VarDecl(Id(func1), StringType, None, None)], Block([])), VarDecl(Id(healthy), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 327))

		input = '''
func def (number func1, bool var2[30.44,90.75,21.69], string func2[54.31,26.84,60.65])	return

var foo <- test
'''
		expect = '''Program([FuncDecl(Id(def), [VarDecl(Id(func1), NumberType, None, None), VarDecl(Id(var2), ArrayType([30.44, 90.75, 21.69], BoolType), None, None), VarDecl(Id(func2), ArrayType([54.31, 26.84, 60.65], StringType), None, None)], Return()), VarDecl(Id(foo), None, var, Id(test))])'''
		self.assertTrue(TestAST.test(input, expect, 328))

		input = '''
func x (number test, bool d)	return 61.49

func abc (string b, string asm2[50.46])	return

'''
		expect = '''Program([FuncDecl(Id(x), [VarDecl(Id(test), NumberType, None, None), VarDecl(Id(d), BoolType, None, None)], Return(NumLit(61.49))), FuncDecl(Id(abc), [VarDecl(Id(b), StringType, None, None), VarDecl(Id(asm2), ArrayType([50.46], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 329))

		input = '''
bool x[76.54,21.35,23.09]
'''
		expect = '''Program([VarDecl(Id(x), ArrayType([76.54, 21.35, 23.09], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 330))

		input = '''
bool func1
string func1 <- "func"
'''
		expect = '''Program([VarDecl(Id(func1), BoolType, None, None), VarDecl(Id(func1), StringType, None, StringLit(func))])'''
		self.assertTrue(TestAST.test(input, expect, 331))

		input = '''
func variable ()
	return 53.52
func test (number function[26.32], number asm2[36.7,78.78], bool test)	return
func def (string x[63.84,2.04,58.51], string a[9.97,56.22])
	return
'''
		expect = '''Program([FuncDecl(Id(variable), [], Return(NumLit(53.52))), FuncDecl(Id(test), [VarDecl(Id(function), ArrayType([26.32], NumberType), None, None), VarDecl(Id(asm2), ArrayType([36.7, 78.78], NumberType), None, None), VarDecl(Id(test), BoolType, None, None)], Return()), FuncDecl(Id(def), [VarDecl(Id(x), ArrayType([63.84, 2.04, 58.51], StringType), None, None), VarDecl(Id(a), ArrayType([9.97, 56.22], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 332))

		input = '''
number foo[71.05,45.62,19.13] <- 31.66
bool y[22.42,27.02]
'''
		expect = '''Program([VarDecl(Id(foo), ArrayType([71.05, 45.62, 19.13], NumberType), None, NumLit(31.66)), VarDecl(Id(y), ArrayType([22.42, 27.02], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 333))

		input = '''
func func2 (number func1, bool x[63.05], number def)	return
number b[69.96,36.93]
func a (string def)
	begin
		func1(12.0, 92.5, false)
		for x until var2 by func1
			asm2 <- "function"
	end

'''
		expect = '''Program([FuncDecl(Id(func2), [VarDecl(Id(func1), NumberType, None, None), VarDecl(Id(x), ArrayType([63.05], BoolType), None, None), VarDecl(Id(def), NumberType, None, None)], Return()), VarDecl(Id(b), ArrayType([69.96, 36.93], NumberType), None, None), FuncDecl(Id(a), [VarDecl(Id(def), StringType, None, None)], Block([CallStmt(Id(func1), [NumLit(12.0), NumLit(92.5), BooleanLit(False)]), For(Id(x), Id(var2), Id(func1), AssignStmt(Id(asm2), StringLit(function)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 334))

		input = '''
func a ()	return

'''
		expect = '''Program([FuncDecl(Id(a), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 335))

		input = '''
func c (string a[77.21,91.66])	return

bool x
func a ()	return false

bool c
string function
'''
		expect = '''Program([FuncDecl(Id(c), [VarDecl(Id(a), ArrayType([77.21, 91.66], StringType), None, None)], Return()), VarDecl(Id(x), BoolType, None, None), FuncDecl(Id(a), [], Return(BooleanLit(False))), VarDecl(Id(c), BoolType, None, None), VarDecl(Id(function), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 336))

		input = '''
func func1 (number a[38.91,60.78,68.2], bool var2[58.13,58.88,96.95])	begin
		if (true)
		for var2 until 45.14 by true
			asm2[abc, "variable"] <- true
		elif ("y") function()
		elif ("foo")
		if (12.85)
		continue
		elif (false) begin
			begin
				variable(92.43, "func1", variable)
			end
			function[false, true, z] <- "a"
		end
		elif (foo)
		bool variable[20.39,49.52,67.08] <- "var2"
		else continue
		elif (true)
		return
		else break
		dynamic x
		if ("var2") return
		elif (func1)
		number asm2[78.54] <- "x"
		elif (false)
		if (87.89) if (true)
		bool asm2 <- func2
		elif (false) return
		elif (39.95)
		continue
		elif (58.87)
		if (90.21) return 43.54
		elif (true)
		if (def) def("def", function)
		elif (43.88) break
		elif (false) for b until 47.89 by 59.02
			if ("healthy") begin
				func2[9.45] <- false
				string test
				break
			end
			elif (true) begin
			end
			elif ("asm2")
			break
			elif (77.91)
			foo[false, "func", 59.67] <- variable
			elif (52.67) continue
			elif (true)
			a(z, 85.68, true)
			else return function
		elif ("z")
		number pizza[50.81,63.01,3.43]
		elif (false) for var2 until true by 2.1
			x(11.72)
		elif ("function")
		return
		elif (c)
		break
		elif ("var1")
		var2("pizza", true, foo)
	end

bool pizza <- 25.72
'''
		expect = '''Program([FuncDecl(Id(func1), [VarDecl(Id(a), ArrayType([38.91, 60.78, 68.2], NumberType), None, None), VarDecl(Id(var2), ArrayType([58.13, 58.88, 96.95], BoolType), None, None)], Block([If((BooleanLit(True), For(Id(var2), NumLit(45.14), BooleanLit(True), AssignStmt(ArrayCell(Id(asm2), [Id(abc), StringLit(variable)]), BooleanLit(True)))), [(StringLit(y), CallStmt(Id(function), [])), (StringLit(foo), If((NumLit(12.85), Continue), [(BooleanLit(False), Block([Block([CallStmt(Id(variable), [NumLit(92.43), StringLit(func1), Id(variable)])]), AssignStmt(ArrayCell(Id(function), [BooleanLit(False), BooleanLit(True), Id(z)]), StringLit(a))])), (Id(foo), VarDecl(Id(variable), ArrayType([20.39, 49.52, 67.08], BoolType), None, StringLit(var2)))], Continue)), (BooleanLit(True), Return())], Break), VarDecl(Id(x), None, dynamic, None), If((StringLit(var2), Return()), [(Id(func1), VarDecl(Id(asm2), ArrayType([78.54], NumberType), None, StringLit(x))), (BooleanLit(False), If((NumLit(87.89), If((BooleanLit(True), VarDecl(Id(asm2), BoolType, None, Id(func2))), [(BooleanLit(False), Return()), (NumLit(39.95), Continue), (NumLit(58.87), If((NumLit(90.21), Return(NumLit(43.54))), [(BooleanLit(True), If((Id(def), CallStmt(Id(def), [StringLit(def), Id(function)])), [(NumLit(43.88), Break), (BooleanLit(False), For(Id(b), NumLit(47.89), NumLit(59.02), If((StringLit(healthy), Block([AssignStmt(ArrayCell(Id(func2), [NumLit(9.45)]), BooleanLit(False)), VarDecl(Id(test), StringType, None, None), Break])), [(BooleanLit(True), Block([])), (StringLit(asm2), Break), (NumLit(77.91), AssignStmt(ArrayCell(Id(foo), [BooleanLit(False), StringLit(func), NumLit(59.67)]), Id(variable))), (NumLit(52.67), Continue), (BooleanLit(True), CallStmt(Id(a), [Id(z), NumLit(85.68), BooleanLit(True)]))], Return(Id(function))))), (StringLit(z), VarDecl(Id(pizza), ArrayType([50.81, 63.01, 3.43], NumberType), None, None)), (BooleanLit(False), For(Id(var2), BooleanLit(True), NumLit(2.1), CallStmt(Id(x), [NumLit(11.72)])))], None)), (StringLit(function), Return())], None)), (Id(c), Break)], None)), [], None)), (StringLit(var1), CallStmt(Id(var2), [StringLit(pizza), BooleanLit(True), Id(foo)]))], None)])), VarDecl(Id(pizza), BoolType, None, NumLit(25.72))])'''
		self.assertTrue(TestAST.test(input, expect, 337))

		input = '''
func asm2 (bool func2, number c[52.07,13.61])	return b

string variable
func asm2 (string variable, bool healthy)
	return
'''
		expect = '''Program([FuncDecl(Id(asm2), [VarDecl(Id(func2), BoolType, None, None), VarDecl(Id(c), ArrayType([52.07, 13.61], NumberType), None, None)], Return(Id(b))), VarDecl(Id(variable), StringType, None, None), FuncDecl(Id(asm2), [VarDecl(Id(variable), StringType, None, None), VarDecl(Id(healthy), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 338))

		input = '''
var abc <- true
number var1[96.97]
func b (bool test, string func2[33.94], number c[6.93])	begin
		continue
		begin
		end
		break
	end
func var2 ()
	return
'''
		expect = '''Program([VarDecl(Id(abc), None, var, BooleanLit(True)), VarDecl(Id(var1), ArrayType([96.97], NumberType), None, None), FuncDecl(Id(b), [VarDecl(Id(test), BoolType, None, None), VarDecl(Id(func2), ArrayType([33.94], StringType), None, None), VarDecl(Id(c), ArrayType([6.93], NumberType), None, None)], Block([Continue, Block([]), Break])), FuncDecl(Id(var2), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 339))

		input = '''
func b (string pizza[12.46,23.44,34.01], string var1[62.1,83.99,54.18])
	begin
	end
string func2[61.82,34.82,25.48]
number d[81.86,3.76]
'''
		expect = '''Program([FuncDecl(Id(b), [VarDecl(Id(pizza), ArrayType([12.46, 23.44, 34.01], StringType), None, None), VarDecl(Id(var1), ArrayType([62.1, 83.99, 54.18], StringType), None, None)], Block([])), VarDecl(Id(func2), ArrayType([61.82, 34.82, 25.48], StringType), None, None), VarDecl(Id(d), ArrayType([81.86, 3.76], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 340))

		input = '''
string var2 <- false
func abc ()
	return "func2"

number asm2
func variable (number x, bool y[95.66,20.07,8.49], number x)
	begin
	end
'''
		expect = '''Program([VarDecl(Id(var2), StringType, None, BooleanLit(False)), FuncDecl(Id(abc), [], Return(StringLit(func2))), VarDecl(Id(asm2), NumberType, None, None), FuncDecl(Id(variable), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(y), ArrayType([95.66, 20.07, 8.49], BoolType), None, None), VarDecl(Id(x), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 341))

		input = '''
dynamic var1
'''
		expect = '''Program([VarDecl(Id(var1), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 342))

		input = '''
var variable <- false
'''
		expect = '''Program([VarDecl(Id(variable), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 343))

		input = '''
func func2 (string variable, bool def, number abc[56.9])	begin
	end

number x
bool y[1.17,57.27,73.47]
func x (bool x[6.32,62.16], string x[88.9], number pizza)	return false

func var2 (string def, string c)
	return "test"

'''
		expect = '''Program([FuncDecl(Id(func2), [VarDecl(Id(variable), StringType, None, None), VarDecl(Id(def), BoolType, None, None), VarDecl(Id(abc), ArrayType([56.9], NumberType), None, None)], Block([])), VarDecl(Id(x), NumberType, None, None), VarDecl(Id(y), ArrayType([1.17, 57.27, 73.47], BoolType), None, None), FuncDecl(Id(x), [VarDecl(Id(x), ArrayType([6.32, 62.16], BoolType), None, None), VarDecl(Id(x), ArrayType([88.9], StringType), None, None), VarDecl(Id(pizza), NumberType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(var2), [VarDecl(Id(def), StringType, None, None), VarDecl(Id(c), StringType, None, None)], Return(StringLit(test)))])'''
		self.assertTrue(TestAST.test(input, expect, 344))

		input = '''
func var2 (bool pizza[72.05,33.5])	return "x"
func var2 (bool x)	return 19.01

bool x[48.78] <- d
func func2 (bool abc, string a, bool variable[58.57,83.74])
	return
string c[1.73,19.58,96.61]
'''
		expect = '''Program([FuncDecl(Id(var2), [VarDecl(Id(pizza), ArrayType([72.05, 33.5], BoolType), None, None)], Return(StringLit(x))), FuncDecl(Id(var2), [VarDecl(Id(x), BoolType, None, None)], Return(NumLit(19.01))), VarDecl(Id(x), ArrayType([48.78], BoolType), None, Id(d)), FuncDecl(Id(func2), [VarDecl(Id(abc), BoolType, None, None), VarDecl(Id(a), StringType, None, None), VarDecl(Id(variable), ArrayType([58.57, 83.74], BoolType), None, None)], Return()), VarDecl(Id(c), ArrayType([1.73, 19.58, 96.61], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 345))

		input = '''
func d (bool var1[30.71,71.16,22.72], bool x)	begin
		break
	end
string x
func asm2 (string abc, string test[23.54,98.64,95.46])	return false

func z (bool function)
	return
'''
		expect = '''Program([FuncDecl(Id(d), [VarDecl(Id(var1), ArrayType([30.71, 71.16, 22.72], BoolType), None, None), VarDecl(Id(x), BoolType, None, None)], Block([Break])), VarDecl(Id(x), StringType, None, None), FuncDecl(Id(asm2), [VarDecl(Id(abc), StringType, None, None), VarDecl(Id(test), ArrayType([23.54, 98.64, 95.46], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(z), [VarDecl(Id(function), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 346))

		input = '''
dynamic b
'''
		expect = '''Program([VarDecl(Id(b), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 347))

		input = '''
string test <- "healthy"
'''
		expect = '''Program([VarDecl(Id(test), StringType, None, StringLit(healthy))])'''
		self.assertTrue(TestAST.test(input, expect, 348))

		input = '''
func abc (number b[97.69,88.5], bool x, bool test[15.83])	return

string x[26.53,23.66]
string variable[30.62]
func function ()
	begin
		bool test
	end

'''
		expect = '''Program([FuncDecl(Id(abc), [VarDecl(Id(b), ArrayType([97.69, 88.5], NumberType), None, None), VarDecl(Id(x), BoolType, None, None), VarDecl(Id(test), ArrayType([15.83], BoolType), None, None)], Return()), VarDecl(Id(x), ArrayType([26.53, 23.66], StringType), None, None), VarDecl(Id(variable), ArrayType([30.62], StringType), None, None), FuncDecl(Id(function), [], Block([VarDecl(Id(test), BoolType, None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 349))

		input = '''
func d ()	begin
		bool x[22.06,85.7,72.45]
		if (77.79)
		pizza <- 58.08
		elif (39.02)
		continue
		elif (true)
		continue
		elif (67.11)
		continue
		break
	end
func c (string y[67.89])	begin
	end

bool b[52.2,42.94,6.96] <- def
string pizza[54.38,8.56] <- true
'''
		expect = '''Program([FuncDecl(Id(d), [], Block([VarDecl(Id(x), ArrayType([22.06, 85.7, 72.45], BoolType), None, None), If((NumLit(77.79), AssignStmt(Id(pizza), NumLit(58.08))), [(NumLit(39.02), Continue), (BooleanLit(True), Continue), (NumLit(67.11), Continue)], None), Break])), FuncDecl(Id(c), [VarDecl(Id(y), ArrayType([67.89], StringType), None, None)], Block([])), VarDecl(Id(b), ArrayType([52.2, 42.94, 6.96], BoolType), None, Id(def)), VarDecl(Id(pizza), ArrayType([54.38, 8.56], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 350))

		input = '''
func z (number b, string a[70.61], number c)
	return pizza

'''
		expect = '''Program([FuncDecl(Id(z), [VarDecl(Id(b), NumberType, None, None), VarDecl(Id(a), ArrayType([70.61], StringType), None, None), VarDecl(Id(c), NumberType, None, None)], Return(Id(pizza)))])'''
		self.assertTrue(TestAST.test(input, expect, 351))

		input = '''
bool x[92.52,83.32] <- "func2"
string abc[40.81]
func z (number def[52.04,3.23], number func1)
	return variable
'''
		expect = '''Program([VarDecl(Id(x), ArrayType([92.52, 83.32], BoolType), None, StringLit(func2)), VarDecl(Id(abc), ArrayType([40.81], StringType), None, None), FuncDecl(Id(z), [VarDecl(Id(def), ArrayType([52.04, 3.23], NumberType), None, None), VarDecl(Id(func1), NumberType, None, None)], Return(Id(variable)))])'''
		self.assertTrue(TestAST.test(input, expect, 352))

		input = '''
number x[84.39,37.93,99.95] <- true
func variable ()
	return

func d (number a)	return "y"

func healthy ()	return pizza

'''
		expect = '''Program([VarDecl(Id(x), ArrayType([84.39, 37.93, 99.95], NumberType), None, BooleanLit(True)), FuncDecl(Id(variable), [], Return()), FuncDecl(Id(d), [VarDecl(Id(a), NumberType, None, None)], Return(StringLit(y))), FuncDecl(Id(healthy), [], Return(Id(pizza)))])'''
		self.assertTrue(TestAST.test(input, expect, 353))

		input = '''
func var1 (number a[2.06,71.01,15.86])	begin
		number b[26.97,87.69,12.0] <- false
		func2()
		healthy("a")
	end
func d (string asm2)	return true

'''
		expect = '''Program([FuncDecl(Id(var1), [VarDecl(Id(a), ArrayType([2.06, 71.01, 15.86], NumberType), None, None)], Block([VarDecl(Id(b), ArrayType([26.97, 87.69, 12.0], NumberType), None, BooleanLit(False)), CallStmt(Id(func2), []), CallStmt(Id(healthy), [StringLit(a)])])), FuncDecl(Id(d), [VarDecl(Id(asm2), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 354))

		input = '''
func func1 (bool asm2[58.1,77.06,68.51], bool d[91.07,35.32], bool b)	begin
		var b <- "healthy"
		return
		for var1 until "var1" by true
			break
	end

func d (string y[11.87,0.42,55.75], string x[80.85,42.66,50.76])
	return true
'''
		expect = '''Program([FuncDecl(Id(func1), [VarDecl(Id(asm2), ArrayType([58.1, 77.06, 68.51], BoolType), None, None), VarDecl(Id(d), ArrayType([91.07, 35.32], BoolType), None, None), VarDecl(Id(b), BoolType, None, None)], Block([VarDecl(Id(b), None, var, StringLit(healthy)), Return(), For(Id(var1), StringLit(var1), BooleanLit(True), Break)])), FuncDecl(Id(d), [VarDecl(Id(y), ArrayType([11.87, 0.42, 55.75], StringType), None, None), VarDecl(Id(x), ArrayType([80.85, 42.66, 50.76], StringType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 355))

		input = '''
func func2 (string function[11.63,92.24,52.13], string pizza[14.8,38.11], bool test)	begin
		return
		continue
		func1[false] <- true
	end

func a ()	return
'''
		expect = '''Program([FuncDecl(Id(func2), [VarDecl(Id(function), ArrayType([11.63, 92.24, 52.13], StringType), None, None), VarDecl(Id(pizza), ArrayType([14.8, 38.11], StringType), None, None), VarDecl(Id(test), BoolType, None, None)], Block([Return(), Continue, AssignStmt(ArrayCell(Id(func1), [BooleanLit(False)]), BooleanLit(True))])), FuncDecl(Id(a), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 356))

		input = '''
number variable <- z
string c[39.15,97.72] <- z
func x (number var1)
	return func1

'''
		expect = '''Program([VarDecl(Id(variable), NumberType, None, Id(z)), VarDecl(Id(c), ArrayType([39.15, 97.72], StringType), None, Id(z)), FuncDecl(Id(x), [VarDecl(Id(var1), NumberType, None, None)], Return(Id(func1)))])'''
		self.assertTrue(TestAST.test(input, expect, 357))

		input = '''
func a (number func1, string pizza)
	begin
		continue
		begin
			if (c)
			break
			elif (53.55) if (82.08) var2(var2)
			elif (false)
			test <- "func1"
			else string c[57.19]
			func1 <- "test"
		end
	end

bool variable <- "z"
'''
		expect = '''Program([FuncDecl(Id(a), [VarDecl(Id(func1), NumberType, None, None), VarDecl(Id(pizza), StringType, None, None)], Block([Continue, Block([If((Id(c), Break), [(NumLit(53.55), If((NumLit(82.08), CallStmt(Id(var2), [Id(var2)])), [], None)), (BooleanLit(False), AssignStmt(Id(test), StringLit(func1)))], VarDecl(Id(c), ArrayType([57.19], StringType), None, None)), AssignStmt(Id(func1), StringLit(test))])])), VarDecl(Id(variable), BoolType, None, StringLit(z))])'''
		self.assertTrue(TestAST.test(input, expect, 358))

		input = '''
func def (string foo[68.4,13.33], string pizza, bool d)
	return

bool asm2 <- test
func d (bool test[6.24,69.1])
	return
'''
		expect = '''Program([FuncDecl(Id(def), [VarDecl(Id(foo), ArrayType([68.4, 13.33], StringType), None, None), VarDecl(Id(pizza), StringType, None, None), VarDecl(Id(d), BoolType, None, None)], Return()), VarDecl(Id(asm2), BoolType, None, Id(test)), FuncDecl(Id(d), [VarDecl(Id(test), ArrayType([6.24, 69.1], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 359))

		input = '''
func c (bool asm2, bool abc)
	begin
		break
		func2(b)
	end

func z (string def[55.85])
	return

bool func1[7.65,64.99,39.4]
'''
		expect = '''Program([FuncDecl(Id(c), [VarDecl(Id(asm2), BoolType, None, None), VarDecl(Id(abc), BoolType, None, None)], Block([Break, CallStmt(Id(func2), [Id(b)])])), FuncDecl(Id(z), [VarDecl(Id(def), ArrayType([55.85], StringType), None, None)], Return()), VarDecl(Id(func1), ArrayType([7.65, 64.99, 39.4], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 360))

		input = '''
number pizza[88.1,18.41]
func var2 (string func1[45.59,28.43], string var1, string var1[55.22,66.89])
	return
func test ()
	begin
		var2()
		return false
	end

func var2 (bool z)	return

string x[23.69,30.83]
'''
		expect = '''Program([VarDecl(Id(pizza), ArrayType([88.1, 18.41], NumberType), None, None), FuncDecl(Id(var2), [VarDecl(Id(func1), ArrayType([45.59, 28.43], StringType), None, None), VarDecl(Id(var1), StringType, None, None), VarDecl(Id(var1), ArrayType([55.22, 66.89], StringType), None, None)], Return()), FuncDecl(Id(test), [], Block([CallStmt(Id(var2), []), Return(BooleanLit(False))])), FuncDecl(Id(var2), [VarDecl(Id(z), BoolType, None, None)], Return()), VarDecl(Id(x), ArrayType([23.69, 30.83], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 361))

		input = '''
number var1
func b ()
	return true

func x (number b[73.94,28.29])	return

number var1 <- abc
'''
		expect = '''Program([VarDecl(Id(var1), NumberType, None, None), FuncDecl(Id(b), [], Return(BooleanLit(True))), FuncDecl(Id(x), [VarDecl(Id(b), ArrayType([73.94, 28.29], NumberType), None, None)], Return()), VarDecl(Id(var1), NumberType, None, Id(abc))])'''
		self.assertTrue(TestAST.test(input, expect, 362))

		input = '''
number c[89.78,46.0,63.99] <- "func"
bool def[83.76]
'''
		expect = '''Program([VarDecl(Id(c), ArrayType([89.78, 46.0, 63.99], NumberType), None, StringLit(func)), VarDecl(Id(def), ArrayType([83.76], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 363))

		input = '''
func test (number y[24.62,8.3,5.72], string func1[1.52], number x)
	begin
		return
		x()
		if (14.93)
		if ("function")
		begin
			continue
			begin
			end
		end
		elif (true) def()
		elif (x) for abc until true by "y"
			d[true] <- "c"
		elif ("d")
		if (variable) a(4.71)
		elif (function)
		number x[23.09] <- 4.7
		elif ("func2")
		if (false)
		break
		elif ("d") if (77.38)
		begin
		end
		elif (43.91)
		break
		elif (true) if (c) for test until 90.08 by true
			return function
		elif (64.86) abc <- 95.12
		elif (58.92) return 90.26
		elif (false) if (19.69) continue
		elif ("variable")
		break
		else z[x, 34.44] <- 37.36
		else pizza <- "asm2"
		elif ("def")
		continue
		else variable(false, false, "a")
		elif (5.0)
		if ("healthy")
		func2 <- 40.16
		elif (var1) number healthy[87.94,18.79,11.24] <- "y"
		elif (y) asm2[73.86, 20.99, "z"] <- abc
		elif (d)
		bool function[89.97,3.38,94.48] <- "x"
		else return false
		elif (94.57) continue
		elif (14.81) return
		elif (64.14)
		x("def")
		else continue
	end

'''
		expect = '''Program([FuncDecl(Id(test), [VarDecl(Id(y), ArrayType([24.62, 8.3, 5.72], NumberType), None, None), VarDecl(Id(func1), ArrayType([1.52], StringType), None, None), VarDecl(Id(x), NumberType, None, None)], Block([Return(), CallStmt(Id(x), []), If((NumLit(14.93), If((StringLit(function), Block([Continue, Block([])])), [(BooleanLit(True), CallStmt(Id(def), [])), (Id(x), For(Id(abc), BooleanLit(True), StringLit(y), AssignStmt(ArrayCell(Id(d), [BooleanLit(True)]), StringLit(c)))), (StringLit(d), If((Id(variable), CallStmt(Id(a), [NumLit(4.71)])), [(Id(function), VarDecl(Id(x), ArrayType([23.09], NumberType), None, NumLit(4.7))), (StringLit(func2), If((BooleanLit(False), Break), [(StringLit(d), If((NumLit(77.38), Block([])), [(NumLit(43.91), Break), (BooleanLit(True), If((Id(c), For(Id(test), NumLit(90.08), BooleanLit(True), Return(Id(function)))), [(NumLit(64.86), AssignStmt(Id(abc), NumLit(95.12))), (NumLit(58.92), Return(NumLit(90.26))), (BooleanLit(False), If((NumLit(19.69), Continue), [(StringLit(variable), Break)], AssignStmt(ArrayCell(Id(z), [Id(x), NumLit(34.44)]), NumLit(37.36))))], AssignStmt(Id(pizza), StringLit(asm2)))), (StringLit(def), Continue)], CallStmt(Id(variable), [BooleanLit(False), BooleanLit(False), StringLit(a)]))), (NumLit(5.0), If((StringLit(healthy), AssignStmt(Id(func2), NumLit(40.16))), [(Id(var1), VarDecl(Id(healthy), ArrayType([87.94, 18.79, 11.24], NumberType), None, StringLit(y))), (Id(y), AssignStmt(ArrayCell(Id(asm2), [NumLit(73.86), NumLit(20.99), StringLit(z)]), Id(abc))), (Id(d), VarDecl(Id(function), ArrayType([89.97, 3.38, 94.48], BoolType), None, StringLit(x)))], Return(BooleanLit(False)))), (NumLit(94.57), Continue)], None)), (NumLit(14.81), Return())], None)), (NumLit(64.14), CallStmt(Id(x), [StringLit(def)]))], Continue)), [], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 364))

		input = '''
bool c[69.41,77.11,69.85] <- "var1"
bool asm2 <- 30.58
'''
		expect = '''Program([VarDecl(Id(c), ArrayType([69.41, 77.11, 69.85], BoolType), None, StringLit(var1)), VarDecl(Id(asm2), BoolType, None, NumLit(30.58))])'''
		self.assertTrue(TestAST.test(input, expect, 365))

		input = '''
func def ()
	return func1

func healthy (number func1)	return "function"
bool test <- healthy
dynamic def
func abc (string z[41.69], number function, number z)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(def), [], Return(Id(func1))), FuncDecl(Id(healthy), [VarDecl(Id(func1), NumberType, None, None)], Return(StringLit(function))), VarDecl(Id(test), BoolType, None, Id(healthy)), VarDecl(Id(def), None, dynamic, None), FuncDecl(Id(abc), [VarDecl(Id(z), ArrayType([41.69], StringType), None, None), VarDecl(Id(function), NumberType, None, None), VarDecl(Id(z), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 366))

		input = '''
func d (string func1[75.72,95.06,59.89], string abc[97.83])
	begin
		x <- "func"
	end
bool foo[58.29] <- 19.88
string foo[30.0,8.58,15.64] <- variable
bool healthy <- "abc"
bool var1
'''
		expect = '''Program([FuncDecl(Id(d), [VarDecl(Id(func1), ArrayType([75.72, 95.06, 59.89], StringType), None, None), VarDecl(Id(abc), ArrayType([97.83], StringType), None, None)], Block([AssignStmt(Id(x), StringLit(func))])), VarDecl(Id(foo), ArrayType([58.29], BoolType), None, NumLit(19.88)), VarDecl(Id(foo), ArrayType([30.0, 8.58, 15.64], StringType), None, Id(variable)), VarDecl(Id(healthy), BoolType, None, StringLit(abc)), VarDecl(Id(var1), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 367))

		input = '''
func c (bool healthy[68.74,99.22])
	return
func asm2 (number function[59.61,93.78], string foo, number pizza[24.85,32.85])
	begin
		return 75.98
		if (pizza) y[true] <- false
		elif (true)
		begin
			func1[92.53] <- healthy
			return true
			bool var2
		end
		else string def
		healthy <- "var1"
	end
string test
'''
		expect = '''Program([FuncDecl(Id(c), [VarDecl(Id(healthy), ArrayType([68.74, 99.22], BoolType), None, None)], Return()), FuncDecl(Id(asm2), [VarDecl(Id(function), ArrayType([59.61, 93.78], NumberType), None, None), VarDecl(Id(foo), StringType, None, None), VarDecl(Id(pizza), ArrayType([24.85, 32.85], NumberType), None, None)], Block([Return(NumLit(75.98)), If((Id(pizza), AssignStmt(ArrayCell(Id(y), [BooleanLit(True)]), BooleanLit(False))), [(BooleanLit(True), Block([AssignStmt(ArrayCell(Id(func1), [NumLit(92.53)]), Id(healthy)), Return(BooleanLit(True)), VarDecl(Id(var2), BoolType, None, None)]))], VarDecl(Id(def), StringType, None, None)), AssignStmt(Id(healthy), StringLit(var1))])), VarDecl(Id(test), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 368))

		input = '''
func func2 (string var1[58.31])
	begin
		for c until var1 by z
			begin
				for func1 until y by false
					begin
						begin
						end
						if (foo)
						continue
						elif (z) begin
							z[false, true, 16.47] <- 45.87
							func1[7.94, "c", "func2"] <- variable
						end
						elif ("b")
						c <- asm2
						elif (45.21)
						break
						elif ("pizza")
						string b[79.94,11.62] <- 26.47
						else return
						pizza(56.75)
					end
				for d until c by def
					continue
				if (asm2) bool abc <- 42.08
				elif (61.23) return
				elif (false)
				pizza()
				elif (true) if (d)
				a(def, "healthy", false)
				elif ("var2")
				return
				elif ("def") function <- 73.78
				elif (16.03)
				if (97.79) begin
				end
				else break
				elif (61.03) for b until "healthy" by true
					variable(d, 71.23, 76.94)
			end
		break
		return
	end

bool d[21.76,98.94] <- "b"
func var1 (string test, string test, bool test[96.87,12.37])	return 95.65

dynamic z <- 56.28
func func2 (bool a, number c[66.35,66.33,55.97])	return
'''
		expect = '''Program([FuncDecl(Id(func2), [VarDecl(Id(var1), ArrayType([58.31], StringType), None, None)], Block([For(Id(c), Id(var1), Id(z), Block([For(Id(func1), Id(y), BooleanLit(False), Block([Block([]), If((Id(foo), Continue), [(Id(z), Block([AssignStmt(ArrayCell(Id(z), [BooleanLit(False), BooleanLit(True), NumLit(16.47)]), NumLit(45.87)), AssignStmt(ArrayCell(Id(func1), [NumLit(7.94), StringLit(c), StringLit(func2)]), Id(variable))])), (StringLit(b), AssignStmt(Id(c), Id(asm2))), (NumLit(45.21), Break), (StringLit(pizza), VarDecl(Id(b), ArrayType([79.94, 11.62], StringType), None, NumLit(26.47)))], Return()), CallStmt(Id(pizza), [NumLit(56.75)])])), For(Id(d), Id(c), Id(def), Continue), If((Id(asm2), VarDecl(Id(abc), BoolType, None, NumLit(42.08))), [(NumLit(61.23), Return()), (BooleanLit(False), CallStmt(Id(pizza), [])), (BooleanLit(True), If((Id(d), CallStmt(Id(a), [Id(def), StringLit(healthy), BooleanLit(False)])), [(StringLit(var2), Return()), (StringLit(def), AssignStmt(Id(function), NumLit(73.78))), (NumLit(16.03), If((NumLit(97.79), Block([])), [], Break))], None)), (NumLit(61.03), For(Id(b), StringLit(healthy), BooleanLit(True), CallStmt(Id(variable), [Id(d), NumLit(71.23), NumLit(76.94)])))], None)])), Break, Return()])), VarDecl(Id(d), ArrayType([21.76, 98.94], BoolType), None, StringLit(b)), FuncDecl(Id(var1), [VarDecl(Id(test), StringType, None, None), VarDecl(Id(test), StringType, None, None), VarDecl(Id(test), ArrayType([96.87, 12.37], BoolType), None, None)], Return(NumLit(95.65))), VarDecl(Id(z), None, dynamic, NumLit(56.28)), FuncDecl(Id(func2), [VarDecl(Id(a), BoolType, None, None), VarDecl(Id(c), ArrayType([66.35, 66.33, 55.97], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 369))

		input = '''
bool pizza[16.22] <- "pizza"
func y (string func2[48.74], string var2, string def)
	return true
bool function[56.91,48.59,88.24] <- asm2
'''
		expect = '''Program([VarDecl(Id(pizza), ArrayType([16.22], BoolType), None, StringLit(pizza)), FuncDecl(Id(y), [VarDecl(Id(func2), ArrayType([48.74], StringType), None, None), VarDecl(Id(var2), StringType, None, None), VarDecl(Id(def), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(function), ArrayType([56.91, 48.59, 88.24], BoolType), None, Id(asm2))])'''
		self.assertTrue(TestAST.test(input, expect, 370))

		input = '''
string d <- 12.53
'''
		expect = '''Program([VarDecl(Id(d), StringType, None, NumLit(12.53))])'''
		self.assertTrue(TestAST.test(input, expect, 371))

		input = '''
number healthy
func asm2 ()
	return
'''
		expect = '''Program([VarDecl(Id(healthy), NumberType, None, None), FuncDecl(Id(asm2), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 372))

		input = '''
func y (string func1, string healthy, bool foo[30.78,95.58,76.28])
	return

bool z[84.32,63.88,41.65]
'''
		expect = '''Program([FuncDecl(Id(y), [VarDecl(Id(func1), StringType, None, None), VarDecl(Id(healthy), StringType, None, None), VarDecl(Id(foo), ArrayType([30.78, 95.58, 76.28], BoolType), None, None)], Return()), VarDecl(Id(z), ArrayType([84.32, 63.88, 41.65], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 373))

		input = '''
func x ()	return
func var1 ()
	begin
		y[33.44, false, "b"] <- 65.49
		func1[true, healthy, true] <- false
	end
func foo (number b[47.44,89.89,59.28])
	return

'''
		expect = '''Program([FuncDecl(Id(x), [], Return()), FuncDecl(Id(var1), [], Block([AssignStmt(ArrayCell(Id(y), [NumLit(33.44), BooleanLit(False), StringLit(b)]), NumLit(65.49)), AssignStmt(ArrayCell(Id(func1), [BooleanLit(True), Id(healthy), BooleanLit(True)]), BooleanLit(False))])), FuncDecl(Id(foo), [VarDecl(Id(b), ArrayType([47.44, 89.89, 59.28], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 374))

		input = '''
var def <- y
func d (number pizza[0.94,3.85,17.64], string variable[76.86,45.26,79.57])	return func2
func var2 (string variable, number def[62.36,68.14])
	begin
		healthy(false)
		break
		return
	end

'''
		expect = '''Program([VarDecl(Id(def), None, var, Id(y)), FuncDecl(Id(d), [VarDecl(Id(pizza), ArrayType([0.94, 3.85, 17.64], NumberType), None, None), VarDecl(Id(variable), ArrayType([76.86, 45.26, 79.57], StringType), None, None)], Return(Id(func2))), FuncDecl(Id(var2), [VarDecl(Id(variable), StringType, None, None), VarDecl(Id(def), ArrayType([62.36, 68.14], NumberType), None, None)], Block([CallStmt(Id(healthy), [BooleanLit(False)]), Break, Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 375))

		input = '''
func pizza (number d, number a)
	return 66.74
func variable (number def, string abc[76.21,60.51,55.65], bool pizza[7.59,86.31])	return
'''
		expect = '''Program([FuncDecl(Id(pizza), [VarDecl(Id(d), NumberType, None, None), VarDecl(Id(a), NumberType, None, None)], Return(NumLit(66.74))), FuncDecl(Id(variable), [VarDecl(Id(def), NumberType, None, None), VarDecl(Id(abc), ArrayType([76.21, 60.51, 55.65], StringType), None, None), VarDecl(Id(pizza), ArrayType([7.59, 86.31], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 376))

		input = '''
func function ()
	return 37.4

'''
		expect = '''Program([FuncDecl(Id(function), [], Return(NumLit(37.4)))])'''
		self.assertTrue(TestAST.test(input, expect, 377))

		input = '''
var c <- "y"
func var2 (number function, string x[21.58,63.43], bool test[28.34,67.18])
	begin
	end
string function
string healthy
'''
		expect = '''Program([VarDecl(Id(c), None, var, StringLit(y)), FuncDecl(Id(var2), [VarDecl(Id(function), NumberType, None, None), VarDecl(Id(x), ArrayType([21.58, 63.43], StringType), None, None), VarDecl(Id(test), ArrayType([28.34, 67.18], BoolType), None, None)], Block([])), VarDecl(Id(function), StringType, None, None), VarDecl(Id(healthy), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 378))

		input = '''
func func2 (string abc, bool func1[22.69,54.97], bool y[13.35,35.52,2.5])	begin
		continue
		begin
			break
		end
	end

bool asm2 <- true
dynamic function
bool def[23.5]
func asm2 (string def, bool func1[5.53], number var2)
	return "x"
'''
		expect = '''Program([FuncDecl(Id(func2), [VarDecl(Id(abc), StringType, None, None), VarDecl(Id(func1), ArrayType([22.69, 54.97], BoolType), None, None), VarDecl(Id(y), ArrayType([13.35, 35.52, 2.5], BoolType), None, None)], Block([Continue, Block([Break])])), VarDecl(Id(asm2), BoolType, None, BooleanLit(True)), VarDecl(Id(function), None, dynamic, None), VarDecl(Id(def), ArrayType([23.5], BoolType), None, None), FuncDecl(Id(asm2), [VarDecl(Id(def), StringType, None, None), VarDecl(Id(func1), ArrayType([5.53], BoolType), None, None), VarDecl(Id(var2), NumberType, None, None)], Return(StringLit(x)))])'''
		self.assertTrue(TestAST.test(input, expect, 379))

		input = '''
func pizza (string healthy, string d[99.79,74.33,10.73])
	return
string var2[58.73,56.19]
number pizza[41.88,30.0,40.17] <- true
func function (number var1, string var1[47.68,66.02])
	begin
		for func2 until false by true
			return 9.25
	end

'''
		expect = '''Program([FuncDecl(Id(pizza), [VarDecl(Id(healthy), StringType, None, None), VarDecl(Id(d), ArrayType([99.79, 74.33, 10.73], StringType), None, None)], Return()), VarDecl(Id(var2), ArrayType([58.73, 56.19], StringType), None, None), VarDecl(Id(pizza), ArrayType([41.88, 30.0, 40.17], NumberType), None, BooleanLit(True)), FuncDecl(Id(function), [VarDecl(Id(var1), NumberType, None, None), VarDecl(Id(var1), ArrayType([47.68, 66.02], StringType), None, None)], Block([For(Id(func2), BooleanLit(False), BooleanLit(True), Return(NumLit(9.25)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 380))

		input = '''
func z (string foo[83.43], string variable, bool var2)	return "a"
func healthy (string variable[87.61], bool variable[2.16])
	return

string foo[10.66] <- "foo"
'''
		expect = '''Program([FuncDecl(Id(z), [VarDecl(Id(foo), ArrayType([83.43], StringType), None, None), VarDecl(Id(variable), StringType, None, None), VarDecl(Id(var2), BoolType, None, None)], Return(StringLit(a))), FuncDecl(Id(healthy), [VarDecl(Id(variable), ArrayType([87.61], StringType), None, None), VarDecl(Id(variable), ArrayType([2.16], BoolType), None, None)], Return()), VarDecl(Id(foo), ArrayType([10.66], StringType), None, StringLit(foo))])'''
		self.assertTrue(TestAST.test(input, expect, 381))

		input = '''
func abc (number foo[72.2,85.28], bool func1[33.25,46.47,30.81])	return b
'''
		expect = '''Program([FuncDecl(Id(abc), [VarDecl(Id(foo), ArrayType([72.2, 85.28], NumberType), None, None), VarDecl(Id(func1), ArrayType([33.25, 46.47, 30.81], BoolType), None, None)], Return(Id(b)))])'''
		self.assertTrue(TestAST.test(input, expect, 382))

		input = '''
number d
string pizza[40.53,81.05]
'''
		expect = '''Program([VarDecl(Id(d), NumberType, None, None), VarDecl(Id(pizza), ArrayType([40.53, 81.05], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 383))

		input = '''
func healthy (number pizza[20.29,98.11], bool abc, number def)	return 73.49

'''
		expect = '''Program([FuncDecl(Id(healthy), [VarDecl(Id(pizza), ArrayType([20.29, 98.11], NumberType), None, None), VarDecl(Id(abc), BoolType, None, None), VarDecl(Id(def), NumberType, None, None)], Return(NumLit(73.49)))])'''
		self.assertTrue(TestAST.test(input, expect, 384))

		input = '''
func abc (number foo[26.72,36.64], bool asm2[17.29,43.54,20.2], string c[60.26,72.84])	begin
		begin
		end
		if (false)
		if (true) func2[32.91] <- x
		elif (c) break
		elif (false) break
		elif (b) if (28.07)
		break
		elif (false) break
		elif ("func2")
		string foo[68.92,8.01,75.17] <- func2
		elif (false) string healthy[37.23]
		elif (88.66)
		return
		else break
		elif ("asm2") return
		elif ("function")
		b["test", true, healthy] <- true
		elif (true) begin
			function(var1, false)
		end
		elif ("variable") for b until x by "c"
			return
		elif (94.18)
		break
		elif (86.8) break
	end

func asm2 (number pizza)	return

func var1 (number a, number c[67.14,49.1])
	begin
		if (85.41) var2[function, "y"] <- func1
		elif (8.56) begin
			continue
			for a until false by "def"
				break
		end
		else break
		continue
		if (y)
		dynamic var1 <- true
		else if (false) dynamic c
		elif (77.02)
		bool function[20.99,12.41,29.25] <- 23.95
	end

bool z[29.5] <- false
dynamic y <- "abc"
'''
		expect = '''Program([FuncDecl(Id(abc), [VarDecl(Id(foo), ArrayType([26.72, 36.64], NumberType), None, None), VarDecl(Id(asm2), ArrayType([17.29, 43.54, 20.2], BoolType), None, None), VarDecl(Id(c), ArrayType([60.26, 72.84], StringType), None, None)], Block([Block([]), If((BooleanLit(False), If((BooleanLit(True), AssignStmt(ArrayCell(Id(func2), [NumLit(32.91)]), Id(x))), [(Id(c), Break), (BooleanLit(False), Break), (Id(b), If((NumLit(28.07), Break), [(BooleanLit(False), Break), (StringLit(func2), VarDecl(Id(foo), ArrayType([68.92, 8.01, 75.17], StringType), None, Id(func2))), (BooleanLit(False), VarDecl(Id(healthy), ArrayType([37.23], StringType), None, None)), (NumLit(88.66), Return())], Break)), (StringLit(asm2), Return()), (StringLit(function), AssignStmt(ArrayCell(Id(b), [StringLit(test), BooleanLit(True), Id(healthy)]), BooleanLit(True))), (BooleanLit(True), Block([CallStmt(Id(function), [Id(var1), BooleanLit(False)])])), (StringLit(variable), For(Id(b), Id(x), StringLit(c), Return())), (NumLit(94.18), Break), (NumLit(86.8), Break)], None)), [], None)])), FuncDecl(Id(asm2), [VarDecl(Id(pizza), NumberType, None, None)], Return()), FuncDecl(Id(var1), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(c), ArrayType([67.14, 49.1], NumberType), None, None)], Block([If((NumLit(85.41), AssignStmt(ArrayCell(Id(var2), [Id(function), StringLit(y)]), Id(func1))), [(NumLit(8.56), Block([Continue, For(Id(a), BooleanLit(False), StringLit(def), Break)]))], Break), Continue, If((Id(y), VarDecl(Id(var1), None, dynamic, BooleanLit(True))), [], If((BooleanLit(False), VarDecl(Id(c), None, dynamic, None)), [(NumLit(77.02), VarDecl(Id(function), ArrayType([20.99, 12.41, 29.25], BoolType), None, NumLit(23.95)))], None))])), VarDecl(Id(z), ArrayType([29.5], BoolType), None, BooleanLit(False)), VarDecl(Id(y), None, dynamic, StringLit(abc))])'''
		self.assertTrue(TestAST.test(input, expect, 385))

		input = '''
func func2 (string b[10.96])	return

func z (number var2)	return

func abc (number variable[36.76], bool def, bool b[66.91])
	begin
		begin
		end
		begin
			def[60.25] <- true
			continue
			continue
		end
	end

number d[10.66,12.7,97.65]
bool d <- variable
'''
		expect = '''Program([FuncDecl(Id(func2), [VarDecl(Id(b), ArrayType([10.96], StringType), None, None)], Return()), FuncDecl(Id(z), [VarDecl(Id(var2), NumberType, None, None)], Return()), FuncDecl(Id(abc), [VarDecl(Id(variable), ArrayType([36.76], NumberType), None, None), VarDecl(Id(def), BoolType, None, None), VarDecl(Id(b), ArrayType([66.91], BoolType), None, None)], Block([Block([]), Block([AssignStmt(ArrayCell(Id(def), [NumLit(60.25)]), BooleanLit(True)), Continue, Continue])])), VarDecl(Id(d), ArrayType([10.66, 12.7, 97.65], NumberType), None, None), VarDecl(Id(d), BoolType, None, Id(variable))])'''
		self.assertTrue(TestAST.test(input, expect, 386))

		input = '''
func var2 (string foo[27.48,44.99], bool a[93.44])
	begin
		if (var1)
		bool func2 <- b
		elif ("b")
		return false
		elif (var1)
		break
		elif (51.19) var func2 <- healthy
		elif ("func1")
		for test until "d" by 67.71
			begin
				test("asm2", a, true)
				return
				for test until "pizza" by "var1"
					if (79.22) for d until 9.43 by "func"
						begin
							for z until "c" by "test"
								break
							return "y"
							break
						end
					elif (4.91) func1 <- false
					elif (false) d(false, 34.58, 85.98)
					elif ("function") bool pizza
					elif (true)
					begin
						begin
							pizza(b, z)
							y()
						end
						bool function
					end
					else for b until 91.87 by false
						pizza()
			end
		elif (64.11)
		bool a[43.68] <- 30.17
		else break
		break
	end
string var1[54.31,53.78] <- asm2
'''
		expect = '''Program([FuncDecl(Id(var2), [VarDecl(Id(foo), ArrayType([27.48, 44.99], StringType), None, None), VarDecl(Id(a), ArrayType([93.44], BoolType), None, None)], Block([If((Id(var1), VarDecl(Id(func2), BoolType, None, Id(b))), [(StringLit(b), Return(BooleanLit(False))), (Id(var1), Break), (NumLit(51.19), VarDecl(Id(func2), None, var, Id(healthy))), (StringLit(func1), For(Id(test), StringLit(d), NumLit(67.71), Block([CallStmt(Id(test), [StringLit(asm2), Id(a), BooleanLit(True)]), Return(), For(Id(test), StringLit(pizza), StringLit(var1), If((NumLit(79.22), For(Id(d), NumLit(9.43), StringLit(func), Block([For(Id(z), StringLit(c), StringLit(test), Break), Return(StringLit(y)), Break]))), [(NumLit(4.91), AssignStmt(Id(func1), BooleanLit(False))), (BooleanLit(False), CallStmt(Id(d), [BooleanLit(False), NumLit(34.58), NumLit(85.98)])), (StringLit(function), VarDecl(Id(pizza), BoolType, None, None)), (BooleanLit(True), Block([Block([CallStmt(Id(pizza), [Id(b), Id(z)]), CallStmt(Id(y), [])]), VarDecl(Id(function), BoolType, None, None)]))], For(Id(b), NumLit(91.87), BooleanLit(False), CallStmt(Id(pizza), []))))]))), (NumLit(64.11), VarDecl(Id(a), ArrayType([43.68], BoolType), None, NumLit(30.17)))], Break), Break])), VarDecl(Id(var1), ArrayType([54.31, 53.78], StringType), None, Id(asm2))])'''
		self.assertTrue(TestAST.test(input, expect, 387))

		input = '''
func z (number asm2, string asm2, number abc[60.23])	return

func asm2 (string c[39.76], bool foo[85.76,69.82,93.26])
	return 36.75

dynamic pizza
func z (number variable[24.19,35.55,26.59], number abc[96.48], number func2)	return

func def ()
	begin
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(z), [VarDecl(Id(asm2), NumberType, None, None), VarDecl(Id(asm2), StringType, None, None), VarDecl(Id(abc), ArrayType([60.23], NumberType), None, None)], Return()), FuncDecl(Id(asm2), [VarDecl(Id(c), ArrayType([39.76], StringType), None, None), VarDecl(Id(foo), ArrayType([85.76, 69.82, 93.26], BoolType), None, None)], Return(NumLit(36.75))), VarDecl(Id(pizza), None, dynamic, None), FuncDecl(Id(z), [VarDecl(Id(variable), ArrayType([24.19, 35.55, 26.59], NumberType), None, None), VarDecl(Id(abc), ArrayType([96.48], NumberType), None, None), VarDecl(Id(func2), NumberType, None, None)], Return()), FuncDecl(Id(def), [], Block([Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 388))

		input = '''
number a[44.72] <- 34.04
func var2 ()	return
func c (number asm2[88.58,14.88])	return
'''
		expect = '''Program([VarDecl(Id(a), ArrayType([44.72], NumberType), None, NumLit(34.04)), FuncDecl(Id(var2), [], Return()), FuncDecl(Id(c), [VarDecl(Id(asm2), ArrayType([88.58, 14.88], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 389))

		input = '''
func var1 (number variable, string y)	return
dynamic z <- false
string x
'''
		expect = '''Program([FuncDecl(Id(var1), [VarDecl(Id(variable), NumberType, None, None), VarDecl(Id(y), StringType, None, None)], Return()), VarDecl(Id(z), None, dynamic, BooleanLit(False)), VarDecl(Id(x), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 390))

		input = '''
string asm2
'''
		expect = '''Program([VarDecl(Id(asm2), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 391))

		input = '''
func x ()
	begin
		break
	end
'''
		expect = '''Program([FuncDecl(Id(x), [], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 392))

		input = '''
bool foo <- 52.41
func var1 (bool test[13.36,63.06,40.57], string pizza[7.45,74.45])	return

number a[27.88,76.5,56.36]
string func2[15.15,89.41]
'''
		expect = '''Program([VarDecl(Id(foo), BoolType, None, NumLit(52.41)), FuncDecl(Id(var1), [VarDecl(Id(test), ArrayType([13.36, 63.06, 40.57], BoolType), None, None), VarDecl(Id(pizza), ArrayType([7.45, 74.45], StringType), None, None)], Return()), VarDecl(Id(a), ArrayType([27.88, 76.5, 56.36], NumberType), None, None), VarDecl(Id(func2), ArrayType([15.15, 89.41], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 393))

		input = '''
number foo <- "a"
string pizza[60.52] <- "x"
number asm2[35.63,17.55]
'''
		expect = '''Program([VarDecl(Id(foo), NumberType, None, StringLit(a)), VarDecl(Id(pizza), ArrayType([60.52], StringType), None, StringLit(x)), VarDecl(Id(asm2), ArrayType([35.63, 17.55], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 394))

		input = '''
bool x[63.84]
func function (string pizza, number foo)
	return 44.39
bool x <- function
func var1 ()	return
'''
		expect = '''Program([VarDecl(Id(x), ArrayType([63.84], BoolType), None, None), FuncDecl(Id(function), [VarDecl(Id(pizza), StringType, None, None), VarDecl(Id(foo), NumberType, None, None)], Return(NumLit(44.39))), VarDecl(Id(x), BoolType, None, Id(function)), FuncDecl(Id(var1), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 395))

		input = '''
func foo ()
	return true
number function[89.5,39.18]
number y
string foo[39.25,2.06]
'''
		expect = '''Program([FuncDecl(Id(foo), [], Return(BooleanLit(True))), VarDecl(Id(function), ArrayType([89.5, 39.18], NumberType), None, None), VarDecl(Id(y), NumberType, None, None), VarDecl(Id(foo), ArrayType([39.25, 2.06], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 396))

		input = '''
func b (string c[51.6,75.86], number var1, string func2[96.18,93.99,87.31])	begin
	end
number abc[23.77] <- false
func func1 (string b[8.76,75.45,8.87], number var1)	return true

func b (string pizza, number var2[40.54,99.34])	return
'''
		expect = '''Program([FuncDecl(Id(b), [VarDecl(Id(c), ArrayType([51.6, 75.86], StringType), None, None), VarDecl(Id(var1), NumberType, None, None), VarDecl(Id(func2), ArrayType([96.18, 93.99, 87.31], StringType), None, None)], Block([])), VarDecl(Id(abc), ArrayType([23.77], NumberType), None, BooleanLit(False)), FuncDecl(Id(func1), [VarDecl(Id(b), ArrayType([8.76, 75.45, 8.87], StringType), None, None), VarDecl(Id(var1), NumberType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(b), [VarDecl(Id(pizza), StringType, None, None), VarDecl(Id(var2), ArrayType([40.54, 99.34], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 397))

		input = '''
func foo (number b[52.22,82.8,97.96], number healthy)	begin
		func2 <- true
		return
	end

func function (number y[30.44,22.78], bool test)
	return abc
func a (number pizza[81.97,72.5,31.63])
	return false

func var2 ()
	return
'''
		expect = '''Program([FuncDecl(Id(foo), [VarDecl(Id(b), ArrayType([52.22, 82.8, 97.96], NumberType), None, None), VarDecl(Id(healthy), NumberType, None, None)], Block([AssignStmt(Id(func2), BooleanLit(True)), Return()])), FuncDecl(Id(function), [VarDecl(Id(y), ArrayType([30.44, 22.78], NumberType), None, None), VarDecl(Id(test), BoolType, None, None)], Return(Id(abc))), FuncDecl(Id(a), [VarDecl(Id(pizza), ArrayType([81.97, 72.5, 31.63], NumberType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(var2), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 398))

		input = '''
func y ()	begin
		begin
		end
		healthy <- "a"
	end

func variable (bool healthy, bool d)
	return
'''
		expect = '''Program([FuncDecl(Id(y), [], Block([Block([]), AssignStmt(Id(healthy), StringLit(a))])), FuncDecl(Id(variable), [VarDecl(Id(healthy), BoolType, None, None), VarDecl(Id(d), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 399))

