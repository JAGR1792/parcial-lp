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
| `2+3` | 3 | ACEPTADA | ACEPTADA | 0.00010687 | 0.00001334 | 8.01x |
| `10-4` | 3 | ACEPTADA | ACEPTADA | 0.00002502 | 0.00000490 | 5.11x |
| `7*8` | 3 | ACEPTADA | ACEPTADA | 0.00002370 | 0.00000476 | 4.98x |
| `9/3` | 3 | ACEPTADA | ACEPTADA | 0.00002183 | 0.00000474 | 4.61x |
| `(2+3)*4` | 7 | ACEPTADA | ACEPTADA | 0.00007056 | 0.00001194 | 5.91x |
| `8/(2+2)` | 7 | ACEPTADA | ACEPTADA | 0.00006046 | 0.00000964 | 6.27x |
| `(10-4)*(6+2)` | 11 | ACEPTADA | ACEPTADA | 0.00011765 | 0.00001014 | 11.60x |
| `18/(3*(2+1))` | 11 | ACEPTADA | ACEPTADA | 0.00010402 | 0.00000990 | 10.51x |
| `5+6*7-8/2` | 9 | ACEPTADA | ACEPTADA | 0.00011223 | 0.00001355 | 8.28x |
| `((1+2)*(3+4))/5` | 15 | ACEPTADA | ACEPTADA | 0.00021573 | 0.00002004 | 10.76x |
| `3+*4` | 4 | RECHAZADA | RECHAZADA | 0.00002876 | 0.00001444 | 1.99x |
| `(5+2` | 4 | RECHAZADA | RECHAZADA | 0.00002864 | 0.00000950 | 3.01x |
| `9/)3(` | 5 | RECHAZADA | RECHAZADA | 0.00003271 | 0.00000672 | 4.87x |
| `1+2+3+4+5+6+7+8+9+10` | 19 | ACEPTADA | ACEPTADA | 0.00274543 | 0.00003793 | 72.38x |
| `1*2*3*4*5*6*7*8*9*10` | 19 | ACEPTADA | ACEPTADA | 0.00051937 | 0.00002929 | 17.73x |
| `(1+2+3+4+5)*(6+7+8+9)` | 21 | ACEPTADA | ACEPTADA | 0.00043334 | 0.00003916 | 11.07x |
| `((1+2)*(3+4)*(5+6))/(7+8)` | 25 | ACEPTADA | ACEPTADA | 0.00061889 | 0.00003815 | 16.22x |
| `(1+(2*(3+(4*(5+6)))))` | 21 | ACEPTADA | ACEPTADA | 0.00038306 | 0.00002559 | 14.97x |
| `1+2+3+4+5+6+7+8+9+10+11+12+13+14+15` | 29 | ACEPTADA | ACEPTADA | 0.00108026 | 0.00003052 | 35.40x |
| `(1*2)+(3*4)+(5*6)+(7*8)+(9*10)+(11*12)` | 35 | ACEPTADA | ACEPTADA | 0.00101691 | 0.00003498 | 29.07x |
| `((1+2+3+4+5)*(6+7+8+9+10))/(11+12)` | 31 | ACEPTADA | ACEPTADA | 0.00073403 | 0.00002642 | 27.78x |
| `(1+(2+(3+(4+(5+(6+(7+8)))))))` | 29 | ACEPTADA | ACEPTADA | 0.00053646 | 0.00002118 | 25.33x |
| `((2+3)*(4+5)*(6+7)*(8+9))/(10+11)` | 31 | ACEPTADA | ACEPTADA | 0.00084576 | 0.00004986 | 16.96x |
| `1+2*3+4*5+6*7+8*9+10*11+12*13+14*15` | 29 | ACEPTADA | ACEPTADA | 0.00093246 | 0.00003184 | 29.29x |
| `(1+2)*(3+4)*(5+6)*(7+8)*(9+10)` | 29 | ACEPTADA | ACEPTADA | 0.00064379 | 0.00003632 | 17.73x |
| `((1+2+3+4+5+6+7+8+9+10)*2)/(3+4)` | 31 | ACEPTADA | ACEPTADA | 0.00126811 | 0.00005266 | 24.08x |
| `(1+(2*(3+(4*(5+(6*(7+8)))))))` | 29 | ACEPTADA | ACEPTADA | 0.00062227 | 0.00003624 | 17.17x |
| `((1+2)*(3+4)+(5+6)*(7+8)+(9+10)*(11+12))` | 37 | ACEPTADA | ACEPTADA | 0.00144237 | 0.00006273 | 22.99x |
| `1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+1...` | 39 | ACEPTADA | ACEPTADA | 0.00237322 | 0.00005611 | 42.30x |
| `(1*2*3*4*5*6)/(7+8+9+10)` | 23 | ACEPTADA | ACEPTADA | 0.00064765 | 0.00003740 | 17.32x |
| `((1+2+3+4+5+6+7+8)*(9+10+11+12+13+14))/(...` | 39 | ACEPTADA | ACEPTADA | 0.00241849 | 0.00007189 | 33.64x |
| `(1+(2+(3+(4+(5+(6+(7+(8+(9+10)))))))))` | 37 | ACEPTADA | ACEPTADA | 0.00145844 | 0.00005286 | 27.59x |
| `((1+2)*(3+4)*(5+6)*(7+8)*(9+10)*(11+12))...` | 43 | ACEPTADA | ACEPTADA | 0.00197618 | 0.00005168 | 38.24x |
| `1++2` | 4 | RECHAZADA | RECHAZADA | 0.00004734 | 0.00001484 | 3.19x |
| `((3+4)` | 6 | RECHAZADA | RECHAZADA | 0.00005094 | 0.00001221 | 4.17x |
| `8/*2` | 4 | RECHAZADA | RECHAZADA | 0.00002468 | 0.00000578 | 4.27x |
| `(1+2))*3` | 8 | RECHAZADA | RECHAZADA | 0.00007509 | 0.00001027 | 7.31x |
| `42/(7-7)` | 7 | ACEPTADA | ACEPTADA | 0.00005697 | 0.00000823 | 6.92x |


