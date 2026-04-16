# Punto 1 - CRUD con ANTLR en Python

Este proyecto implementa el punto 1 con ANTLR4, visitor y `EvalVisitor`, usando Python y una base en memoria.

## Comandos soportados

- `CREATE COLLECTION nombre;`
- `INSERT INTO nombre { campo: valor, ... };`
- `FIND nombre WHERE condicion;`
- `UPDATE nombre SET campo = valor WHERE condicion;`
- `DELETE FROM nombre WHERE condicion;`
- `SHOW COLLECTIONS;`

## Ejemplo

```text
CREATE COLLECTION users;
INSERT INTO users { name: "Ana", age: 20, active: true };
FIND users WHERE age >= 18;
UPDATE users SET active = false WHERE name == "Ana";
DELETE FROM users WHERE age < 18;
```

## Ejecutar

1. Generar el parser de ANTLR en Python dentro de `generated/`.
2. Ejecutar el programa:

```bash
python app.py examples/ejemplo.nosql
```

## Probar

```bash
pytest
```