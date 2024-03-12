from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):
    # program: NEWLINE* declLst EOF;
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.declLst()))

    # declLst: decl declLst | decl;
    def visitDeclLst(self, ctx:ZCodeParser.DeclLstContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.decl())] + self.visit(ctx.declLst())
        return [self.visit(ctx.decl())]

    # decl: varDecl ignore| funDecl;
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        return self.visit(ctx.funDecl())

    # varDecl: varDeclCase1 | varDeclCase2 | varDeclCase3;
    def visitVarDecl(self, ctx:ZCodeParser.VarDeclContext):
        return self.visitChildren(ctx)

    # varDeclCase1: VAR ID declare; // implicit
    def visitVarDeclCase1(self, ctx:ZCodeParser.VarDeclCase1Context):
        id = ctx.ID().getText()
        var = self.visit(ctx.declare())
        return VarDecl(Id(id), None, "var", var)

    # varDeclCase2: dataType ID (LBRACK dimenslist RBRACK)? declare?; // normal
    def visitVarDeclCase2(self, ctx:ZCodeParser.VarDeclCase2Context):
        typ = self.visit(ctx.dataType())
        id = ctx.ID().getText()
        if ctx.declare():
            var = self.visit(ctx.declare())
        else:
            var = None
        if ctx.dimenslist():
            return VarDecl(Id(id), ArrayType(self.visit(ctx.dimenslist()), typ), None, var)
        return VarDecl(Id(id), typ, None, var)

    # varDeclCase3: DYNAMIC ID declare?; // dynamic
    def visitVarDeclCase3(self, ctx:ZCodeParser.VarDeclCase3Context):
        id = ctx.ID().getText()
        if ctx.declare():
            var = self.visit(ctx.declare())
        else:
            var = None
        return VarDecl(Id(id), None, "dynamic", var)

    # declare: ASSIGN expr;
    def visitDeclare(self, ctx:ZCodeParser.DeclareContext):
        return self.visit(ctx.expr())

    # dimenslist: NUMLIT COMMA dimenslist | NUMLIT;
    def visitDimenslist(self, ctx:ZCodeParser.DimenslistContext):
        if ctx.getChildCount() == 1:
            return [float(ctx.NUMLIT().getText())]
        return [float(ctx.NUMLIT().getText())] + self.visit(ctx.dimenslist())

    # ignore: NEWLINE+;
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        pass

    # funDecl: FUNC ID LPAREN (paramLst | ) RPAREN (ignore | ignore? blockStmt | ignore? returnStmt);
    def visitFunDecl(self, ctx:ZCodeParser.FunDeclContext):
        id = ctx.ID().getText()
        if ctx.paramLst():
            param = self.visit(ctx.paramLst())
        else:
            param = []
        if ctx.returnStmt():
            ret = self.visit(ctx.returnStmt())
            return FuncDecl(Id(id), param, ret)
        elif ctx.blockStmt():
            block = self.visit(ctx.blockStmt())
            return FuncDecl(Id(id), param, block)
        return FuncDecl(Id(id), param, None)

    # paramLst: paramDecl COMMA paramLst | paramDecl;
    def visitParamLst(self, ctx:ZCodeParser.ParamLstContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.paramDecl())] + self.visit(ctx.paramLst())
        return [self.visit(ctx.paramDecl())]

    # paramDecl: dataType ID (LBRACK dimenslist RBRACK | );
    def visitParamDecl(self, ctx:ZCodeParser.ParamDeclContext):
        typ = self.visit(ctx.dataType())
        id = ctx.ID().getText()
        dimenslist = []
        if ctx.dimenslist():
            dimenslist = self.visit(ctx.dimenslist())
            return VarDecl(Id(id), ArrayType(dimenslist, typ), None, None)
        return VarDecl(Id(id), typ, None, None)
        
    # dataType: NUMBER | BOOL | STRING;
    def visitDataType(self, ctx:ZCodeParser.DataTypeContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        return StringType()

    # exprLst: expr COMMA exprLst | expr;
    def visitExprLst(self, ctx:ZCodeParser.ExprLstContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expr())] + self.visit(ctx.exprLst())
        return [self.visit(ctx.expr())]

    # expr: expr1;
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)

    # expr1: expr2 CONCAT expr2 | expr2; // string
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.CONCAT().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        return self.visit(ctx.getChild(0))

    # expr2: expr3 (EQ | COMPARE | NEQ | LT | GT | LTE | GTE) expr3| expr3; // relational
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr3(0)), self.visit(ctx.expr3(1)))
        return self.visit(ctx.getChild(0))

    # expr3: expr3 (AND | OR) expr4 | expr4; // logical
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        return self.visit(ctx.getChild(0))

    # expr4: expr4 (ADD | SUB) expr5 | expr5; // adding
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return self.visit(ctx.getChild(0))

    # expr5: expr5 (MUL | DIV | MOD) expr6 | expr6; // multiplying
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr5()), self.visit(ctx.expr6()))
        return self.visit(ctx.getChild(0))

    # expr6: NOT expr6 | expr7; // logical
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr6()))
        return self.visit(ctx.getChild(0))

    # expr7: (SUB | ADD) expr7 | operand; // sign
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr7()))
        return self.visit(ctx.getChild(0))

    # operand: subexpr | arrayEle | funccall | ID |literal;
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visitChildren(ctx)

    # subexpr: LPAREN expr RPAREN;
    def visitSubexpr(self, ctx:ZCodeParser.SubexprContext):
        return self.visit(ctx.expr())

    # arrayEle: (ID | funccall) LBRACK exprLst RBRACK;
    def visitArrayEle(self, ctx:ZCodeParser.ArrayEleContext):
        return ArrayCell(Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.funccall()), self.visit(ctx.exprLst()))

    # funccall: ID LPAREN exprLst? RPAREN;
    def visitFunccall(self, ctx:ZCodeParser.FunccallContext):
        return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.exprLst()) if ctx.exprLst() else [])

    # arrayLit: LBRACK exprLst RBRACK;
    def visitArrayLit(self, ctx:ZCodeParser.ArrayLitContext):
        return ArrayLiteral(self.visit(ctx.exprLst()))

    # literal: NUMLIT | TRUE | FALSE | STRLIT | arrayLit;
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        if ctx.NUMLIT():
            return NumberLiteral(float(ctx.NUMLIT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.STRLIT():
            return StringLiteral(ctx.STRLIT().getText())
        return self.visit(ctx.arrayLit())

    # stmtLst: stmt stmtLst | stmt;
    def visitStmtLst(self, ctx:ZCodeParser.StmtLstContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmtLst())
        return [self.visit(ctx.stmt())]
    
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visit(ctx.getChild(0))

    # assignmentStmt: ID (LBRACK exprLst RBRACK)? ASSIGN expr ignore;
    def visitAssignmentStmt(self, ctx:ZCodeParser.AssignmentStmtContext):
        if ctx.exprLst():
            return Assign(ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.exprLst())), self.visit(ctx.expr()))
        return Assign(Id(ctx.ID().getText()), self.visit(ctx.expr()))

    # ifStmt: IF LPAREN expr RPAREN ignore? stmt elifLst ;
    def visitIfStmt(self, ctx:ZCodeParser.IfStmtContext):
        elifStmt, elseStmt = self.visit(ctx.elifLst())
        return If(self.visit(ctx.expr()), self.visit(ctx.stmt()), elifStmt, elseStmt)

    # elifLst: elifEle elifLst | elseClause | ;
    def visitElifLst(self, ctx:ZCodeParser.ElifLstContext):
        if (ctx.getChildCount() == 0):
            return [], None
    
        if (ctx.elseClause()):
            return [], self.visit(ctx.elseClause())
        
        elifStmt, elseStmt = self.visit(ctx.elifLst())
        
        return [self.visit(ctx.elifEle())] + elifStmt, elseStmt

    # elifEle: ELIF LPAREN expr RPAREN ignore? stmt;
    def visitElifEle(self, ctx:ZCodeParser.ElifEleContext):
        return [self.visit(ctx.expr()), self.visit(ctx.stmt())]
    
    # elseClause: ELSE ignore? stmt ;
    def visitElseClause(self, ctx:ZCodeParser.ElseClauseContext):
        return self.visit(ctx.stmt())

    # forStmt: FOR ID  UNTIL expr BY expr ignore? stmt;
    def visitForStmt(self, ctx:ZCodeParser.ForStmtContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.stmt()))

    # breakStmt: BREAK ignore;
    def visitBreakStmt(self, ctx:ZCodeParser.BreakStmtContext):
        return Break()

    # continueStmt: CONTINUE ignore ;
    def visitContinueStmt(self, ctx:ZCodeParser.ContinueStmtContext):
        return Continue()

    # returnStmt: RETURN (expr |) ignore;
    def visitReturnStmt(self, ctx:ZCodeParser.ReturnStmtContext):
        return Return(self.visit(ctx.expr()) if ctx.expr() else None)


    # funCallStmt: ID LPAREN (exprLst |) RPAREN ignore;
    def visitFunCallStmt(self, ctx:ZCodeParser.FunCallStmtContext):
        return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.exprLst()) if ctx.exprLst() else [])

    # blockStmt: BEGIN ignore (stmtLst |) END ignore;
    def visitBlockStmt(self, ctx:ZCodeParser.BlockStmtContext):
        return Block(self.visit(ctx.stmtLst()) if ctx.stmtLst() else [])