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

### En Windows

En PowerShell normal `make` no viene instalado por defecto. En Arch seguramente te funcionaba porque ya tenias `make`, `lex/yacc` y el compilador disponibles en el sistema.

Para usar este proyecto en Windows necesitas una de estas opciones:

1. WSL con un entorno Linux que tenga `make`, `flex`/`lex`, `bison`/`yacc` y `gcc` o `cc`.
2. MSYS2 o una shell Unix-like que provea esas herramientas.
3. Instalar manualmente las utilidades equivalentes en tu entorno actual.

Si falta cualquiera de esas herramientas, el `Makefile` no va a funcionar.

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

Si no quieres usar `make`, o si prefieres ver el flujo completo paso a paso, puedes hacerlo manualmente asi:

```bash
yacc -d calc.yacc
lex calc.lex
cc -Wall -Wextra -O2 y.tab.c lex.yy.c -o calculadora
./calculadora < ejemplo.txt
```

Si en tu sistema los comandos se llaman `bison` y `flex`, el equivalente suele ser:

```bash
bison -y -d calc.yacc
flex calc.lex
cc -Wall -Wextra -O2 y.tab.c lex.yy.c -o calculadora
./calculadora < ejemplo.txt
```

En PowerShell, si quieres ejecutar el binario y leer el archivo de entrada, prueba:

```powershell
.\calculadora.exe < ejemplo.txt
```

Si al ejecutar `./calculadora` aparece `no such file or directory`, significa que aun no has compilado; primero corre `make` o los comandos manuales anteriores.

## Nota sobre la salida

El programa imprime el resultado de cada expresion en una linea nueva. Las expresiones booleanas se representan como `0` o `1`.