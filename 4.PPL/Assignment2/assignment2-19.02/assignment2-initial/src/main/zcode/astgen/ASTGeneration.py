from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):

    # program: NEWLINE* list_declared EOF; 
    def visitProgram(self,ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.list_declared()))
    
    # list_declared: declared list_declared | declared;
    def visitList_declared(self, ctx:ZCodeParser.List_declaredContext):
        if ctx.list_declared():
            return [self.visit(ctx.declared())] + self.visit(ctx.list_declared())
        return [self.visit(ctx.declared())]

    # declared: function | variables ignore;
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        if ctx.function():
            return self.visit(ctx.function())
        return self.visit(ctx.variables())

    # variables: implicit_var | keyword_var | implicit_dynamic;
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        if ctx.implicit_var():
            return self.visit(ctx.implicit_var())
        elif ctx.keyword_var():
            return self.visit(ctx.keyword_var())
        return self.visit(ctx.implicit_dynamic())

    # keyword_var: typ ID (LSB dimenslist RSB)? decl?;
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):
        id = ctx.ID().getText()
        typ = self.visit(ctx.typ())
        modifier = None
        if ctx.decl():
            varinit = self.visit(ctx.decl())
        else:   
            varinit = None
        if ctx.dimenslist():
            dimen_list = self.visit(ctx.dimenslist())
            varType = ArrayType(dimen_list, typ)
            return VarDecl(name = Id(id), varType = varType, modifier = modifier, varInit = varinit)
        else: 
            return VarDecl(name = Id(id), varType = typ, modifier = modifier, varInit = varinit)

    # implicit_var: VAR ID decl;
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        id = ctx.ID().getText()
        varinit = self.visit(ctx.decl())
        return VarDecl(name = Id(id), varType = None, modifier = "var", varInit = varinit)

    # implicit_dynamic: DYNAMIC ID decl?;
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        id = ctx.ID().getText()
        if ctx.decl():
            varinit = self.visit(ctx.decl())
        else:   
            varinit = None
        return VarDecl(name = Id(id), varType = None, modifier = "dynamic", varInit = varinit)

    # decl: ASSIGNINIT expression;
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visit(ctx.expression())

    # dimenslist: NUMBER_LIT CM dimenslist | NUMBER_LIT;
    def visitDimenslist(self, ctx:ZCodeParser.DimenslistContext):
        if ctx.getChildCount() == 1:
            return [float(ctx.NUMBER_LIT().getText())]
        else:
            return [float(ctx.NUMBER_LIT().getText())] + self.visit(ctx.dimenslist())
            
    """
        function:
	FUNC ID LB parameters_list? RB (
		ignore? return_statement
		| ignore? block_statement
		| ignore
	);
    """
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        id = ctx.ID().getText()
        if ctx.parameters_list():
            param_list = self.visit(ctx.parameters_list())
        else:
            param_list = []
        if ctx.return_statement():
            return_stmt = self.visit(ctx.return_statement())
            return FuncDecl(Id(id), param_list, return_stmt)
        elif ctx.block_statement():
            block_stmt = self.visit(ctx.block_statement())
            return FuncDecl(Id(id), param_list, block_stmt)
        else:
            return FuncDecl(Id(id), param_list, None)

    # parameters_list: parameter CM parameters_list | parameter;
    def visitParameters_list(self, ctx:ZCodeParser.Parameters_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.getChild(0))]
        else:
            return [self.visit(ctx.parameter())] + self.visit(ctx.parameters_list())
    
    # parameter: typ ID (LSB dimenslist RSB)?;
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        typ = self.visit(ctx.typ())
        id = ctx.ID().getText()
        if ctx.getChildCount() == 2:
            return VarDecl(name = Id(id), varType = typ, modifier = None, varInit = None)
        else:
            dimen_list = self.visit(ctx.dimenslist())
            varType = ArrayType(dimen_list, typ)
            return VarDecl(name = Id(id), varType = varType, modifier = None, varInit = None)

    # list_expr: expression CM list_expr | expression;
    def visitList_expr(self, ctx:ZCodeParser.List_exprContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        else:
            return [self.visit(ctx.expression())] + self.visit(ctx.list_expr())

    # list_expr: expression CM list_expr | expression;
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            op = ctx.CONCAT().getText()
            left = self.visit(ctx.expression1(0))
            right = self.visit(ctx.expression1(1))
            return BinaryOp(op, left, right)

    # expression1: expression2 relational expression2 | expression2;
    def visitExpression1(self, ctx:ZCodeParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else: 
            op = self.visit(ctx.relational())
            left = self.visit(ctx.expression2(0))
            right = self.visit(ctx.expression2(1))
            return BinaryOp(op, left, right)

    # expression2: expression2 logical expresisson3 | expresisson3;
    def visitExpression2(self, ctx:ZCodeParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else: 
            op = self.visit(ctx.logical())
            left = self.visit(ctx.expression2())
            right = self.visit(ctx.expresisson3())
            return BinaryOp(op, left, right)

    # expresisson3: expresisson3 adding expression4 | expression4;
    def visitExpresisson3(self, ctx:ZCodeParser.Expresisson3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else: 
            op = self.visit(ctx.adding())
            left = self.visit(ctx.expresisson3())
            right = self.visit(ctx.expression4())
            return BinaryOp(op, left, right)

    # expression4: expression4 multiplying expression5 | expression5;
    def visitExpression4(self, ctx:ZCodeParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else: 
            op = self.visit(ctx.multiplying())
            left = self.visit(ctx.expression4())
            right = self.visit(ctx.expression5())
            return BinaryOp(op, left, right)

    # expression5: NOT expression5 | expression6;
    def visitExpression5(self, ctx:ZCodeParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else: 
            op = ctx.NOT().getText()
            operand = self.visit(ctx.expression5())
            return UnaryOp(op, operand)

    # expression6: (SUB | ADD) expression6 | expression7;
    def visitExpression6(self, ctx:ZCodeParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else: 
            if ctx.SUB():
                op = ctx.SUB().getText()
            else:
                op = ctx.ADD().getText()
            operand = self.visit(ctx.expression6())
            return UnaryOp(op, operand)
        
    # expression7: subexpr | arrayele | funccall | ID | literal;
    def visitExpression7(self, ctx:ZCodeParser.Expression7Context):
        if ctx.subexpr():
            return self.visit(ctx.subexpr())
        elif ctx.arrayele():
            return self.visit(ctx.arrayele())
        elif ctx.funccall():
            return self.visit(ctx.funccall())
        elif ctx.literal():
            return self.visit(ctx.literal())
        else:
            return Id(ctx.ID().getText())

    # relational: EQ | SAME | DIF | LT | GT | LTE | GTE;
    def visitRelational(self, ctx:ZCodeParser.RelationalContext):
        if ctx.EQ():
            return ctx.EQ().getText()
        elif ctx.SAME():
            return ctx.SAME().getText()
        elif ctx.DIF():
            return ctx.DIF().getText()
        elif ctx.LT():
            return ctx.LT().getText()
        elif ctx.GT():
            return ctx.GT().getText()
        elif ctx.LTE():
            return ctx.LTE().getText()
        else:
            return ctx.GTE().getText()

    # logical: AND | OR;
    def visitLogical(self, ctx:ZCodeParser.LogicalContext):
        if ctx.AND():
            return ctx.AND().getText()
        else:
            return ctx.OR().getText()

    # adding: ADD | SUB;
    def visitAdding(self, ctx:ZCodeParser.AddingContext):
        if ctx.ADD():
            return ctx.ADD().getText()
        else:
            return ctx.SUB().getText()

    # multiplying: MUL | DIV | MOD;
    def visitMultiplying(self, ctx:ZCodeParser.MultiplyingContext):
        if ctx.MUL():
            return ctx.MUL().getText()
        elif ctx.DIV():
            return ctx.DIV().getText()
        else:
            return ctx.MOD().getText()   

    # subexpr: LB expression RB;
    def visitSubexpr(self, ctx:ZCodeParser.SubexprContext):
        return self.visit(ctx.expression())

    # arrayele: (ID | funccall) LSB list_expr RSB;
    def visitArrayele(self, ctx:ZCodeParser.ArrayeleContext):
        if ctx.ID():
            arr = Id(ctx.ID().getText())
        elif ctx.funccall():
            arr = self.visit(ctx.funccall())
        idx = self.visit(ctx.list_expr())
        return ArrayCell(arr, idx)

    # funccall: ID LB list_expr? RB;
    def visitFunccall(self, ctx:ZCodeParser.FunccallContext):
        id = ctx.ID().getText()
        if ctx.list_expr():
            args = self.visit(ctx.list_expr())
            return CallExpr(Id(id), args)
        else:
            return CallExpr(Id(id), [])

    # array_lit: LSB list_expr RSB;
    def visitArray_lit(self, ctx:ZCodeParser.Array_litContext):
        value = self.visit(ctx.list_expr())
        return ArrayLiteral(value)

    # literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_lit;
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        if ctx.NUMBER_LIT():
            return NumberLiteral(float(ctx.NUMBER_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        else:
            return self.visit(ctx.array_lit())

    # typ: NUMBER | BOOL | STRING;
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        else: 
            return StringType()

    # statement_list: statement statement_list |;
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return [self.visit(ctx.statement())] + self.visit(ctx.statement_list())

    """statement:
          declaration_statement
        | assignment_statement
        | if_statement
        | for_statement
        | break_statement
        | continue_statement
        | return_statement
        | call_statement
        | block_statement;
    """    
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        if ctx.declaration_statement():
            return self.visit(ctx.declaration_statement())
        elif ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.call_statement():
            return self.visit(ctx.call_statement())
        else: 
            return self.visit(ctx.block_statement())

    # declaration_statement: variables ignore;
    def visitDeclaration_statement(self, ctx:ZCodeParser.Declaration_statementContext):
        return self.visit(ctx.variables())

    # assignment_statement: lhs ASSIGNINIT expression ignore;
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.expression())
        return Assign(lhs, exp)

    # lhs: ID (LSB list_expr RSB)?;
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        if ctx.getChildCount() == 1:
            arr = Id(ctx.ID().getText())
            return arr
        else:
            arr = Id(ctx.ID().getText())
            args = self.visit(ctx.list_expr())
            return ArrayCell(arr, args)

    # return_statement: RETURN (expression | ) ignore;
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        if ctx.expression():
            expr = self.visit(ctx.expression())
            return Return(expr)
        else:
            return Return(None)

    # block_statement: BEGIN ignore statement_list END ignore;
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        stmt = self.visit(ctx.statement_list())
        return Block(stmt)

    # # if_statement: IF LB expression RB ignore? statement list_elif? else_stmt?;
    # def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
    #     expr = self.visit(ctx.expression())
    #     thenStmt = self.visit(ctx.statement())
    #     if ctx.list_elif():
    #         elifStmt = self.visit(ctx.list_elif())
    #     else:
    #         elifStmt = []
    #     if ctx.else_stmt():
    #         elseStmt = self.visit(ctx.else_stmt())
    #     else:
    #         elseStmt = None
    #     return If(expr, thenStmt, elifStmt, elseStmt)

    # # list_elif: elseif_stmt list_elif | elseif_stmt;
    # def visitList_elif(self, ctx:ZCodeParser.List_elifContext):
    #     if ctx.getChildCount() == 1:
    #         return [self.visit(ctx.elseif_stmt())]
    #     else:
    #         return [self.visit(ctx.elseif_stmt())] + self.visit(ctx.list_elif())

    # # else_stmt: ELSE ignore? statement;
    # def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
    #     return self.visit(ctx.statement())

    # # elseif_stmt: ELIF LB expression RB ignore? statement;
    # def visitElseif_stmt(self, ctx:ZCodeParser.Elseif_stmtContext):
    #     expr = self.visit(ctx.expression())
    #     stmt = self.visit(ctx.statement())
    #     return [expr, stmt]

    # if_statement: IF LB expression RB ignore? statement list_elif;
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        exp = self.visit(ctx.expression())
        stmt = self.visit(ctx.statement())
        list_elif, else_stmt = self.visit(ctx.list_elif())
        return If(exp, stmt, list_elif, else_stmt)

    # list_elif: elseif_stmt list_elif | else_stmt;
    def visitList_elif(self, ctx:ZCodeParser.List_elifContext):
        if ctx.else_stmt():
            return [], self.visit(ctx.else_stmt())
        elif_stmt = self.visit(ctx.elseif_stmt())
        tail_list_elif, else_stmt = self.visit(ctx.list_elif())
        return [elif_stmt] + tail_list_elif, else_stmt
            
    # else_stmt: ELSE ignore? statement |;
    def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
        if ctx.statement():
            return self.visit(ctx.statement())
        return None

    # elseif_stmt: ELIF LB expression RB ignore? statement;
    def visitElseif_stmt(self, ctx:ZCodeParser.Elseif_stmtContext):
        expr = self.visit(ctx.expression())
        stmt = self.visit(ctx.statement())
        return [expr, stmt]

    # for_statement: FOR ID UNTIL expression BY expression ignore? statement;
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        id = ctx.ID().getText()
        condExpr = self.visit(ctx.expression(0))
        updpExpr = self.visit(ctx.expression(1))
        stmt = self.visit(ctx.statement())
        return For(Id(id), condExpr, updpExpr, stmt)

    # break_statement: BREAK ignore;
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return Break()

    # continue_statement: CONTINUE ignore;
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return Continue()

    # call_statement: ID LB list_expr? RB ignore;
    def visitCall_statement(self, ctx:ZCodeParser.Call_statementContext):
        id = ctx.ID().getText()
        if ctx.list_expr():
            args = self.visit(ctx.list_expr())
        else:   
            args = []
        return CallStmt(Id(id), args)

    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext): 
        return None

