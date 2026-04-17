grammar Ejemplo;

expresion : termino ((PLUS | MINUS) termino)* EOF ;
termino   : factor ((MUL | DIV) factor)* ;
factor    : NUM | LPAREN expresion RPAREN ;

PLUS   : '+' ;
MINUS  : '-' ;
MUL    : '*' ;
DIV    : '/' ;
LPAREN : '(' ;
RPAREN : ')' ;
NUM    : [0-9]+ ('.' [0-9]+)? ;

WS : [ \t\r\n]+ -> skip ;
