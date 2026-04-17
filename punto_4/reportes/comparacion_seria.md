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
| `2+3` | 3 | ACEPTADA | ACEPTADA | 0.00015610 | 0.00003130 | 4.99x |
| `10-4` | 3 | ACEPTADA | ACEPTADA | 0.00006840 | 0.00001780 | 3.84x |
| `7*8` | 3 | ACEPTADA | ACEPTADA | 0.00008120 | 0.00001940 | 4.19x |
| `9/3` | 3 | ACEPTADA | ACEPTADA | 0.00006160 | 0.00001790 | 3.44x |
| `(2+3)*4` | 7 | ACEPTADA | ACEPTADA | 0.00017470 | 0.00003920 | 4.46x |
| `8/(2+2)` | 7 | ACEPTADA | ACEPTADA | 0.00013570 | 0.00003180 | 4.27x |
| `(10-4)*(6+2)` | 11 | ACEPTADA | ACEPTADA | 0.00022460 | 0.00003230 | 6.95x |
| `18/(3*(2+1))` | 11 | ACEPTADA | ACEPTADA | 0.00021680 | 0.00003180 | 6.82x |
| `5+6*7-8/2` | 9 | ACEPTADA | ACEPTADA | 0.00024740 | 0.00002410 | 10.27x |
| `((1+2)*(3+4))/5` | 15 | ACEPTADA | ACEPTADA | 0.00036920 | 0.00003760 | 9.82x |
| `3+*4` | 4 | RECHAZADA | RECHAZADA | 0.00008880 | 0.00002810 | 3.16x |
| `(5+2` | 4 | RECHAZADA | RECHAZADA | 0.00006570 | 0.00002020 | 3.25x |
| `9/)3(` | 5 | RECHAZADA | RECHAZADA | 0.00008390 | 0.00001890 | 4.44x |
| `1+2+3+4+5+6+7+8+9+10` | 19 | ACEPTADA | ACEPTADA | 0.00104500 | 0.00006950 | 15.04x |
| `1*2*3*4*5*6*7*8*9*10` | 19 | ACEPTADA | ACEPTADA | 0.00114700 | 0.00005400 | 21.24x |
| `(1+2+3+4+5)*(6+7+8+9)` | 21 | ACEPTADA | ACEPTADA | 0.00096230 | 0.00006470 | 14.87x |
| `((1+2)*(3+4)*(5+6))/(7+8)` | 25 | ACEPTADA | ACEPTADA | 0.00086940 | 0.00005070 | 17.15x |
| `(1+(2*(3+(4*(5+6)))))` | 21 | ACEPTADA | ACEPTADA | 0.00067600 | 0.00005480 | 12.34x |
| `1+2+3+4+5+6+7+8+9+10+11+12+13+14+15` | 29 | ACEPTADA | ACEPTADA | 0.00158640 | 0.00006300 | 25.18x |
| `(1*2)+(3*4)+(5*6)+(7*8)+(9*10)+(11*12)` | 35 | ACEPTADA | ACEPTADA | 0.00229360 | 0.00008950 | 25.63x |
| `((1+2+3+4+5)*(6+7+8+9+10))/(11+12)` | 31 | ACEPTADA | ACEPTADA | 0.00272100 | 0.00009950 | 27.35x |
| `(1+(2+(3+(4+(5+(6+(7+8)))))))` | 29 | ACEPTADA | ACEPTADA | 0.00138790 | 0.00014280 | 9.72x |
| `((2+3)*(4+5)*(6+7)*(8+9))/(10+11)` | 31 | ACEPTADA | ACEPTADA | 0.00211550 | 0.00010290 | 20.56x |
| `1+2*3+4*5+6*7+8*9+10*11+12*13+14*15` | 29 | ACEPTADA | ACEPTADA | 0.00246210 | 0.00008620 | 28.56x |
| `(1+2)*(3+4)*(5+6)*(7+8)*(9+10)` | 29 | ACEPTADA | ACEPTADA | 0.00176920 | 0.00009690 | 18.26x |
| `((1+2+3+4+5+6+7+8+9+10)*2)/(3+4)` | 31 | ACEPTADA | ACEPTADA | 0.00239030 | 0.00009740 | 24.54x |
| `(1+(2*(3+(4*(5+(6*(7+8)))))))` | 29 | ACEPTADA | ACEPTADA | 0.00160180 | 0.00009390 | 17.06x |
| `((1+2)*(3+4)+(5+6)*(7+8)+(9+10)*(11+12))` | 37 | ACEPTADA | ACEPTADA | 0.00287460 | 0.00010880 | 26.42x |
| `1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+1...` | 39 | ACEPTADA | ACEPTADA | 0.00795690 | 0.00045000 | 17.68x |
| `(1*2*3*4*5*6)/(7+8+9+10)` | 23 | ACEPTADA | ACEPTADA | 0.00403880 | 0.00008010 | 50.42x |
| `((1+2+3+4+5+6+7+8)*(9+10+11+12+13+14))/(...` | 39 | ACEPTADA | ACEPTADA | 0.00485250 | 0.00012370 | 39.23x |
| `(1+(2+(3+(4+(5+(6+(7+(8+(9+10)))))))))` | 37 | ACEPTADA | ACEPTADA | 0.00265450 | 0.00011150 | 23.81x |
| `((1+2)*(3+4)*(5+6)*(7+8)*(9+10)*(11+12))...` | 43 | ACEPTADA | ACEPTADA | 0.00444540 | 0.00016300 | 27.27x |
| `1++2` | 4 | RECHAZADA | RECHAZADA | 0.00008870 | 0.00002600 | 3.41x |
| `((3+4)` | 6 | RECHAZADA | RECHAZADA | 0.00011580 | 0.00002910 | 3.98x |
| `8/*2` | 4 | RECHAZADA | RECHAZADA | 0.00007580 | 0.00001640 | 4.62x |
| `(1+2))*3` | 8 | RECHAZADA | RECHAZADA | 0.00021900 | 0.00003980 | 5.50x |
| `42/(7-7)` | 7 | ACEPTADA | ACEPTADA | 0.00015170 | 0.00002370 | 6.40x |


