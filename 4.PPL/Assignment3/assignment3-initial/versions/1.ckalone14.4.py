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
    #* typ : Type có thể là number, bool, string, arrayType or None (có thể hiểu nhanh đang FuncZcode)
        #! -> nên khi gọi callFunc thì trả về typ nếu có (khác None) không thì trả về chính nó this (VarZcode)    
    def __init__(self, typ = None):
        self.typ = typ    

class ArrayZcode(Type):
    #* eleType: List[Type]
    #* Type ở đây có thể là Zcode, ArrayZcode, String, bool, number, arraytype
    def __init__(self, eleType):
        self.eleType = eleType

class StaticChecker(BaseVisitor, Utils):
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
        typ1 = type(LHS)
        typ2 = type(RHS)
        if typ1 is ArrayType() and typ2 is ArrayType():
            if LHS.size != RHS.size:
                return False 
            #^ xét từng phần tử trong size của 2 thằng nếu không giống nhau trả Flase
            elif type(LHS.eleType) != type(RHS.eleType):
                return False
        else:
            return typ1 is typ2
      

        """_comparListType
        #* LHS và RHS chỉ có thể list các type sau Void, number, string, bool, arrayType
        #* TH1 nếu LHS và RHS khác kích thước -> Flase
        #* duyệt từng phần tử gọi self.comparType(LHS[i], RHS[i])
    """    
    def comparListType(self, LHS, RHS):
        #TODO implement
        if len(LHS) != len(RHS):
            return False 
        
        for i in range(0, len(LHS)):
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
    # ----------------------------------------------------------------

    def visitProgram(self, ast, param):
        #* duyệt qua các biến và hàm toàn cục
        for i in ast.decl: self.visit(i, param)
        
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
        for key, value in self.listFunction.items():
            if value.body == False:
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
        cond1 = 'main' not in self.listFunction
        # print('cond1: ', cond1)
        if cond1:
            raise NoEntryPoint()
        cond2 = self.listFunction['main'].param != []
        cond3 = self.listFunction['main'].typ != VoidType()
        # print('cond2: ', cond2)
        # print('cond3: ', cond3)

        if cond2 or cond3:
            raise NoEntryPoint()
            
    # ----------------------------------------------------------------

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
        name = ast.name.name
        if name in param[0]:
            raise Redeclared(Variable(), name)

        param[0][name] = VarZcode(ast.varType) #! cập nhật param mới đưa tên vào, biến dynamic hay var sẽ type = None

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
            name = self.visit(ast.name, param)
            init = self.visit(ast.varInit, param)
            if type(name) is Zcode() and type(init) is Zcode():
                raise TypeCannotBeInferred(ast)
            elif type(name) is Zcode() and type(init) is ArrayZcode():
                raise TypeCannotBeInferred(ast)
            elif type(name) is not Zcode() and type(init) is ArrayZcode():
                if type(name) in [StringType(), BoolType(), NumberType()]:
                    raise TypeMismatchInStatement(ast)
                elif type(name) is ArrayType():
                    # if self.setTypeArray(LHS, RHS)
                    pass
            elif type(name) is Zcode() and type(init) in [StringType(), BoolType(), NumberType()]:
                param[0][name] = VarZcode(type(init))
            # elif type(name) in [StringType(), BoolType(), NumberType()] and type(init) is Zcode() :
            elif not self.comparType(name, init):
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
        method = self.listFunction.get(ast.name.name)

        #TODO implement
        name = ast.name.name
        if name in param[0]:
            raise Redeclared(Function(), name)   
        
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
        for decl in ast.param:
            self.visit(decl, [listParam] + param)
            typeParam.append(decl.varType)
        
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
            #todo: implement TH1
            self.listFunction[name] = FuncZcode([], None, False)

        if method:
            #todo: implement TH2
            if listParam != self.listFunction[name].param:
                raise Redeclared(Function(), name)
        else:
            pass
            #todo: implement TH3
            
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
        #TODO implement
        flag = False
        name = ast.name
        for env in param:
            if name in env:
                typ = env[name].typ
                flag = True 
        if flag == False:
            raise Undeclared(Identifier(), name) 
        if typ == None:
            return VarZcode()
        return VarZcode.typ

    # ----------------------------------------------------------------

    def visitBlock(self, ast, param):
        for item in ast.stmt:
            if type(item) is Block: 
                self.visit(item, [{}] + param)
            else: 
                self.visit(item, param)   

    def visitContinue(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)  

    def visitNumberType(self, ast, param): 
        return ast
    
    def visitBoolType(self, ast, param): 
        return ast
    
    def visitStringType(self, ast, param): 
        return ast
    
    def visitArrayType(self, ast, param): 
        return ast
    
    def visitNumberLiteral(self, ast, param): 
        return NumberType()
    
    def visitBooleanLiteral(self, ast, param): 
        return BoolType()
    
    def visitStringLiteral(self, ast, param): 
        return StringType()