---

## Resultado de la Comparación Gráfica

![Grafica de Comparacion CYK vs Predictivo](../resultados/grafica_comparacion.png)

---

## Análisis Matemático de Rendimiento

### Estadísticas Temporales Promedio

**CYK (Complejidad O(n³)):**
- Tiempo promedio: **0.00062894 s**
- Tiempo mediano: **0.00040820 s**
- Rango: 0.00002183 s - 0.00274543 s

**Predictivo LL(1) (Complejidad O(n)):**
- Tiempo promedio: **0.00002652 s**
- Tiempo mediano: **0.00002339 s**
- Rango: 0.00000474 s - 0.00007189 s

### Ratio de Rendimiento Relativo

**El parser predictivo es 17.08x mas rapido que CYK en promedio**

Desglose del ratio CYK/Predictivo:
- Ratio promedio: **17.08x**
- Ratio mediano: **13.29x**
- Ratio máximo: **72.38x** (CYK es 72.38 veces más lento)
- Ratio mínimo: **1.99x** (casi equivalentes en entradas pequeñas)

### Interpretación

La curva azul (CYK) crece mas rapido mientras que la curva roja (Predictivo) permanece casi plana. Esto valida:

1. **Entradas pequenas (< 10 tokens):** Ratio ~1.99x - CYK es casi equivalente
2. **Entradas medianas (10-40 tokens):** Ratio ~17.08x - Diferencia clara
3. **Entradas grandes (> 40 tokens):** Ratio alcanza **72.38x** - CYK es dramáticamente más lento

### Conclusion Cuantitativa

Para entradas de tamano moderado a grande, **el parser predictivo es 17.1 veces mas eficiente** que CYK, corroborando que:
$$\text{Eficiencia Predictivo} = \frac{O(n^3)}{O(n)} \approx 17.08 \text{ en promedio}$$

---

## Créditos

Implementacion del algoritmo CYK basada en: [CYK Algorithm Explained - YouTube](https://youtu.be/DE2Ti-6Xcg0?si=-lHB-n1ptJGTW0SM)

**Fecha de Reporte:** 16 de April de 2026  
**Herramientas:** Python 3.x, Parser predictivo LL(1), Pillow 12.1.0  
**Archivo CSV:** /home/antonio/Downloads/PARCIAL_LP/punto_4/resultados/mediciones_comparacion.csv
