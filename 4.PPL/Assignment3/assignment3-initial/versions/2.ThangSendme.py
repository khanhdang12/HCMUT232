"""
^name : Võ Tiến
^FB : https://www.facebook.com/profile.php?id=100056605580171
^GROUP: https://www.facebook.com/groups/211867931379013/
^DAY : 10/4/2024
"""

"""
Kiến thức cần 
List : https://www.w3schools.com/python/python_lists.asp
Dict : https://www.w3schools.com/python/python_dictionaries.asp
isinstance() : https://www.w3schools.com/python/ref_func_isinstance.asp
"""

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

"""
    * Type gồm
        * NumberType, BoolType, StringType
        * ArrayType : gồm size, eleType (NumberType, BoolType, StringType)
        * ArrayZcode : eleType chỉ bao gồm các type kiểu Zcode và ArrayZcode, typ chưa được suy diễn
        * Zcode : typ chưa được suy diễn cần xác định khi lần dùng đầu tiên
            *  FuncZcode : kiểu typ của hàm chưa suy diễn or có thể đã được suy diễn gồm
                ^ param : danh sách các biến cần truyền vào hàm được biểu diễn dưới dạng danh sách kiêu
                ^ typ : kiểu type của hàm hiện tại nếu typ là None thì hàm này chưa xác định kiểu ngược lại có typ thì đã xác định được kiểu
                ^ body : xem thử hàm khai báo trước 1 phần (nghĩa là không có body) hay không
            * VarZcode : kiểu typ của biến chưa được suy diễn or có thể đã được suy diễn
                ^ typ : kiểu type của hàm hiện tại nếu typ là None thì biến này chưa xác định kiểu ngược lại có typ thì đã xác định được kiểu
"""

class Zcode(Type):
    pass

class FuncZcode(Zcode):
    #* param : list[Type]
    #* typ : Type có thể là number, bool, string, arrayType or None (có thể hiểu nhanh đang FuncZcode)
        #! -> nên khi gọi callFunc thì trả về typ nếu có (khác None) không thì trả về chính nó this (FuncZcode)
    #* body : Bool nếu là true nghĩa là body đã có (khai báo toàn bộ có body hàm), nếu False nghĩa là khai báo 1 phần (khai báo không có body)
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):
    #* typ : Type có thể là number, bool, string, arrayType or None (có thể hiểu nhanh đang VarZcode)
        #! -> nên khi gọi callFunc thì trả về typ nếu có (khác None) không thì trả về chính nó this (VarZcode)    
    def __init__(self, typ = None):
        self.typ = typ    

class ArrayZcode(Type):
    #* eleType: List[Type]
    #* Type ở đây có thể là Zcode, ArrayZcode, String, bool, number, arraytype
    def __init__(self, eleType):
        self.eleType = eleType

