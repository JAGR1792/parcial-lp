grammar LenguajeNoRelacional;

programa
    : instruccion* EOF
    ;

instruccion
    : crearColeccion PUNTO_Y_COMA?
    | insertar PUNTO_Y_COMA?
    | buscar PUNTO_Y_COMA?
    | actualizar PUNTO_Y_COMA?
    | eliminar PUNTO_Y_COMA?
    | mostrarColecciones PUNTO_Y_COMA?
    ;

crearColeccion
    : CREAR COLECCION IDENTIFICADOR
    ;

insertar
    : INSERTAR EN IDENTIFICADOR objeto
    ;

buscar
    : BUSCAR IDENTIFICADOR condicionDonde?
    ;

actualizar
    : ACTUALIZAR IDENTIFICADOR FIJAR listaAsignaciones condicionDonde?
    ;

eliminar
    : ELIMINAR DE IDENTIFICADOR condicionDonde?
    ;

mostrarColecciones
    : MOSTRAR COLECCIONES
    ;

condicionDonde
    : DONDE expresion
    ;

listaAsignaciones
    : asignacion (COMA asignacion)*
    ;

asignacion
    : IDENTIFICADOR IGUAL expresion
    ;

objeto
    : LLAVE_ABRE (par (COMA par)*)? LLAVE_CIERRA
    ;

par
    : IDENTIFICADOR DOS_PUNTOS expresion
    ;

expresion
    : expresionO
    ;

expresionO
    : expresionY (O expresionY)*
    ;

expresionY
    : expresionIgualdad (Y expresionIgualdad)*
    ;

expresionIgualdad
    : expresionRelacional ((IGUAL_IGUAL | DIFERENTE) expresionRelacional)*
    ;

expresionRelacional
    : primario ((MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL) primario)*
    ;

primario
    : literal
    | IDENTIFICADOR
    | PARENTESIS_ABRE expresion PARENTESIS_CIERRA
    ;

literal
    : CADENA
    | NUMERO
    | BOOLEANO
    | NULO
    ;

CREAR : 'CREAR';
COLECCION : 'COLECCION';
INSERTAR : 'INSERTAR';
EN : 'EN';
BUSCAR : 'BUSCAR';
ACTUALIZAR : 'ACTUALIZAR';
FIJAR : 'FIJAR';
ELIMINAR : 'ELIMINAR';
DE : 'DE';
MOSTRAR : 'MOSTRAR';
COLECCIONES : 'COLECCIONES';
DONDE : 'DONDE';
O : 'O';
Y : 'Y';
BOOLEANO : 'verdadero' | 'falso';
NULO : 'nulo';

IGUAL_IGUAL : '==';
DIFERENTE : '!=';
MENOR_IGUAL : '<=';
MAYOR_IGUAL : '>=';
MENOR : '<';
MAYOR : '>';
IGUAL : '=';
DOS_PUNTOS : ':';
COMA : ',';
PUNTO_Y_COMA : ';';
PARENTESIS_ABRE : '(';
PARENTESIS_CIERRA : ')';
LLAVE_ABRE : '{';
LLAVE_CIERRA : '}';

IDENTIFICADOR
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

NUMERO
    : '-'? [0-9]+ ('.' [0-9]+)?
    ;

CADENA
    : '"' ( '\\' . | ~["\\] )* '"'
    ;

COMENTARIO_LINEA
    : '//' ~[\r\n]* -> skip
    ;

COMENTARIO_BLOQUE
    : '/*' .*? '*/' -> skip
    ;

ESPACIO
    : [ \t\r\n]+ -> skip
    ;