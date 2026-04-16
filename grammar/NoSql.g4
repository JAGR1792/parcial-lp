grammar NoSql;

program
    : statement* EOF
    ;

statement
    : createCollectionStatement SEMI?
    | insertStatement SEMI?
    | findStatement SEMI?
    | updateStatement SEMI?
    | deleteStatement SEMI?
    | showCollectionsStatement SEMI?
    ;

createCollectionStatement
    : CREATE COLLECTION IDENTIFIER
    ;

insertStatement
    : INSERT INTO IDENTIFIER objectLiteral
    ;

findStatement
    : FIND IDENTIFIER whereClause?
    ;

updateStatement
    : UPDATE IDENTIFIER SET assignmentList whereClause?
    ;

deleteStatement
    : DELETE FROM IDENTIFIER whereClause?
    ;

showCollectionsStatement
    : SHOW COLLECTIONS
    ;

whereClause
    : WHERE expression
    ;

assignmentList
    : assignment (COMMA assignment)*
    ;

assignment
    : IDENTIFIER EQUAL expression
    ;

objectLiteral
    : LBRACE (pair (COMMA pair)*)? RBRACE
    ;

pair
    : IDENTIFIER COLON expression
    ;

expression
    : orExpr
    ;

orExpr
    : andExpr (OR andExpr)*
    ;

andExpr
    : equalityExpr (AND equalityExpr)*
    ;

equalityExpr
    : relationalExpr ((EQ | NEQ) relationalExpr)*
    ;

relationalExpr
    : primary ((LT | LTE | GT | GTE) primary)*
    ;

primary
    : literal
    | IDENTIFIER
    | LPAREN expression RPAREN
    ;

literal
    : STRING
    | NUMBER
    | BOOLEAN
    | NULL
    ;

CREATE : 'CREATE';
COLLECTION : 'COLLECTION';
INSERT : 'INSERT';
INTO : 'INTO';
FIND : 'FIND';
UPDATE : 'UPDATE';
SET : 'SET';
DELETE : 'DELETE';
FROM : 'FROM';
SHOW : 'SHOW';
COLLECTIONS : 'COLLECTIONS';
WHERE : 'WHERE';
OR : 'OR';
AND : 'AND';
BOOLEAN : 'true' | 'false';
NULL : 'null';

EQ : '==';
NEQ : '!=';
LTE : '<=';
GTE : '>=';
LT : '<';
GT : '>';
EQUAL : '=';
COLON : ':';
COMMA : ',';
SEMI : ';';
LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';

IDENTIFIER
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

NUMBER
    : '-'? [0-9]+ ('.' [0-9]+)?
    ;

STRING
    : '"' ( '\\' . | ~["\\] )* '"'
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;