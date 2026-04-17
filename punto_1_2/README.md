# Punto 1 y 2

CRUD minimo con ANTLR4 en Python.

## Ejecutar

Desde la raiz del repo:

```bash
python3 "punto_1_2/analizador.py" "punto_1_2/ejemplos/ejemplo.txt"
```

## Probar
Desde carpeta
```bash
cd punto_1_2/
pytest
```

## Contenido clave

- `gramatica/LenguajeNoRelacional.g4`
- `analizador.py`
- `visitante_evaluacion.py`
- `pruebas/prueba_visitante.py`