# Punto 5

Calculadora de escritorio en `lex` y `yacc`.

## Que implementa

- Operaciones aritmeticas: `+`, `-`, `*`, `/`, `%`.
- Operaciones booleanas y relacionales: `&&`, `||`, `!`, `==`, `!=`, `<`, `<=`, `>`, `>=`.
- Variables de una sola letra minuscula, con asignacion como `m=4`.



- Constantes booleanas `verdadero`, `falso`, `true` y `false`.

## Compilar

Desde esta carpeta:

```bash
yacc -d calc.yacc
lex calc.lex
cc y.tab.c lex.yy.c -o calculadora
```

## Ejecutar

```bash
./calculadora
```

O con un archivo de ejemplo:

```bash
./calculadora < ejemplo.txt
```

## Nota sobre la salida

El programa imprime el resultado de cada expresion en una linea nueva. Las expresiones booleanas se representan como `0` o `1`.