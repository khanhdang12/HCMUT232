from Emitter import *
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *
from functools import reduce


class CodeGenerator:
    def gen(self, ast, path):
        # ast: AST
        # dir_: String
        gc = CodeGenVisitor(ast, path)
        gc.visit(ast, None)

class Access():
    def __init__(self, frame, symbol, isLeft, checkTypeLHS_RHS = False):
        self.frame = frame #* không gian stack và local cần dùng để chạy 1 hàm
        self.symbol = symbol #* giống phần param ở BTL3 nhưng này hiện thực list<list>> (có thể dùng list<dict> như btl3)
        self.isLeft = isLeft #* hiện tại vế trên trái hay bên phải để xác định get và put cho biến
        self.checkTypeLHS_RHS = checkTypeLHS_RHS  #* kiểm tra kiểu đúng không

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, path):
        self.astTree = astTree
        self.path = path
        self.className = "ZCodeClass"
        self.emit = Emitter(self.path + "/" + self.className  + ".j")
        self.Listfunction = []
        self.function = None
        self.Return = False
        self.arrayCell = "" 
    
    def printListfunction(self):
        print(f"self.function: {str(self.function)}" )
        print(f"self.Return  : {str(self.Return)}" )
        print(f"listFunction :")
        for item in self.Listfunction:
            print(f"         : {str(item)}" )
    


    
    #* CẬP NHẬT TYPE
    def LHS_RHS(self, LHS, RHS, o):
        #* TRUYỀN checkTypeLHS_RHS = Flase -> nghĩa là chúng ta xét type trước, trước khi lấy stack
        _, rhsType = self.visit(RHS, Access(o.frame, o.symbol, False, True))
        _, lhsType = self.visit(LHS, Access(o.frame, o.symbol, True, True))
        if isinstance(lhsType, Zcode):
            lhsType.typ = rhsType
            self.emit.setType(lhsType) #* cập nhật lại type vì trước đó type là None
            # print(self.emit.buff[lhsType.line])
            
            
        elif isinstance(rhsType, Zcode):
           rhsType.typ = lhsType
           self.emit.setType(rhsType) #* cập nhật lại type vì trước đó type là None
    
    def visitProgram(self, ast:Program, o):
        #* khởi tạo chương trình ZCodeClass
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
    
        #* cập nhật biến toàn cục và function, và khởi tạo self.emit.emitATTRIBUTE cho biến toàn cục
        Symbol = [[]]
        Main = None
        function = None
        for item in ast.decl:
            if type(item) is VarDecl:
                index = -1
                Symbol[0].append(VarZcode(item.name.name, item.varType, -1, True if item.varInit else False))
                self.emit.printout(self.emit.emitATTRIBUTE(item.name.name, item.varType if item.varType else Symbol[0][-1], False, self.className))
                Symbol[0][-1].line = self.emit.printIndexNew()
            elif type(item) is FuncDecl and item.body is not None:
                self.Listfunction += [FuncZcode(item.name.name, None, [i.varType for i in item.param])]
                if item.name.name == "main":
                    function = self.Listfunction[-1]
                    Main = item
        
    
        #* hàm khởi tạo trong Zcode (contructor bắt buộc)
        frame = Frame("<init>", VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme="<init>", in_=FuncZcode("init", VoidType(), []), isStatic=False, frame=frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", Zcode(), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", self.className, 0, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))   
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()


        #* hàm khởi tạo biến static Zcode (contructor cho static)
        frame = Frame("<clinit>", VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme="<clinit>", in_=FuncZcode("clinit", VoidType(), []), isStatic=True, frame=frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        #* có 2 TH là khởi tạo và khởi tạo array
        for var in ast.decl:
            if type(var) is VarDecl and var.varInit is not None:
                self.visit(Assign(var.name, var.varInit), Access(frame, Symbol, False)) 
            elif type(var) is VarDecl and type(var.varType) is ArrayType:
                if len(var.varType.size) == 1:
                    self.emit.printout(self.visit(NumberLiteral(var.varType.size[0]), Access(frame, Symbol, False))[0])
                    self.emit.printout(self.emit.emitF2I(frame))
                    self.emit.printout(self.emit.emitNEWARRAY(var.varType.eleType, frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + var.name.name, var.varType, frame))
                else:
                    for i in var.varType.size:
                        self.emit.printout(self.visit(NumberLiteral(i), Access(frame, Symbol, False))[0])
                        self.emit.printout(self.emit.emitF2I(frame))
                    self.emit.printout(self.emit.emitMULTIANEWARRAY(var.varType, frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + var.name.name, var.varType, frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()    
    
    
        
        #* khởi tạo các hàm static
        i = 0
        for item in ast.decl:
            if type(item) is FuncDecl and item.body is not None and item.name.name != "main":
                self.function = self.Listfunction[i]
                self.visit(item, Symbol)
            if type(item) is FuncDecl and item.body is not None:
                i += 1
                
        
        #* khởi tạo hàm main
        frame = Frame("main", VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme="main", in_=FuncZcode("main", VoidType(), [ArrayType([1], StringType())]), isStatic=True, frame=frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        index = frame.getNewIndex()
        typeParam = [VarZcode("for", NumberType(), index, True)]
        self.emit.printout(self.emit.emitVAR(index, "for", NumberType(), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.function = function
        self.visit(Main.body, Access(frame, [typeParam] + Symbol, False))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))   
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()    
        self.emit.emitEPILOG()
    
    def visitVarDecl(self, ast, o):
        """#TODO: Implement
        #* tạo emitVAR và o.symbol[0].append, cập nhật o.symbol[0][-1].line
        #* if ast.varInit is not None:
            #* elf.visit(Assign(ast.name, ast.varInit), o) 
        #* elif type(ast.varType) is ArrayType:
            #* giống phần khai báo biến static gần giống ý tưởng
        """
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
        """TODO: Implement
        #* giống hàm main, nhưng phần này có param
        """
        frame = Frame(ast.name.name, None)
        
        self.emit.printout(self.emit.emitMETHOD(lexeme=ast.name.name, in_=self.function, isStatic=True, frame=frame))
        self.function.line = self.emit.printIndexNew()
        
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        typeParam = []
        # typ = []
        for index, param in enumerate(ast.param):
            # self.visit(param, Access(frame, Symbol, False))
            idx = frame.getNewIndex()
            code = self.emit.emitVAR(idx, param.name.name, param.varType, frame.getStartLabel(), frame.getEndLabel(), frame)
            self.emit.printout(code)
            typeParam += [VarZcode(param.name.name, param.varType, index, True if param.varInit else False)]
            # self.emit.printout(self.emit.emitVAR(index, param.name.name, param.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
            # typ += [param.varType]
                
        index = frame.getNewIndex()
        typeParam += [VarZcode("for", NumberType(), index, True)]        
        self.emit.printout(self.emit.emitVAR(index, "for", NumberType(), frame.getStartLabel(), frame.getEndLabel(), frame))
        # self.function = function
        self.visit(ast.body, Access(frame, [typeParam] + Symbol, False))
        
        if not self.Return:
            self.function.typ = VoidType()
            self.emit.printout(self.emit.emitRETURN(self.function.typ, frame))
        # update the type of function after visit return
        # print("*************", self.function.line)
        self.emit.buff[self.function.line] = self.emit.emitMETHOD(lexeme=ast.name.name, in_=self.function, isStatic=True, frame=frame)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))   
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        
        frame.exitScope()    

    def visitId(self, ast, o):
        frame = o.frame
        Symbol = o.symbol
        
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            for item in Symbol:
                for sym in item:
                    if sym.name == ast.name:
                        return None, sym.typ if sym.typ else sym
        """#TODO : gọi emitINVOKESTATIC
        #* biến cục bộ dùng emitREADVAR, emitWRITEVAR tùy isleft
        #* biến toàn cục (static)  dùng emitPUTSTATIC, emitGETSTATIC tùy isleft
        """  
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
            # write
            if isStatic:
                code = self.emit.emitPUTSTATIC(self.className + '.' + sym.name, sym.typ, o.frame)
            else:
                code = self.emit.emitWRITEVAR(sym.name, sym.typ, sym.index, o.frame)
        else:
            # read
            if isStatic:                 
                code = self.emit.emitGETSTATIC(self.className + '.' + sym.name, sym.typ, o.frame)
            else:  
                code = self.emit.emitREADVAR(sym.name, sym.typ, sym.index, o.frame)
        
        return code, sym.typ
                                      

    def visitCallExpr(self, ast, o):
        #* phần io -> gọi qua class io.java trong pahanf lib
        if ast.name.name in ["readNumber", "readBool", "readString"]:
            if ast.name.name == "readNumber": 
                if o.checkTypeLHS_RHS: return None, NumberType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, NumberType(), []), o.frame), NumberType()
            elif ast.name.name == "readBool": 
                if o.checkTypeLHS_RHS: return None, BoolType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, BoolType(), []), o.frame), BoolType()
            elif ast.name.name == "readString": 
                if o.checkTypeLHS_RHS: return None, StringType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, StringType(), []), o.frame), StringType()

        #* tìm function trong self.Listfunction
        function = None
        for item in self.Listfunction:
            if item.name == ast.name.name:
                function = item
                
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            for i in range(len(function.param)):
                self.LHS_RHS(function.param[i], ast.args[i], o)
            return None, function.typ if function.typ else function            
            
        
        """#TODO : gọi emitINVOKESTATIC
        ví dụ : 
        .line 12 -> foo(1,true)
        0: iconst_1
        1: iconst_1
        2: invokestatic ZCodeClass/foo(IZ)V        
        """
        code = ""
        typArg = []
        for exp in ast.args:
            expCode, expType = self.visit(exp, o)
            code += expCode
            typArg.append(expType)
            
        code += self.emit.emitINVOKESTATIC(self.className + '.' + ast.name.name, FuncZcode(ast.name.name, function.typ, typArg), o.frame)
        return code, function.typ
     

    def visitBinaryOp(self, ast, o):
        op = ast.op
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            if op in ['+', '-', '*', '/', '%']:
                self.LHS_RHS(ast.left, NumberType(), o)
                self.LHS_RHS(ast.right, NumberType(), o)
                return None, NumberType()
            elif op in ['=', '!=', '<', '>', '>=', '<=']:
                self.LHS_RHS(ast.left, NumberType(), o)
                self.LHS_RHS(ast.right, NumberType(), o)
                return None, BoolType()
            elif op in ['and', 'or']:
                self.LHS_RHS(ast.left, BoolType(), o)
                self.LHS_RHS(ast.right, BoolType(), o)
                return None, BoolType()
            elif op in ['==']:
                self.LHS_RHS(ast.left, StringType(), o)
                self.LHS_RHS(ast.right, StringType(), o)
                return None, BoolType()
            elif op in ['...']:
                self.LHS_RHS(ast.left, StringType(), o)
                self.LHS_RHS(ast.right, StringType(), o)
                return None, StringType()
        
        codeLeft, _ = self.visit(ast.left, o)
        codeRight, _ = self.visit(ast.right, o)
        """#TODO emitADDOP, emitMULOP, emitREOP, emitANDOP,emitOROP, emitREOP, emitINVOKEVIRTUAL (dùng java/lang/String/concat và java/lang/String/equals)
        #^ mọi năm có tính toán lười cho and và or năm này thấy thầy ko mô tả lạ thật :((
        #* khó nhất chắc là % ta dùng như sau 
            codeLeft
            codeRight
            codeLeft
            codeRight
            '/'
            emitF2I -> ép kiểu sang int
            emitI2F -> từ in ép kiểu ngược lại
            '*'
            '-'
        """
        if op in ['+', '-']:
            code = self.emit.emitADDOP(ast.op, NumberType(), o.frame)
            rt = NumberType()
        elif op in ['*', '/']:
            code = self.emit.emitMULOP(ast.op, NumberType(), o.frame)
            rt = NumberType()
        elif op in ['and']:
            code = self.emit.emitANDOP(o.frame)
            rt = BoolType()
        elif op in ['or']:
            code = self.emit.emitOROP(o.frame)
            rt = BoolType()
        elif op in ['%']:
            o.frame.push()
            o.frame.push()
            code = codeLeft + codeRight + self.emit.emitMULOP('/', NumberType(), o.frame) + self.emit.emitF2I(o.frame) + self.emit.emitI2F(o.frame) + self.emit.emitMULOP('*', NumberType(), o.frame) + self.emit.emitADDOP('-', NumberType(), o.frame)
            rt = NumberType()
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            code = self.emit.emitREOP(ast.op, NumberType(), o.frame)
            rt = BoolType()
        elif op in ['==']:
            code = self.emit.emitINVOKEVIRTUAL("java/lang/String/equals", FuncZcode("equals", BoolType(), [None]), o.frame)
            rt = BoolType()
        elif op in ['...']:
            code = self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", FuncZcode("concat", StringType(), [StringType()]), o.frame)
            rt = StringType()    
        
        return codeLeft + codeRight + code, rt
       

    def visitUnaryOp(self, ast, o):
        op = ast.op
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            if op in ['-']:
                self.LHS_RHS(ast.operand, NumberType(), o)
                return None, NumberType()
            elif op in ['not']:
                self.LHS_RHS(ast.operand, BoolType(), o)
                return None, BoolType()
        """#TODO emitNEGOP, emitNOT
        """
        codeOp, _ = self.visit(ast.operand, o)
        
        if op in ['-']:
            code = self.emit.emitNEGOP(NumberType(), o.frame)
            rt = NumberType()
        elif op in ['not']:
            code = self.emit.emitNOT(BoolType(), o.frame)
            rt = BoolType()
        
        return codeOp + code, rt            
    
    def visitArrayLiteral(self, ast, o):
        frame = o.frame
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            mainTyp = None
            for item in ast.value:
                _, checkTyp = self.visit(item, o)
                if mainTyp is None and isinstance(checkTyp, (BoolType, StringType, NumberType, ArrayType)):
                    mainTyp = checkTyp
                    break
        
            for item in ast.value:
                self.LHS_RHS(mainTyp, item, o)
            
            if isinstance(mainTyp, (BoolType, StringType, NumberType)):
                return None, ArrayType([len(ast.value)], mainTyp)
            return None, ArrayType([float(len(ast.value))] + mainTyp.size, mainTyp.eleType)

        """#TODO:
        #* trường hợp mảng 1 chiều
            emitPUSHCONST -> giá trị khởi tạo của mảng
            emitF2I -> ép kiểu sang int
            emitNEWARRAY -> khởi tạo mảng
            for
                emitDUP -> nhân 2 ở đây là địa chỉ của mảng khởi tạo phía trên
                emitPUSHCONST -> giá trị index trong mảng
                emitF2I
                visit -> giá trị biến
                emitASTORE -> lưu trữ
    
        #* trường hợp mảng nhiều chiều
            emitPUSHCONST -> giá trị khởi tạo của mảng
            emitF2I -> ép kiểu sang int
            emitANEWARRAY -> khởi tạo mảng
            for
                emitDUP -> nhân 2 ở đây là địa chỉ của mảng khởi tạo phía trên
                emitPUSHCONST -> giá trị index trong mảng
                emitF2I
                visit -> giá trị biến
                emitASTORE -> lưu trữ             
        """
        _, typ = self.visit(ast.value[0], o)
        code = self.emit.emitPUSHCONST(len(ast.value), NumberType(), frame)
        code += self.emit.emitF2I(frame)
        if type(typ) in [NumberType, StringType, BoolType]: 
            code += self.emit.emitNEWARRAY(typ, frame)
        else:
            code += self.emit.emitANEWARRAY(typ, frame)
        
        for index, val in enumerate(ast.value):
            code += self.emit.emitDUP(frame)
            code += self.emit.emitPUSHCONST(index, NumberType(), frame)
            code += self.emit.emitF2I(frame)
            code += self.visit(val, Access(frame, o.symbol, False))[0]
            code += self.emit.emitASTORE(typ, frame)

        if type(typ) in [NumberType, StringType, BoolType]:
            return code, ArrayType([len(ast.value)], typ)
        return code, ArrayType([len(ast.value)] + typ.size, typ.eleType)
       
    def visitArrayCell(self, ast, o):
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            _, arr = self.visit(ast.arr, Access(o.frame, o.symbol, False, False))
            for i in ast.idx:
                self.LHS_RHS(NumberType(), i, o)
            if len(arr.size) == len(ast.idx): return None, arr.eleType
            return None, ArrayType(arr.size[len(ast.idx):], arr.eleType)   

    # arr: Expr
    # idx: List[Expr] 
    # a[1,2,3]

        """#TODO: implement
        #* trường trả về giá trị khác mảng
            visit(ast.arr) -> lấy ra get/put/read/write
            for 0 -> size - 1
               giá trị tại index
               f2i
               aload
            giá trị tại index = -1
            f2i
            float/bload/aload(string)  (nếu o.isLeft thì bỏ qua không gọi mà gán self.arrayCell = typ)  
    
        #* trường hợp tra về magnr
            visit(ast.arr) -> lấy ra get/put/read/write
            for 0 -> size - 1
               giá trị tại index
               f2i
               aload
            giá trị tại index = -1
            f2i
            aload -> địa chỉ   (nếu o.isLeft thì bỏ qua không gọi mà gán self.arrayCell = typ)            
        """
        
        code, arrT = self.visit(ast.arr, Access(o.frame, o.symbol, False, False))
        
        # return ko phải mảng
        if len(arrT.size) == len(ast.idx):            
            for i, item in enumerate(ast.idx):
                itemC, itemT = self.visit(item, Access(o.frame, o.symbol, False))
                code += itemC
                code += self.emit.emitF2I(o.frame)
                if o.isLeft:
                    if (i < len(ast.idx) - 1):
                        code += self.emit.emitALOAD(ArrayType(arrT.size[len(ast.idx):], arrT.eleType), o.frame)
                    self.arrayCell = arrT.eleType
                elif i == len(ast.idx) - 1: 
                    code += self.emit.emitALOAD(arrT.eleType, o.frame)
                else:
                    code += self.emit.emitALOAD(ArrayType(arrT.size[len(ast.idx):], arrT.eleType), o.frame)
            rt = arrT.eleType
        else:
            # return mảng
            for i, item in enumerate(ast.idx):
                itemC, itemT = self.visit(item, Access(o.frame, o.symbol, False))
                code += itemC
                code += self.emit.emitF2I(o.frame)
                if o.isLeft:
                    self.arrayCell = ArrayType(arrT.size[len(ast.idx):], arrT.eleType)
                else: 
                    code += self.emit.emitALOAD(ArrayType(arrT.size[len(ast.idx):], arrT.eleType), o.frame)
            
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
        #* CHECK TYPE BTL3
        self.LHS_RHS(self.function, ast.expr if ast.expr else VoidType(),o)
        
        self.Return = True #* đã có return
        
        """#TODO emitRETURN
        #* TH1 : nếu  ast.expr is None
        return
        
        #* TH2 : Ngc lại vd : return 1
        iconst_1
        freturn
        """
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
        
        """#TODO
        TH1 : LHS = ArrayCell
        lhsCode
        rhsCode
        self.emit.emitASTORE(self.arrayCell, frame))
        
        TH2 : 
        lhsCode
        rhsCode        
        """
        if type(ast.lhs) is ArrayCell:
            self.emit.printout(lc)
            self.emit.printout(rc)
            self.emit.printout(self.emit.emitASTORE(self.arrayCell, frame))  
        else:
            self.emit.printout(rc)
            self.emit.printout(lc)        
  
    
    def visitCallStmt(self, ast, o):
        #* phần io
        if ast.name.name in ["writeNumber", "writeBool", "writeString"]:
            if ast.name.name == "writeNumber": self.LHS_RHS(ast.args[0], NumberType(), o)
            elif ast.name.name == "writeBool": self.LHS_RHS(ast.args[0], BoolType(),  o)
            elif ast.name.name == "writeString": self.LHS_RHS(ast.args[0], StringType(), o)
            
            argsCode, argsType = self.visit(ast.args[0], o)
            self.emit.printout(argsCode)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, VoidType(), [argsType]), o.frame))
            return

        """#TODO giống call expr"""
        #* tìm function trong self.Listfunction
        function = None
        for item in self.Listfunction:
            if item.name == ast.name.name:
                function = item
        
        code = ""
        typArgs = []
        for exp in ast.args:
            expCode, expType = self.visit(exp, o)
            code += expCode
            typArgs.append(expType)
            
        code += self.emit.emitINVOKESTATIC(self.className + '.' + ast.name.name, FuncZcode(ast.name.name, function.typ, typArgs), o.frame)
        self.emit.printout(code)
  
          
    def visitBlock(self, ast, o):
        symbolnew = [[]] + o.symbol #! tăng tầm vực
        o.frame.enterScope(False) #* tầm vực mới, vì biến khởi tạo sẽ được xóa khi kết thúc tầm vực nên cần scope
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame)) #* đánh số tầm vực mới
        for item in ast.stmt: 
            self.visit(item,Access(o.frame, symbolnew, False))   
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame)) #* đánh số tầm vực mới
        o.frame.exitScope()  #* kết thức tầm vực
       
    def visitIf(self, ast, o):
        #* CHECK TYPE BTL3       
        self.LHS_RHS(BoolType(), ast.expr, o)        
        for item in ast.elifStmt:
            self.LHS_RHS(BoolType(), item[0], o)   
        
        """_enterLoop_
            điều kiện if -> nhảy đến đặt label end if
                |
            visit body
                |
            goto exit
                |
            đặt label end if
                |
            nếu có eilf -> for
                        tạo lable mới
                            |
                        điều kiện -> nhảy lable mới
                            | 
                        visit
                            |
                        goto exit
                            |
                        đặt đến lable mới
                            |
            -- end for
                |
            nếu có else
                            |
                          visit
                            |
            lable exit
        """
        #TODO: implement
        # Xin từ frame: exitLabel
        exitLabel = o.frame.getNewLabel()
        
        endIfLabel = o.frame.getNewLabel()
        # Sinh mã cho expr
        ec, et = self.visit(ast.expr, Access(o.frame, o.symbol, False))
        self.emit.printout(ec)
        # Nhảy đến elIfLabel nếu False
        code = self.emit.emitIFFALSE(endIfLabel, o.frame)
        self.emit.printout(code)
        # Sinh mã cho thenStmt
        self.visit(ast.thenStmt, o)
        
        # Nhảy đến exitLabel
        self.emit.printout(self.emit.emitGOTO(exitLabel, o.frame))
        
        # Đặt elIfLabel tại đây
        self.emit.printout(self.emit.emitLABEL(endIfLabel, o.frame))
        
        for item in ast.elifStmt:
            loopLabel = o.frame.getNewLabel()
            
            itemEc, _ = self.visit(item[0], o)
            self.emit.printout(itemEc)
            self.emit.printout(self.emit.emitIFFALSE(loopLabel, o.frame))
            
            self.visit(item[1], o)
            self.emit.printout(self.emit.emitGOTO(exitLabel, o.frame))
            
            self.emit.printout(self.emit.emitLABEL(loopLabel, o.frame))
        
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, o)

        # Đặt exitLabel tại đây
        self.emit.printout(self.emit.emitLABEL(exitLabel, o.frame))  
        
        
    def visitFor(self, ast, o):
        
        #* CHECK TYPE BTL3
        """_typID_"""        
        self.LHS_RHS(NumberType(), ast.name, o)        
        
        """_typCondExpr_"""    
        self.LHS_RHS(BoolType(), ast.condExpr, o) 

        """_typUpdExpr_"""            
        self.LHS_RHS(NumberType(), ast.updExpr, o) 

        self.visit(ast.name, o)
        
        """_enterLoop_
            gán for <- ast.name
                |
            tạo Loop
                |
            lable_new
                |
            kiểm tra exp để goto đến lable_Break
                |
            visit body
                |
            đặt lable continue
                |
            gọi phép gán Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr))
                |
            goto đến lable_new
                |
            đặt lable_Break
                |
            end loop
                |
            gán for <- ast.name
            
        """
        
        self.visit(Assign(Id("for"), ast.name), o)
        #TODO implement
        o.frame.enterLoop()
        cLabel = o.frame.getContinueLabel()
        bLabel = o.frame.getBreakLabel()
        
        # New loop
        newLabel = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(newLabel, o.frame))
        
        # Sinh mã cho condExpr
        ec, et = self.visit(ast.condExpr, Access(o.frame, o.symbol, False))
        self.emit.printout(ec)
        # Nhảy đến bLabel nếu False
        self.emit.printout(self.emit.emitIFTRUE(bLabel, o.frame))
        
        # Visit body
        self.visit(ast.body, o)
        
        # Đặt continue
        self.emit.printout(self.emit.emitLABEL(cLabel, o.frame))
        
        # Sinh mã cho updExpr
        self.visit(Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr)), o)
        # Loop        
        self.emit.printout(self.emit.emitGOTO(newLabel, o.frame))

        # Đặt break label
        self.emit.printout(self.emit.emitLABEL(bLabel, o.frame))
        o.frame.exitLoop()
        self.visit(Assign(ast.name, Id("for")), o)
        

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
        
