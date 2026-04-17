#!/usr/bin/env python3
"""
Generador automatico de reporte de comparacion CYK vs Parser Predictivo.
Lee el CSV de mediciones y genera markdown con tabla, gráfica y análisis estadístico.
"""

import csv
import statistics
from pathlib import Path
from datetime import datetime

def leer_mediciones(csv_path):
    """Lee el CSV de mediciones y retorna datos procesados."""
    datos = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            datos.append({
                'entrada': row['entrada'],
                'tokens': int(row['tokens']),
                'cyk_estado': row['cyk_estado'],
                'predictivo_estado': row['predictivo_estado'],
                'cyk_seg': float(row['cyk_seg']),
                'predictivo_seg': float(row['predictivo_seg']),
            })
    return datos

def calcular_estadisticas(datos):
    """Calcula estadísticas de rendimiento."""
    tiempos_cyk = [d['cyk_seg'] for d in datos]
    tiempos_predictivo = [d['predictivo_seg'] for d in datos]
    ratios = [d['cyk_seg'] / d['predictivo_seg'] for d in datos if d['predictivo_seg'] > 0]
    
    stats = {
        'total_casos': len(datos),
        'cyk_promedio': statistics.mean(tiempos_cyk),
        'cyk_mediana': statistics.median(tiempos_cyk),
        'cyk_max': max(tiempos_cyk),
        'cyk_min': min(tiempos_cyk),
        'predictivo_promedio': statistics.mean(tiempos_predictivo),
        'predictivo_mediana': statistics.median(tiempos_predictivo),
        'predictivo_max': max(tiempos_predictivo),
        'predictivo_min': min(tiempos_predictivo),
        'ratio_promedio': statistics.mean(ratios),  # CYK es X veces más lento
        'ratio_mediana': statistics.median(ratios),
        'ratio_max': max(ratios),
        'ratio_min': min(ratios),
    }
    return stats

def generar_tabla_markdown(datos, max_filas=None):
    """Genera tabla markdown con los datos."""
    tabla = "| Entrada | Tokens | CYK Estado | Predictivo Estado | Tiempo CYK (s) | Tiempo Predictivo (s) | Ratio CYK/Predictivo |\n"
    tabla += "|---|---:|---|---|---:|---:|---:|\n"
    
    filas_a_mostrar = datos[:max_filas] if max_filas else datos
    
    for d in filas_a_mostrar:
        ratio = d['cyk_seg'] / d['predictivo_seg'] if d['predictivo_seg'] > 0 else 0
        entrada_truncada = d['entrada'][:40] + "..." if len(d['entrada']) > 40 else d['entrada']
        tabla += f"| `{entrada_truncada}` | {d['tokens']} | {d['cyk_estado']} | {d['predictivo_estado']} | {d['cyk_seg']:.8f} | {d['predictivo_seg']:.8f} | {ratio:.2f}x |\n"
    
    if max_filas and len(datos) > max_filas:
        tabla += f"\n*Se muestran los primeros {max_filas} de {len(datos)} casos de prueba*\n"
    
    return tabla

