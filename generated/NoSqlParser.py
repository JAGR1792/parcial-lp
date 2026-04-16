# Generated from /home/antonio/Downloads/PARCIAL_LP/grammar/NoSql.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,181,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,1,1,1,3,1,51,8,1,1,1,1,1,3,
        1,55,8,1,1,1,1,1,3,1,59,8,1,1,1,1,1,3,1,63,8,1,1,1,1,1,3,1,67,8,
        1,1,1,1,1,3,1,71,8,1,3,1,73,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,3,4,87,8,4,1,5,1,5,1,5,1,5,1,5,3,5,94,8,5,1,6,1,
        6,1,6,1,6,3,6,100,8,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,5,9,111,
        8,9,10,9,12,9,114,9,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,5,
        11,124,8,11,10,11,12,11,127,9,11,3,11,129,8,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,13,1,13,1,14,1,14,1,14,5,14,142,8,14,10,14,12,14,
        145,9,14,1,15,1,15,1,15,5,15,150,8,15,10,15,12,15,153,9,15,1,16,
        1,16,1,16,5,16,158,8,16,10,16,12,16,161,9,16,1,17,1,17,1,17,5,17,
        166,8,17,10,17,12,17,169,9,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,
        177,8,18,1,19,1,19,1,19,0,0,20,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,0,3,1,0,17,18,1,0,19,22,2,0,15,16,32,33,184,
        0,43,1,0,0,0,2,72,1,0,0,0,4,74,1,0,0,0,6,78,1,0,0,0,8,83,1,0,0,0,
        10,88,1,0,0,0,12,95,1,0,0,0,14,101,1,0,0,0,16,104,1,0,0,0,18,107,
        1,0,0,0,20,115,1,0,0,0,22,119,1,0,0,0,24,132,1,0,0,0,26,136,1,0,
        0,0,28,138,1,0,0,0,30,146,1,0,0,0,32,154,1,0,0,0,34,162,1,0,0,0,
        36,176,1,0,0,0,38,178,1,0,0,0,40,42,3,2,1,0,41,40,1,0,0,0,42,45,
        1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,
        46,47,5,0,0,1,47,1,1,0,0,0,48,50,3,4,2,0,49,51,5,26,0,0,50,49,1,
        0,0,0,50,51,1,0,0,0,51,73,1,0,0,0,52,54,3,6,3,0,53,55,5,26,0,0,54,
        53,1,0,0,0,54,55,1,0,0,0,55,73,1,0,0,0,56,58,3,8,4,0,57,59,5,26,
        0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,73,1,0,0,0,60,62,3,10,5,0,61,
        63,5,26,0,0,62,61,1,0,0,0,62,63,1,0,0,0,63,73,1,0,0,0,64,66,3,12,
        6,0,65,67,5,26,0,0,66,65,1,0,0,0,66,67,1,0,0,0,67,73,1,0,0,0,68,
        70,3,14,7,0,69,71,5,26,0,0,70,69,1,0,0,0,70,71,1,0,0,0,71,73,1,0,
        0,0,72,48,1,0,0,0,72,52,1,0,0,0,72,56,1,0,0,0,72,60,1,0,0,0,72,64,
        1,0,0,0,72,68,1,0,0,0,73,3,1,0,0,0,74,75,5,1,0,0,75,76,5,2,0,0,76,
        77,5,31,0,0,77,5,1,0,0,0,78,79,5,3,0,0,79,80,5,4,0,0,80,81,5,31,
        0,0,81,82,3,22,11,0,82,7,1,0,0,0,83,84,5,5,0,0,84,86,5,31,0,0,85,
        87,3,16,8,0,86,85,1,0,0,0,86,87,1,0,0,0,87,9,1,0,0,0,88,89,5,6,0,
        0,89,90,5,31,0,0,90,91,5,7,0,0,91,93,3,18,9,0,92,94,3,16,8,0,93,
        92,1,0,0,0,93,94,1,0,0,0,94,11,1,0,0,0,95,96,5,8,0,0,96,97,5,9,0,
        0,97,99,5,31,0,0,98,100,3,16,8,0,99,98,1,0,0,0,99,100,1,0,0,0,100,
        13,1,0,0,0,101,102,5,10,0,0,102,103,5,11,0,0,103,15,1,0,0,0,104,
        105,5,12,0,0,105,106,3,26,13,0,106,17,1,0,0,0,107,112,3,20,10,0,
        108,109,5,25,0,0,109,111,3,20,10,0,110,108,1,0,0,0,111,114,1,0,0,
        0,112,110,1,0,0,0,112,113,1,0,0,0,113,19,1,0,0,0,114,112,1,0,0,0,
        115,116,5,31,0,0,116,117,5,23,0,0,117,118,3,26,13,0,118,21,1,0,0,
        0,119,128,5,29,0,0,120,125,3,24,12,0,121,122,5,25,0,0,122,124,3,
        24,12,0,123,121,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,
        1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,128,120,1,0,0,0,128,129,
        1,0,0,0,129,130,1,0,0,0,130,131,5,30,0,0,131,23,1,0,0,0,132,133,
        5,31,0,0,133,134,5,24,0,0,134,135,3,26,13,0,135,25,1,0,0,0,136,137,
        3,28,14,0,137,27,1,0,0,0,138,143,3,30,15,0,139,140,5,13,0,0,140,
        142,3,30,15,0,141,139,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,
        144,1,0,0,0,144,29,1,0,0,0,145,143,1,0,0,0,146,151,3,32,16,0,147,
        148,5,14,0,0,148,150,3,32,16,0,149,147,1,0,0,0,150,153,1,0,0,0,151,
        149,1,0,0,0,151,152,1,0,0,0,152,31,1,0,0,0,153,151,1,0,0,0,154,159,
        3,34,17,0,155,156,7,0,0,0,156,158,3,34,17,0,157,155,1,0,0,0,158,
        161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,33,1,0,0,0,161,159,
        1,0,0,0,162,167,3,36,18,0,163,164,7,1,0,0,164,166,3,36,18,0,165,
        163,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,
        35,1,0,0,0,169,167,1,0,0,0,170,177,3,38,19,0,171,177,5,31,0,0,172,
        173,5,27,0,0,173,174,3,26,13,0,174,175,5,28,0,0,175,177,1,0,0,0,
        176,170,1,0,0,0,176,171,1,0,0,0,176,172,1,0,0,0,177,37,1,0,0,0,178,
        179,7,2,0,0,179,39,1,0,0,0,19,43,50,54,58,62,66,70,72,86,93,99,112,
        125,128,143,151,159,167,176
    ]

