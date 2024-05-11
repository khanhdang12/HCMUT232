from Emitter import *
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *
from functools import reduce

class CodeGenerator:
    def gen(self, ast, path):
        codegen = CodeGenVisitor(ast, path)
        codegen.visit(ast, None)

class Access():
    def __init__(self, frame, symbol, isLeft, checkTypeLHS_RHS = False):
        self.frame = frame 
        self.checkTypeLHS_RHS = checkTypeLHS_RHS  
        self.isLeft = isLeft
        self.symbol = symbol   

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, path):
        self.astTree = astTree
        self.arrayCell = ""
        self.Return = False
        self.Listfunction = []
        self.function = None
        self.path = path
        self.className = "ZCodeClass"
        self.emit = Emitter(self.path + "/" + self.className  + ".j")
     
    def LHS_RHS(self, LHS, RHS, o):
        frame = o.frame
        symbol = o.symbol
        _, rhsTyp = self.visit(RHS, Access(frame, symbol, False, True))
        _, lhsTyp = self.visit(LHS, Access(frame, symbol, True, True))
        if isinstance(rhsTyp, Zcode):
           rhsTyp.typ = lhsTyp
           self.emit.setType(rhsTyp) 

        elif isinstance(lhsTyp, Zcode):
            lhsTyp.typ = rhsTyp
            self.emit.setType(lhsTyp) 
    
    def visitProgram(self, ast:Program, o):
        className = self.className
        self.emit.printout(self.emit.emitPROLOG(className, "java.lang.Object"))

        function = None
        Symbol = [[]]
        Main = None

        for decl in ast.decl:
            if type(decl) is VarDecl:
                index = -1
                Symbol[0].append(VarZcode(decl.name.name, decl.varType, -1, True if decl.varInit else False))
                self.emit.printout(self.emit.emitATTRIBUTE(decl.name.name, decl.varType if decl.varType else Symbol[0][-1], False, className))
                Symbol[0][-1].line = self.emit.printIndexNew()

            elif type(decl) is FuncDecl and decl.body is not None:
                self.Listfunction += [FuncZcode(decl.name.name, None, [i.varType for i in decl.param])]
                if decl.name.name == "main":
                    function = self.Listfunction[-1]
                    Main = decl
        
        myFrame = Frame("<init>", VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme="<init>", in_=FuncZcode("init", VoidType(), []), isStatic=False, frame=myFrame))
        myFrame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(myFrame.getStartLabel(), myFrame))
        self.emit.printout(self.emit.emitVAR(myFrame.getNewIndex(), "this", Zcode(), myFrame.getStartLabel(), myFrame.getEndLabel(), myFrame))
        self.emit.printout(self.emit.emitREADVAR("this", self.className, 0, myFrame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(myFrame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), myFrame))   
        self.emit.printout(self.emit.emitLABEL(myFrame.getEndLabel(), myFrame))
        self.emit.printout(self.emit.emitENDMETHOD(myFrame))
        myFrame.exitScope()

        myFrame = Frame("<clinit>", VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme="<clinit>", in_=FuncZcode("clinit", VoidType(), []), isStatic=True, frame=myFrame))
        myFrame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(myFrame.getStartLabel(), myFrame))
        
        for var in ast.decl:
            if type(var) is VarDecl and var.varInit is not None:
                self.visit(Assign(var.name, var.varInit), Access(myFrame, Symbol, False)) 
            elif type(var) is VarDecl and type(var.varType) is ArrayType:
                if len(var.varType.size) == 1:
                    self.emit.printout(self.visit(NumberLiteral(var.varType.size[0]), Access(myFrame, Symbol, False))[0])
                    self.emit.printout(self.emit.emitF2I(myFrame))
                    self.emit.printout(self.emit.emitNEWARRAY(var.varType.eleType, myFrame))
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + var.name.name, var.varType, myFrame))
                else:
                    for i in var.varType.size:
                        self.emit.printout(self.visit(NumberLiteral(i), Access(myFrame, Symbol, False))[0])
                        self.emit.printout(self.emit.emitF2I(myFrame))
                    self.emit.printout(self.emit.emitMULTIANEWARRAY(var.varType, myFrame))
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + var.name.name, var.varType, myFrame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), myFrame)) 
        self.emit.printout(self.emit.emitLABEL(myFrame.getEndLabel(), myFrame))  
        self.emit.printout(self.emit.emitENDMETHOD(myFrame))
        myFrame.exitScope()    
    
        i = 0
        for decl in ast.decl:
            if type(decl) is FuncDecl and decl.body is not None and decl.name.name != "main":
                self.function = self.Listfunction[i]
                self.visit(decl, Symbol)
            if type(decl) is FuncDecl and decl.body is not None:
                i += 1
                
        myFrame = Frame("main", VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme="main", in_=FuncZcode("main", VoidType(), [ArrayType([1], StringType())]), isStatic=True, frame=myFrame))
        myFrame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(myFrame.getStartLabel(), myFrame))
        self.emit.printout(self.emit.emitVAR(myFrame.getNewIndex(), "args", ArrayType([], StringType()), myFrame.getStartLabel(), myFrame.getEndLabel(), myFrame))
        index = myFrame.getNewIndex()
        typeParam = [VarZcode("for", NumberType(), index, True)]
        self.emit.printout(self.emit.emitVAR(index, "for", NumberType(), myFrame.getStartLabel(), myFrame.getEndLabel(), myFrame))
        self.function = function
        self.visit(Main.body, Access(myFrame, [typeParam] + Symbol, False))
        self.emit.printout(self.emit.emitRETURN(VoidType(), myFrame))
        self.emit.printout(self.emit.emitLABEL(myFrame.getEndLabel(), myFrame))   
        self.emit.printout(self.emit.emitENDMETHOD(myFrame))
        myFrame.exitScope()    
        self.emit.emitEPILOG()
    
    def visitVarDecl(self, ast, o):
        idx = o.frame.getNewIndex()
        code = self.emit.emitVAR(idx, ast.name.name, ast.varType if ast.varType else VarZcode(ast.name.name, None, idx), o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
        self.emit.printout(code)
        
        o.symbol[0].append(VarZcode(ast.name.name, ast.varType, idx, True if ast.varInit else False))
        o.symbol[0][-1].line = self.emit.printIndexNew()
        
        if ast.varInit is not None:
            self.visit(Assign(ast.name, ast.varInit), o)
        elif type(ast.varType) is ArrayType:
            if len(ast.varType.size) == 1:
                self.emit.printout(self.visit(NumberLiteral(ast.varType.size[0]), Access(o.frame, o.symbol, False))[0])
                self.emit.printout(self.emit.emitF2I(o.frame))
                self.emit.printout(self.emit.emitNEWARRAY(ast.varType.eleType, o.frame))
                self.emit.printout(self.emit.emitWRITEVAR(ast.name.name, ast.varType, idx, o.frame))
            else:
                for i in ast.varType.size:
                    self.emit.printout(self.visit(NumberLiteral(i), Access(o.frame, o.symbol, False))[0])
                    self.emit.printout(self.emit.emitF2I(o.frame))
                self.emit.printout(self.emit.emitMULTIANEWARRAY(ast.varType, o.frame))
                self.emit.printout(self.emit.emitWRITEVAR(ast.name.name, ast.varType, idx, o.frame))
                              
    def visitFuncDecl(self, ast, Symbol):
        self.Return = False
        frame = Frame(ast.name.name, None)
        
        self.emit.printout(self.emit.emitMETHOD(lexeme=ast.name.name, in_=self.function, isStatic=True, frame=frame))
        self.function.line = self.emit.printIndexNew()
        
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        typeParam = []
        for index, param in enumerate(ast.param):
            idx = frame.getNewIndex()
            code = self.emit.emitVAR(idx, param.name.name, param.varType, frame.getStartLabel(), frame.getEndLabel(), frame)
            self.emit.printout(code)
            typeParam += [VarZcode(param.name.name, param.varType, index, True if param.varInit else False)]
                
        index = frame.getNewIndex()
        typeParam += [VarZcode("for", NumberType(), index, True)]        
        self.emit.printout(self.emit.emitVAR(index, "for", NumberType(), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.visit(ast.body, Access(frame, [typeParam] + Symbol, False))
        
        if not self.Return:
            self.function.typ = VoidType()
            self.emit.printout(self.emit.emitRETURN(self.function.typ, frame))
        self.emit.buff[self.function.line] = self.emit.emitMETHOD(lexeme=ast.name.name, in_=self.function, isStatic=True, frame=frame)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))   
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        
        frame.exitScope()    

    def visitId(self, ast, o):
        Symbol = o.symbol
        
        if o.checkTypeLHS_RHS:
            for item in Symbol:
                for sym in item:
                    if sym.name == ast.name:
                        return None, sym.typ if sym.typ else sym
        isStatic = False
        sym = None
        for i in range(len(Symbol)):
            flag = list(filter(lambda x: x.name == ast.name, Symbol[i]))
            if flag:
                sym = flag[0]
                if i == len(Symbol) - 1:
                    isStatic = True
                break
                       
        if o.isLeft:
            if isStatic:
                code = self.emit.emitPUTSTATIC(self.className + '.' + sym.name, sym.typ, o.frame)
            else:
                code = self.emit.emitWRITEVAR(sym.name, sym.typ, sym.index, o.frame)
        else:
            if isStatic:                 
                code = self.emit.emitGETSTATIC(self.className + '.' + sym.name, sym.typ, o.frame)
            else:  
                code = self.emit.emitREADVAR(sym.name, sym.typ, sym.index, o.frame)
        
        return code, sym.typ
                                      

    def visitCallExpr(self, ast, o):
        lst = ["readNumber", "readBool", "readString"]
        if ast.name.name in lst:
            if ast.name.name == "readBool": 
                if o.checkTypeLHS_RHS: return None, BoolType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, BoolType(), []), o.frame), BoolType()
            
            elif ast.name.name == "readString": 
                if o.checkTypeLHS_RHS: return None, StringType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, StringType(), []), o.frame), StringType()
            
            elif ast.name.name == "readNumber": 
                if o.checkTypeLHS_RHS: return None, NumberType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, NumberType(), []), o.frame), NumberType()
            
        function = None
        for itemFunction in self.Listfunction:
            if itemFunction.name == ast.name.name:
                function = itemFunction
                
        if o.checkTypeLHS_RHS:
            for i in range(len(function.param)):
                self.LHS_RHS(function.param[i], ast.args[i], o)
            if function.typ:
                return None, function.typ            
            return function 
        
        code = ""
        typArg = []
        for exp in ast.args:
            expCode, expType = self.visit(exp, o)
            code += expCode
            typArg.append(expType)
            
        code += self.emit.emitINVOKESTATIC(self.className + '.' + ast.name.name, FuncZcode(ast.name.name, function.typ, typArg), o.frame)
        return code, function.typ

    def visitBinaryOp(self, ast, o):
        operator = ast.op
        if o.checkTypeLHS_RHS:
            if operator in ['+', '-', '*', '/', '%']:
                self.LHS_RHS(ast.right, NumberType(), o)
                self.LHS_RHS(ast.left, NumberType(), o)
                return None, NumberType()
            elif operator in ['...']:
                self.LHS_RHS(ast.right, StringType(), o)
                self.LHS_RHS(ast.left, StringType(), o)
                return None, StringType()
            elif operator in ['==']:
                self.LHS_RHS(ast.right, StringType(), o)
                self.LHS_RHS(ast.left, StringType(), o)
                return None, BoolType()
            elif operator in ['and', 'or']:
                self.LHS_RHS(ast.right, BoolType(), o)
                self.LHS_RHS(ast.left, BoolType(), o)
                return None, BoolType()
            elif operator in ['=', '!=', '<', '>', '>=', '<=']:
                self.LHS_RHS(ast.right, NumberType(), o)
                self.LHS_RHS(ast.left, NumberType(), o)
                return None, BoolType()

        codeL, _ = self.visit(ast.left, o)
        codeR, _ = self.visit(ast.right, o)

        if operator in ['+', '-']:
            code = self.emit.emitADDOP(ast.op, NumberType(), o.frame)
            rt = NumberType()
        elif operator in ['and']:
            code = self.emit.emitANDOP(o.frame)
            rt = BoolType()
        elif operator in ['==']:
            code = self.emit.emitINVOKEVIRTUAL("java/lang/String/equals", FuncZcode("equals", BoolType(), [None]), o.frame)
            rt = BoolType()
        elif operator in ['*', '/']:
            code = self.emit.emitMULOP(ast.op, NumberType(), o.frame)
            rt = NumberType()
        elif operator in ['%']:
            o.frame.push()
            o.frame.push()
            code = codeL + codeR + self.emit.emitMULOP('/', NumberType(), o.frame) + self.emit.emitF2I(o.frame) + self.emit.emitI2F(o.frame) + self.emit.emitMULOP('*', NumberType(), o.frame) + self.emit.emitADDOP('-', NumberType(), o.frame)
            rt = NumberType()
        elif operator in ['or']:
            code = self.emit.emitOROP(o.frame)
            rt = BoolType()
        elif operator in ['...']:
            code = self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", FuncZcode("concat", StringType(), [StringType()]), o.frame)
            rt = StringType() 
        elif operator in ['=', '!=', '<', '>', '>=', '<=']:
            code = self.emit.emitREOP(ast.op, NumberType(), o.frame)
            rt = BoolType()

        return codeL + codeR + code, rt

    def visitUnaryOp(self, ast, o):
        operator = ast.op
        if o.checkTypeLHS_RHS:
            if operator in ['not']:
                self.LHS_RHS(ast.operand, BoolType(), o)
                return None, BoolType()
            elif operator in ['-']:
                self.LHS_RHS(ast.operand, NumberType(), o)
                return None, NumberType()
       
        codeOp, _ = self.visit(ast.operand, o)
        
        if operator in ['-']:
            code = self.emit.emitNEGOP(NumberType(), o.frame)
            rt = NumberType()
        elif operator in ['not']:
            code = self.emit.emitNOT(BoolType(), o.frame)
            rt = BoolType()
        
        return codeOp + code, rt            
    
    def visitArrayLiteral(self, ast, o):
        myFrame = o.frame
        if o.checkTypeLHS_RHS:
            typ = None
            for value in ast.value:
                _, checkTyp = self.visit(value, o)
                if typ is None and isinstance(checkTyp, (BoolType, StringType, NumberType, ArrayType)):
                    typ = checkTyp
                    break
        
            for value in ast.value:
                self.LHS_RHS(typ, value, o)
            
            if isinstance(typ, (BoolType, StringType, NumberType)):
                return None, ArrayType([len(ast.value)], typ)
            return None, ArrayType([float(len(ast.value))] + typ.size, typ.eleType)

        _, typ = self.visit(ast.value[0], o)
        code = self.emit.emitPUSHCONST(len(ast.value), NumberType(), myFrame)
        code += self.emit.emitF2I(myFrame)
        if type(typ) in [NumberType, StringType, BoolType]: 
            code += self.emit.emitNEWARRAY(typ, myFrame)
        else:
            code += self.emit.emitANEWARRAY(typ, myFrame)
        
        for index, val in enumerate(ast.value):
            code += self.emit.emitDUP(myFrame)
            code += self.emit.emitPUSHCONST(index, NumberType(), myFrame)
            code += self.emit.emitF2I(myFrame)
            code += self.visit(val, Access(myFrame, o.symbol, False))[0]
            code += self.emit.emitASTORE(typ, myFrame)

        if type(typ) in [NumberType, StringType, BoolType]:
            return code, ArrayType([len(ast.value)], typ)
        return code, ArrayType([len(ast.value)] + typ.size, typ.eleType)
       
    def visitArrayCell(self, ast, o):
        myFrame = o.frame
        mySymbol = o.symbol
        if o.checkTypeLHS_RHS:
            _, array = self.visit(ast.arr, Access(myFrame, mySymbol, False, False))
            for idx in ast.idx:
                self.LHS_RHS(NumberType(), idx, o)
            if len(array.size) == len(ast.idx): return None, array.eleType
            return None, ArrayType(array.size[len(ast.idx):], array.eleType)   
    
        code, arrT = self.visit(ast.arr, Access(myFrame, mySymbol, False, False))
        
        if len(arrT.size) == len(ast.idx):            
            for idx, item in enumerate(ast.idx):
                itemC, itemT = self.visit(item, Access(myFrame, mySymbol, False))
                code += itemC
                code += self.emit.emitF2I(myFrame)
                if o.isLeft:
                    if (idx < len(ast.idx) - 1):
                        code += self.emit.emitALOAD(ArrayType(arrT.size[len(ast.idx):], arrT.eleType), myFrame)
                    self.arrayCell = arrT.eleType
                elif idx == len(ast.idx) - 1: 
                    code += self.emit.emitALOAD(arrT.eleType, myFrame)
                else:
                    code += self.emit.emitALOAD(ArrayType(arrT.size[len(ast.idx):], arrT.eleType), myFrame)
            rt = arrT.eleType
        else:
            for idx, item in enumerate(ast.idx):
                itemC, itemT = self.visit(item, Access(myFrame, mySymbol, False))
                code += itemC
                code += self.emit.emitF2I(myFrame)
                if o.isLeft:
                    self.arrayCell = ArrayType(arrT.size[len(ast.idx):], arrT.eleType)
                else: 
                    code += self.emit.emitALOAD(ArrayType(arrT.size[len(ast.idx):], arrT.eleType), myFrame)
            
            rt = ArrayType(arrT.size[len(ast.idx):], arrT.eleType)
        
        return code, rt
        
    def visitNumberLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, NumberType(), o.frame) if not o.checkTypeLHS_RHS else None, NumberType()
    
    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, BoolType(), o.frame) if not o.checkTypeLHS_RHS else None, BoolType()
    
    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o.frame) if not o.checkTypeLHS_RHS else None, StringType()
    
    def visitArrayType(self, ast, param): return None, ast

    def visitNumberType(self, ast, param): return None, NumberType()

    def visitVoidType(self, ast, param): return None, VoidType()

    def visitBoolType(self, ast, param): return None, BoolType()

    def visitStringType(self, ast, param): return None, StringType()

    def visitFuncZcode(self, ast, param): return None, ast.typ if ast.typ else ast

    def visitVarZcode(self, ast, param): return None, ast.typ if ast.typ else ast
    
    def visitReturn(self, ast, o):
        self.LHS_RHS(self.function, ast.expr if ast.expr else VoidType(),o)
        
        self.Return = True 
        
        if ast.expr is None:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame))
        else:
            ec, et = self.visit(ast.expr, o)
            self.emit.printout(ec)
            self.emit.printout(self.emit.emitRETURN(et, o.frame))

    def visitAssign(self, ast, o):
        self.LHS_RHS(ast.lhs, ast.rhs, o)
        frame = o.frame
        rc, _ = self.visit(ast.rhs, Access(frame, o.symbol, False))
        lc, _ = self.visit(ast.lhs, Access(frame, o.symbol, True))
        
        if type(ast.lhs) is ArrayCell:
            self.emit.printout(lc)
            self.emit.printout(rc)
            self.emit.printout(self.emit.emitASTORE(self.arrayCell, frame))  
        else:
            self.emit.printout(rc)
            self.emit.printout(lc)        
  
    
    def visitCallStmt(self, ast, o):
        name = ast.name.name
        lst = ["writeNumber", "writeBool", "writeString"]
        if name in lst:
            if name == "writeBool": self.LHS_RHS(ast.args[0], BoolType(),  o)
            elif name == "writeString": self.LHS_RHS(ast.args[0], StringType(), o)
            elif name == "writeNumber": self.LHS_RHS(ast.args[0], NumberType(), o)
                   
            code, typ = self.visit(ast.args[0], o)
            self.emit.printout(code)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"io/{name}", FuncZcode(name, VoidType(), [typ]), o.frame))
            return

        function = None
        for item in self.Listfunction:
            if item.name == name:
                function = item
        
        code = ""
        typArgs = []
        for exp in ast.args:
            expCode, expType = self.visit(exp, o)
            code += expCode
            typArgs.append(expType)
            
        code += self.emit.emitINVOKESTATIC(self.className + '.' + name, FuncZcode(name, function.typ, typArgs), o.frame)
        self.emit.printout(code)
  
          
    def visitBlock(self, ast, o):
        newEnv = [[]] + o.symbol 
        o.frame.enterScope(False) 
        sttLabel = o.frame.getStartLabel()
        self.emit.printout(self.emit.emitLABEL(sttLabel, o.frame)) 
        for item in ast.stmt: 
            self.visit(item,Access(o.frame, newEnv, False))   
        endLabel = o.frame.getEndLabel()
        self.emit.printout(self.emit.emitLABEL(endLabel, o.frame))
        o.frame.exitScope()  
       
    def visitIf(self, ast, o):     
        self.LHS_RHS(BoolType(), ast.expr, o)        
        for elifStmt in ast.elifStmt:
            self.LHS_RHS(BoolType(), elifStmt[0], o)   
        
        exitLabel = o.frame.getNewLabel()
        
        endIfLabel = o.frame.getNewLabel()
        ec, et = self.visit(ast.expr, Access(o.frame, o.symbol, False))
        self.emit.printout(ec)
        code = self.emit.emitIFFALSE(endIfLabel, o.frame)
        self.emit.printout(code)
        self.visit(ast.thenStmt, o)
        self.emit.printout(self.emit.emitGOTO(exitLabel, o.frame))
        self.emit.printout(self.emit.emitLABEL(endIfLabel, o.frame))
        
        for elifStmt in ast.elifStmt:
            loopLabel = o.frame.getNewLabel()
            
            itemEc, _ = self.visit(elifStmt[0], o)
            self.emit.printout(itemEc)
            self.emit.printout(self.emit.emitIFFALSE(loopLabel, o.frame))
            
            self.visit(elifStmt[1], o)
            self.emit.printout(self.emit.emitGOTO(exitLabel, o.frame))
            
            self.emit.printout(self.emit.emitLABEL(loopLabel, o.frame))
        
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, o)

        self.emit.printout(self.emit.emitLABEL(exitLabel, o.frame))  
        
    def visitFor(self, ast, o):
        self.LHS_RHS(NumberType(), ast.updExpr, o) 
        self.LHS_RHS(BoolType(), ast.condExpr, o) 
        self.LHS_RHS(NumberType(), ast.name, o)  
        
        self.visit(ast.name, o)
    
        self.visit(Assign(Id("for"), ast.name), o)
        o.frame.enterLoop()
        cLabel = o.frame.getContinueLabel()
        bLabel = o.frame.getBreakLabel()
        
        newLabel = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(newLabel, o.frame))
        
        ec, et = self.visit(ast.condExpr, Access(o.frame, o.symbol, False))
        self.emit.printout(ec)
        self.emit.printout(self.emit.emitIFTRUE(bLabel, o.frame))
        
        self.visit(ast.body, o)
        
        self.emit.printout(self.emit.emitLABEL(cLabel, o.frame))
        
        self.visit(Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr)), o)
        self.emit.printout(self.emit.emitGOTO(newLabel, o.frame))

        self.emit.printout(self.emit.emitLABEL(bLabel, o.frame))
        o.frame.exitLoop()
        self.visit(Assign(ast.name, Id("for")), o)

    def visitContinue(self, ast, o):
        cntLabel = o.frame.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(cntLabel, o.frame))

    def visitBreak(self, ast, o):
        brkLabel = o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(brkLabel, o.frame))
        
