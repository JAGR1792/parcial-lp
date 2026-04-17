# Punto 3

Este punto reutiliza codigo de una tarea anterior de la materia. Ya era funcional y aqui se uso tal cual para cubrir el calculo de PRIMEROS, SIGUIENTES y PREDICCION, que es lo que se requiere para poder acotar que algo es LL(1).

## Ejecutar

```bash
cd punto_3
python3 ASD_Recursivo.py gramatica1.txt
```

Si quieres ver la ayuda:

```bash
python3 ASD_Recursivo.py -h
```

## Que hace
- calcula first, follow y hace la tabla de parseo, que es el metódo para demostrar que una gramatica es LL(1), para más información, ir a la explicación ya dada en el repositorio original de esta tarea.

- https://github.com/JAGR1792/Tareas_LP

## Que hay aqui

- `ASD_Recursivo.py`: logica principal.
- `gramatica1.txt`: ejemplo de entrada.