class StaticChecker(BaseVisitor, Utils):
    #* ast : cây ở BTL2
    #* BlockFor : int, kiểm tra xem chúng ta đang ở trong vòng for thứ mấy
    #* function: FuncZcode, kiểm tra hàm hiện tại chúng ta đang vào body của nó checkStatic
    #* listFunction : Dict<string, FuncZcode>, Danh sách các hàm, ban đầu sẽ mặc định các hàm read, write file
    #* return : Bool, kiểm tra hàm hiện tại có return hay không nếu không có thì xác đinh hàm này là VoidType
    def __init__(self,ast):
        self.ast = ast 
        self.BlockFor = 0
        self.function = None
        self.Return = False
        self.listFunction = {
            "readNumber" : FuncZcode([], NumberType(), True),
            "readBool" : FuncZcode([], BoolType(), True),
            "readString" : FuncZcode([], StringType(), True),
            "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
            "writeBool" : FuncZcode([BoolType()], VoidType(), True),
            "writeString" : FuncZcode([StringType()], VoidType(), True)
        }
        
        
    def check(self):
        self.visit(self.ast, [{}])
        return None
    
    """_comparType_
        #* LHS và RHS chỉ có thể là Void, number, string, bool, arrayType
        #* TH1 nếu LHS và RHS đều là array
            #^ xét kích thước size có giống nha không nếu không giống nhau trả Flase
            #^ xét từng phần tử trong size của 2 thằng nếu không giống nhau trả Flase
            #^ xét tiếp eleType nếu không giống nhau trả Flase
        #* TH2 nếu cả 2 không phải array -> so sánh type của 2 nó thôi      
    """
    def comparType(self, LHS, RHS):
        if type(LHS) is ArrayType and type(RHS) is ArrayType:
            return LHS.size == RHS.size and type(LHS.eleType) is type(RHS.eleType)
        
        return type(LHS) is type(RHS)
            
    
    """_comparListType
        #* LHS và RHS chỉ có thể list các type sau Void, number, string, bool, arrayType
        #* TH1 nếu LHS và RHS khác kích thước -> Flase
        #* duyệt từng phần tử gọi self.comparType(LHS[i], RHS[i])
    """    
    def comparListType(self, LHS, RHS):
        if len(LHS) != len(RHS):
            return False
        
        for i in range(len(LHS)):
            if not self.comparType(LHS[i], RHS[i]):
                return False
            
        return True
        
    
    def setTypeArray(self, typeArray, typeArrayZcode, arrliteral, param):
        #* Trường hợp size khác nhau
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False 
        
        #* trường hợp bên trong array là các kiểu nguyên thủy (array 1 chiều)
           #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = typeArray.eleType
           #^ nếu typeArrayZcode.eleType[i] là arrayZcode : trả về False (vì 1 chiều mà bắt gán 2 chiều :) )
        if len(typeArray.size) == 1:
            for i in range(len(typeArrayZcode.eleType)):
                if isinstance(typeArrayZcode.eleType[i], Zcode):
                    typeArrayZcode.eleType[i].typ = typeArray.eleType
                    idname = arrliteral.value[i].name
                    for j in range(len(param)):
                        id = param[j].get(idname)
                        if id is not None:
                            param[j][idname] = VarZcode(typeArray.eleType)
                            break
                elif type(typeArrayZcode.eleType[i]) is ArrayZcode:
                    return False  
            
        #* trường hợp bên trong array là các arrayType (array >= 2 chiều)
           #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = typeArray.eleType
           #^ nếu typeArrayZcode.eleType[i] là arrayZcode : gọi đệ quy self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType),typeArrayZcode[i]) để vào bên trong xem có lỗi gì không       
        else:      
            for i in range(len(typeArrayZcode.eleType)):
                if isinstance(typeArrayZcode.eleType[i], Zcode):
                    typeArrayZcode.eleType[i].typ = ArrayType(typeArray.size[1:], typeArray.eleType)
                    idname = arrliteral.value[i].name
                    for j in range(len(param)):
                        id = param[j].get(idname)
                        if id is not None:
                            param[j][idname] = VarZcode(ArrayType(typeArray.size[1:], typeArray.eleType))
                            break
                elif type(typeArrayZcode.eleType[i]) is ArrayZcode:
                    self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType), typeArrayZcode.eleType[i], arrliteral.value[i], param)

        return True
    
    def visitProgram(self, ast, param):
        #* duyệt qua các biến và hàm toàn cục
        for i in ast.decl: self.visit(i, param)
        
        print("AAAAAAAAAAAAAAAAA", param)
        
        """_NoDefinition_
            #TODO check No definition for a function in self.listFunction
            ví dụ 1 -> đúng
            func foo(number a)
            func foo(number a) return
            
            ví dụ 2 -> đúng
            func foo(number a) return
            
            ví dụ 3 -> sai NoDefinition
            func foo(number a)
        """
        #TODO implement
        for key, val in self.listFunction.items():
            if not val.body:
                raise NoDefinition(key)

        """_NoEntryPoint_
            #TODO check No entry Point in listFunction, tìm hàm tên "main"
            ví dụ 1 -> đúng
            func main() return
            
            ví dụ 2 -> đúng
            func main()
            func main() begin
            end
            
            ví dụ 3 -> sai NoEntryPonumber, sai param
            func main(number a) return
            
            ví dụ 4 -> sai NoEntryPonumber, sai returnType
            func main() return 1       
            
            ví dụ 5 -> sai NoEntryPonumber, không tồn tại
            không có hàm main      
        """        
        #TODO implement
        main = self.listFunction.get("main")
        if not main:
            raise NoEntryPoint()
        elif main.param or type(main.typ) is not VoidType: 
            raise NoEntryPoint()

    def visitVarDecl(self, ast, param):
        """_Redeclared_
            #TODO kiểm tra name có trong param[0] hay không nén ra lỗi Redeclared
            ví dụ 1 -> đúng
            number a

            ví dụ 2 -> Redeclared(Variable(), ast.name.name)
            number a
            string a    

        """           
        #TODO implement
        if param[0].get(ast.name.name):
            raise Redeclared(Variable(), ast.name.name)
            
        param[0][ast.name.name] = VarZcode(ast.varType) #! cập nhật param mới đưa tên vào, biến dynamic hay var sẽ type = None
        """_TypeCannotBeInferred_TypeMismatchInStatement_
            # TODO kiểm tra TypeCannotBeInferred và TypeMismatchInStatement xử lí ast.varInit (nếu khác None)
            #* nguyên lí LHS (ast.varType) và RHS (ast.varInit), cả 2 đều là Type, chú ý LHS không bao giờ là ArrayZcode
                #^ TH1 cả 2 đều là Zcode chưa suy diễn được : raise TypeCannotBeInferred(ast)
                #^ TH2 nếu LHS là Zcode và RHS là ArrayZcode: raise TypeCannotBeInferred(ast) 
                #^ TH3 nếu LHS không phải Zcode và RHS là ArrayZcode:
                    #^ TH3.1 nếu LHS là string, bool, number : raise TypeMismatchInStatement(ast) 
                    #^ TH3.2 nếu LHS là arrayType kiểm tra self.setTypeArray(LHS, RHS) nếu không đúng raise TypeMismatchInStatement(ast)
                #^ TH4 nếu LHS là Zcode và RHS là string, bool, number, arrytype : LHS.typ = RHS
                #^ TH5 ngược lại TH4
                #^ TH6 cả LHS và RHS có kiểu string, bool, number, arrytype -> kiểm tra self.comparType(LHS, RHS): raise TypeMismatchInStatement(ast)
            
            #! TH1 TypeCannotBeInferred
            func foo()
            var a <- foo()    
            
            #! TH2 TypeCannotBeInferred(ast)
            dynamic x
            var a <- [x]
            
            #! TH3.1 TypeMismatchInStatement(ast)
            dynamic x
            number a <- [x] -> raise TypeMismatchInStatement(ast) 
            
            #! TH3.2 : X = arraytype([3], number)
            dynamic x
            number a[1][3] <- [x]
                        
            #! TH4, 5 : foo().typ = b.typ = numberType()
            func foo()
            number a <- foo()
            var b <- a            

            #! TH6 TypeMismatchInStatement
            number a <- "1"                
        """ 
        if ast.varInit:    
            #TODO implement
            expType = self.visit(ast.varInit, param)
            if ast.modifier == 'var' or ast.modifier == 'dynamic':
                if isinstance(expType, Zcode) or type(expType) is ArrayZcode:
                    raise TypeCannotBeInferred(ast)
                param[0][ast.name.name].typ = expType
            elif type(expType) is ArrayZcode:
                if type(ast.varType) in [StringType, BoolType, NumberType]:
                    raise TypeMismatchInStatement(ast)
                elif type(ast.varType) is ArrayType:
                    if not self.setTypeArray(ast.varType, expType, ast.varInit, param):
                        raise TypeMismatchInStatement(ast)
                            
            elif isinstance(expType, Zcode):
                if type(expType) is FuncZcode:
                    self.listFunction[ast.varInit.name.name].typ = ast.varType
                elif type(expType) is VarZcode:
                    for i in range(len(param)):
                        id = param[i].get(ast.varInit.name)
                        if id is not None:
                            param[i][ast.varInit.name].typ = ast.varType
                            break
                        
            elif not self.comparType(ast.varType, expType):
                raise TypeMismatchInStatement(ast)
            

    def visitFuncDecl(self, ast, param):
        """
            #TODO kiểm tra name có trong self.listFunction hay không nén ra lỗi Redeclared 
            ví dụ 1 -> đúng
            func foo() return

            ví dụ 2 -> đúng
            func foo()
            func foo() return
            
            ví dụ 3 -> Redeclared
            func foo() return
            func foo()

            ví dụ 4 -> Redeclared
            func foo()
            func foo()
            
            ví dụ 5 -> Redeclared
            func foo() return
            func foo() return
        """ 
        print("Visiting FuncDecl")
        method = self.listFunction.get(ast.name.name)
        #TODO implement
        if method and (method.body or (not method.body and not ast.body)):
            raise Redeclared(Function(), ast.name.name)
        
        listParam = {} #! dạng Dict có name khi visit dùng self.visit(ast.body, [listParam] + param)
        typeParam = [] #! dạng mảng không cần name truyền agrc vào FuncZcode
        """
            # TODO kiểm tra ast.param trong hàm trong listParam giống phần vardecl
                #^ cập nhật listParam (giống prama) và typeParam (chỉ gồm các type)
                #^ typeParam = [numberType, stringType, ...], listParam dạng DICT giống param
            
            ví dụ 1 -> đúng 
            func foo(number a, string b) return  
            -> typeParam = [numberType, stringType], listParam = {'a' : VarZcode(numberType), 'b' : VarZcode(stringType}         
            
            ví dụ 2 -> Redeclared
            func foo(number a, string a) return
        """ 
        #TODO implement
        for param_decl in ast.param:
            if listParam.get(param_decl.name.name) is not None:
                raise Redeclared(Parameter(), param_decl.name.name)
            
            listParam[param_decl.name.name] = VarZcode(param_decl.varType)
            typeParam.append(param_decl.varType)
            # print(listParam)
            
        
        """
            # TODO kiểm tra self.function = method hàm hiện tại chuẩn bị vào body nó xử lí
                #^ TH1 : method khai báo 1 phần
                    #todo : cập nhật trong self.listFunction
            func foo()
            
                #^ TH2 : method đã khai bó 1 phần trước đó
                    #todo 1 : kiểm trả list param có giống nhau không không nếu không trả về Redeclared(Function(), ast.name.name)
                    #todo 2 : cập nhật self.listFunction[].body, self.Return, self.function và self.visit(ast.body, [listParam] + param) 
                    #todo 3 : sau khi gọi hàm kiểm tra self.Return có trong hàm hay không nếu không thì xác định typ nó VoidType, rồi xem xét với typ của hàm, nếu hàm cũng voidtype thì đúng nếu không thì lỗi  raise TypeMismatchInStatement(Return(None))
            func foo() 
            func foo() begin
            end
            
                #^ TH3 : method khai báo đầu đủ lần đầu không có khai báo 1 phần
                    #todo 1 : cập nhật self.listFunction[].body, self.Return, self.function, self.listFunction
                    #todo 2 : giống todo 3 trên
            func foo() begin 
            end
            
                #^ ví dụ todo 3 của TH2
            #! xác định kiểu
            func foo() begin 
            end     
            -> type foo là VoidType  
            
            #! xác định kiểu
            func foo()
            number a <- foo() -> foo() có typ là number
            func foo() begin  -> này lại có typ là void nên lỗi raise TypeMismatchInStatement(Return(None))
            end     
        
        """
        self.Return = False
        if ast.body is None: 
            print("Without body")
            self.listFunction[ast.name.name] = FuncZcode(typeParam, None, False)
        
        elif method: 
            print("Lan 2: khai bao body")
            if not self.comparListType(typeParam, method.param):
                raise Redeclared(Function(), ast.name.name)
            self.listFunction[ast.name.name].body = True
            self.Return = False
            self.function = self.listFunction[ast.name.name]
            
            self.visit(ast.body, [listParam] + param)

            if not self.Return:
                if self.function.typ is None: 
                    self.function.typ = VoidType()
                    self.listFunction[ast.name.name].typ = VoidType()                  
                elif type(self.function.typ) is not VoidType:
                    raise TypeMismatchInStatement(Return())
        else:
            print("Khai bao ham lan dau, co body")
            self.listFunction[ast.name.name] = FuncZcode(typeParam, None, True)
            self.Return = False
            self.function = self.listFunction[ast.name.name]
            
            self.visit(ast.body, [listParam] + param)
            
            if not self.Return:
                if self.function.typ is None: 
                    self.function.typ = VoidType()
                    self.listFunction[ast.name.name].typ = VoidType()
                elif type(self.function.typ) is not VoidType:
                    raise TypeMismatchInStatement(Return())
                

    def visitId(self, ast, param):
        """
            # TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
                #^ đối với giá trị trả về nếu Id.typ = None thì trả về chính nó luôn varZcode, nếu cso Id.typ thì trả về typ của nó
            VD 1:
            number b <- a -> Undeclared(Identifier(), 'a') 
            
            VD 2:
            number a
            number b <- a -> a đã có VarZcode.typ nên return VarZcode.typ

            VD 3:
            var a
            number b <- a -> a có VarZcode.typ = None nên return VarZcode              
        """
        for env in param:
            id = env.get(ast.name)
            if id is not None:
                return id.typ if id.typ else VarZcode()
        
        raise Undeclared(Identifier(), ast.name)
                

    def visitCallExpr(self, ast, param):
        """
            TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
            VD 1: đúng 
            func foo()
            func main()begin
                var a <- foo()
            end
            
            VD 2: Undeclared
            func foo()
            func main()begin
                var a <- foo1()
            end
            
            VD 3: Undeclared
            func foo()
            func main()begin
                var foo <- 1
                var a <- foo()
            end
        """  
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí ast.varInit nếu tồn tại
            ^ xét listLHS (là method.param) và listRHS (là ast.args)
                ^ nếu len khác nhau TypeMismatchInExpression
                ^ nếu self.comparType(LHS[i], RHS[i]) -> TypeMismatchInExpression
            ^ nếu FuncZcode.typ is None thì return FuncZcode
            ^ nếu comparType(FuncZcode.typ, VoidType()) -> TypeMismatchInExpression
            ^ còn lại return FuncZcode.typ (giống phần VarZcode)
        """   

        method = self.listFunction.get(ast.name.name)
    
        if not method:
            raise Undeclared(Function(), ast.name.name)
        
        listLHS = method.param
        listRHS = ast.args
                
        if len(listLHS) != len(listRHS):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(listLHS)):
            rtype = self.visit(ast.args[i], param)
            
            if isinstance(listLHS[i], Zcode):
                if (isinstance(rtype, Zcode) or type(rtype) is ArrayZcode):
                    raise TypeCannotBeInferred(ast)
                elif type(rtype) in [StringType, BoolType, NumberType, ArrayType]:
                    listLHS[i].typ = rtype
                    self.listFunction[ast.name.name].param[i] = rtype
                    
            else:
                if type(rtype) is ArrayZcode:
                    if type(listLHS[i]) in [StringType, BoolType, NumberType]:
                        raise TypeMismatchInExpression(ast)
                    elif type(listLHS[i]) is ArrayType:
                        if not self.setTypeArray(listLHS[i], rtype, ast.args[i], param):
                            raise TypeMismatchInExpression(ast)
                elif isinstance(rtype, Zcode):
                    if type(rtype) is FuncZcode:
                        self.listFunction[ast.args[i].name.name].typ = listLHS[i]
                    else:
                        for j in range(len(param)):
                            id = param[j].get(ast.args[i].name)
                            if id is not None:
                                param[j][ast.args[i].name].typ = listLHS[i]
                                break
                else:
                    if not self.comparType(listLHS[i], rtype):
                        raise TypeMismatchInExpression(ast)
        
        if method.typ is None:
            return FuncZcode()
        elif self.comparType(method.typ, VoidType()):
            raise TypeMismatchInExpression(ast)
        
        return method.typ

    def visitCallStmt(self, ast, param):
        """như CallExpr chỉ khác ở chỗ not comparType(FuncZcode.typ, VoidType()) -> TypeMismatchInStatement"""
        method = self.listFunction.get(ast.name.name)
    
        if not method:
            raise Undeclared(Function(), ast.name.name)
        
        listLHS = method.param
        listRHS = ast.args
        if len(listLHS) != len(listRHS):
            raise TypeMismatchInStatement(ast)
        for i in range(len(listLHS)):
            rtype = self.visit(ast.args[i], param)
            
            if isinstance(listLHS[i], Zcode):
                if (isinstance(rtype, Zcode) or type(rtype) is ArrayZcode):
                    raise TypeCannotBeInferred(ast)
                elif type(rtype) in [StringType, BoolType, NumberType, ArrayType]:
                    listLHS[i].typ = rtype
                    self.listFunction[ast.name.name].param[i] = rtype
                    
            else:
                if type(rtype) is ArrayZcode:
                    if type(listLHS[i]) in [StringType, BoolType, NumberType]:
                        raise TypeMismatchInStatement(ast)
                    elif type(listLHS[i]) is ArrayType:
                        if not self.setTypeArray(listLHS[i], rtype, ast.args[i], param):
                            raise TypeMismatchInStatement(ast)
                elif isinstance(rtype, Zcode):
                    if type(rtype) is FuncZcode:
                        self.listFunction[ast.args[i].name.name].typ = listLHS[i]
                    else:
                        for j in range(len(param)):
                            id = param[j].get(ast.args[i].name)
                            if id is not None:
                                param[j][ast.args[i].name].typ = listLHS[i]
                                break
                else:
                    if not self.comparType(listLHS[i], rtype):
                        raise TypeMismatchInStatement(ast)
        
        if method.typ is None:
            return FuncZcode()
        elif not self.comparType(method.typ, VoidType()):
            raise TypeMismatchInStatement(ast)
        
        return method.typ

    def visitIf(self, ast, param):
        """_typExpr_
            # TODO giống phần kiểm tra TypeMismatchInStatement theo nguyên lí LHS và RHS
                #^ xét typExpr và self.visit(ast.thenStmt, [{}] + param)
            ^ LHS = BoolType(), RHS = self.visit(ast.expr, param)
        """   
        typExpr = self.visit(ast.expr, param)
        if type(typExpr) is VarZcode:
            for i in range(len(param)):
                id = param[i].get(ast.expr.name)
                if id is not None:
                    param[i][ast.expr.name].typ = BoolType()
                    break
        elif type(typExpr) is FuncZcode:
            self.listFunction[ast.expr.name.name].typ = BoolType()
        elif type(typExpr) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.thenStmt, [{}] + param)
        
        """_elifStmt_
            #TODO giống trên, LHS = BoolType()
        """   
        for stmt in ast.elifStmt:
            typ = self.visit(stmt[0], param)
            if type(typ) is VarZcode:
                for i in range(len(param)):
                    id = param[i].get(stmt[0].name)
                    if id is not None:
                        param[i][stmt[0].name].typ = BoolType()
                        break
            elif type(typExpr) is FuncZcode:
                self.listFunction[stmt[0].name.name].typ = BoolType()
            elif type(typ) is not BoolType:
                raise TypeMismatchInStatement(ast)
            
            self.visit(stmt[1], [{}] + param)
            
        """_elseStmt_
        """            
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, [{}] + param)
        
    def visitFor(self, ast, param):
        """_typID_
            #TODO giống mấy thằng trong if, LHS = NumberType()
        """        
        typId = self.visit(ast.name, param)
        if type(typId) is VarZcode:
            for i in range(len(param)):
                id = param[i].get(ast.name.name)
                if id is not None:
                    param[i][ast.name.name].typ = NumberType()
                    break
        elif type(typId) is not NumberType:
            raise TypeMismatchInStatement(ast)
        
        """_typCondExpr_
            #TODO giống mấy thằng trong if, LHS = BoolType()
        """    
        typCondExpr = self.visit(ast.condExpr, param)
        if type(typCondExpr) is VarZcode:
            for i in range(len(param)):
                id = param[i].get(ast.condExpr.name)
                if id is not None:
                    param[i][ast.condExpr.name].typ = BoolType()
                    break
        elif type(typCondExpr) is not BoolType:
            raise TypeMismatchInStatement(ast)

        """_typUpdExpr_
            #TODO giống mấy thằng trong if, LHS = NumberType()
        """            
        typUpdExpr = self.visit(ast.updExpr, param)
        if type(typUpdExpr) is VarZcode:
            for i in range(len(param)):
                id = param[i].get(ast.updExpr.name)
                if id is not None:
                    param[i][ast.updExpr.name].typ = NumberType()
                    break
        elif type(typUpdExpr) is not NumberType:
            raise TypeMismatchInStatement(ast)       
        
        
        self.BlockFor += 1 #! vào trong vòng for nào anh em
        self.visit(ast.body, [{}] + param) #! tạo ra tầm vực mới
        self.BlockFor -= 1 #! cút khỏi vòng for nào anh em
    
    def visitReturn(self, ast, param):
        """
            # TODO kiểm tra TypeCannotBeInferred và TypeMismatchInStatement nguyên lí LHS và RHS
                #^ LHS là self.function.typ if self.function.typ else self.function
                #^ RHS là self.visit(ast.expr, param) if ast.expr else VoidType()
        """
        self.Return = True
        LHS = self.function.typ if self.function.typ else self.function
        RHS = self.visit(ast.expr, param) if ast.expr else VoidType()
        
        print(type(LHS) is FuncZcode)
        print(isinstance(RHS, Zcode))
        
        if isinstance(LHS, Zcode):
            if (isinstance(RHS, Zcode) or type(RHS) is ArrayZcode):
                raise TypeCannotBeInferred(ast)
            elif type(RHS) in [StringType, BoolType, NumberType, ArrayType]:
                LHS.typ = RHS
                self.function.typ = RHS
            else:
                self.function.typ = VoidType()
                
        else:
            if type(RHS) is ArrayZcode:
                if type(LHS) in [StringType, BoolType, NumberType]:
                    raise TypeMismatchInStatement(ast)
                elif type(LHS) is ArrayType:
                    if not self.setTypeArray(LHS, RHS, ast.expr, param):
                        raise TypeMismatchInStatement(ast)
                    else: # infer type
                        pass
            elif isinstance(RHS, Zcode):
                if type(RHS) is FuncZcode:
                    self.listFunction[ast.expr.name.name].typ = LHS
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.expr.name)
                        if id is not None:
                            param[i][ast.expr.name].typ = LHS
                            break
            else:
                if not self.comparType(LHS, RHS):
                    raise TypeMismatchInStatement(ast)
        

    def visitAssign(self, ast, param):
        """
            # TODO kiểm tra TypeCannotBeInferred và TypeMismatchInStatement nguyên lí LHS và RHS
        """
        LHS = self.visit(ast.lhs, param)
        RHS = self.visit(ast.rhs, param)
        
        if isinstance(LHS, Zcode):
            if (isinstance(RHS, Zcode) or type(RHS) is ArrayZcode):
                raise TypeCannotBeInferred(ast)
            elif type(RHS) in [StringType, BoolType, NumberType, ArrayType]:
                LHS.typ = RHS
                for i in range(len(param)):
                    id = param[i].get(ast.lhs.name)
                    if id is not None:
                        param[i][ast.lhs.name].typ = RHS
                        break
                
        else:
            if type(RHS) is ArrayZcode:
                if type(LHS) in [StringType, BoolType, NumberType]:
                    raise TypeMismatchInStatement(ast)
                elif type(LHS) is ArrayType:
                    if not self.setTypeArray(LHS, RHS):
                        raise TypeMismatchInStatement(ast)
            elif isinstance(RHS, Zcode):
                if type(RHS) is FuncZcode:
                    self.listFunction[ast.rhs.name.name].typ = LHS
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.rhs.name)
                        if id is not None:
                            param[i][ast.rhs.name].typ = LHS
                            break
            else:
                if not self.comparType(LHS, RHS):
                    raise TypeMismatchInStatement(ast)
        
            
    def visitBinaryOp(self, ast, param):
        #! vì các Association đều là left nên tiến hành ở left rồi tiếp theo right, thầy mà cho có Association right thì trúng bẫy hết
        op = ast.op
        """_left_ 
            # TODO kiểm tra TypeCannotBeInferred và TypeMismatchInExpression nguyên lí LHS và RHS
            #! op in ['+', '-', '*', '/', '%']
                #^ LHS = NumberType(), left = self.visit(ast.left, param)
            #! op in ['=', '!=', '<', '>', '>=', '<=']
                #^ LHS = NumberType(), left = self.visit(ast.left, param)
            #! op in ['and', 'or']
                #^ LHS = boolType(), left = self.visit(ast.left, param)
            #! op in ['==']
                #^ LHS = StringType(), left = self.visit(ast.left, param)           
            #! op in ['...']
                #^ LHS = StringType(), left = self.visit(ast.left, param)  
        """        
        
        ltype = self.visit(ast.left, param)
        #TODO implement
        if op in ['+', '-', '*', '/', '%']:
            if isinstance(ltype, Zcode):
                if type(ltype) is FuncZcode:
                    self.listFunction[ast.left.name.name].typ = NumberType()
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.left.name)
                        if id is not None:
                            param[i][ast.left.name].typ = NumberType()
                            break
                ltype = NumberType()
                
        if op in ['=', '!=', '<', '>', '>=', '<=']:          
            if isinstance(ltype, Zcode):
                if type(ltype) is FuncZcode:
                    self.listFunction[ast.left.name.name].typ = NumberType()
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.left.name)
                        if id is not None:
                            param[i][ast.left.name].typ = NumberType()
                            break
                ltype = NumberType()
                
        if op in ['and', 'or']:
            if isinstance(ltype, Zcode):
                if type(ltype) is FuncZcode:
                    self.listFunction[ast.left.name.name].typ = BoolType()
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.left.name)
                        if id is not None:
                            param[i][ast.left.name].typ = BoolType()
                            break
                ltype = BoolType()
    
        if op in ['==']:
            if isinstance(ltype, Zcode):
                if type(ltype) is FuncZcode:
                    self.listFunction[ast.left.name.name].typ = StringType()
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.left.name)
                        if id is not None:
                            param[i][ast.left.name].typ = StringType()
                            break
                ltype = BoolType()
        
        if op in ['...']:
            if isinstance(ltype, Zcode):
                if type(ltype) is FuncZcode:
                    self.listFunction[ast.left.name.name].typ = StringType()
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.left.name)
                        if id is not None:
                            param[i][ast.left.name].typ = StringType()
                            break
                ltype = StringType()

        """_right_             
        """        
        rtype = self.visit(ast.right, param)
        #TODO implement
        if op in ['+', '-', '*', '/', '%']:
            if type(ltype) is NumberType and type(rtype) is NumberType:
                return NumberType()
            
            if isinstance(rtype, Zcode):
                if type(rtype) is FuncZcode:
                    self.listFunction[ast.right.name.name].typ = NumberType()
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.right.name)
                        if id is not None:
                            param[i][ast.right.name].typ = NumberType()
                            break
                return NumberType()
            
            raise TypeMismatchInExpression(ast)
        
        if op in ['=', '!=', '<', '>', '>=', '<=']:
            if type(ltype) is NumberType and type(rtype) is NumberType:
                return BoolType()
            
            if isinstance(rtype, Zcode):
                if type(rtype) is FuncZcode:
                    self.listFunction[ast.right.name.name].typ = NumberType()
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.right.name)
                        if id is not None:
                            param[i][ast.right.name].typ = NumberType()
                            break
                return BoolType()
            
            raise TypeMismatchInExpression(ast)
        
        if op in ['and', 'or']:
            if type(ltype) is BoolType and type(rtype) is BoolType:
                return BoolType()
            
            if isinstance(rtype, Zcode):
                if type(rtype) is FuncZcode:
                    self.listFunction[ast.right.name.name].typ = BoolType()
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.right.name)
                        if id is not None:
                            param[i][ast.right.name].typ = BoolType()
                            break
                return BoolType()          
            
            raise TypeMismatchInExpression(ast)
    
        if op in ['==']:
            if type(ltype) is StringType and type(rtype) is StringType:
                return BoolType()
            
            if isinstance(rtype, Zcode):
                if type(rtype) is FuncZcode:
                    self.listFunction[ast.right.name.name].typ = StringType()
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.right.name)
                        if id is not None:
                            param[i][ast.right.name].typ = StringType()
                            break
                return BoolType()
            
            raise TypeMismatchInExpression(ast)
        
        if op in ['...']:
            if type(ltype) is StringType and type(rtype) is StringType:
                return StringType()
            
            if isinstance(rtype, Zcode):
                if type(rtype) is FuncZcode:
                    self.listFunction[ast.right.name.name].typ = StringType()
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.right.name)
                        if id is not None:
                            param[i][ast.right.name].typ = StringType()
                            break
                return StringType()
            
            raise TypeMismatchInExpression(ast)
        
        # ##########################
        
        # if op in ['+', '-', '*', '/', '%']:
        #     if type(ltype) is NumberType and type(rtype) is NumberType:
        #         return NumberType()
            
        #     if isinstance(ltype, Zcode):
        #         if type(ltype) is FuncZcode:
        #             self.listFunction[ast.left.name.name].typ = NumberType()
        #         else:
        #             for i in range(len(param)):
        #                 id = param[i].get(ast.left.name)
        #                 if id is not None:
        #                     param[i][ast.left.name].typ = NumberType()
        #                     break
        #         return NumberType()
            
        #     if isinstance(rtype, Zcode):
        #         if type(rtype) is FuncZcode:
        #             self.listFunction[ast.right.name.name].typ = NumberType()
        #         else:
        #             for i in range(len(param)):
        #                 id = param[i].get(ast.right.name)
        #                 if id is not None:
        #                     param[i][ast.right.name].typ = NumberType()
        #                     break
        #         return NumberType()
            
        #     raise TypeMismatchInExpression(ast)
        
        # if op in ['=', '!=', '<', '>', '>=', '<=']:
        #     if type(ltype) is NumberType and type(rtype) is NumberType:
        #         return BoolType()
            
        #     if isinstance(ltype, Zcode):
        #         if type(ltype) is FuncZcode:
        #             self.listFunction[ast.left.name.name].typ = NumberType()
        #         else:
        #             for i in range(len(param)):
        #                 id = param[i].get(ast.left.name)
        #                 if id is not None:
        #                     param[i][ast.left.name].typ = NumberType()
        #                     break
        #         return BoolType()
            
        #     if isinstance(rtype, Zcode):
        #         if type(rtype) is FuncZcode:
        #             self.listFunction[ast.right.name.name].typ = NumberType()
        #         else:
        #             for i in range(len(param)):
        #                 id = param[i].get(ast.right.name)
        #                 if id is not None:
        #                     param[i][ast.right.name].typ = NumberType()
        #                     break
        #         return BoolType()
            
        #     raise TypeMismatchInExpression(ast)
        
        # if op in ['and', 'or']:
        #     if type(ltype) is BoolType() and type(rtype) is BoolType:
        #         return BoolType()

        #     if isinstance(ltype, Zcode):
        #         if type(ltype) is FuncZcode:
        #             self.listFunction[ast.left.name.name].typ = BoolType()
        #         else:
        #             for i in range(len(param)):
        #                 id = param[i].get(ast.left.name)
        #                 if id is not None:
        #                     param[i][ast.left.name].typ = BoolType()
        #                     break
        #         return BoolType()
            
        #     if isinstance(rtype, Zcode):
        #         if type(rtype) is FuncZcode:
        #             self.listFunction[ast.right.name.name].typ = BoolType()
        #         else:
        #             for i in range(len(param)):
        #                 id = param[i].get(ast.right.name)
        #                 if id is not None:
        #                     param[i][ast.right.name].typ = BoolType()
        #                     break
        #         return BoolType()          
            
        #     raise TypeMismatchInExpression(ast)
    
        # if op in ['==']:
        #     if type(ltype) is StringType and type(rtype) is StringType:
        #         return BoolType()
            
        #     if isinstance(ltype, Zcode):
        #         if type(ltype) is FuncZcode:
        #             self.listFunction[ast.left.name.name].typ = StringType()
        #         else:
        #             for i in range(len(param)):
        #                 id = param[i].get(ast.left.name)
        #                 if id is not None:
        #                     param[i][ast.left.name].typ = StringType()
        #                     break
        #         return BoolType()
            
        #     if isinstance(rtype, Zcode):
        #         if type(rtype) is FuncZcode:
        #             self.listFunction[ast.right.name.name].typ = StringType()
        #         else:
        #             for i in range(len(param)):
        #                 id = param[i].get(ast.right.name)
        #                 if id is not None:
        #                     param[i][ast.right.name].typ = StringType()
        #                     break
        #         return BoolType()
            
        #     raise TypeMismatchInExpression(ast)
        
        # if op in ['...']:
        #     if type(ltype) is StringType and type(rtype) is StringType:
        #         return StringType()
            
        #     if isinstance(ltype, Zcode):
        #         if type(ltype) is FuncZcode:
        #             self.listFunction[ast.left.name.name].typ = StringType()
        #         else:
        #             for i in range(len(param)):
        #                 id = param[i].get(ast.left.name)
        #                 if id is not None:
        #                     param[i][ast.left.name].typ = StringType()
        #                     break
        #         return StringType()
            
        #     if isinstance(rtype, Zcode):
        #         if type(rtype) is FuncZcode:
        #             self.listFunction[ast.right.name.name].typ = StringType()
        #         else:
        #             for i in range(len(param)):
        #                 id = param[i].get(ast.right.name)
        #                 if id is not None:
        #                     param[i][ast.right.name].typ = StringType()
        #                     break
        #         return StringType()
            
        #     raise TypeMismatchInExpression(ast)
            

    def visitUnaryOp(self, ast, param):
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí giống BinaryOp
            ^ '+', '-' -> kiểu numbertype -> return Numbertype
            ^ ['not'] -> kiểu booltype -> return booltype
        """       
        right = self.visit(ast.operand, param)
        op = ast.op
        
        if op in ['+', '-']:
            if type(right) is NumberType():
                return NumberType()

            if isinstance(right, Zcode):
                if type(right) is FuncZcode:
                    self.listFunction[ast.operand.name.name].typ = NumberType()
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.operand.name)
                        if id is not None:
                            param[i][ast.operand.name].typ = NumberType()
                            break
                return NumberType()           
            
            raise TypeMismatchInExpression(ast) 
        
        if op in ['not']:
            if type(right) is BoolType():
                return BoolType()
            
            if isinstance(right, Zcode):
                if type(right) is FuncZcode:
                    self.listFunction[ast.operand.name.name].typ = BoolType()
                else:
                    for i in range(len(param)):
                        id = param[i].get(ast.operand.name)
                        if id is not None:
                            param[i][ast.operand.name].typ = BoolType()
                            break
                return BoolType()  
            
            raise TypeMismatchInExpression(ast) 
            

    def visitArrayCell(self, ast, param):
        """
            TODO kiểm tra TypeMismatchInExpression
            ^ Phần type ast.arr phải là array type nếu không lỗi TypeMismatchInExpression
        """ 
        left = self.visit(ast.arr, param)
        if type(left) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        
        """
            # TODO kiểm tra TypeMismatchInExpression
            ^ từng phần tử trong ast.idx với LHS = NumberType(), RHS = ....
        """         
        for i in ast.idx:
            itype = self.visit(i, param)
            if isinstance(itype, Zcode):
                if type(itype) is FuncZcode:
                    self.listFunction[i.name.name].typ = NumberType()
                elif type(itype) is VarZcode:
                    for j in range(len(param)):
                        id = param[j].get(i.name)
                        if id is not None:
                            param[j][i.name].typ = NumberType()
                            
            elif type(itype) is not NumberType:
                raise TypeMismatchInExpression(ast)

       
        """
            # TODO kiểm tra TypeMismatchInExpression kiểm tra len(left.size) và len(ast.idx) 
            ^ len(left.size) < len(ast.idx) -> trả về lỗi TypeMismatchInExpression ví dụ
            number a[1,2]
            var c <- a[1,2,3]
            ^ len(left.size) = len(ast.idx) -> trả về type eleType không phải là arraytype
            number a[1,2]
            var c <- a[1,2] -> c : numbertype
            ^ len(left.size) > len(ast.idx) -> trả về arraytype cắt đi đoạn ban đầu
            number a[1,2,3]
            var c <- a[1] -> c : number c[2,3]                   
        """ 
        if len(left.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        elif len(left.size) == len(ast.idx):
            return left.eleType
        else:
            return ArrayType(left.size[1:], left.eleType)

    def visitArrayLiteral(self, ast, param):
        #* bước 1 chọn được type đã xác định kiểm trong ast.value (typ không phải là Zcode và ArrayZcode)
        typ = None
        for item in ast.value:
            checkTyp = self.visit(item, param)
            if not (isinstance(checkTyp, Zcode) or isinstance(checkTyp, ArrayZcode)):
                typ = checkTyp
                break

        #* Bước 2: xét kiểu từng phần tử
        #^ TH1 : typ is None nghĩa là trong array chỉ gồm Zcode và ArrayZcode nên return ArrayZcode
        #^ TH2 : typ in [StringType, BoolType, NumberType] duyệt qua ast.value nếu typ từng phần tử có ArrayZcode hay là comparType bị khác thì nén TypeMismatchInExpression
        """_VD_
            [1, "2"] -> lỗi TypeMismatchInExpression vì khác type trong array
            dymaic x
            [1, [x,x]] -> lỗi TypeMismatchInExpression
            [1, x] -> x = numbertype
        """
        #^ TH3 : typ in arraytype duyệt qua ast.value giống TH2 nhưng nếu ArrayType yêu cầu dùng setTypeArray để chỉnh typ 
        #^ bước 2 và 3 trả về arraytype
        if typ is None:
            eleType = []
            for val in ast.value:
                eleType += [self.visit(val, param)]
            return ArrayZcode(eleType)
        elif type(typ) in [StringType, BoolType, NumberType]: 
            for val in ast.value:
                valType = self.visit(val, param)
                if type(valType) is VarZcode:
                    for i in range(len(param)):
                        id = param[i].get(val.name)
                        if id is not None:
                            param[i][val.name].typ = typ
                            break
                elif type(valType) is FuncZcode:
                    self.listFunction[val.name.name].typ = typ
                elif type(valType) is ArrayZcode or not self.comparType(typ, valType):
                    raise TypeMismatchInExpression(ast)
            return ArrayType([len(ast.value)], typ)
        else: 
            print('//////////////////', typ)
            for val in ast.value:
                valType = self.visit(val, param)
                if type(valType) is FuncZcode:
                    self.listFunction[val.name.name].typ = typ
                elif type(valType) is VarZcode:
                    for i in range(len(param)):
                        id = param[i].get(val.name)
                        if id is not None:
                            param[i][val.name].typ = typ
                            break
                elif type(valType) is ArrayZcode:
                    if not self.setTypeArray(typ, valType, val, param):
                        raise TypeMismatchInExpression(ast)
                elif not self.comparType(typ, valType):
                    raise TypeMismatchInExpression(ast)
            return ArrayType([len(ast.value)] + typ.size, typ.eleType)
            




    """phần này sẽ là cố định do ngắn quá :(( """
    def visitBlock(self, ast, param):
        for item in ast.stmt:
            #! trường hợp gặp block
            if type(item) is Block: self.visit(item, [{}] + param)
            else: self.visit(item, param)           
    def visitContinue(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)
    def visitBreak(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)   
    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()

        
        





