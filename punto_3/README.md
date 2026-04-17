# Calculo de Conjuntos PRIMEROS, SIGUIENTES y PREDICCION

## Descripcion
-----

ESTE README, ES EL MISMO DE UNA TAREA ANTERIOR, QUE COPIE Y PEGUE PORQUE BASICAMENTE HACE LO QUE ESTE PUNTO ESPECIFICO PIDE, DEMOSTRAR QUE UNA GRAMATICA ES LL(1), LO HACE INDIRECTAMENTE.

Esta tarea implementa el calculo de los conjuntos:

- PRIMEROS (FIRST)
- SIGUIENTES (FOLLOW)
- PREDICCION

para una gramatica libre de contexto, leyendo las producciones desde archivo de texto y mostrando los resultados en tablas ASCII en terminal.

## Requisitos

- Python 3



## Formato de entrada

Cada produccion debe escribirse en una linea con la forma:

```text
NoTerminal -> simbolo simbolo simbolo
```

Convenciones de las diapositivas:

- Derivacion: `->`
- Alternativas: `|`
- Vacio: `ε`
- Simbolo inicial: primer no terminal que aparece en el archivo

Ejemplo:

```text
S -> A uno B C
S -> S dos
A -> B C D
A -> A tres
A -> ε
```

## Ejecucion

```bash
python ASD_Recursivo.py gramatica1.txt
```

Tambien se pueden procesar varios archivos en una sola ejecucion:

```bash
python ASD_Recursivo.py gramatica1.txt gramatica2.txt
```

Con `-h` se muestra ayuda de uso:

```bash
python ASD_Recursivo.py -h
```

Si falta el argumento del archivo:

```text
Uso: python nombre.py archivo.txt
FALTA <<archivo.txt>>
```

## Reglas de calculo

### Conjunto de PRIMEROS (FIRST)

Sea `X` un simbolo o una secuencia de simbolos.

Regla 1:

Si `X` es un terminal, entonces:

`FIRST(X) = {X}`

Regla 2:

Si existe una produccion de la forma:

`X -> ε`

entonces:

`ε in FIRST(X)`

Regla 3:

Si existe una produccion:

`X -> Y1 Y2 ... Yn`

entonces:

- Se agrega `FIRST(Y1)` sin `ε` a `FIRST(X)`.
- Si `ε in FIRST(Y1)`, se agrega `FIRST(Y2)` (sin `ε`).
- Se continua asi sucesivamente.
- Si todos los `Yi` producen `ε`, entonces `ε in FIRST(X)`.

### Conjunto de SIGUIENTES (FOLLOW)

Sea `A` un no terminal.

Regla 1:

El simbolo inicial `S` siempre contiene:

`$ in FOLLOW(S)`

Regla 2:

Si existe una produccion:

`A -> α B β`

entonces:

`FIRST(β) - {ε} subset FOLLOW(B)`

Regla 3:

Si existe una produccion:

`A -> α B`

o

`A -> α B β` donde `ε in FIRST(β)`

entonces:

`FOLLOW(A) subset FOLLOW(B)`

### Conjunto de PREDICCION (PREDICT)

Sea una produccion:

`A -> α`

El conjunto de prediccion se define como:

Regla 1:

Si `ε ∉ FIRST(α)`, entonces:

`PREDICT(A -> α) = FIRST(α)`

Regla 2:

Si `ε ∈ FIRST(α)`, entonces:

`PREDICT(A -> α) = (FIRST(α) - {ε}) ∪ FOLLOW(A)`

### Interpretacion

- FIRST indica que puede empezar una derivacion.
- FOLLOW indica que puede venir despues.
- PREDICT combina ambos para decidir que produccion usar.

### Nota

Los conjuntos FIRST y FOLLOW se calculan de manera iterativa hasta alcanzar un punto fijo, es decir, hasta que no se agreguen nuevos elementos a ningun conjunto.

Los conjuntos de prediccion permiten construir analizadores sintacticos predictivos (LL(1)), ya que determinan de manera unica que produccion aplicar en funcion del simbolo de entrada.

