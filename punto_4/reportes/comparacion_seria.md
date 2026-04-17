# Comparacion: CYK vs Parser Predictivo

## Objetivo

Comparar experimentalmente dos enfoques de análisis sintáctico:
- **CYK**: Algoritmo bottom-up con complejidad $O(n^3)$
- **Parser predictivo LL(1)**: Parser top-down con complejidad $O(n)$

---

## Gramática de Referencia

```antlr
grammar Ejemplo;

expresion : termino ((PLUS | MINUS) termino)* EOF ;
termino   : factor ((MUL | DIV) factor)* ;
factor    : NUM | LPAREN expresion RPAREN ;

PLUS   : '+' ;
MINUS  : '-' ;
MUL    : '*' ;
DIV    : '/' ;
LPAREN : '(' ;
RPAREN : ')' ;
NUM    : [0-9]+ ('.' [0-9]+)? ;
WS     : [ 	
]+ -> skip ;
```

---

## Resultados Experimentales

Total de casos procesados: **38**

| Entrada | Tokens | CYK Estado | Predictivo Estado | Tiempo CYK (s) | Tiempo Predictivo (s) | Ratio CYK/Predictivo |
|---|---:|---|---|---:|---:|---:|
| `2+3` | 3 | ACEPTADA | ACEPTADA | 0.00007838 | 0.00001767 | 4.44x |
| `10-4` | 3 | ACEPTADA | ACEPTADA | 0.00004292 | 0.00001285 | 3.34x |
| `7*8` | 3 | ACEPTADA | ACEPTADA | 0.00004828 | 0.00000903 | 5.35x |
| `9/3` | 3 | ACEPTADA | ACEPTADA | 0.00003661 | 0.00000688 | 5.32x |
| `(2+3)*4` | 7 | ACEPTADA | ACEPTADA | 0.00011198 | 0.00001352 | 8.28x |
| `8/(2+2)` | 7 | ACEPTADA | ACEPTADA | 0.00010826 | 0.00001696 | 6.38x |
| `(10-4)*(6+2)` | 11 | ACEPTADA | ACEPTADA | 0.00023128 | 0.00002509 | 9.22x |
| `18/(3*(2+1))` | 11 | ACEPTADA | ACEPTADA | 0.00021637 | 0.00001792 | 12.07x |
| `5+6*7-8/2` | 9 | ACEPTADA | ACEPTADA | 0.00018782 | 0.00001876 | 10.01x |
| `((1+2)*(3+4))/5` | 15 | ACEPTADA | ACEPTADA | 0.00035194 | 0.00002230 | 15.78x |
| `3+*4` | 4 | RECHAZADA | RECHAZADA | 0.00004427 | 0.00002553 | 1.73x |
| `(5+2` | 4 | RECHAZADA | RECHAZADA | 0.00004534 | 0.00001165 | 3.89x |
| `9/)3(` | 5 | RECHAZADA | RECHAZADA | 0.00004570 | 0.00001243 | 3.68x |
| `1+2+3+4+5+6+7+8+9+10` | 19 | ACEPTADA | ACEPTADA | 0.00069019 | 0.00002496 | 27.65x |
| `1*2*3*4*5*6*7*8*9*10` | 19 | ACEPTADA | ACEPTADA | 0.00078516 | 0.00002452 | 32.02x |
| `(1+2+3+4+5)*(6+7+8+9)` | 21 | ACEPTADA | ACEPTADA | 0.00076692 | 0.00003023 | 25.37x |
| `((1+2)*(3+4)*(5+6))/(7+8)` | 25 | ACEPTADA | ACEPTADA | 0.00093152 | 0.00005394 | 17.27x |
| `(1+(2*(3+(4*(5+6)))))` | 21 | ACEPTADA | ACEPTADA | 0.00074471 | 0.00006859 | 10.86x |
| `1+2+3+4+5+6+7+8+9+10+11+12+13+14+15` | 29 | ACEPTADA | ACEPTADA | 0.00189479 | 0.00005768 | 32.85x |
| `(1*2)+(3*4)+(5*6)+(7*8)+(9*10)+(11*12)` | 35 | ACEPTADA | ACEPTADA | 0.00317157 | 0.00005590 | 56.74x |
| `((1+2+3+4+5)*(6+7+8+9+10))/(11+12)` | 31 | ACEPTADA | ACEPTADA | 0.00171320 | 0.00006400 | 26.77x |
| `(1+(2+(3+(4+(5+(6+(7+8)))))))` | 29 | ACEPTADA | ACEPTADA | 0.00119653 | 0.00005311 | 22.53x |
| `((2+3)*(4+5)*(6+7)*(8+9))/(10+11)` | 31 | ACEPTADA | ACEPTADA | 0.00138780 | 0.00004806 | 28.88x |
| `1+2*3+4*5+6*7+8*9+10*11+12*13+14*15` | 29 | ACEPTADA | ACEPTADA | 0.00178606 | 0.00004321 | 41.33x |
| `(1+2)*(3+4)*(5+6)*(7+8)*(9+10)` | 29 | ACEPTADA | ACEPTADA | 0.00138455 | 0.00005623 | 24.62x |
| `((1+2+3+4+5+6+7+8+9+10)*2)/(3+4)` | 31 | ACEPTADA | ACEPTADA | 0.00169235 | 0.00005279 | 32.06x |
| `(1+(2*(3+(4*(5+(6*(7+8)))))))` | 29 | ACEPTADA | ACEPTADA | 0.00149135 | 0.00010318 | 14.45x |
| `((1+2)*(3+4)+(5+6)*(7+8)+(9+10)*(11+12))` | 37 | ACEPTADA | ACEPTADA | 0.00270985 | 0.00007904 | 34.28x |
| `1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+1...` | 39 | ACEPTADA | ACEPTADA | 0.00336034 | 0.00005695 | 59.01x |
| `(1*2*3*4*5*6)/(7+8+9+10)` | 23 | ACEPTADA | ACEPTADA | 0.00088216 | 0.00003143 | 28.07x |
| `((1+2+3+4+5+6+7+8)*(9+10+11+12+13+14))/(...` | 39 | ACEPTADA | ACEPTADA | 0.00301663 | 0.00009309 | 32.41x |
| `(1+(2+(3+(4+(5+(6+(7+(8+(9+10)))))))))` | 37 | ACEPTADA | ACEPTADA | 0.00194958 | 0.00006813 | 28.62x |
| `((1+2)*(3+4)*(5+6)*(7+8)*(9+10)*(11+12))...` | 43 | ACEPTADA | ACEPTADA | 0.00336249 | 0.00008063 | 41.70x |
| `1++2` | 4 | RECHAZADA | RECHAZADA | 0.00005649 | 0.00001803 | 3.13x |
| `((3+4)` | 6 | RECHAZADA | RECHAZADA | 0.00007349 | 0.00001678 | 4.38x |
| `8/*2` | 4 | RECHAZADA | RECHAZADA | 0.00003740 | 0.00000798 | 4.69x |
| `(1+2))*3` | 8 | RECHAZADA | RECHAZADA | 0.00010520 | 0.00001428 | 7.37x |
| `42/(7-7)` | 7 | ACEPTADA | ACEPTADA | 0.00009305 | 0.00001140 | 8.16x |


