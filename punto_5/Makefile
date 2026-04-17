LEX=lex
YACC=yacc
CC=cc
CFLAGS=-Wall -Wextra -O2

all: calculadora

y.tab.c y.tab.h: calc.yacc
	$(YACC) -d calc.yacc

lex.yy.c: calc.lex y.tab.h
	$(LEX) calc.lex

calculadora: y.tab.c lex.yy.c
	$(CC) $(CFLAGS) y.tab.c lex.yy.c -o calculadora

run: calculadora
	./calculadora < ejemplo.txt

clean:
	rm -f calculadora lex.yy.c y.tab.c y.tab.h

.PHONY: all run clean