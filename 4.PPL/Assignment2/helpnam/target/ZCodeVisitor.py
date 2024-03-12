# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declLst.
    def visitDeclLst(self, ctx:ZCodeParser.DeclLstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#varDecl.
    def visitVarDecl(self, ctx:ZCodeParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#varDeclCase1.
    def visitVarDeclCase1(self, ctx:ZCodeParser.VarDeclCase1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#varDeclCase2.
    def visitVarDeclCase2(self, ctx:ZCodeParser.VarDeclCase2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#varDeclCase3.
    def visitVarDeclCase3(self, ctx:ZCodeParser.VarDeclCase3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declare.
    def visitDeclare(self, ctx:ZCodeParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dimenslist.
    def visitDimenslist(self, ctx:ZCodeParser.DimenslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funDecl.
    def visitFunDecl(self, ctx:ZCodeParser.FunDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramLst.
    def visitParamLst(self, ctx:ZCodeParser.ParamLstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramDecl.
    def visitParamDecl(self, ctx:ZCodeParser.ParamDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dataType.
    def visitDataType(self, ctx:ZCodeParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprLst.
    def visitExprLst(self, ctx:ZCodeParser.ExprLstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#subexpr.
    def visitSubexpr(self, ctx:ZCodeParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayEle.
    def visitArrayEle(self, ctx:ZCodeParser.ArrayEleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funccall.
    def visitFunccall(self, ctx:ZCodeParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayLit.
    def visitArrayLit(self, ctx:ZCodeParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtLst.
    def visitStmtLst(self, ctx:ZCodeParser.StmtLstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignmentStmt.
    def visitAssignmentStmt(self, ctx:ZCodeParser.AssignmentStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifStmt.
    def visitIfStmt(self, ctx:ZCodeParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifLst.
    def visitElifLst(self, ctx:ZCodeParser.ElifLstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifEle.
    def visitElifEle(self, ctx:ZCodeParser.ElifEleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elseClause.
    def visitElseClause(self, ctx:ZCodeParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forStmt.
    def visitForStmt(self, ctx:ZCodeParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakStmt.
    def visitBreakStmt(self, ctx:ZCodeParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continueStmt.
    def visitContinueStmt(self, ctx:ZCodeParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnStmt.
    def visitReturnStmt(self, ctx:ZCodeParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funCallStmt.
    def visitFunCallStmt(self, ctx:ZCodeParser.FunCallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockStmt.
    def visitBlockStmt(self, ctx:ZCodeParser.BlockStmtContext):
        return self.visitChildren(ctx)



del ZCodeParser