class NoSqlParser ( Parser ):

    grammarFileName = "NoSql.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREATE'", "'COLLECTION'", "'INSERT'", 
                     "'INTO'", "'FIND'", "'UPDATE'", "'SET'", "'DELETE'", 
                     "'FROM'", "'SHOW'", "'COLLECTIONS'", "'WHERE'", "'OR'", 
                     "'AND'", "<INVALID>", "'null'", "'=='", "'!='", "'<='", 
                     "'>='", "'<'", "'>'", "'='", "':'", "','", "';'", "'('", 
                     "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "CREATE", "COLLECTION", "INSERT", "INTO", 
                      "FIND", "UPDATE", "SET", "DELETE", "FROM", "SHOW", 
                      "COLLECTIONS", "WHERE", "OR", "AND", "BOOLEAN", "NULL", 
                      "EQ", "NEQ", "LTE", "GTE", "LT", "GT", "EQUAL", "COLON", 
                      "COMMA", "SEMI", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "IDENTIFIER", "NUMBER", "STRING", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_createCollectionStatement = 2
    RULE_insertStatement = 3
    RULE_findStatement = 4
    RULE_updateStatement = 5
    RULE_deleteStatement = 6
    RULE_showCollectionsStatement = 7
    RULE_whereClause = 8
    RULE_assignmentList = 9
    RULE_assignment = 10
    RULE_objectLiteral = 11
    RULE_pair = 12
    RULE_expression = 13
    RULE_orExpr = 14
    RULE_andExpr = 15
    RULE_equalityExpr = 16
    RULE_relationalExpr = 17
    RULE_primary = 18
    RULE_literal = 19

    ruleNames =  [ "program", "statement", "createCollectionStatement", 
                   "insertStatement", "findStatement", "updateStatement", 
                   "deleteStatement", "showCollectionsStatement", "whereClause", 
                   "assignmentList", "assignment", "objectLiteral", "pair", 
                   "expression", "orExpr", "andExpr", "equalityExpr", "relationalExpr", 
                   "primary", "literal" ]

    EOF = Token.EOF
    CREATE=1
    COLLECTION=2
    INSERT=3
    INTO=4
    FIND=5
    UPDATE=6
    SET=7
    DELETE=8
    FROM=9
    SHOW=10
    COLLECTIONS=11
    WHERE=12
    OR=13
    AND=14
    BOOLEAN=15
    NULL=16
    EQ=17
    NEQ=18
    LTE=19
    GTE=20
    LT=21
    GT=22
    EQUAL=23
    COLON=24
    COMMA=25
    SEMI=26
    LPAREN=27
    RPAREN=28
    LBRACE=29
    RBRACE=30
    IDENTIFIER=31
    NUMBER=32
    STRING=33
    LINE_COMMENT=34
    BLOCK_COMMENT=35
    WS=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(NoSqlParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NoSqlParser.StatementContext)
            else:
                return self.getTypedRuleContext(NoSqlParser.StatementContext,i)


        def getRuleIndex(self):
            return NoSqlParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = NoSqlParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1386) != 0):
                self.state = 40
                self.statement()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(NoSqlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def createCollectionStatement(self):
            return self.getTypedRuleContext(NoSqlParser.CreateCollectionStatementContext,0)


        def SEMI(self):
            return self.getToken(NoSqlParser.SEMI, 0)

        def insertStatement(self):
            return self.getTypedRuleContext(NoSqlParser.InsertStatementContext,0)


        def findStatement(self):
            return self.getTypedRuleContext(NoSqlParser.FindStatementContext,0)


        def updateStatement(self):
            return self.getTypedRuleContext(NoSqlParser.UpdateStatementContext,0)


        def deleteStatement(self):
            return self.getTypedRuleContext(NoSqlParser.DeleteStatementContext,0)


        def showCollectionsStatement(self):
            return self.getTypedRuleContext(NoSqlParser.ShowCollectionsStatementContext,0)


        def getRuleIndex(self):
            return NoSqlParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = NoSqlParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.createCollectionStatement()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 49
                    self.match(NoSqlParser.SEMI)


                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.insertStatement()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 53
                    self.match(NoSqlParser.SEMI)


                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.findStatement()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 57
                    self.match(NoSqlParser.SEMI)


                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.updateStatement()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 61
                    self.match(NoSqlParser.SEMI)


                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.deleteStatement()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 65
                    self.match(NoSqlParser.SEMI)


                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 68
                self.showCollectionsStatement()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 69
                    self.match(NoSqlParser.SEMI)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateCollectionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(NoSqlParser.CREATE, 0)

        def COLLECTION(self):
            return self.getToken(NoSqlParser.COLLECTION, 0)

        def IDENTIFIER(self):
            return self.getToken(NoSqlParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return NoSqlParser.RULE_createCollectionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateCollectionStatement" ):
                listener.enterCreateCollectionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateCollectionStatement" ):
                listener.exitCreateCollectionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateCollectionStatement" ):
                return visitor.visitCreateCollectionStatement(self)
            else:
                return visitor.visitChildren(self)




    def createCollectionStatement(self):

        localctx = NoSqlParser.CreateCollectionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_createCollectionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(NoSqlParser.CREATE)
            self.state = 75
            self.match(NoSqlParser.COLLECTION)
            self.state = 76
            self.match(NoSqlParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(NoSqlParser.INSERT, 0)

        def INTO(self):
            return self.getToken(NoSqlParser.INTO, 0)

        def IDENTIFIER(self):
            return self.getToken(NoSqlParser.IDENTIFIER, 0)

        def objectLiteral(self):
            return self.getTypedRuleContext(NoSqlParser.ObjectLiteralContext,0)


        def getRuleIndex(self):
            return NoSqlParser.RULE_insertStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsertStatement" ):
                listener.enterInsertStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsertStatement" ):
                listener.exitInsertStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertStatement" ):
                return visitor.visitInsertStatement(self)
            else:
                return visitor.visitChildren(self)




    def insertStatement(self):

        localctx = NoSqlParser.InsertStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_insertStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(NoSqlParser.INSERT)
            self.state = 79
            self.match(NoSqlParser.INTO)
            self.state = 80
            self.match(NoSqlParser.IDENTIFIER)
            self.state = 81
            self.objectLiteral()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FindStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIND(self):
            return self.getToken(NoSqlParser.FIND, 0)

        def IDENTIFIER(self):
            return self.getToken(NoSqlParser.IDENTIFIER, 0)

        def whereClause(self):
            return self.getTypedRuleContext(NoSqlParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return NoSqlParser.RULE_findStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFindStatement" ):
                listener.enterFindStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFindStatement" ):
                listener.exitFindStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFindStatement" ):
                return visitor.visitFindStatement(self)
            else:
                return visitor.visitChildren(self)




    def findStatement(self):

        localctx = NoSqlParser.FindStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_findStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(NoSqlParser.FIND)
            self.state = 84
            self.match(NoSqlParser.IDENTIFIER)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 85
                self.whereClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(NoSqlParser.UPDATE, 0)

        def IDENTIFIER(self):
            return self.getToken(NoSqlParser.IDENTIFIER, 0)

        def SET(self):
            return self.getToken(NoSqlParser.SET, 0)

        def assignmentList(self):
            return self.getTypedRuleContext(NoSqlParser.AssignmentListContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(NoSqlParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return NoSqlParser.RULE_updateStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdateStatement" ):
                listener.enterUpdateStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdateStatement" ):
                listener.exitUpdateStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateStatement" ):
                return visitor.visitUpdateStatement(self)
            else:
                return visitor.visitChildren(self)




    def updateStatement(self):

        localctx = NoSqlParser.UpdateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_updateStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(NoSqlParser.UPDATE)
            self.state = 89
            self.match(NoSqlParser.IDENTIFIER)
            self.state = 90
            self.match(NoSqlParser.SET)
            self.state = 91
            self.assignmentList()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 92
                self.whereClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(NoSqlParser.DELETE, 0)

        def FROM(self):
            return self.getToken(NoSqlParser.FROM, 0)

        def IDENTIFIER(self):
            return self.getToken(NoSqlParser.IDENTIFIER, 0)

        def whereClause(self):
            return self.getTypedRuleContext(NoSqlParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return NoSqlParser.RULE_deleteStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteStatement" ):
                listener.enterDeleteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteStatement" ):
                listener.exitDeleteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteStatement" ):
                return visitor.visitDeleteStatement(self)
            else:
                return visitor.visitChildren(self)




    def deleteStatement(self):

        localctx = NoSqlParser.DeleteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_deleteStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(NoSqlParser.DELETE)
            self.state = 96
            self.match(NoSqlParser.FROM)
            self.state = 97
            self.match(NoSqlParser.IDENTIFIER)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 98
                self.whereClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShowCollectionsStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHOW(self):
            return self.getToken(NoSqlParser.SHOW, 0)

        def COLLECTIONS(self):
            return self.getToken(NoSqlParser.COLLECTIONS, 0)

        def getRuleIndex(self):
            return NoSqlParser.RULE_showCollectionsStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShowCollectionsStatement" ):
                listener.enterShowCollectionsStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShowCollectionsStatement" ):
                listener.exitShowCollectionsStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowCollectionsStatement" ):
                return visitor.visitShowCollectionsStatement(self)
            else:
                return visitor.visitChildren(self)




    def showCollectionsStatement(self):

        localctx = NoSqlParser.ShowCollectionsStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_showCollectionsStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(NoSqlParser.SHOW)
            self.state = 102
            self.match(NoSqlParser.COLLECTIONS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(NoSqlParser.WHERE, 0)

        def expression(self):
            return self.getTypedRuleContext(NoSqlParser.ExpressionContext,0)


        def getRuleIndex(self):
            return NoSqlParser.RULE_whereClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereClause" ):
                listener.enterWhereClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereClause" ):
                listener.exitWhereClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhereClause" ):
                return visitor.visitWhereClause(self)
            else:
                return visitor.visitChildren(self)




    def whereClause(self):

        localctx = NoSqlParser.WhereClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(NoSqlParser.WHERE)
            self.state = 105
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NoSqlParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(NoSqlParser.AssignmentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NoSqlParser.COMMA)
            else:
                return self.getToken(NoSqlParser.COMMA, i)

        def getRuleIndex(self):
            return NoSqlParser.RULE_assignmentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentList" ):
                listener.enterAssignmentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentList" ):
                listener.exitAssignmentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentList" ):
                return visitor.visitAssignmentList(self)
            else:
                return visitor.visitChildren(self)




    def assignmentList(self):

        localctx = NoSqlParser.AssignmentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignmentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.assignment()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 108
                self.match(NoSqlParser.COMMA)
                self.state = 109
                self.assignment()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(NoSqlParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(NoSqlParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(NoSqlParser.ExpressionContext,0)


        def getRuleIndex(self):
            return NoSqlParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = NoSqlParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(NoSqlParser.IDENTIFIER)
            self.state = 116
            self.match(NoSqlParser.EQUAL)
            self.state = 117
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(NoSqlParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(NoSqlParser.RBRACE, 0)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NoSqlParser.PairContext)
            else:
                return self.getTypedRuleContext(NoSqlParser.PairContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NoSqlParser.COMMA)
            else:
                return self.getToken(NoSqlParser.COMMA, i)

        def getRuleIndex(self):
            return NoSqlParser.RULE_objectLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectLiteral" ):
                listener.enterObjectLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectLiteral" ):
                listener.exitObjectLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectLiteral" ):
                return visitor.visitObjectLiteral(self)
            else:
                return visitor.visitChildren(self)




    def objectLiteral(self):

        localctx = NoSqlParser.ObjectLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_objectLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(NoSqlParser.LBRACE)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 120
                self.pair()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 121
                    self.match(NoSqlParser.COMMA)
                    self.state = 122
                    self.pair()
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 130
            self.match(NoSqlParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(NoSqlParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(NoSqlParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(NoSqlParser.ExpressionContext,0)


        def getRuleIndex(self):
            return NoSqlParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = NoSqlParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(NoSqlParser.IDENTIFIER)
            self.state = 133
            self.match(NoSqlParser.COLON)
            self.state = 134
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orExpr(self):
            return self.getTypedRuleContext(NoSqlParser.OrExprContext,0)


        def getRuleIndex(self):
            return NoSqlParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = NoSqlParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.orExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NoSqlParser.AndExprContext)
            else:
                return self.getTypedRuleContext(NoSqlParser.AndExprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(NoSqlParser.OR)
            else:
                return self.getToken(NoSqlParser.OR, i)

        def getRuleIndex(self):
            return NoSqlParser.RULE_orExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def orExpr(self):

        localctx = NoSqlParser.OrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_orExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.andExpr()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 139
                self.match(NoSqlParser.OR)
                self.state = 140
                self.andExpr()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NoSqlParser.EqualityExprContext)
            else:
                return self.getTypedRuleContext(NoSqlParser.EqualityExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(NoSqlParser.AND)
            else:
                return self.getToken(NoSqlParser.AND, i)

        def getRuleIndex(self):
            return NoSqlParser.RULE_andExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def andExpr(self):

        localctx = NoSqlParser.AndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_andExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.equalityExpr()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 147
                self.match(NoSqlParser.AND)
                self.state = 148
                self.equalityExpr()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NoSqlParser.RelationalExprContext)
            else:
                return self.getTypedRuleContext(NoSqlParser.RelationalExprContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(NoSqlParser.EQ)
            else:
                return self.getToken(NoSqlParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(NoSqlParser.NEQ)
            else:
                return self.getToken(NoSqlParser.NEQ, i)

        def getRuleIndex(self):
            return NoSqlParser.RULE_equalityExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpr(self):

        localctx = NoSqlParser.EqualityExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_equalityExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.relationalExpr()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 155
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 156
                self.relationalExpr()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NoSqlParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(NoSqlParser.PrimaryContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(NoSqlParser.LT)
            else:
                return self.getToken(NoSqlParser.LT, i)

        def LTE(self, i:int=None):
            if i is None:
                return self.getTokens(NoSqlParser.LTE)
            else:
                return self.getToken(NoSqlParser.LTE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(NoSqlParser.GT)
            else:
                return self.getToken(NoSqlParser.GT, i)

        def GTE(self, i:int=None):
            if i is None:
                return self.getTokens(NoSqlParser.GTE)
            else:
                return self.getToken(NoSqlParser.GTE, i)

        def getRuleIndex(self):
            return NoSqlParser.RULE_relationalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpr(self):

        localctx = NoSqlParser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_relationalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.primary()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0):
                self.state = 163
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 164
                self.primary()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(NoSqlParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(NoSqlParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(NoSqlParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(NoSqlParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(NoSqlParser.RPAREN, 0)

        def getRuleIndex(self):
            return NoSqlParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = NoSqlParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primary)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.literal()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(NoSqlParser.IDENTIFIER)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.match(NoSqlParser.LPAREN)
                self.state = 173
                self.expression()
                self.state = 174
                self.match(NoSqlParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(NoSqlParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(NoSqlParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(NoSqlParser.BOOLEAN, 0)

        def NULL(self):
            return self.getToken(NoSqlParser.NULL, 0)

        def getRuleIndex(self):
            return NoSqlParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = NoSqlParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 12885000192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





