# Punto 4: Comparacion CYK vs Parser Predictivo

Este modulo implementa el cuarto ejercicio del parcial: construir un parser con CYK para
expresiones de calculadora y compararlo contra un parser predictivo LL(1).

Se comparan tiempos de ejecucion para evidenciar la diferencia teorica:

- CYK con complejidad $O(n^3)$
- Parser predictivo con complejidad $O(n)$

## Estructura del punto

```text
.
├── analizadores/
│   ├── algoritmo_cyk.py
│   ├── analizador_predictivo.py
│   ├── comparar_metodos.py
│   ├── graficar_comparacion.py
│   └── generar_reporte.py
├── entradas/
│   └── entrada_tarea2.txt
├── gramatica/
│   └── Ejemplo.g4
├── reportes/
│   └── comparacion_seria.md
├── resultados/
│   ├── mediciones_comparacion.csv
│   └── grafica_comparacion.png
├── main.py
└── requirements.txt
```

## Instalacion

```bash
git pull --ff-only
```

Luego prepara el entorno local:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecucion recomendada (todo automatico)

```bash
python3 main.py entradas/entrada_tarea2.txt
```

Este comando ejecuta el flujo completo:

1. Corre CYK y parser predictivo sobre el archivo de entrada
2. Genera el CSV de mediciones
3. Genera la grafica comparativa en PNG
4. Genera el reporte markdown automaticamente con tabla y analisis matematico

Salidas:

- resultados/mediciones_comparacion.csv
- resultados/grafica_comparacion.png
- reportes/comparacion_seria.md

## Ejecucion manual por componentes

```bash
python3 analizadores/algoritmo_cyk.py entradas/entrada_tarea2.txt
python3 analizadores/analizador_predictivo.py entradas/entrada_tarea2.txt
python3 analizadores/comparar_metodos.py entradas/entrada_tarea2.txt
python3 analizadores/graficar_comparacion.py resultados/mediciones_comparacion.csv resultados/grafica_comparacion.png
python3 analizadores/generar_reporte.py
```

## Formato de entrada

Todos los scripts reciben archivo de entrada por argumento. Si no se pasa archivo, reportan:

```text
No se detecto archivo de entrada
```

## Gramatica utilizada

```antlr
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
```

## Formato de entrada

Cada linea del archivo de entrada es una expresion independiente. Ejemplos validos:

- `2+3`
- `(10-4)*7`
- `8/(2+2)`

Tambien se incluyen casos invalidos para contrastar comportamiento de rechazo, por ejemplo:

- `3+*4`
- `(5+2`
- `9/)3(`
