# Punto 4

Este punto tambien parte de codigo de una tarea anterior, pero aqui si hubo ajustes para que el analizador aceptara operaciones aritmeticas tipo calculadora.
La logica de comparar, medir, generar CSV, graficar y escribir el reporte es la misma idea del trabajo previo; solo se adapto al nuevo caso.

## Ejecutar

```bash
cd punto_4
python3 main.py entradas/entrada.txt
```

## Salidas

- `resultados/mediciones_comparacion.csv`
- `resultados/grafica_comparacion.png`
- `reportes/comparacion_seria.md`

## Que hay aqui

- `main.py`: ejecuta el flujo completo.
- `analizadores/algoritmo_cyk.py`: CYK.
- `analizadores/analizador_predictivo.py`: parser predictivo.
- `analizadores/comparar_metodos.py`: medicion y reporte base.
- `analizadores/graficar_comparacion.py`: grafica.
- `analizadores/generar_reporte.py`: markdown final.