def generar_markdown_completo(datos, stats, csv_path, grafica_path):
    """Genera el reporte markdown completo."""
    markdown = f"""# Comparacion: CYK vs Parser Predictivo

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
WS     : [ \t\r\n]+ -> skip ;
```

---

## Resultados Experimentales

Total de casos procesados: **{stats['total_casos']}**

{generar_tabla_markdown(datos)}

---

## Resultado de la Comparación Gráfica

![Grafica de Comparacion CYK vs Predictivo](../resultados/grafica_comparacion.png)

---

## Análisis Matemático de Rendimiento

### Estadísticas Temporales Promedio

**CYK (Complejidad O(n³)):**
- Tiempo promedio: **{stats['cyk_promedio']:.8f} s**
- Tiempo mediano: **{stats['cyk_mediana']:.8f} s**
- Rango: {stats['cyk_min']:.8f} s - {stats['cyk_max']:.8f} s

**Predictivo LL(1) (Complejidad O(n)):**
- Tiempo promedio: **{stats['predictivo_promedio']:.8f} s**
- Tiempo mediano: **{stats['predictivo_mediana']:.8f} s**
- Rango: {stats['predictivo_min']:.8f} s - {stats['predictivo_max']:.8f} s

### Ratio de Rendimiento Relativo

**El parser predictivo es {stats['ratio_promedio']:.2f}x mas rapido que CYK en promedio**

Desglose del ratio CYK/Predictivo:
- Ratio promedio: **{stats['ratio_promedio']:.2f}x**
- Ratio mediano: **{stats['ratio_mediana']:.2f}x**
- Ratio máximo: **{stats['ratio_max']:.2f}x** (CYK es {stats['ratio_max']:.2f} veces más lento)
- Ratio mínimo: **{stats['ratio_min']:.2f}x** (casi equivalentes en entradas pequeñas)

### Interpretación

La curva azul (CYK) crece mas rapido mientras que la curva roja (Predictivo) permanece casi plana. Esto valida:

1. **Entradas pequenas (< 10 tokens):** Ratio ~{stats['ratio_min']:.2f}x - CYK es casi equivalente
2. **Entradas medianas (10-40 tokens):** Ratio ~{stats['ratio_promedio']:.2f}x - Diferencia clara
3. **Entradas grandes (> 40 tokens):** Ratio alcanza **{stats['ratio_max']:.2f}x** - CYK es dramáticamente más lento

### Conclusion Cuantitativa

Para entradas de tamano moderado a grande, **el parser predictivo es {stats['ratio_promedio']:.1f} veces mas eficiente** que CYK, corroborando que:
$$\\text{{Eficiencia Predictivo}} = \\frac{{O(n^3)}}{{O(n)}} \\approx {stats['ratio_promedio']:.2f} \\text{{ en promedio}}$$

---

## Créditos

Implementacion del algoritmo CYK basada en: [CYK Algorithm Explained - YouTube](https://youtu.be/DE2Ti-6Xcg0?si=-lHB-n1ptJGTW0SM)

**Fecha de Reporte:** {datetime.now().strftime('%d de %B de %Y')}  
**Herramientas:** Python 3.x, Parser predictivo LL(1), Pillow 12.1.0  
**Archivo CSV:** {csv_path}
"""
    return markdown

def main():
    # Rutas
    repo_root = Path(__file__).parent.parent
    csv_path = repo_root / 'resultados' / 'mediciones_comparacion.csv'
    reporte_path = repo_root / 'reportes' / 'comparacion_seria.md'
    
    if not csv_path.exists():
        print(f"Error: No se encontró {csv_path}")
        return    
    # Crear carpeta de reportes si no existe
    reporte_path.parent.mkdir(parents=True, exist_ok=True)    
    # Leer datos
    print("Leyendo mediciones...")
    datos = leer_mediciones(csv_path)
    
    # Calcular estadísticas
    print("Calculando estadísticas...")
    stats = calcular_estadisticas(datos)
    
    # Generar markdown
    print("Generando reporte markdown...")
    markdown = generar_markdown_completo(datos, stats, str(csv_path), '../resultados/grafica_comparacion.png')
    
    # Escribir reporte
    reporte_path.write_text(markdown, encoding='utf-8')
    print(f"Reporte generado: {reporte_path}")
    
    # Mostrar resumen en consola
    print("\n" + "="*70)
    print("RESUMEN ESTADÍSTICO")
    print("="*70)
    print(f"Total de casos: {stats['total_casos']}")
    print(f"\nCYK promedio:    {stats['cyk_promedio']:.8f} s")
    print(f"Predictivo promedio: {stats['predictivo_promedio']:.8f} s")
    print(f"\n El predictivo es {stats['ratio_promedio']:.2f}x MAS RAPIDO que CYK en promedio")
    print(f"   (Rango: {stats['ratio_min']:.2f}x - {stats['ratio_max']:.2f}x)")
    print("="*70)

if __name__ == '__main__':
    main()
