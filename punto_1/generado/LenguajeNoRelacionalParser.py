# Generated from /home/antonio/Downloads/PARCIAL_LP/punto_1/gramatica/LenguajeNoRelacional.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,181,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,1,1,1,3,1,51,8,1,1,1,1,1,3,
        1,55,8,1,1,1,1,1,3,1,59,8,1,1,1,1,1,3,1,63,8,1,1,1,1,1,3,1,67,8,
        1,1,1,1,1,3,1,71,8,1,3,1,73,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,3,4,87,8,4,1,5,1,5,1,5,1,5,1,5,3,5,94,8,5,1,6,1,
        6,1,6,1,6,3,6,100,8,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,5,9,111,
        8,9,10,9,12,9,114,9,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,5,
        11,124,8,11,10,11,12,11,127,9,11,3,11,129,8,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,13,1,13,1,14,1,14,1,14,5,14,142,8,14,10,14,12,14,
        145,9,14,1,15,1,15,1,15,5,15,150,8,15,10,15,12,15,153,9,15,1,16,
        1,16,1,16,5,16,158,8,16,10,16,12,16,161,9,16,1,17,1,17,1,17,5,17,
        166,8,17,10,17,12,17,169,9,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,
        177,8,18,1,19,1,19,1,19,0,0,20,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,0,3,1,0,17,18,1,0,19,22,2,0,15,16,32,33,184,
        0,43,1,0,0,0,2,72,1,0,0,0,4,74,1,0,0,0,6,78,1,0,0,0,8,83,1,0,0,0,
        10,88,1,0,0,0,12,95,1,0,0,0,14,101,1,0,0,0,16,104,1,0,0,0,18,107,
        1,0,0,0,20,115,1,0,0,0,22,119,1,0,0,0,24,132,1,0,0,0,26,136,1,0,
        0,0,28,138,1,0,0,0,30,146,1,0,0,0,32,154,1,0,0,0,34,162,1,0,0,0,
        36,176,1,0,0,0,38,178,1,0,0,0,40,42,3,2,1,0,41,40,1,0,0,0,42,45,
        1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,
        46,47,5,0,0,1,47,1,1,0,0,0,48,50,3,4,2,0,49,51,5,26,0,0,50,49,1,
        0,0,0,50,51,1,0,0,0,51,73,1,0,0,0,52,54,3,6,3,0,53,55,5,26,0,0,54,
        53,1,0,0,0,54,55,1,0,0,0,55,73,1,0,0,0,56,58,3,8,4,0,57,59,5,26,
        0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,73,1,0,0,0,60,62,3,10,5,0,61,
        63,5,26,0,0,62,61,1,0,0,0,62,63,1,0,0,0,63,73,1,0,0,0,64,66,3,12,
        6,0,65,67,5,26,0,0,66,65,1,0,0,0,66,67,1,0,0,0,67,73,1,0,0,0,68,
        70,3,14,7,0,69,71,5,26,0,0,70,69,1,0,0,0,70,71,1,0,0,0,71,73,1,0,
        0,0,72,48,1,0,0,0,72,52,1,0,0,0,72,56,1,0,0,0,72,60,1,0,0,0,72,64,
        1,0,0,0,72,68,1,0,0,0,73,3,1,0,0,0,74,75,5,1,0,0,75,76,5,2,0,0,76,
        77,5,31,0,0,77,5,1,0,0,0,78,79,5,3,0,0,79,80,5,4,0,0,80,81,5,31,
        0,0,81,82,3,22,11,0,82,7,1,0,0,0,83,84,5,5,0,0,84,86,5,31,0,0,85,
        87,3,16,8,0,86,85,1,0,0,0,86,87,1,0,0,0,87,9,1,0,0,0,88,89,5,6,0,
        0,89,90,5,31,0,0,90,91,5,7,0,0,91,93,3,18,9,0,92,94,3,16,8,0,93,
        92,1,0,0,0,93,94,1,0,0,0,94,11,1,0,0,0,95,96,5,8,0,0,96,97,5,9,0,
        0,97,99,5,31,0,0,98,100,3,16,8,0,99,98,1,0,0,0,99,100,1,0,0,0,100,
        13,1,0,0,0,101,102,5,10,0,0,102,103,5,11,0,0,103,15,1,0,0,0,104,
        105,5,12,0,0,105,106,3,26,13,0,106,17,1,0,0,0,107,112,3,20,10,0,
        108,109,5,25,0,0,109,111,3,20,10,0,110,108,1,0,0,0,111,114,1,0,0,
        0,112,110,1,0,0,0,112,113,1,0,0,0,113,19,1,0,0,0,114,112,1,0,0,0,
        115,116,5,31,0,0,116,117,5,23,0,0,117,118,3,26,13,0,118,21,1,0,0,
        0,119,128,5,29,0,0,120,125,3,24,12,0,121,122,5,25,0,0,122,124,3,
        24,12,0,123,121,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,
        1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,128,120,1,0,0,0,128,129,
        1,0,0,0,129,130,1,0,0,0,130,131,5,30,0,0,131,23,1,0,0,0,132,133,
        5,31,0,0,133,134,5,24,0,0,134,135,3,26,13,0,135,25,1,0,0,0,136,137,
        3,28,14,0,137,27,1,0,0,0,138,143,3,30,15,0,139,140,5,13,0,0,140,
        142,3,30,15,0,141,139,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,
        144,1,0,0,0,144,29,1,0,0,0,145,143,1,0,0,0,146,151,3,32,16,0,147,
        148,5,14,0,0,148,150,3,32,16,0,149,147,1,0,0,0,150,153,1,0,0,0,151,
        149,1,0,0,0,151,152,1,0,0,0,152,31,1,0,0,0,153,151,1,0,0,0,154,159,
        3,34,17,0,155,156,7,0,0,0,156,158,3,34,17,0,157,155,1,0,0,0,158,
        161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,33,1,0,0,0,161,159,
        1,0,0,0,162,167,3,36,18,0,163,164,7,1,0,0,164,166,3,36,18,0,165,
        163,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,
        35,1,0,0,0,169,167,1,0,0,0,170,177,3,38,19,0,171,177,5,31,0,0,172,
        173,5,27,0,0,173,174,3,26,13,0,174,175,5,28,0,0,175,177,1,0,0,0,
        176,170,1,0,0,0,176,171,1,0,0,0,176,172,1,0,0,0,177,37,1,0,0,0,178,
        179,7,2,0,0,179,39,1,0,0,0,19,43,50,54,58,62,66,70,72,86,93,99,112,
        125,128,143,151,159,167,176
    ]

