from __future__ import annotations

from collections import OrderedDict
from decimal import Decimal
from typing import Any

from antlr4 import ParseTreeVisitor


class VisitanteEvaluacion(ParseTreeVisitor):
    def __init__(self) -> None:
        self.colecciones: dict[str, list[dict[str, Any]]] = OrderedDict()
        self.documento_actual: dict[str, Any] | None = None

    def visitPrograma(self, ctx):
        for instruccion in ctx.instruccion():
            self.visit(instruccion)
        return None

    def visitCrearColeccion(self, ctx):
        nombre_coleccion = ctx.IDENTIFICADOR().getText()
        self.colecciones.setdefault(nombre_coleccion, [])
        print(f"Coleccion creada: {nombre_coleccion}")
        return None

    def visitInsertar(self, ctx):
        nombre_coleccion = ctx.IDENTIFICADOR().getText()
        documento = self.visit(ctx.objeto())
        self.colecciones.setdefault(nombre_coleccion, []).append(documento)
        print(f"Insertado en {nombre_coleccion}: {documento}")
        return documento

    def visitBuscar(self, ctx):
        nombre_coleccion = ctx.IDENTIFICADOR().getText()
        documentos = self.colecciones.get(nombre_coleccion, [])
        coincidencias = [documento for documento in documentos if self._cumple_condicion(ctx.condicionDonde(), documento)]
        print(f"Consulta en {nombre_coleccion}: {coincidencias}")
        return coincidencias

    def visitActualizar(self, ctx):
        nombre_coleccion = ctx.IDENTIFICADOR().getText()
        documentos = self.colecciones.get(nombre_coleccion, [])
        cambios = self.visit(ctx.listaAsignaciones())
        actualizados = 0

        for documento in documentos:
            if self._cumple_condicion(ctx.condicionDonde(), documento):
                documento.update(cambios)
                actualizados += 1

        print(f"Actualizacion en {nombre_coleccion}: {actualizados} documentos")
        return actualizados

    def visitEliminar(self, ctx):
        nombre_coleccion = ctx.IDENTIFICADOR().getText()
        documentos = self.colecciones.get(nombre_coleccion, [])
        antes = len(documentos)
        documentos[:] = [documento for documento in documentos if not self._cumple_condicion(ctx.condicionDonde(), documento)]
        eliminados = antes - len(documentos)
        print(f"Eliminacion en {nombre_coleccion}: {eliminados} documentos")
        return eliminados

    def visitMostrarColecciones(self, ctx):
        print(f"Colecciones: {list(self.colecciones.keys())}")
        return list(self.colecciones.keys())

    def visitObjeto(self, ctx):
        documento: dict[str, Any] = {}
        for par in ctx.par():
            documento[par.IDENTIFICADOR().getText()] = self.visit(par.expresion())
        return documento

    def visitListaAsignaciones(self, ctx):
        cambios: dict[str, Any] = {}
        for asignacion in ctx.asignacion():
            cambios[asignacion.IDENTIFICADOR().getText()] = self.visit(asignacion.expresion())
        return cambios

    def visitExpresion(self, ctx):
        return self.visit(ctx.expresionO())

    def visitExpresionO(self, ctx):
        resultado = self.visit(ctx.expresionY(0))
        if len(ctx.expresionY()) == 1:
            return resultado

        for indice in range(1, len(ctx.expresionY())):
            if self._como_booleano(resultado):
                return True
            resultado = self.visit(ctx.expresionY(indice))
        return self._como_booleano(resultado)

    def visitExpresionY(self, ctx):
        resultado = self.visit(ctx.expresionIgualdad(0))
        if len(ctx.expresionIgualdad()) == 1:
            return resultado

        for indice in range(1, len(ctx.expresionIgualdad())):
            if not self._como_booleano(resultado):
                return False
            resultado = self.visit(ctx.expresionIgualdad(indice))
        return self._como_booleano(resultado)

    def visitExpresionIgualdad(self, ctx):
        izquierdo = self.visit(ctx.expresionRelacional(0))
        if len(ctx.expresionRelacional()) == 1:
            return izquierdo

        for indice in range(1, len(ctx.expresionRelacional())):
            derecho = self.visit(ctx.expresionRelacional(indice))
            operador = ctx.getChild(2 * indice - 1).getText()
            izquierdo = self._iguales(izquierdo, derecho) if operador == '==' else not self._iguales(izquierdo, derecho)
        return izquierdo

    def visitExpresionRelacional(self, ctx):
        izquierdo = self.visit(ctx.primario(0))
        if len(ctx.primario()) == 1:
            return izquierdo

        for indice in range(1, len(ctx.primario())):
            derecho = self.visit(ctx.primario(indice))
            operador = ctx.getChild(2 * indice - 1).getText()
            comparacion = self._comparar(izquierdo, derecho)
            izquierdo = {
                '<': comparacion < 0,
                '<=': comparacion <= 0,
                '>': comparacion > 0,
                '>=': comparacion >= 0,
            }[operador]
        return izquierdo

    def visitPrimario(self, ctx):
        if ctx.literal() is not None:
            return self.visit(ctx.literal())
        if ctx.IDENTIFICADOR() is not None:
            if self.documento_actual is None:
                return None
            return self.documento_actual.get(ctx.IDENTIFICADOR().getText())
        return self.visit(ctx.expresion())

    def visitLiteral(self, ctx):
        if ctx.CADENA() is not None:
            return self._desescapar_cadena(ctx.CADENA().getText())
        if ctx.NUMERO() is not None:
            return Decimal(ctx.NUMERO().getText())
        if ctx.BOOLEANO() is not None:
            return ctx.BOOLEANO().getText() == 'verdadero'
        return None

    def _cumple_condicion(self, condicion_ctx, documento: dict[str, Any]) -> bool:
        if condicion_ctx is None:
            return True
        anterior = self.documento_actual
        self.documento_actual = documento
        try:
            return self._como_booleano(self.visit(condicion_ctx.expresion()))
        finally:
            self.documento_actual = anterior

    def _como_booleano(self, valor: Any) -> bool:
        if isinstance(valor, bool):
            return valor
        if isinstance(valor, (int, float, Decimal)):
            return valor != 0
        if isinstance(valor, str):
            return valor != ''
        return valor is not None

    def _iguales(self, izquierdo: Any, derecho: Any) -> bool:
        if isinstance(izquierdo, Decimal) and isinstance(derecho, Decimal):
            return izquierdo == derecho
        return izquierdo == derecho

    def _comparar(self, izquierdo: Any, derecho: Any) -> int:
        if isinstance(izquierdo, Decimal) and isinstance(derecho, Decimal):
            return (izquierdo > derecho) - (izquierdo < derecho)
        if isinstance(izquierdo, str) and isinstance(derecho, str):
            return (izquierdo > derecho) - (izquierdo < derecho)
        if isinstance(izquierdo, bool) and isinstance(derecho, bool):
            return (izquierdo > derecho) - (izquierdo < derecho)
        raise ValueError(f"No se pueden comparar valores: {izquierdo!r} y {derecho!r}")

    def _desescapar_cadena(self, texto_crudo: str) -> str:
        contenido = texto_crudo[1:-1]
        return (
            contenido.replace('\\n', '\n')
            .replace('\\t', '\t')
            .replace('\\r', '\r')
            .replace('\\"', '"')
            .replace('\\\\', '\\')
        )