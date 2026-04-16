from __future__ import annotations

import sys
from pathlib import Path

from antlr4 import CommonTokenStream, InputStream

RAIZ = Path(__file__).resolve().parents[1]
if str(RAIZ) not in sys.path:
    sys.path.insert(0, str(RAIZ))
GENERADO = RAIZ / "generado"
if str(GENERADO) not in sys.path:
    sys.path.insert(0, str(GENERADO))

from LenguajeNoRelacionalLexer import LenguajeNoRelacionalLexer
from LenguajeNoRelacionalParser import LenguajeNoRelacionalParser

from visitante_evaluacion import VisitanteEvaluacion


def test_programa_crud():
    programa = """
    CREAR COLECCION usuarios;
    INSERTAR EN usuarios { nombre: "Ana", edad: 20, activo: verdadero };
    INSERTAR EN usuarios { nombre: "Luis", edad: 17, activo: falso };
    BUSCAR usuarios DONDE edad >= 18;
    ACTUALIZAR usuarios FIJAR activo = falso DONDE nombre == "Ana";
    ELIMINAR DE usuarios DONDE edad < 18;
    """

    lexer = LenguajeNoRelacionalLexer(InputStream(programa))
    parser = LenguajeNoRelacionalParser(CommonTokenStream(lexer))
    visitante = VisitanteEvaluacion()
    visitante.visit(parser.programa())

    assert "usuarios" in visitante.colecciones
    assert len(visitante.colecciones["usuarios"]) == 1
    assert visitante.colecciones["usuarios"][0]["nombre"] == "Ana"
    assert visitante.colecciones["usuarios"][0]["activo"] is False