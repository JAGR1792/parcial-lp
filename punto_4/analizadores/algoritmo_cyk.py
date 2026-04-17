from __future__ import annotations

import re
import sys
import time
from typing import Dict, List, Set, Tuple


TOKEN_REGEX = re.compile(r"\s*(\d+(?:\.\d+)?|[()+\-*/])\s*")


def tokenizar_expresion(texto: str) -> List[str]:
    """Convierte una expresion aritmetica en tokens simbolicos para los analizadores."""
    tokens: List[str] = []
    indice = 0
    while indice < len(texto):
        coincidencia = TOKEN_REGEX.match(texto, indice)
        if not coincidencia:
            raise ValueError(f"Token invalido cerca de: '{texto[indice:]}'")

        lexema = coincidencia.group(1)
        if lexema[0].isdigit():
            tokens.append("NUM")
        elif lexema == "+":
            tokens.append("PLUS")
        elif lexema == "-":
            tokens.append("MINUS")
        elif lexema == "*":
            tokens.append("MUL")
        elif lexema == "/":
            tokens.append("DIV")
        elif lexema == "(":
            tokens.append("LP")
        elif lexema == ")":
            tokens.append("RP")
        else:
            raise ValueError(f"Simbolo no soportado: {lexema}")
        indice = coincidencia.end()

    return tokens


class AnalizadorCYK:
    """CYK para expresiones aritmeticas con +, -, *, / y parentesis."""

    def __init__(self) -> None:
        self.simbolo_inicial = "S"
        self.reglas_terminales: Dict[str, Set[str]] = {}
        self.reglas_binarias: Dict[Tuple[str, str], Set[str]] = {}
        self.reglas_unitarias: Dict[str, Set[str]] = {}
        self._cargar_gramatica_cnf()

    def _cargar_gramatica_cnf(self) -> None:
        # Preterminales
        self.reglas_terminales = {
            "T_NUM": {"NUM"},
            "T_PLUS": {"PLUS"},
            "T_MINUS": {"MINUS"},
            "T_MUL": {"MUL"},
            "T_DIV": {"DIV"},
            "T_LP": {"LP"},
            "T_RP": {"RP"},
        }

        # Reglas binarias para una CFG equivalente a:
        # E -> E (+|-) T | T
        # T -> T (*|/) F | F
        # F -> NUM | (E)
        # Se modela con auxiliares y reglas unitarias para cierre.
        self.reglas_binarias = {
            ("E", "P1"): {"E"},
            ("E", "P2"): {"E"},
            ("T_PLUS", "T"): {"P1"},
            ("T_MINUS", "T"): {"P2"},

            ("T", "P3"): {"T"},
            ("T", "P4"): {"T"},
            ("T_MUL", "F"): {"P3"},
            ("T_DIV", "F"): {"P4"},

            ("T_LP", "P5"): {"F"},
            ("E", "T_RP"): {"P5"},
        }

        self.reglas_unitarias = {
            "E": {"S"},
            "T": {"E"},
            "F": {"T"},
            "T_NUM": {"F"},
        }

    def _cerradura_unitaria(self, simbolos: Set[str]) -> Set[str]:
        cerradura = set(simbolos)
        cambio = True
        while cambio:
            cambio = False
            nuevos: Set[str] = set()
            for simbolo in cerradura:
                nuevos.update(self.reglas_unitarias.get(simbolo, set()))
            if not nuevos.issubset(cerradura):
                cerradura.update(nuevos)
                cambio = True
        return cerradura

    def analizar_cyk(self, tokens: List[str]) -> bool:
        n = len(tokens)
        if n == 0:
            return False

        tabla: List[List[Set[str]]] = [[set() for _ in range(n)] for _ in range(n)]

        for i, token in enumerate(tokens):
            for no_terminal, terminales in self.reglas_terminales.items():
                if token in terminales:
                    tabla[i][i].add(no_terminal)
            tabla[i][i] = self._cerradura_unitaria(tabla[i][i])

        for longitud in range(2, n + 1):
            for i in range(n - longitud + 1):
                j = i + longitud - 1
                for k in range(i, j):
                    for izq in tabla[i][k]:
                        for der in tabla[k + 1][j]:
                            padres = self.reglas_binarias.get((izq, der), set())
                            if padres:
                                tabla[i][j].update(padres)
                if tabla[i][j]:
                    tabla[i][j] = self._cerradura_unitaria(tabla[i][j])

        return self.simbolo_inicial in tabla[0][n - 1]


def principal() -> None:
    analizador = AnalizadorCYK()

    if len(sys.argv) <= 1:
        print("No se detecto archivo de entrada")
        return

    ruta_entrada = sys.argv[1]
    with open(ruta_entrada, "r", encoding="utf-8") as archivo:
        lineas = archivo.read().splitlines()

    for linea in lineas:
        if not linea.strip():
            continue
        t_0 = time.perf_counter()
        try:
            tokens = tokenizar_expresion(linea.strip())
            resultado = analizador.analizar_cyk(tokens)
        except ValueError:
            resultado = False
        t_1 = time.perf_counter()
        estado = "ACEPTADA" if resultado else "RECHAZADA"
        print(f"{linea} -> {estado} ({t_1 - t_0:.6f} s)")


if __name__ == "__main__":
    principal()
