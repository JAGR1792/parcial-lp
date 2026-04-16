from __future__ import annotations

import sys
from pathlib import Path

from antlr4 import CommonTokenStream, InputStream

RAIZ = Path(__file__).resolve().parent
GENERADO = RAIZ / "generado"
if str(GENERADO) not in sys.path:
    sys.path.insert(0, str(GENERADO))

from LenguajeNoRelacionalLexer import LenguajeNoRelacionalLexer
from LenguajeNoRelacionalParser import LenguajeNoRelacionalParser

from visitante_evaluacion import VisitanteEvaluacion


def ejecutar_programa(texto_programa: str) -> VisitanteEvaluacion:
    lexer = LenguajeNoRelacionalLexer(InputStream(texto_programa))
    parser = LenguajeNoRelacionalParser(CommonTokenStream(lexer))
    visitante = VisitanteEvaluacion()
    visitante.visit(parser.programa())
    return visitante


def principal() -> None:
    if len(sys.argv) > 1:
        ruta_programa = Path(sys.argv[1])
        texto_programa = ruta_programa.read_text(encoding="utf-8")
    else:
        texto_programa = sys.stdin.read()

    ejecutar_programa(texto_programa)


if __name__ == "__main__":
    principal()