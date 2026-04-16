# Generated from /home/antonio/Downloads/PARCIAL_LP/punto_1/gramatica/LenguajeNoRelacional.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LenguajeNoRelacionalParser import LenguajeNoRelacionalParser
else:
    from LenguajeNoRelacionalParser import LenguajeNoRelacionalParser

# This class defines a complete generic visitor for a parse tree produced by LenguajeNoRelacionalParser.

class LenguajeNoRelacionalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LenguajeNoRelacionalParser#programa.
    def visitPrograma(self, ctx:LenguajeNoRelacionalParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#instruccion.
    def visitInstruccion(self, ctx:LenguajeNoRelacionalParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#crearColeccion.
    def visitCrearColeccion(self, ctx:LenguajeNoRelacionalParser.CrearColeccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#insertar.
    def visitInsertar(self, ctx:LenguajeNoRelacionalParser.InsertarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#buscar.
    def visitBuscar(self, ctx:LenguajeNoRelacionalParser.BuscarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#actualizar.
    def visitActualizar(self, ctx:LenguajeNoRelacionalParser.ActualizarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#eliminar.
    def visitEliminar(self, ctx:LenguajeNoRelacionalParser.EliminarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#condicionDonde.
    def visitCondicionDonde(self, ctx:LenguajeNoRelacionalParser.CondicionDondeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#listaAsignaciones.
    def visitListaAsignaciones(self, ctx:LenguajeNoRelacionalParser.ListaAsignacionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#asignacion.
    def visitAsignacion(self, ctx:LenguajeNoRelacionalParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#objeto.
    def visitObjeto(self, ctx:LenguajeNoRelacionalParser.ObjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#par.
    def visitPar(self, ctx:LenguajeNoRelacionalParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#expresion.
    def visitExpresion(self, ctx:LenguajeNoRelacionalParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#expresionO.
    def visitExpresionO(self, ctx:LenguajeNoRelacionalParser.ExpresionOContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#expresionY.
    def visitExpresionY(self, ctx:LenguajeNoRelacionalParser.ExpresionYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#expresionIgualdad.
    def visitExpresionIgualdad(self, ctx:LenguajeNoRelacionalParser.ExpresionIgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#expresionRelacional.
    def visitExpresionRelacional(self, ctx:LenguajeNoRelacionalParser.ExpresionRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#primario.
    def visitPrimario(self, ctx:LenguajeNoRelacionalParser.PrimarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeNoRelacionalParser#literal.
    def visitLiteral(self, ctx:LenguajeNoRelacionalParser.LiteralContext):
        return self.visitChildren(ctx)



del LenguajeNoRelacionalParser