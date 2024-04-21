# 2053105
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode(Type):
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body
    def __str__(self):
        return f"FuncZcode(param=[{', '.join(str(i) for i in self.param)}],typ={str(self.typ)},body={self.body})"

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    
    def __str__(self):
        return f"VarZcode(type={self.typ})"

class ArrayZcode(Type):
    def __init__(self, eleType):
        self.eleType = eleType
    def __str__(self):
        return f"ArrayZcode(eleType=[{', '.join(str(i) for i in self.eleType)}])"
    
class CannotBeInferredZcode(Type):
    def __str__(self):
        return "CannotBeInferredZcode()"

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
    
    def print(self):
        print(f"BlockFor {self.BlockFor}")
        print(f"function {str(self.function)}")
        print(f"Return {self.Return}")
        print(f"listFunction :")
        for key, value in self.listFunction.items():
            print(f"    {key}  {str(value)}")       
    
    def check(self):
        self.visit(self.ast, [{}])
        return None

    def LHS_RHS_stmt(self, LHS : Type, RHS : Type, ast, param):
        if type(LHS) is CannotBeInferredZcode or type(RHS) is CannotBeInferredZcode:
            raise TypeCannotBeInferred(ast)
        
        elif isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            raise TypeCannotBeInferred(ast)
    
        elif isinstance(LHS, Zcode) and type(RHS) is ArrayZcode:
            raise TypeCannotBeInferred(ast)
        
        elif type(LHS) is ArrayType and type(RHS) is ArrayZcode:
            if not self.setTypeArray(LHS, RHS):
                raise TypeMismatchInStatement(ast) 

        elif type(RHS) is ArrayZcode:
            raise TypeCannotBeInferred(ast)
            
        elif isinstance(LHS, Zcode):
            LHS.typ = RHS   
        
        elif isinstance(RHS, Zcode):
            RHS.typ = LHS

        elif not self.comparType(LHS, RHS):
            raise TypeMismatchInStatement(ast)

    def LHS_RHS_expr(self, LHS : Type, RHS : Type, ast, param) -> bool:
        if type(LHS) is CannotBeInferredZcode or type(RHS) is CannotBeInferredZcode:
            return True
        
        elif isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
           return True

        elif isinstance(LHS, Zcode) and type(RHS) is ArrayZcode:
            return True
        
        elif type(LHS) is ArrayType and type(RHS) is ArrayZcode:
            if not self.setTypeArray(LHS, RHS):
                raise TypeMismatchInExpression(ast)
            
        elif type(RHS) is ArrayZcode:
            return True
        
        elif isinstance(LHS, Zcode):
            LHS.typ = RHS   
        
        elif isinstance(RHS, Zcode):
            RHS.typ = LHS

        elif not self.comparType(LHS, RHS):
            raise TypeMismatchInExpression(ast)

        return False

    def comparType(self, LHS : Type, RHS : Type) -> bool:
        if type(LHS) is ArrayType and type(RHS) is ArrayType:
            return LHS.size == RHS.size and type(LHS.eleType) is type(RHS.eleType)
        
        return type(LHS) is type(RHS)
  
    def comparListType(self, LHS, RHS):
        if len(LHS) != len(RHS):
            return False
        
        for i in range(len(LHS)):
            if not self.comparType(LHS[i], RHS[i]):
                return False
            
        return True
    
    def setTypeArray(self, typeArray, typeArrayZcode):
        
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False 

        if len(typeArray.size) == 1:
            
            for i in range(len(typeArrayZcode.eleType)):
                if isinstance(typeArrayZcode.eleType[i], Zcode):
                    typeArrayZcode.eleType[i].typ = typeArray.eleType
                    
                elif type(typeArrayZcode.eleType[i]) is ArrayZcode:
                    return False
            
        else:
            for i in range(len(typeArrayZcode.eleType)):
                if isinstance(typeArrayZcode.eleType[i], Zcode):
                    typeArrayZcode.eleType[i].typ = ArrayType(typeArray.size[1:], typeArray.eleType)
                elif type(typeArrayZcode.eleType[i]) is ArrayZcode:
                    self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType), typeArrayZcode.eleType[i])

        return True

    def visitProgram(self, ast, param):
        for i in ast.decl: self.visit(i, param)
        
        for key, val in self.listFunction.items():
            if not val.body:
                raise NoDefinition(key)
        
        main = self.listFunction.get("main")
        if not main:
            raise NoEntryPoint()
        elif main.param or type(main.typ) is not VoidType: 
            raise NoEntryPoint()
        
    def visitVarDecl(self, ast, param):
        name = ast.name.name
        if param[0].get(name):
            raise Redeclared(Variable(), name)
        
        if param[0].get(name): raise Redeclared(Variable(), name)
        
        param[0][name] = VarZcode(ast.varType)
        
        if ast.varInit:
            LHS = param[0][name].typ if param[0][name].typ else param[0][name]
            RHS = self.visit(ast.varInit, param)
            self.LHS_RHS_stmt(LHS, RHS , ast, param)

    def visitFuncDecl(self, ast, param):
        name = ast.name.name
        method = self.listFunction.get(name)
        if method and (method.body or (not method.body and not ast.body)):
            raise Redeclared(Function(), name)

        listParam = {} 
        typeParam = []
        for param_decl in ast.param:
            if listParam.get(param_decl.name.name) is not None:
                raise Redeclared(Parameter(), param_decl.name.name)
            
            listParam[param_decl.name.name] = VarZcode(param_decl.varType)
            typeParam.append(param_decl.varType)

        if ast.body is None:
            self.listFunction[name] = FuncZcode(typeParam, None, False)
            return

        elif method:
            if not self.comparListType(typeParam, method.param):
                raise Redeclared(Function(), name)

            self.listFunction[name].body = True
            self.Return = False
            self.function = self.listFunction[name]
            self.visit(ast.body, [listParam] + param)

        else:
            self.listFunction[name] = FuncZcode(typeParam, None, True)

            self.Return = False
            self.function = self.listFunction[name] 
            self.visit(ast.body, [listParam] + param)

        if not self.Return:
            if self.function.typ is None: 
                self.function.typ = VoidType()
                self.listFunction[name].typ = VoidType()
            elif not isinstance(self.listFunction[name].typ, VoidType):
                raise TypeMismatchInStatement(Return())
 
    def visitId(self, ast, param):
        name = ast.name
        for env in param:
            id = env.get(name)
            if id is not None:
                return id.typ if id.typ else id
        
        raise Undeclared(Identifier(), name)

    def visitCallExpr(self, ast, param):
        name = ast.name.name
        method = self.listFunction.get(name)
        if not method:
            raise Undeclared(Function(), name)
        
        listLHS = method.param
        listRHS = ast.args   
        if len(listLHS) != len(listRHS):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(method.param)):
            LHS = self.visit(listLHS[i], param)
            RHS = self.visit(ast.args[i], param)
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS , ast, param)
            if cannotBeInferred: 
                return CannotBeInferredZcode()
        
        if method.typ is None:
            return method
        elif self.comparType(method.typ, VoidType()):
            raise TypeMismatchInExpression(ast)
        return method.typ

    def visitCallStmt(self, ast, param):
        name = ast.name.name
        method = self.listFunction.get(name)
        method = self.listFunction.get(name)
        if not method:
            raise Undeclared(Function(), name)
        
        listLHS = method.param
        listRHS = ast.args
        if len(listLHS) != len(listRHS):
            raise TypeMismatchInStatement(ast)
        
        for i in range(len(method.param)):
            LHS = self.visit(listLHS[i], param)
            RHS = self.visit(ast.args[i], param)
            self.LHS_RHS_stmt(LHS, RHS , ast, param)
    
        if method.typ is None:
            method.typ = VoidType()
        elif not self.comparType(method.typ, VoidType()):
            raise TypeMismatchInStatement(ast)
        return method.typ

    def visitIf(self, ast, param):
        LHS = self.visit(ast.expr, param)
        RHS = BoolType()
        self.LHS_RHS_stmt(LHS, RHS , ast, param)

        self.visit(ast.thenStmt, param)    
        
        for item in ast.elifStmt:
            LHS = self.visit(item[0], param)
            RHS = BoolType()
            self.LHS_RHS_stmt(LHS, RHS , ast, param)

            self.visit(item[1], param)           
       
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, param)
        
    def visitFor(self, ast, param):      
        LHS = self.visit(ast.name, param)
        RHS = NumberType()
        self.LHS_RHS_stmt(LHS, RHS , ast, param)

        LHS = self.visit(ast.condExpr, param)
        RHS = BoolType()
        self.LHS_RHS_stmt(LHS, RHS , ast, param) 

        LHS = self.visit(ast.updExpr, param)
        RHS = NumberType()
        self.LHS_RHS_stmt(LHS, RHS , ast, param) 
        
        self.BlockFor += 1 
        self.visit(ast.body, param)
        self.BlockFor -= 1 
    
    def visitReturn(self, ast, param):
        self.Return = True
        LHS = self.function.typ if self.function.typ else self.function
        RHS = self.visit(ast.expr, param) if ast.expr else VoidType()
        self.LHS_RHS_stmt(LHS, RHS , ast, param) 

    def visitAssign(self, ast, param):
        LHS = self.visit(ast.lhs, param)
        RHS = self.visit(ast.rhs, param)
        self.LHS_RHS_stmt(LHS, RHS , ast, param) 
            
    def visitBinaryOp(self, ast, param):
        op = ast.op
        LHS1 = self.visit(ast.left, param)

        if op in ['+', '-', '*', '/', '%']:
            RHS1 = NumberType()

        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            RHS1 = NumberType()

        elif op in ['and', 'or']:
            RHS1 = BoolType()

        elif op in ['==']:
            RHS1 = StringType()

        elif op in ['...']:
            RHS1 = StringType()
        
        cannotBeInferred = self.LHS_RHS_expr(LHS1, RHS1 , ast, param)
        if cannotBeInferred: return CannotBeInferredZcode()
          
        RHS2 = self.visit(ast.right, param)
        if op in ['+', '-', '*', '/', '%']:
            LHS2 = NumberType()
            cannotBeInferred = self.LHS_RHS_expr(LHS2, RHS2 , ast, param)
            if cannotBeInferred: return CannotBeInferredZcode()
            return NumberType()

        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            LHS2 = NumberType()
            cannotBeInferred = self.LHS_RHS_expr(LHS2, RHS2 , ast, param)
            if cannotBeInferred: return CannotBeInferredZcode()
            return BoolType()

        elif op in ['and', 'or']:
            LHS2 = BoolType()
            cannotBeInferred = self.LHS_RHS_expr(LHS2, RHS2 , ast, param)
            if cannotBeInferred: return CannotBeInferredZcode()
            return BoolType()

        elif op in ['==']:
            LHS2 = StringType()
            cannotBeInferred = self.LHS_RHS_expr(LHS2, RHS2 , ast, param)
            if cannotBeInferred: return CannotBeInferredZcode()
            return BoolType()

        elif op in ['...']:
            LHS2 = StringType()
            cannotBeInferred = self.LHS_RHS_expr(LHS2, RHS2 , ast, param)
            if cannotBeInferred: return CannotBeInferredZcode()
            return StringType()

    def visitUnaryOp(self, ast, param):
        op = ast.op
        LHS = self.visit(ast.operand, param)
        if op in ['+', '-']:
            RHS = NumberType()
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS , ast, param)
            if cannotBeInferred: return CannotBeInferredZcode()
            return NumberType()
            
        if op in ['not']:
            RHS = BoolType()
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS , ast, param)
            if cannotBeInferred: return CannotBeInferredZcode()
            return BoolType()
            
    def visitArrayCell(self, ast, param):
        arr = self.visit(ast.arr, param)
        if isinstance(arr, (BoolType, StringType, NumberType)):
            raise TypeMismatchInExpression(ast)
        elif not isinstance(arr, ArrayType):
            return CannotBeInferredZcode()

        for item in ast.idx:
            LHS = NumberType()
            RHS = self.visit(item, param) 
            if self.LHS_RHS_expr(LHS, RHS , ast, param): return CannotBeInferredZcode()
            
        if len(arr.size) < len(ast.idx): raise TypeMismatchInExpression(ast)
        elif len(arr.size) == len(ast.idx): return arr.eleType
        return ArrayType(arr.size[len(ast.idx):], arr.eleType)   

    def visitArrayLiteral(self, ast, param):
        mainTyp = None
        for item in ast.value:
            checkTyp = self.visit(item, param)
            if mainTyp is None and isinstance(checkTyp, (BoolType, StringType, NumberType, ArrayType)):
                mainTyp = checkTyp
                break
            elif isinstance(checkTyp, CannotBeInferredZcode):
                return CannotBeInferredZcode()
        
        if mainTyp is None:
            eleType = [self.visit(val, param) for val in ast.value]
            return ArrayZcode(eleType)

        elif type(mainTyp) in [BoolType, StringType, NumberType]:
            for item in ast.value:
                LHS = mainTyp 
                RHS = self.visit(item, param)
                if self.LHS_RHS_expr(LHS, RHS , ast, param): 
                    return CannotBeInferredZcode()
            return ArrayType([len(ast.value)], mainTyp)
        
        else:
            for item in ast.value:
                LHS = self.visit(item, param)
                RHS = mainTyp
                if type(LHS) is ArrayZcode:
                    if not self.setTypeArray(mainTyp, LHS):
                        raise TypeMismatchInExpression(ast)
                elif self.LHS_RHS_expr(LHS, RHS , ast, param): 
                    return CannotBeInferredZcode()
            return ArrayType([float(len(ast.value))] + mainTyp.size, mainTyp.eleType)
            
    def visitBlock(self, ast, param):
        paramNew = [{}] + param 
        for item in ast.stmt: 
            self.visit(item,paramNew)   

    def visitContinue(self, ast, param):
        if self.BlockFor == 0: 
            raise MustInLoop(ast)
        
    def visitBreak(self, ast, param):
        if self.BlockFor == 0: 
            raise MustInLoop(ast)   
        
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