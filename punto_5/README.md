# Punto 5

Calculadora de escritorio en `lex` y `yacc`.

## Que implementa

- Operaciones aritmeticas: `+`, `-`, `*`, `/`, `%`.
- Operaciones booleanas y relacionales: `&&`, `||`, `!`, `==`, `!=`, `<`, `<=`, `>`, `>=`.
- Variables de una sola letra minuscula, con asignacion como `m=4`.
- Constantes booleanas `verdadero`, `falso`, `true` y `false`.

## Compilar con Makefile

Desde esta carpeta, `make` genera el analizador, compila y deja el ejecutable `calculadora` listo para usar:

```bash
make
```

El `Makefile` hace esto en orden:

1. Ejecuta `yacc -d calc.yacc` y genera `y.tab.c` y `y.tab.h`.
2. Ejecuta `lex calc.lex` y genera `lex.yy.c`.
3. Compila y enlaza con `cc` para producir `calculadora`.

## Ejecutar

Una vez compilado, puedes correrlo asi:

```bash
./calculadora
```

O usando el archivo de ejemplo:

```bash
./calculadora < ejemplo.txt
```

Tambien puedes usar el atajo:

```bash
make run
```

## Limpiar

Si quieres borrar el ejecutable y los archivos generados por `lex` y `yacc`:

```bash
make clean
```

## Comandos manuales

Si no quieres usar `make`, o no funciona (según mis pruebas en windows para ver si compilaba en diferentes OS), puedes hacerlo manualmente asi:

```bash
yacc -d calc.yacc
lex calc.lex
cc -Wall -Wextra -O2 y.tab.c lex.yy.c -o calculadora
./calculadora < ejemplo.txt
```
