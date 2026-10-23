
from functools import reduce

from datos_generales.memoria import materias


def suma_recursiva(valores):
    """Suma una lista de forma recursiva (caso base: lista vacía)."""
    if not valores:
        return 0
    return valores[0] + suma_recursiva(valores[1:])


def contar_recursivo(valores, condicion):
    """Cuenta recursivamente los elementos que cumplen una condición."""
    if not valores:
        return 0
    cumple = 1 if condicion(valores[0]) else 0
    return cumple + contar_recursivo(valores[1:], condicion)


def maximo_recursivo(valores):
    """Obtiene el máximo de una lista no vacía de forma recursiva."""
    if len(valores) == 1:
        return valores[0]
    maximo_resto = maximo_recursivo(valores[1:])
    return valores[0] if valores[0] > maximo_resto else maximo_resto


# PROMEDIO DE UN ALUMNO
def calcular_promedio(notas):
    if len(notas) == 0:
        return None

    return suma_recursiva(notas) / len(notas)


# ESTADISTICAS POR MATERIA
def estadisticas_materia(nombre_materia):
    if nombre_materia not in materias:
        return None
    return _estadisticas_alumnos(materias[nombre_materia]["alumnos"])


def estadisticas_generales():
    """Combina notas de todas las materias y calcula el resumen general."""
    alumnos = []
    for materia in materias.values():
        alumnos.extend(materia["alumnos"])
    if not alumnos:
        return None
    return _estadisticas_alumnos(alumnos)


def _estadisticas_alumnos(alumnos):
    """Calcula estadísticas reutilizables para un conjunto de cursadas."""
    promedios = list(filter(
        lambda promedio: promedio is not None,
        map(lambda alumno: calcular_promedio(alumno["notas"]), alumnos),
    ))
    todas_las_notas = reduce(
        lambda acumuladas, alumno: acumuladas + alumno["notas"], alumnos, []
    )
    if not promedios:
        return None
    aprobados = contar_recursivo(promedios, lambda promedio: promedio >= 4)
    desaprobados = contar_recursivo(promedios, lambda promedio: promedio < 4)
    altos = contar_recursivo(promedios, lambda promedio: promedio >= 8)
    promedio_general = reduce(lambda total, promedio: total + promedio, promedios, 0) / len(promedios)
    return {
        "promedio_general": promedio_general,
        "aprobados": aprobados,
        "desaprobados": desaprobados,
        "porcentaje_altos": altos * 100 / len(promedios),
        "cantidad_alumnos_evaluados": len(promedios),
        "cantidad_notas": len(todas_las_notas),
        "nota_minima": min(todas_las_notas) if todas_las_notas else None,
        "nota_maxima": maximo_recursivo(todas_las_notas) if todas_las_notas else None,
        "resumen": (
            f"{aprobados} aprobados, {desaprobados} desaprobados; "
            f"promedio {promedio_general:.2f}"
        ),
    }
