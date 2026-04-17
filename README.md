# PARCIAL LP

Guia general del repo y comandos mas utiles.

## Estructura

- `punto_1_&&_2/`: CRUD con ANTLR y visitor en Python.
- `punto_3/`: calculo de PRIMEROS, SIGUIENTES y PREDICCION.
- `punto_4/`: comparacion CYK vs parser predictivo.
- `punto5/`: vacio por ahora.
- `bitacora_taller.tex`: bitacora final en LaTeX.

## Instalacion rapida

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Punto 1 y 2

CRUD con ANTLR4. Ejecutar desde la raiz:

```bash
python3 punto_1_&&_2/analizador.py punto_1_&&_2/ejemplos/ejemplo.txt
```

Pruebas:

```bash
pytest
```

## Punto 3

Aqui se reutilizo codigo de una tarea anterior de la materia; ya era funcional y solo se integro como solucion al ejercicio.

Ejecutar:

```bash
cd punto_3
python3 ASD_Recursivo.py gramatica1.txt
```

## Punto 4

Aqui tambien se reutilizo base de una tarea anterior; se modifico la logica para aceptar expresiones aritmeticas tipo calculadora.
La parte de reporte, CSV y grafica sigue la misma idea del trabajo previo, solo adaptada al nuevo escenario.

Ejecutar:

```bash
cd punto_4
python3 main.py entradas/entrada.txt
```

## Punto 5

Ya tiene una calculadora de escritorio en `punto_5/` con `calc.lex`, `calc.yacc`, `ejemplo.txt` y un `README.md` con los comandos de compilacion.

## Bitacora

La guia para completar la bitacora esta en [bitacora_taller.tex](bitacora_taller.tex).