class LenguajeNoRelacionalParser ( Parser ):

    grammarFileName = "LenguajeNoRelacional.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREAR'", "'COLECCION'", "'INSERTAR'", 
                     "'EN'", "'BUSCAR'", "'ACTUALIZAR'", "'FIJAR'", "'ELIMINAR'", 
                     "'DE'", "'MOSTRAR'", "'COLECCIONES'", "'DONDE'", "'O'", 
                     "'Y'", "<INVALID>", "'nulo'", "'=='", "'!='", "'<='", 
                     "'>='", "'<'", "'>'", "'='", "':'", "','", "';'", "'('", 
                     "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "CREAR", "COLECCION", "INSERTAR", "EN", 
                      "BUSCAR", "ACTUALIZAR", "FIJAR", "ELIMINAR", "DE", 
                      "MOSTRAR", "COLECCIONES", "DONDE", "O", "Y", "BOOLEANO", 
                      "NULO", "IGUAL_IGUAL", "DIFERENTE", "MENOR_IGUAL", 
                      "MAYOR_IGUAL", "MENOR", "MAYOR", "IGUAL", "DOS_PUNTOS", 
                      "COMA", "PUNTO_Y_COMA", "PARENTESIS_ABRE", "PARENTESIS_CIERRA", 
                      "LLAVE_ABRE", "LLAVE_CIERRA", "IDENTIFICADOR", "NUMERO", 
                      "CADENA", "COMENTARIO_LINEA", "COMENTARIO_BLOQUE", 
                      "ESPACIO" ]

    RULE_programa = 0
    RULE_instruccion = 1
    RULE_crearColeccion = 2
    RULE_insertar = 3
    RULE_buscar = 4
    RULE_actualizar = 5
    RULE_eliminar = 6
    RULE_mostrarColecciones = 7
    RULE_condicionDonde = 8
    RULE_listaAsignaciones = 9
    RULE_asignacion = 10
    RULE_objeto = 11
    RULE_par = 12
    RULE_expresion = 13
    RULE_expresionO = 14
    RULE_expresionY = 15
    RULE_expresionIgualdad = 16
    RULE_expresionRelacional = 17
    RULE_primario = 18
    RULE_literal = 19

    ruleNames =  [ "programa", "instruccion", "crearColeccion", "insertar", 
                   "buscar", "actualizar", "eliminar", "mostrarColecciones", 
                   "condicionDonde", "listaAsignaciones", "asignacion", 
                   "objeto", "par", "expresion", "expresionO", "expresionY", 
                   "expresionIgualdad", "expresionRelacional", "primario", 
                   "literal" ]

    EOF = Token.EOF
    CREAR=1
    COLECCION=2
    INSERTAR=3
    EN=4
    BUSCAR=5
    ACTUALIZAR=6
    FIJAR=7
    ELIMINAR=8
    DE=9
    MOSTRAR=10
    COLECCIONES=11
    DONDE=12
    O=13
    Y=14
    BOOLEANO=15
    NULO=16
    IGUAL_IGUAL=17
    DIFERENTE=18
    MENOR_IGUAL=19
    MAYOR_IGUAL=20
    MENOR=21
    MAYOR=22
    IGUAL=23
    DOS_PUNTOS=24
    COMA=25
    PUNTO_Y_COMA=26
    PARENTESIS_ABRE=27
    PARENTESIS_CIERRA=28
    LLAVE_ABRE=29
    LLAVE_CIERRA=30
    IDENTIFICADOR=31
    NUMERO=32
    CADENA=33
    COMENTARIO_LINEA=34
    COMENTARIO_BLOQUE=35
    ESPACIO=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LenguajeNoRelacionalParser.EOF, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeNoRelacionalParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(LenguajeNoRelacionalParser.InstruccionContext,i)


        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = LenguajeNoRelacionalParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1386) != 0):
                self.state = 40
                self.instruccion()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(LenguajeNoRelacionalParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def crearColeccion(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.CrearColeccionContext,0)


        def PUNTO_Y_COMA(self):
            return self.getToken(LenguajeNoRelacionalParser.PUNTO_Y_COMA, 0)

        def insertar(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.InsertarContext,0)


        def buscar(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.BuscarContext,0)


        def actualizar(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.ActualizarContext,0)


        def eliminar(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.EliminarContext,0)


        def mostrarColecciones(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.MostrarColeccionesContext,0)


        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = LenguajeNoRelacionalParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        self._la = 0 # Token type
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.crearColeccion()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 49
                    self.match(LenguajeNoRelacionalParser.PUNTO_Y_COMA)


                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.insertar()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 53
                    self.match(LenguajeNoRelacionalParser.PUNTO_Y_COMA)


                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.buscar()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 57
                    self.match(LenguajeNoRelacionalParser.PUNTO_Y_COMA)


                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.actualizar()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 61
                    self.match(LenguajeNoRelacionalParser.PUNTO_Y_COMA)


                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.eliminar()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 65
                    self.match(LenguajeNoRelacionalParser.PUNTO_Y_COMA)


                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 68
                self.mostrarColecciones()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 69
                    self.match(LenguajeNoRelacionalParser.PUNTO_Y_COMA)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CrearColeccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREAR(self):
            return self.getToken(LenguajeNoRelacionalParser.CREAR, 0)

        def COLECCION(self):
            return self.getToken(LenguajeNoRelacionalParser.COLECCION, 0)

        def IDENTIFICADOR(self):
            return self.getToken(LenguajeNoRelacionalParser.IDENTIFICADOR, 0)

        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_crearColeccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCrearColeccion" ):
                listener.enterCrearColeccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCrearColeccion" ):
                listener.exitCrearColeccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCrearColeccion" ):
                return visitor.visitCrearColeccion(self)
            else:
                return visitor.visitChildren(self)




    def crearColeccion(self):

        localctx = LenguajeNoRelacionalParser.CrearColeccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_crearColeccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(LenguajeNoRelacionalParser.CREAR)
            self.state = 75
            self.match(LenguajeNoRelacionalParser.COLECCION)
            self.state = 76
            self.match(LenguajeNoRelacionalParser.IDENTIFICADOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERTAR(self):
            return self.getToken(LenguajeNoRelacionalParser.INSERTAR, 0)

        def EN(self):
            return self.getToken(LenguajeNoRelacionalParser.EN, 0)

        def IDENTIFICADOR(self):
            return self.getToken(LenguajeNoRelacionalParser.IDENTIFICADOR, 0)

        def objeto(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.ObjetoContext,0)


        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_insertar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsertar" ):
                listener.enterInsertar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsertar" ):
                listener.exitInsertar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertar" ):
                return visitor.visitInsertar(self)
            else:
                return visitor.visitChildren(self)




    def insertar(self):

        localctx = LenguajeNoRelacionalParser.InsertarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_insertar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(LenguajeNoRelacionalParser.INSERTAR)
            self.state = 79
            self.match(LenguajeNoRelacionalParser.EN)
            self.state = 80
            self.match(LenguajeNoRelacionalParser.IDENTIFICADOR)
            self.state = 81
            self.objeto()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BuscarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BUSCAR(self):
            return self.getToken(LenguajeNoRelacionalParser.BUSCAR, 0)

        def IDENTIFICADOR(self):
            return self.getToken(LenguajeNoRelacionalParser.IDENTIFICADOR, 0)

        def condicionDonde(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.CondicionDondeContext,0)


        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_buscar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuscar" ):
                listener.enterBuscar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuscar" ):
                listener.exitBuscar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuscar" ):
                return visitor.visitBuscar(self)
            else:
                return visitor.visitChildren(self)




    def buscar(self):

        localctx = LenguajeNoRelacionalParser.BuscarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_buscar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(LenguajeNoRelacionalParser.BUSCAR)
            self.state = 84
            self.match(LenguajeNoRelacionalParser.IDENTIFICADOR)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 85
                self.condicionDonde()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActualizarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTUALIZAR(self):
            return self.getToken(LenguajeNoRelacionalParser.ACTUALIZAR, 0)

        def IDENTIFICADOR(self):
            return self.getToken(LenguajeNoRelacionalParser.IDENTIFICADOR, 0)

        def FIJAR(self):
            return self.getToken(LenguajeNoRelacionalParser.FIJAR, 0)

        def listaAsignaciones(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.ListaAsignacionesContext,0)


        def condicionDonde(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.CondicionDondeContext,0)


        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_actualizar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActualizar" ):
                listener.enterActualizar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActualizar" ):
                listener.exitActualizar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActualizar" ):
                return visitor.visitActualizar(self)
            else:
                return visitor.visitChildren(self)




    def actualizar(self):

        localctx = LenguajeNoRelacionalParser.ActualizarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_actualizar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(LenguajeNoRelacionalParser.ACTUALIZAR)
            self.state = 89
            self.match(LenguajeNoRelacionalParser.IDENTIFICADOR)
            self.state = 90
            self.match(LenguajeNoRelacionalParser.FIJAR)
            self.state = 91
            self.listaAsignaciones()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 92
                self.condicionDonde()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliminarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIMINAR(self):
            return self.getToken(LenguajeNoRelacionalParser.ELIMINAR, 0)

        def DE(self):
            return self.getToken(LenguajeNoRelacionalParser.DE, 0)

        def IDENTIFICADOR(self):
            return self.getToken(LenguajeNoRelacionalParser.IDENTIFICADOR, 0)

        def condicionDonde(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.CondicionDondeContext,0)


        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_eliminar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEliminar" ):
                listener.enterEliminar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEliminar" ):
                listener.exitEliminar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliminar" ):
                return visitor.visitEliminar(self)
            else:
                return visitor.visitChildren(self)




    def eliminar(self):

        localctx = LenguajeNoRelacionalParser.EliminarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_eliminar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(LenguajeNoRelacionalParser.ELIMINAR)
            self.state = 96
            self.match(LenguajeNoRelacionalParser.DE)
            self.state = 97
            self.match(LenguajeNoRelacionalParser.IDENTIFICADOR)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 98
                self.condicionDonde()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MostrarColeccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOSTRAR(self):
            return self.getToken(LenguajeNoRelacionalParser.MOSTRAR, 0)

        def COLECCIONES(self):
            return self.getToken(LenguajeNoRelacionalParser.COLECCIONES, 0)

        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_mostrarColecciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMostrarColecciones" ):
                listener.enterMostrarColecciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMostrarColecciones" ):
                listener.exitMostrarColecciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMostrarColecciones" ):
                return visitor.visitMostrarColecciones(self)
            else:
                return visitor.visitChildren(self)




    def mostrarColecciones(self):

        localctx = LenguajeNoRelacionalParser.MostrarColeccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mostrarColecciones)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(LenguajeNoRelacionalParser.MOSTRAR)
            self.state = 102
            self.match(LenguajeNoRelacionalParser.COLECCIONES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionDondeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DONDE(self):
            return self.getToken(LenguajeNoRelacionalParser.DONDE, 0)

        def expresion(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.ExpresionContext,0)


        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_condicionDonde

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicionDonde" ):
                listener.enterCondicionDonde(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicionDonde" ):
                listener.exitCondicionDonde(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicionDonde" ):
                return visitor.visitCondicionDonde(self)
            else:
                return visitor.visitChildren(self)




    def condicionDonde(self):

        localctx = LenguajeNoRelacionalParser.CondicionDondeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condicionDonde)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(LenguajeNoRelacionalParser.DONDE)
            self.state = 105
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaAsignacionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeNoRelacionalParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(LenguajeNoRelacionalParser.AsignacionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeNoRelacionalParser.COMA)
            else:
                return self.getToken(LenguajeNoRelacionalParser.COMA, i)

        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_listaAsignaciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaAsignaciones" ):
                listener.enterListaAsignaciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaAsignaciones" ):
                listener.exitListaAsignaciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaAsignaciones" ):
                return visitor.visitListaAsignaciones(self)
            else:
                return visitor.visitChildren(self)




    def listaAsignaciones(self):

        localctx = LenguajeNoRelacionalParser.ListaAsignacionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_listaAsignaciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.asignacion()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 108
                self.match(LenguajeNoRelacionalParser.COMA)
                self.state = 109
                self.asignacion()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(LenguajeNoRelacionalParser.IDENTIFICADOR, 0)

        def IGUAL(self):
            return self.getToken(LenguajeNoRelacionalParser.IGUAL, 0)

        def expresion(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.ExpresionContext,0)


        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = LenguajeNoRelacionalParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(LenguajeNoRelacionalParser.IDENTIFICADOR)
            self.state = 116
            self.match(LenguajeNoRelacionalParser.IGUAL)
            self.state = 117
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjetoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE_ABRE(self):
            return self.getToken(LenguajeNoRelacionalParser.LLAVE_ABRE, 0)

        def LLAVE_CIERRA(self):
            return self.getToken(LenguajeNoRelacionalParser.LLAVE_CIERRA, 0)

        def par(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeNoRelacionalParser.ParContext)
            else:
                return self.getTypedRuleContext(LenguajeNoRelacionalParser.ParContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeNoRelacionalParser.COMA)
            else:
                return self.getToken(LenguajeNoRelacionalParser.COMA, i)

        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_objeto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjeto" ):
                listener.enterObjeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjeto" ):
                listener.exitObjeto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjeto" ):
                return visitor.visitObjeto(self)
            else:
                return visitor.visitChildren(self)




    def objeto(self):

        localctx = LenguajeNoRelacionalParser.ObjetoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_objeto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(LenguajeNoRelacionalParser.LLAVE_ABRE)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 120
                self.par()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 121
                    self.match(LenguajeNoRelacionalParser.COMA)
                    self.state = 122
                    self.par()
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 130
            self.match(LenguajeNoRelacionalParser.LLAVE_CIERRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(LenguajeNoRelacionalParser.IDENTIFICADOR, 0)

        def DOS_PUNTOS(self):
            return self.getToken(LenguajeNoRelacionalParser.DOS_PUNTOS, 0)

        def expresion(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.ExpresionContext,0)


        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_par

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar" ):
                return visitor.visitPar(self)
            else:
                return visitor.visitChildren(self)




    def par(self):

        localctx = LenguajeNoRelacionalParser.ParContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_par)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(LenguajeNoRelacionalParser.IDENTIFICADOR)
            self.state = 133
            self.match(LenguajeNoRelacionalParser.DOS_PUNTOS)
            self.state = 134
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionO(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.ExpresionOContext,0)


        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = LenguajeNoRelacionalParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.expresionO()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionOContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionY(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeNoRelacionalParser.ExpresionYContext)
            else:
                return self.getTypedRuleContext(LenguajeNoRelacionalParser.ExpresionYContext,i)


        def O(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeNoRelacionalParser.O)
            else:
                return self.getToken(LenguajeNoRelacionalParser.O, i)

        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_expresionO

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionO" ):
                listener.enterExpresionO(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionO" ):
                listener.exitExpresionO(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionO" ):
                return visitor.visitExpresionO(self)
            else:
                return visitor.visitChildren(self)




    def expresionO(self):

        localctx = LenguajeNoRelacionalParser.ExpresionOContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expresionO)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.expresionY()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 139
                self.match(LenguajeNoRelacionalParser.O)
                self.state = 140
                self.expresionY()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionYContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionIgualdad(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeNoRelacionalParser.ExpresionIgualdadContext)
            else:
                return self.getTypedRuleContext(LenguajeNoRelacionalParser.ExpresionIgualdadContext,i)


        def Y(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeNoRelacionalParser.Y)
            else:
                return self.getToken(LenguajeNoRelacionalParser.Y, i)

        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_expresionY

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionY" ):
                listener.enterExpresionY(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionY" ):
                listener.exitExpresionY(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionY" ):
                return visitor.visitExpresionY(self)
            else:
                return visitor.visitChildren(self)




    def expresionY(self):

        localctx = LenguajeNoRelacionalParser.ExpresionYContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expresionY)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.expresionIgualdad()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 147
                self.match(LenguajeNoRelacionalParser.Y)
                self.state = 148
                self.expresionIgualdad()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionIgualdadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionRelacional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeNoRelacionalParser.ExpresionRelacionalContext)
            else:
                return self.getTypedRuleContext(LenguajeNoRelacionalParser.ExpresionRelacionalContext,i)


        def IGUAL_IGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeNoRelacionalParser.IGUAL_IGUAL)
            else:
                return self.getToken(LenguajeNoRelacionalParser.IGUAL_IGUAL, i)

        def DIFERENTE(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeNoRelacionalParser.DIFERENTE)
            else:
                return self.getToken(LenguajeNoRelacionalParser.DIFERENTE, i)

        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_expresionIgualdad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionIgualdad" ):
                listener.enterExpresionIgualdad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionIgualdad" ):
                listener.exitExpresionIgualdad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionIgualdad" ):
                return visitor.visitExpresionIgualdad(self)
            else:
                return visitor.visitChildren(self)




    def expresionIgualdad(self):

        localctx = LenguajeNoRelacionalParser.ExpresionIgualdadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expresionIgualdad)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.expresionRelacional()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 155
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 156
                self.expresionRelacional()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionRelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeNoRelacionalParser.PrimarioContext)
            else:
                return self.getTypedRuleContext(LenguajeNoRelacionalParser.PrimarioContext,i)


        def MENOR(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeNoRelacionalParser.MENOR)
            else:
                return self.getToken(LenguajeNoRelacionalParser.MENOR, i)

        def MENOR_IGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeNoRelacionalParser.MENOR_IGUAL)
            else:
                return self.getToken(LenguajeNoRelacionalParser.MENOR_IGUAL, i)

        def MAYOR(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeNoRelacionalParser.MAYOR)
            else:
                return self.getToken(LenguajeNoRelacionalParser.MAYOR, i)

        def MAYOR_IGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeNoRelacionalParser.MAYOR_IGUAL)
            else:
                return self.getToken(LenguajeNoRelacionalParser.MAYOR_IGUAL, i)

        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_expresionRelacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionRelacional" ):
                listener.enterExpresionRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionRelacional" ):
                listener.exitExpresionRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionRelacional" ):
                return visitor.visitExpresionRelacional(self)
            else:
                return visitor.visitChildren(self)




    def expresionRelacional(self):

        localctx = LenguajeNoRelacionalParser.ExpresionRelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expresionRelacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.primario()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0):
                self.state = 163
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 164
                self.primario()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.LiteralContext,0)


        def IDENTIFICADOR(self):
            return self.getToken(LenguajeNoRelacionalParser.IDENTIFICADOR, 0)

        def PARENTESIS_ABRE(self):
            return self.getToken(LenguajeNoRelacionalParser.PARENTESIS_ABRE, 0)

        def expresion(self):
            return self.getTypedRuleContext(LenguajeNoRelacionalParser.ExpresionContext,0)


        def PARENTESIS_CIERRA(self):
            return self.getToken(LenguajeNoRelacionalParser.PARENTESIS_CIERRA, 0)

        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_primario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimario" ):
                listener.enterPrimario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimario" ):
                listener.exitPrimario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimario" ):
                return visitor.visitPrimario(self)
            else:
                return visitor.visitChildren(self)




    def primario(self):

        localctx = LenguajeNoRelacionalParser.PrimarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primario)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.literal()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(LenguajeNoRelacionalParser.IDENTIFICADOR)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.match(LenguajeNoRelacionalParser.PARENTESIS_ABRE)
                self.state = 173
                self.expresion()
                self.state = 174
                self.match(LenguajeNoRelacionalParser.PARENTESIS_CIERRA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADENA(self):
            return self.getToken(LenguajeNoRelacionalParser.CADENA, 0)

        def NUMERO(self):
            return self.getToken(LenguajeNoRelacionalParser.NUMERO, 0)

        def BOOLEANO(self):
            return self.getToken(LenguajeNoRelacionalParser.BOOLEANO, 0)

        def NULO(self):
            return self.getToken(LenguajeNoRelacionalParser.NULO, 0)

        def getRuleIndex(self):
            return LenguajeNoRelacionalParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = LenguajeNoRelacionalParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 12885000192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