---

## Resultado de la Comparación Gráfica

![Grafica de Comparacion CYK vs Predictivo](../resultados/grafica_comparacion.png)

---

## Análisis Matemático de Rendimiento

### Estadísticas Temporales Promedio

**CYK (Complejidad O(n³)):**
- Tiempo promedio: **0.00138093 s**
- Tiempo mediano: **0.00077270 s**
- Rango: 0.00006160 s - 0.00795690 s

**Predictivo LL(1) (Complejidad O(n)):**
- Tiempo promedio: **0.00007074 s**
- Tiempo mediano: **0.00005235 s**
- Rango: 0.00001640 s - 0.00045000 s

### Ratio de Rendimiento Relativo

**El parser predictivo es 14.63x mas rapido que CYK en promedio**

Desglose del ratio CYK/Predictivo:
- Ratio promedio: **14.63x**
- Ratio mediano: **11.30x**
- Ratio máximo: **50.42x** (CYK es 50.42 veces más lento)
- Ratio mínimo: **3.16x** (casi equivalentes en entradas pequeñas)

### Interpretación

La curva azul (CYK) crece mas rapido mientras que la curva roja (Predictivo) permanece casi plana. Esto valida:

1. **Entradas pequenas (< 10 tokens):** Ratio ~3.16x - CYK es casi equivalente
2. **Entradas medianas (10-40 tokens):** Ratio ~14.63x - Diferencia clara
3. **Entradas grandes (> 40 tokens):** Ratio alcanza **50.42x** - CYK es dramáticamente más lento

### Conclusion Cuantitativa

Para entradas de tamano moderado a grande, **el parser predictivo es 14.6 veces mas eficiente** que CYK, corroborando que:
$$\text{Eficiencia Predictivo} = \frac{O(n^3)}{O(n)} \approx 14.63 \text{ en promedio}$$

---

## Créditos

Implementacion del algoritmo CYK basada en: [CYK Algorithm Explained - YouTube](https://youtu.be/DE2Ti-6Xcg0?si=-lHB-n1ptJGTW0SM)

**Fecha de Reporte:** 17 de April de 2026  
**Herramientas:** Python 3.x, Parser predictivo LL(1), Pillow 12.1.0  
**Archivo CSV:** C:\Users\jorge\Documents\GitHub\parcial-lp\punto_4\resultados\mediciones_comparacion.csv
