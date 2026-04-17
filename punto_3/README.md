# Punto 3

Este punto reutiliza codigo de una tarea anterior de la materia. Ya era funcional y aqui se uso tal cual para cubrir el calculo de PRIMEROS, SIGUIENTES y PREDICCION.

## Ejecutar

```bash
cd punto_3
python3 ASD_Recursivo.py gramatica1.txt
```

Si quieres ver la ayuda:

```bash
python3 ASD_Recursivo.py -h
```

## Que hay aqui

- `ASD_Recursivo.py`: logica principal.
- `gramatica1.txt`: ejemplo de entrada.
- `Prueba.jpeg`: evidencia para la bitacora.
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
