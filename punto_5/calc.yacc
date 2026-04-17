%{
#include <stdio.h>

int regs[26];
int base;

int yylex(void);
void yyerror(char *s);

static void print_value(int value);

%}

%start list

%union { int a; }

%token <a> DIGIT LETTER TRUE FALSE
%token AND OR NOT EQ NE LT LE GT GE
%type <a> stat expr number

%left OR
%left AND
%nonassoc EQ NE LT LE GT GE
%left '+' '-'
%left '*' '/' '%'
%right UMINUS NOT

%%

list:
        /* empty */
      | list line
      ;

line:
        stat '\n'
      | stat
      | error '\n'
        {
          yyerrok;
        }
      ;

stat:
        expr
        {
          print_value($1);
        }
      | LETTER '=' expr
        {
          regs[$1] = $3;
        }
      ;

expr:
        '(' expr ')'
        {
          $$ = $2;
        }
      | expr '*' expr
        {
          $$ = $1 * $3;
        }
      | expr '/' expr
        {
          if ($3 == 0)
          {
            yyerror("division por cero");
            YYERROR;
          }
          $$ = $1 / $3;
        }
      | expr '%' expr
        {
          if ($3 == 0)
          {
            yyerror("modulo por cero");
            YYERROR;
          }
          $$ = $1 % $3;
        }
      | expr '+' expr
        {
          $$ = $1 + $3;
        }
      | expr '-' expr
        {
          $$ = $1 - $3;
        }
      | expr LT expr
        {
          $$ = ($1 < $3);
        }
      | expr LE expr
        {
          $$ = ($1 <= $3);
        }
      | expr GT expr
        {
          $$ = ($1 > $3);
        }
      | expr GE expr
        {
          $$ = ($1 >= $3);
        }
      | expr EQ expr
        {
          $$ = ($1 == $3);
        }
      | expr NE expr
        {
          $$ = ($1 != $3);
        }
      | expr AND expr
        {
          $$ = ($1 && $3);
        }
      | expr OR expr
        {
          $$ = ($1 || $3);
        }
      | NOT expr %prec NOT
        {
          $$ = !$2;
        }
      | '-' expr %prec UMINUS
        {
          $$ = -$2;
        }
      | LETTER
        {
          $$ = regs[$1];
        }
      | number
        {
          $$ = $1;
        }
      | TRUE
        {
          $$ = 1;
        }
      | FALSE
        {
          $$ = 0;
        }
      ;

number:
        DIGIT
        {
          $$ = $1;
          base = ($1 == 0) ? 8 : 10;
        }
      | number DIGIT
        {
          $$ = base * $1 + $2;
        }
      ;

%%

static void print_value(int value)
{
  if (value == 0)
  {
    printf("0\n");
    return;
  }

  if (value == 1)
  {
    printf("1\n");
    return;
  }

  printf("%d\n", value);
}

int main(void)
{
  return yyparse();
}

void yyerror(char *s)
{
  fprintf(stderr, "%s\n", s);
}

int yywrap(void)
{
  return 1;
}