## Referencia que nos ayudo en el taller

Durante el desarrollo de este punto nos sirvio mucho la explicacion de por que una gramatica LL(1) requiere solo un simbolo de anticipacion al construir un parser descendente recursivo:

- https://www.quora.com/How-can-you-prove-or-explain-with-words-that-an-LL-1-grammar-only-needs-one-lookahead-if-you-make-a-recursive-descent-parser-form-it

Fue una referencia eficiente para orientar la justificacion teorica de lo que nos pidieron en el taller.

## Ejecucion de gramatica1

Comando ejecutado:

```bash
python ASD_Recursivo.py gramatica1.txt
```

Salida:

```text
PRIMEROS:
+-------------+--------------------------------+
| No Terminal | PRIMEROS                       |
+-------------+--------------------------------+
| A           | cinco, cuatro, seis, tres, ε   |
| B           | cuatro, seis, ε                |
| C           | cinco, ε                       |
| D           | seis, ε                        |
| S           | cinco, cuatro, seis, tres, uno |
+-------------+--------------------------------+

SIGUIENTES:
+-------------+---------------------------------+
| No Terminal | SIGUIENTES                      |
+-------------+---------------------------------+
| A           | tres, uno                       |
| B           | $, cinco, dos, seis, tres, uno  |
| C           | $, dos, seis, tres, uno         |
| D           | $, cuatro, dos, seis, tres, uno |
| S           | $, dos                          |
+-------------+---------------------------------+

PREDICCION:
+----------------------+---------------------------------+
| Regla                | PREDICCION                      |
+----------------------+---------------------------------+
| S -> A uno B C       | cinco, cuatro, seis, tres, uno  |
| S -> S dos           | cinco, cuatro, seis, tres, uno  |
| A -> B C D           | cinco, cuatro, seis, tres, uno  |
| A -> A tres          | cinco, cuatro, seis, tres       |
| A -> ε               | tres, uno                       |
| B -> D cuatro C tres | cuatro, seis                    |
| B -> ε               | $, cinco, dos, seis, tres, uno  |
| C -> cinco D B       | cinco                           |
| C -> ε               | $, dos, seis, tres, uno         |
| D -> seis            | seis                            |
| D -> ε               | $, cuatro, dos, seis, tres, uno |
+----------------------+---------------------------------+
```

## Ejecucion de gramatica2

Comando ejecutado:

```bash
python ASD_Recursivo.py gramatica2.txt
```

Salida:

```text
PRIMEROS:
+-------------+-------------------------------+
| No Terminal | PRIMEROS                      |
+-------------+-------------------------------+
| A           | dos, ε                        |
| B           | cinco, cuatro, tres, ε        |
| C           | cinco, cuatro                 |
| D           | seis, ε                       |
| S           | cinco, cuatro, dos, tres, uno |
+-------------+-------------------------------+

SIGUIENTES:
+-------------+--------------------------------+
| No Terminal | SIGUIENTES                     |
+-------------+--------------------------------+
| A           | cinco, cuatro, seis, tres, uno |
| B           | cinco, cuatro, seis, tres, uno |
| C           | cinco, cuatro, seis, tres, uno |
| D           | cinco, cuatro, seis, tres, uno |
| S           | $                              |
+-------------+--------------------------------+

PREDICCION:
+-----------------+--------------------------------+
| Regla           | PREDICCION                     |
+-----------------+--------------------------------+
| S -> A B uno    | cinco, cuatro, dos, tres, uno  |
| A -> dos B      | dos                            |
| A -> ε          | cinco, cuatro, seis, tres, uno |
| B -> C D        | cinco, cuatro                  |
| B -> tres       | tres                           |
| B -> ε          | cinco, cuatro, seis, tres, uno |
| C -> cuatro A B | cuatro                         |
| C -> cinco      | cinco                          |
| D -> seis       | seis                           |
| D -> ε          | cinco, cuatro, seis, tres, uno |
+-----------------+--------------------------------+
```
