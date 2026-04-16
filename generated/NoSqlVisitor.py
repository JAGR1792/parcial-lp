# Generated from /home/antonio/Downloads/PARCIAL_LP/grammar/NoSql.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .NoSqlParser import NoSqlParser
else:
    from NoSqlParser import NoSqlParser

# This class defines a complete generic visitor for a parse tree produced by NoSqlParser.

class NoSqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NoSqlParser#program.
    def visitProgram(self, ctx:NoSqlParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#statement.
    def visitStatement(self, ctx:NoSqlParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#createCollectionStatement.
    def visitCreateCollectionStatement(self, ctx:NoSqlParser.CreateCollectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#insertStatement.
    def visitInsertStatement(self, ctx:NoSqlParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#findStatement.
    def visitFindStatement(self, ctx:NoSqlParser.FindStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#updateStatement.
    def visitUpdateStatement(self, ctx:NoSqlParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#deleteStatement.
    def visitDeleteStatement(self, ctx:NoSqlParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#showCollectionsStatement.
    def visitShowCollectionsStatement(self, ctx:NoSqlParser.ShowCollectionsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#whereClause.
    def visitWhereClause(self, ctx:NoSqlParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#assignmentList.
    def visitAssignmentList(self, ctx:NoSqlParser.AssignmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#assignment.
    def visitAssignment(self, ctx:NoSqlParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#objectLiteral.
    def visitObjectLiteral(self, ctx:NoSqlParser.ObjectLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#pair.
    def visitPair(self, ctx:NoSqlParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#expression.
    def visitExpression(self, ctx:NoSqlParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#orExpr.
    def visitOrExpr(self, ctx:NoSqlParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#andExpr.
    def visitAndExpr(self, ctx:NoSqlParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#equalityExpr.
    def visitEqualityExpr(self, ctx:NoSqlParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#relationalExpr.
    def visitRelationalExpr(self, ctx:NoSqlParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#primary.
    def visitPrimary(self, ctx:NoSqlParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSqlParser#literal.
    def visitLiteral(self, ctx:NoSqlParser.LiteralContext):
        return self.visitChildren(ctx)



del NoSqlParser