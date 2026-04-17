# Punto 1 y 2

CRUD minimo con ANTLR4 en Python.

## Ejecutar

Desde la raiz del repo:

```bash
python3 "punto_1_&_2/analizador.py" "punto_1_&_2/ejemplos/ejemplo.txt"
```

## Probar

```bash
pytest
```

## Contenido clave

- `gramatica/LenguajeNoRelacional.g4`
- `analizador.py`
- `visitante_evaluacion.py`
- `pruebas/prueba_visitante.py`