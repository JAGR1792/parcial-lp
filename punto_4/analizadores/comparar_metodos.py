from __future__ import annotations

import csv
import sys
import time
from pathlib import Path

from algoritmo_cyk import AnalizadorCYK, tokenizar_expresion
from analizador_predictivo import AnalizadorPredictivo


def principal() -> None:
    if len(sys.argv) <= 1:
        print("No se detecto archivo de entrada")
        return

    ruta_entrada = Path(sys.argv[1])
    ruta_csv = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("resultados/mediciones_comparacion.csv")
    ruta_md = Path(sys.argv[3]) if len(sys.argv) > 3 else Path("resultados/comparacion_resultados.md")

    cyk = AnalizadorCYK()
    predictivo = AnalizadorPredictivo()

    ruta_csv.parent.mkdir(parents=True, exist_ok=True)
    ruta_md.parent.mkdir(parents=True, exist_ok=True)

    filas = []
    with open(ruta_entrada, "r", encoding="utf-8") as archivo:
        for linea in archivo.read().splitlines():
            if not linea.strip():
                continue

            texto = linea.strip()

            t0 = time.perf_counter()
            try:
                tokens = tokenizar_expresion(texto)
                res_cyk = cyk.analizar_cyk(tokens)
            except ValueError:
                tokens = []
                res_cyk = False
            t1 = time.perf_counter()

            t2 = time.perf_counter()
            res_predictivo, _ = predictivo.analizar(texto)
            t3 = time.perf_counter()

            tiempo_cyk = t1 - t0
            tiempo_predictivo = t3 - t2

            filas.append(
                {
                    "entrada": texto,
                    "tokens": len(tokens),
                    "cyk_estado": "ACEPTADA" if res_cyk else "RECHAZADA",
                    "predictivo_estado": "ACEPTADA" if res_predictivo else "RECHAZADA",
                    "cyk_seg": f"{tiempo_cyk:.8f}",
                    "predictivo_seg": f"{tiempo_predictivo:.8f}",
                }
            )
            print(
                f"{texto} -> CYK:{'ACEPTADA' if res_cyk else 'RECHAZADA'} ({tiempo_cyk:.6f} s) "
                f"| PREDICTIVO:{'ACEPTADA' if res_predictivo else 'RECHAZADA'} ({tiempo_predictivo:.6f} s)"
            )

    with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo_csv:
        escritor = csv.DictWriter(
            archivo_csv,
            fieldnames=[
                "entrada",
                "tokens",
                "cyk_estado",
                "predictivo_estado",
                "cyk_seg",
                "predictivo_seg",
            ],
        )
        escritor.writeheader()
        escritor.writerows(filas)

    with open(ruta_md, "w", encoding="utf-8") as archivo_md:
        archivo_md.write("# Resultados de Comparacion CYK vs Parser Predictivo\n\n")
        archivo_md.write("| Entrada | Tokens | CYK | Predictivo | Tiempo CYK (s) | Tiempo Predictivo (s) |\n")
        archivo_md.write("|---|---:|---|---|---:|---:|\n")
        for fila in filas:
            archivo_md.write(
                f"| {fila['entrada']} | {fila['tokens']} | {fila['cyk_estado']} | {fila['predictivo_estado']} | {fila['cyk_seg']} | {fila['predictivo_seg']} |\n"
            )


if __name__ == "__main__":
    principal()
