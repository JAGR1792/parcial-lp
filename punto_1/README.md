# Punto 1 - CRUD con ANTLR en Python

Este punto implementa un CRUD minimo con ANTLR4 en Python sobre una base en memoria.

## Operaciones soportadas

- `CREAR COLECCION nombre;`
- `INSERTAR EN nombre { campo: valor, ... };`
- `BUSCAR nombre DONDE condicion;`
- `ACTUALIZAR nombre FIJAR campo = valor DONDE condicion;`
- `ELIMINAR DE nombre DONDE condicion;`
## Ejemplo

```text
CREAR COLECCION usuarios;
INSERTAR EN usuarios { nombre: "Ana", edad: 20, activo: verdadero };
BUSCAR usuarios DONDE edad >= 18;
ACTUALIZAR usuarios FIJAR activo = falso DONDE nombre == "Ana";
ELIMINAR DE usuarios DONDE edad < 18;
```

## Ejecutar

1. Generar el parser de ANTLR en Python dentro de `generado/`.
2. Ejecutar el programa:

```bash
.venv/bin/python punto_1/analizador.py punto_1/ejemplos/ejemplo.txt
```

## Probar

```bash
pytest
```