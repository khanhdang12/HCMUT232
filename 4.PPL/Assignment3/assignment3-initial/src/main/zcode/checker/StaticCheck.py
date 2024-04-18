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

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    

class ArrayZcode(Type):
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

    def comparType(self, LHS, RHS):
        typ1 = type(LHS)
        typ2 = type(RHS)
        if typ1 is ArrayType and typ2 is ArrayType:
            if LHS.size != RHS.size:
                return False 
            elif type(LHS.eleType) != type(RHS.eleType):
                return False
            else:
                return True
        else:
            return typ1 is typ2
            
    def comparListType(self, LHS, RHS):
        if len(LHS) != len(RHS):
            return False 
        
        for i in range(0, len(LHS)):
            if not self.comparType(LHS[i], RHS[i]):
                return False 
        return True 
        
    
    def setTypeArray(self, typeArray, typeArrayZcode, arrliteral, param):
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False 
        
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
        for i in ast.decl: self.visit(i, param)
        
        # print("AAAAAAAAAAAAAAAAA", param)

        for key, value in self.listFunction.items():
            if value.body == False:
                raise NoDefinition(key)
     
        if 'main' not in self.listFunction:
            raise NoEntryPoint()
        elif self.listFunction['main'].param != [] or type(self.listFunction['main'].typ) != VoidType: 
            raise NoEntryPoint()

    def visitVarDecl(self, ast, param):
        name = ast.name.name
        if name in param[0]:
            raise Redeclared(Variable(), name)

        param[0][name] = VarZcode(ast.varType) 

        if ast.varInit:    
            expType = self.visit(ast.varInit, param)
            if ast.modifier == 'var' or ast.modifier == 'dynamic':
                if isinstance(expType, Zcode) or type(expType) is ArrayZcode:
                    raise TypeCannotBeInferred(ast)
                param[0][name].typ = expType
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
        # print("Visiting FuncDecl")
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
            # print(listParam)
            
        self.Return = False
        if ast.body is None: 
            # print("Without body")
            self.listFunction[name] = FuncZcode(typeParam, None, False)
        
        elif method: 
            # print("Lan 2: khai bao body")
            if not self.comparListType(typeParam, method.param):
                raise Redeclared(Function(), name)
            self.listFunction[name].body = True
            self.Return = False
            self.function = self.listFunction[name]
            
            self.visit(ast.body, [listParam] + param)

            if not self.Return:
                if self.function.typ is None: 
                    self.function.typ = VoidType()
                    self.listFunction[name].typ = VoidType()                  
                elif type(self.function.typ) is not VoidType:
                    raise TypeMismatchInStatement(Return())
        else:
            # print("Khai bao ham lan dau, co body")
            self.listFunction[name] = FuncZcode(typeParam, None, True)
            self.Return = False
            self.function = self.listFunction[name]
            
            self.visit(ast.body, [listParam] + param)
            
            if not self.Return:
                if self.function.typ is None: 
                    self.function.typ = VoidType()
                    self.listFunction[name].typ = VoidType()
                elif type(self.function.typ) is not VoidType:
                    raise TypeMismatchInStatement(Return())
                

    def visitId(self, ast, param):
        for env in param:
            id = env.get(ast.name)
            if id is not None:
                return id.typ if id.typ else VarZcode()
        
        raise Undeclared(Identifier(), ast.name)
                

    def visitCallExpr(self, ast, param):
        name = ast.name.name
        method = self.listFunction.get(name)
    
        if not method:
            raise Undeclared(Function(), name)
        
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
                    self.listFunction[name].param[i] = rtype
                    
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
        name = ast.name.name
        method = self.listFunction.get(name)
    
        if not method:
            raise Undeclared(Function(), name)
        
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
                    self.listFunction[name].param[i] = rtype
                    
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
                    
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, [{}] + param)
        
    def visitFor(self, ast, param):      
        typId = self.visit(ast.name, param)
        if type(typId) is VarZcode:
            for i in range(len(param)):
                id = param[i].get(ast.name.name)
                if id is not None:
                    param[i][ast.name.name].typ = NumberType()
                    break
        elif type(typId) is not NumberType:
            raise TypeMismatchInStatement(ast)
         
        typCondExpr = self.visit(ast.condExpr, param)
        if type(typCondExpr) is VarZcode:
            for i in range(len(param)):
                id = param[i].get(ast.condExpr.name)
                if id is not None:
                    param[i][ast.condExpr.name].typ = BoolType()
                    break
        elif type(typCondExpr) is not BoolType:
            raise TypeMismatchInStatement(ast)
                
        typUpdExpr = self.visit(ast.updExpr, param)
        if type(typUpdExpr) is VarZcode:
            for i in range(len(param)):
                id = param[i].get(ast.updExpr.name)
                if id is not None:
                    param[i][ast.updExpr.name].typ = NumberType()
                    break
        elif type(typUpdExpr) is not NumberType:
            raise TypeMismatchInStatement(ast)       
        
        
        self.BlockFor += 1 
        self.visit(ast.body, [{}] + param) 
        self.BlockFor -= 1 
    
    def visitReturn(self, ast, param):
        self.Return = True
        LHS = self.function.typ if self.function.typ else self.function
        RHS = self.visit(ast.expr, param) if ast.expr else VoidType()
        
        # print(type(LHS) is FuncZcode)
        # print(isinstance(RHS, Zcode))
        
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
                    else: 
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
        op = ast.op      
        
        ltype = self.visit(ast.left, param)

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

        rtype = self.visit(ast.right, param)
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

    def visitUnaryOp(self, ast, param):      
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
        left = self.visit(ast.arr, param)
        if type(left) is not ArrayType:
            raise TypeMismatchInExpression(ast)
               
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

        if len(left.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        elif len(left.size) == len(ast.idx):
            return left.eleType
        else:
            return ArrayType(left.size[1:], left.eleType)

    def visitArrayLiteral(self, ast, param):
        typ = None
        for item in ast.value:
            checkTyp = self.visit(item, param)
            if not (isinstance(checkTyp, Zcode) or isinstance(checkTyp, ArrayZcode)):
                typ = checkTyp
                break

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
            # print('//////////////////', typ)
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
            
    def visitBlock(self, ast, param):
        for item in ast.stmt:
            if type(item) is Block: 
                self.visit(item, [{}] + param)
            else: 
                self.visit(item, param)  

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