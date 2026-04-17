from __future__ import annotations

import re
import sys
import time
from typing import List, Optional, Tuple


TOKEN_REGEX = re.compile(r"\s*(\d+(?:\.\d+)?|[()+\-*/])\s*")


class ErrorSintactico(Exception):
    pass


class AnalizadorPredictivo:
    """Parser predictivo LL(1) para expresiones aritmeticas."""

    def __init__(self) -> None:
        self.tokens: List[str] = []
        self.pos = 0

    def tokenizar(self, texto: str) -> List[str]:
        tokens: List[str] = []
        indice = 0
        while indice < len(texto):
            coincidencia = TOKEN_REGEX.match(texto, indice)
            if not coincidencia:
                raise ErrorSintactico(f"Token invalido cerca de: '{texto[indice:]}'")

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
                raise ErrorSintactico(f"Simbolo no soportado: {lexema}")
            indice = coincidencia.end()

        return tokens

    def _actual(self) -> str:
        if self.pos >= len(self.tokens):
            return "EOF"
        return self.tokens[self.pos]

    def _consumir(self, token_esperado: str) -> None:
        if self._actual() != token_esperado:
            raise ErrorSintactico(f"Se esperaba {token_esperado}, se encontro {self._actual()}")
        self.pos += 1

    # E  -> T E'
    # E' -> + T E' | - T E' | epsilon
    # T  -> F T'
    # T' -> * F T' | / F T' | epsilon
    # F  -> NUM | ( E )
    def _E(self) -> None:
        self._T()
        self._E_prima()

    def _E_prima(self) -> None:
        while self._actual() in {"PLUS", "MINUS"}:
            self.pos += 1
            self._T()

    def _T(self) -> None:
        self._F()
        self._T_prima()

    def _T_prima(self) -> None:
        while self._actual() in {"MUL", "DIV"}:
            self.pos += 1
            self._F()

    def _F(self) -> None:
        token = self._actual()
        if token == "NUM":
            self._consumir("NUM")
            return
        if token == "LP":
            self._consumir("LP")
            self._E()
            self._consumir("RP")
            return
        raise ErrorSintactico(f"Factor invalido con token {token}")

    def analizar(self, texto: str) -> Tuple[bool, Optional[str]]:
        try:
            self.tokens = self.tokenizar(texto)
            self.pos = 0
            if not self.tokens:
                return False, "La expresion esta vacia"
            self._E()
            if self._actual() != "EOF":
                raise ErrorSintactico(f"Token sobrante: {self._actual()}")
            return True, None
        except ErrorSintactico as exc:
            return False, str(exc)


def principal() -> None:
    analizador = AnalizadorPredictivo()

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
        aceptada, _ = analizador.analizar(linea.strip())
        t_1 = time.perf_counter()
        estado = "ACEPTADA" if aceptada else "RECHAZADA"
        print(f"{linea} -> {estado} ({t_1 - t_0:.6f} s)")


if __name__ == "__main__":
    principal()
