# ID:2053105
from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.declarationList()))

    def visitDeclarationList(self, ctx: MT22Parser.DeclarationListContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.declaration())
        return self.visit(ctx.declaration()) + self.visit(ctx.declarationList())

    def visitDeclaration(self, ctx: MT22Parser.DeclarationContext):
        if ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())
        return self.visit(ctx.functionDeclaration())

    def visitVariableDeclaration(self, ctx: MT22Parser.VariableDeclarationContext):
        if ctx.variableRes():
            idlist, typ, exprlist = self.visit(ctx.variableRes())
            idlist = [ctx.ID()] + idlist
            exprlist = [(self.visit(ctx.expression()))] + exprlist
            exprlist.reverse()
            return list(map(lambda x, y: VarDecl(x, typ, y), idlist, exprlist))

        else:
            idlist = self.visit(ctx.idlist())
            typ = self.visit(ctx.typ())
            return [VarDecl(x, typ) for x in idlist]

    def visitVariableRes(self, ctx: MT22Parser.VariableResContext):
        if ctx.typ():
            a = self.visit(ctx.typ())
            return [], a, []
        else:
            idlist = [(ctx.ID())]
            exprlist = [(self.visit(ctx.expression()))]
            rest_idlist, rest_typ, rest_exprlist = self.visit(
                ctx.variableRes())
            return idlist + rest_idlist, rest_typ or ctx.typ(), exprlist + rest_exprlist

    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.idlist():
            return [ctx.ID()] + self.visit(ctx.idlist())
        else:
            return [ctx.ID()]

    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.VOID():
            return VoidType()
        elif ctx.AUTO():
            return AutoType()
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        return self.visit(ctx.atomic_types())

    def visitArray_type(self, ctx: MT22Parser.Array_typeContext):
        typ = self.visit(ctx.atomic_types())
        dimension = self.visit(ctx.intlist())
        return ArrayType(dimension, typ)

    def visitIntlist(self, ctx: MT22Parser.IntlistContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.intlist())

    def visitAtomic_types(self, ctx: MT22Parser.Atomic_typesContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.STRING():
            return StringType()

    def visitExpression(self, ctx: MT22Parser.ExpressionContext):
        return self.visit(ctx.stringExp())

    def visitStringExp(self, ctx: MT22Parser.StringExpContext):
        if ctx.DOUBLE_COLON():
            op = ctx.DOUBLE_COLON().getText()
            left = self.visit(ctx.relationalExp(0))
            right = self.visit(ctx.relationalExp(1))
            return BinExpr(op, left, right)
        else:
            return self.visit(ctx.relationalExp(0))

    def visitRelationalExp(self, ctx: MT22Parser.RelationalExpContext):
        if ctx.getChildCount() == 3:
            if ctx.EQUALS():
                op = ctx.EQUALS().getText()
            elif ctx.NOT_EQUAL():
                op = ctx.NOT_EQUAL().getText()
            elif ctx.LESS_THAN():
                op = ctx.LESS_THAN().getText()
            elif ctx.GREATER_THAN():
                op = ctx.GREATER_THAN().getText()
            elif ctx.LESS_THAN_EQUAL():
                op = ctx.LESS_THAN_EQUAL().getText()
            elif ctx.GREATER_THAN_EQUAL():
                op = ctx.GREATER_THAN_EQUAL().getText()
            left = self.visit(ctx.logical1Exp(0))
            right = self.visit(ctx.logical1Exp(1))
            return BinExpr(op, left, right)
        else:
            return self.visit(ctx.logical1Exp(0))

    def visitLogical1Exp(self, ctx: MT22Parser.Logical1ExpContext):
        if ctx.getChildCount() == 3:
            if ctx.AND():
                op = ctx.AND().getText()
            elif ctx.OR():
                op = ctx.OR().getText()
            left = self.visit(ctx.logical1Exp())
            right = self.visit(ctx.addingExp())
            return BinExpr(op, left, right)

        else:
            return self.visit(ctx.addingExp())

    def visitAddingExp(self, ctx: MT22Parser.AddingExpContext):
        if ctx.getChildCount() == 3:
            if ctx.ADD():
                op = ctx.ADD().getText()
            elif ctx.SUB():
                op = ctx.SUB().getText()
            left = self.visit(ctx.addingExp())
            right = self.visit(ctx.multiplyingExp())
            return BinExpr(op, left, right)

        else:
            return self.visit(ctx.multiplyingExp())

    def visitMultiplyingExp(self, ctx: MT22Parser.MultiplyingExpContext):
        if ctx.getChildCount() == 3:
            if ctx.MUL():
                op = ctx.MUL().getText()
            elif ctx.DIV():
                op = ctx.DIV().getText()
            elif ctx.MOD():
                op = ctx.MOD().getText()
            left = self.visit(ctx.multiplyingExp())
            right = self.visit(ctx.logical2Exp())
            return BinExpr(op, left, right)

        else:
            return self.visit(ctx.logical2Exp())

    def visitLogical2Exp(self, ctx: MT22Parser.Logical2ExpContext):
        if ctx.getChildCount() == 2:
            op = ctx.DIFF().getText()
            exp = self.visit(ctx.logical2Exp())
            return UnExpr(op, exp)

        else:
            return self.visit(ctx.signExp())

    def visitSignExp(self, ctx: MT22Parser.SignExpContext):
        if ctx.getChildCount() == 2:
            op = ctx.SUB().getText()
            exp = self.visit(ctx.signExp())
            return UnExpr(op, exp)
        else:
            return self.visit(ctx.operand())

    def visitOperand(self, ctx: MT22Parser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.indexOp():
            return self.visit(ctx.indexOp())
        elif ctx.subExpr():
            return self.visit(ctx.subExpr())

    def visitSubExpr(self, ctx: MT22Parser.SubExprContext):
        return self.visit(ctx.expression())

    def visitIndexOp(self, ctx: MT22Parser.IndexOpContext):
        id = ctx.ID().getText()
        exp = self.visit(ctx.expPrime())
        return ArrayCell(id, exp)

    def visitFunctionCall(self, ctx: MT22Parser.FunctionCallContext):
        id = ctx.ID().getText()
        exp = self.visit(ctx.expressionList())
        return FuncCall(id, exp)

    def visitExpPrime(self, ctx: MT22Parser.ExpPrimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.expPrime())

    def visitExpressionList(self, ctx: MT22Parser.ExpressionListContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.expPrime())

    def visitStatement(self, ctx: MT22Parser.StatementContext):
        if ctx.assignmentStatement():
            return self.visit(ctx.assignmentStatement())
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.forStatement():
            return self.visit(ctx.forStatement())
        elif ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        elif ctx.doWhileStatement():
            return self.visit(ctx.doWhileStatement())
        elif ctx.breakStatement():
            return self.visit(ctx.breakStatement())
        elif ctx.continueStatement():
            return self.visit(ctx.continueStatement())
        elif ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        elif ctx.callStatement():
            return self.visit(ctx.callStatement())
        elif ctx.blockStatement():
            return self.visit(ctx.blockStatement())

    def visitAssignmentStatement(self, ctx: MT22Parser.AssignmentStatementContext):
        lhs = self.visit(ctx.scalar_variable())
        rhs = self.visit(ctx.expression())
        return AssignStmt(lhs, rhs)

    def visitScalar_variable(self, ctx: MT22Parser.Scalar_variableContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.indexOp())

    def visitIfStatement(self, ctx: MT22Parser.IfStatementContext):
        cond = self.visit(ctx.expression())
        tstmt = self.visit(ctx.statement(0))
        if ctx.ELSE():
            fstmt = self.visit(ctx.statement(1))
            return IfStmt(cond, tstmt, fstmt)
        else:
            return IfStmt(cond, tstmt, None)

    def visitForStatement(self, ctx: MT22Parser.ForStatementContext):
        s_var = self.visit(ctx.scalar_variable())
        init = self.visit(ctx.expression(0))
        cond = self.visit(ctx.expression(1))
        inc = self.visit(ctx.expression(2))
        st = self.visit(ctx.statement())
        assStmtInit = AssignStmt(s_var, init)
        return ForStmt(assStmtInit, cond, inc, st)

    def visitWhileStatement(self, ctx: MT22Parser.WhileStatementContext):
        left = self.visit(ctx.expression())
        right = self.visit(ctx.statement())
        return WhileStmt(left, right)

    def visitDoWhileStatement(self, ctx: MT22Parser.DoWhileStatementContext):
        exp = self.visit(ctx.expression())
        block = self.visit(ctx.blockStatement())
        return DoWhileStmt(exp, block)

    def visitBreakStatement(self, ctx: MT22Parser.BreakStatementContext):
        return BreakStmt()

    def visitContinueStatement(self, ctx: MT22Parser.ContinueStatementContext):
        return ContinueStmt()

    def visitReturnStatement(self, ctx: MT22Parser.ReturnStatementContext):
        if ctx.expression():
            exp = self.visit(ctx.expression())
            return ReturnStmt(exp)
        else:
            return ReturnStmt(None)

    def visitCallStatement(self, ctx: MT22Parser.CallStatementContext):
        id = ctx.ID()
        exprs = self.visit(ctx.expressionList())
        return CallStmt(id, exprs)

    def visitBlockStatement(self, ctx: MT22Parser.BlockStatementContext):
        return BlockStmt(self.visit(ctx.blocklist()))

    def visitBlocklist(self, ctx: MT22Parser.BlocklistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.blockcontent()) + self.visit(ctx.blocklist())

    def visitBlockcontent(self, ctx: MT22Parser.BlockcontentContext):
        if ctx.statement():
            return [self.visit(ctx.statement())]
        return self.visit(ctx.variableDeclaration())

    def visitLiteral(self, ctx: MT22Parser.LiteralContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            st = ctx.FLOATLIT().getText()
            if st[0] == '.' and st[1] == 'e':
                st = '0.0'
            return FloatLit(float(st))
        elif ctx.BOOLEANLIT():
            return BooleanLit(ctx.BOOLEANLIT().getText() == "true")
        elif ctx.STRINGLIT():
            return StringLit(str(ctx.STRINGLIT().getText()))
        elif ctx.arrayLit():
            return self.visit(ctx.arrayLit())

    def visitArrayLit(self, ctx: MT22Parser.ArrayLitContext):
        explist = self.visit(ctx.expressionList())
        return ArrayLit(explist)

    def visitFunctionDeclaration(self, ctx: MT22Parser.FunctionDeclarationContext):
        name = ctx.ID(0).getText()
        typ = self.visit(ctx.typ())
        inheritname = None
        params = []
        if ctx.parameterList():
            params = self.visit(ctx.parameterList())
        if ctx.INHERIT():
            inheritname = ctx.ID(1)
        params.reverse()
        block_stmt = self.visit(ctx.blockStatement())
        return [FuncDecl(name, typ, params, inheritname, block_stmt)]

    def visitParameterList(self, ctx: MT22Parser.ParameterListContext):
        params = []
        if ctx.parameterList():
            params += self.visit(ctx.parameterList())
        params.append(self.visit(ctx.parameter()))
        return params

    def visitParameter(self, ctx: MT22Parser.ParameterContext):
        name = ctx.ID()
        typ = self.visit(ctx.typ())
        is_inherit = False
        is_out = False
        if ctx.INHERIT():
            is_inherit = True
        if ctx.OUT():
            is_out = True
        return ParamDecl(name, typ, is_out, is_inherit)
