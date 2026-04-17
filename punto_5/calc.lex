%{
#include <stdio.h>
#include <string.h>
#include "y.tab.h"

int c;
%}

%%
[ \t\r]+      ;
"verdadero"   { return TRUE; }
"falso"       { return FALSE; }
"true"        { return TRUE; }
"false"       { return FALSE; }
"&&"          { return AND; }
"||"          { return OR; }
"!"           { return NOT; }
"=="          { return EQ; }
"!="          { return NE; }
"<="          { return LE; }
">="          { return GE; }
"<"           { return LT; }
">"           { return GT; }
[a-z]          {
                 c = yytext[0];
                 yylval.a = c - 'a';
                 return LETTER;
               }
[0-9]          {
                 c = yytext[0];
                 yylval.a = c - '0';
                 return DIGIT;
               }
\n             { return '\n'; }
.              { return yytext[0]; }
%%