---

## Resultado de la Comparación Gráfica

![Grafica de Comparacion CYK vs Predictivo](../resultados/grafica_comparacion.png)

---

## Análisis Matemático de Rendimiento

### Estadísticas Temporales Promedio

**CYK (Complejidad O(n³)):**
- Tiempo promedio: **0.00096928 s**
- Tiempo mediano: **0.00071745 s**
- Rango: 0.00003661 s - 0.00336249 s

**Predictivo LL(1) (Complejidad O(n)):**
- Tiempo promedio: **0.00003749 s**
- Tiempo mediano: **0.00002531 s**
- Rango: 0.00000688 s - 0.00010318 s

### Ratio de Rendimiento Relativo

**El parser predictivo es 19.33x mas rapido que CYK en promedio**

Desglose del ratio CYK/Predictivo:
- Ratio promedio: **19.33x**
- Ratio mediano: **15.12x**
- Ratio máximo: **59.01x** (CYK es 59.01 veces más lento)
- Ratio mínimo: **1.73x** (casi equivalentes en entradas pequeñas)

### Interpretación

La curva azul (CYK) crece mas rapido mientras que la curva roja (Predictivo) permanece casi plana. Esto valida:

1. **Entradas pequenas (< 10 tokens):** Ratio ~1.73x - CYK es casi equivalente
2. **Entradas medianas (10-40 tokens):** Ratio ~19.33x - Diferencia clara
3. **Entradas grandes (> 40 tokens):** Ratio alcanza **59.01x** - CYK es dramáticamente más lento

### Conclusion Cuantitativa

Para entradas de tamano moderado a grande, **el parser predictivo es 19.3 veces mas eficiente** que CYK, corroborando que:
$$\text{Eficiencia Predictivo} = \frac{O(n^3)}{O(n)} \approx 19.33 \text{ en promedio}$$

---

## Créditos

Implementacion del algoritmo CYK basada en: [CYK Algorithm Explained - YouTube](https://youtu.be/DE2Ti-6Xcg0?si=-lHB-n1ptJGTW0SM)

**Fecha de Reporte:** 16 de April de 2026  
**Herramientas:** Python 3.x, Parser predictivo LL(1), Pillow 12.1.0  
**Archivo CSV:** /home/antonio/Downloads/PARCIAL_LP/punto_4/resultados/mediciones_comparacion.csv
