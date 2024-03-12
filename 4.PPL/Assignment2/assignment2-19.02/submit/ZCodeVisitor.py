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


    # Visit a parse tree produced by ZCodeParser#list_declared.
    def visitList_declared(self, ctx:ZCodeParser.List_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declared.
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variables.
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#keyword_var.
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_var.
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_dynamic.
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dimenslist.
    def visitDimenslist(self, ctx:ZCodeParser.DimenslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function.
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameters_list.
    def visitParameters_list(self, ctx:ZCodeParser.Parameters_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_expr.
    def visitList_expr(self, ctx:ZCodeParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression1.
    def visitExpression1(self, ctx:ZCodeParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression2.
    def visitExpression2(self, ctx:ZCodeParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expresisson3.
    def visitExpresisson3(self, ctx:ZCodeParser.Expresisson3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression4.
    def visitExpression4(self, ctx:ZCodeParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression5.
    def visitExpression5(self, ctx:ZCodeParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression6.
    def visitExpression6(self, ctx:ZCodeParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression7.
    def visitExpression7(self, ctx:ZCodeParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational.
    def visitRelational(self, ctx:ZCodeParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logical.
    def visitLogical(self, ctx:ZCodeParser.LogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#adding.
    def visitAdding(self, ctx:ZCodeParser.AddingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multiplying.
    def visitMultiplying(self, ctx:ZCodeParser.MultiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#subexpr.
    def visitSubexpr(self, ctx:ZCodeParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayele.
    def visitArrayele(self, ctx:ZCodeParser.ArrayeleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funccall.
    def visitFunccall(self, ctx:ZCodeParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_lit.
    def visitArray_lit(self, ctx:ZCodeParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement_list.
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration_statement.
    def visitDeclaration_statement(self, ctx:ZCodeParser.Declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment_statement.
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_statement.
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_statement.
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_statement.
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_elif.
    def visitList_elif(self, ctx:ZCodeParser.List_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_stmt.
    def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elseif_stmt.
    def visitElseif_stmt(self, ctx:ZCodeParser.Elseif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_statement.
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_statement.
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_statement.
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#call_statement.
    def visitCall_statement(self, ctx:ZCodeParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return self.visitChildren(ctx)



del ZCodeParser