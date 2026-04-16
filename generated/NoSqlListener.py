# Generated from /home/antonio/Downloads/PARCIAL_LP/grammar/NoSql.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .NoSqlParser import NoSqlParser
else:
    from NoSqlParser import NoSqlParser

# This class defines a complete listener for a parse tree produced by NoSqlParser.
class NoSqlListener(ParseTreeListener):

    # Enter a parse tree produced by NoSqlParser#program.
    def enterProgram(self, ctx:NoSqlParser.ProgramContext):
        pass

    # Exit a parse tree produced by NoSqlParser#program.
    def exitProgram(self, ctx:NoSqlParser.ProgramContext):
        pass


    # Enter a parse tree produced by NoSqlParser#statement.
    def enterStatement(self, ctx:NoSqlParser.StatementContext):
        pass

    # Exit a parse tree produced by NoSqlParser#statement.
    def exitStatement(self, ctx:NoSqlParser.StatementContext):
        pass


    # Enter a parse tree produced by NoSqlParser#createCollectionStatement.
    def enterCreateCollectionStatement(self, ctx:NoSqlParser.CreateCollectionStatementContext):
        pass

    # Exit a parse tree produced by NoSqlParser#createCollectionStatement.
    def exitCreateCollectionStatement(self, ctx:NoSqlParser.CreateCollectionStatementContext):
        pass


    # Enter a parse tree produced by NoSqlParser#insertStatement.
    def enterInsertStatement(self, ctx:NoSqlParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by NoSqlParser#insertStatement.
    def exitInsertStatement(self, ctx:NoSqlParser.InsertStatementContext):
        pass


    # Enter a parse tree produced by NoSqlParser#findStatement.
    def enterFindStatement(self, ctx:NoSqlParser.FindStatementContext):
        pass

    # Exit a parse tree produced by NoSqlParser#findStatement.
    def exitFindStatement(self, ctx:NoSqlParser.FindStatementContext):
        pass


    # Enter a parse tree produced by NoSqlParser#updateStatement.
    def enterUpdateStatement(self, ctx:NoSqlParser.UpdateStatementContext):
        pass

    # Exit a parse tree produced by NoSqlParser#updateStatement.
    def exitUpdateStatement(self, ctx:NoSqlParser.UpdateStatementContext):
        pass


    # Enter a parse tree produced by NoSqlParser#deleteStatement.
    def enterDeleteStatement(self, ctx:NoSqlParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by NoSqlParser#deleteStatement.
    def exitDeleteStatement(self, ctx:NoSqlParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by NoSqlParser#showCollectionsStatement.
    def enterShowCollectionsStatement(self, ctx:NoSqlParser.ShowCollectionsStatementContext):
        pass

    # Exit a parse tree produced by NoSqlParser#showCollectionsStatement.
    def exitShowCollectionsStatement(self, ctx:NoSqlParser.ShowCollectionsStatementContext):
        pass


    # Enter a parse tree produced by NoSqlParser#whereClause.
    def enterWhereClause(self, ctx:NoSqlParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by NoSqlParser#whereClause.
    def exitWhereClause(self, ctx:NoSqlParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by NoSqlParser#assignmentList.
    def enterAssignmentList(self, ctx:NoSqlParser.AssignmentListContext):
        pass

    # Exit a parse tree produced by NoSqlParser#assignmentList.
    def exitAssignmentList(self, ctx:NoSqlParser.AssignmentListContext):
        pass


    # Enter a parse tree produced by NoSqlParser#assignment.
    def enterAssignment(self, ctx:NoSqlParser.AssignmentContext):
        pass

    # Exit a parse tree produced by NoSqlParser#assignment.
    def exitAssignment(self, ctx:NoSqlParser.AssignmentContext):
        pass


    # Enter a parse tree produced by NoSqlParser#objectLiteral.
    def enterObjectLiteral(self, ctx:NoSqlParser.ObjectLiteralContext):
        pass

    # Exit a parse tree produced by NoSqlParser#objectLiteral.
    def exitObjectLiteral(self, ctx:NoSqlParser.ObjectLiteralContext):
        pass


    # Enter a parse tree produced by NoSqlParser#pair.
    def enterPair(self, ctx:NoSqlParser.PairContext):
        pass

    # Exit a parse tree produced by NoSqlParser#pair.
    def exitPair(self, ctx:NoSqlParser.PairContext):
        pass


    # Enter a parse tree produced by NoSqlParser#expression.
    def enterExpression(self, ctx:NoSqlParser.ExpressionContext):
        pass

    # Exit a parse tree produced by NoSqlParser#expression.
    def exitExpression(self, ctx:NoSqlParser.ExpressionContext):
        pass


    # Enter a parse tree produced by NoSqlParser#orExpr.
    def enterOrExpr(self, ctx:NoSqlParser.OrExprContext):
        pass

    # Exit a parse tree produced by NoSqlParser#orExpr.
    def exitOrExpr(self, ctx:NoSqlParser.OrExprContext):
        pass


    # Enter a parse tree produced by NoSqlParser#andExpr.
    def enterAndExpr(self, ctx:NoSqlParser.AndExprContext):
        pass

    # Exit a parse tree produced by NoSqlParser#andExpr.
    def exitAndExpr(self, ctx:NoSqlParser.AndExprContext):
        pass


    # Enter a parse tree produced by NoSqlParser#equalityExpr.
    def enterEqualityExpr(self, ctx:NoSqlParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by NoSqlParser#equalityExpr.
    def exitEqualityExpr(self, ctx:NoSqlParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by NoSqlParser#relationalExpr.
    def enterRelationalExpr(self, ctx:NoSqlParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by NoSqlParser#relationalExpr.
    def exitRelationalExpr(self, ctx:NoSqlParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by NoSqlParser#primary.
    def enterPrimary(self, ctx:NoSqlParser.PrimaryContext):
        pass

    # Exit a parse tree produced by NoSqlParser#primary.
    def exitPrimary(self, ctx:NoSqlParser.PrimaryContext):
        pass


    # Enter a parse tree produced by NoSqlParser#literal.
    def enterLiteral(self, ctx:NoSqlParser.LiteralContext):
        pass

    # Exit a parse tree produced by NoSqlParser#literal.
    def exitLiteral(self, ctx:NoSqlParser.LiteralContext):
        pass



del NoSqlParser