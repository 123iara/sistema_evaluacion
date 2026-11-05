

# ESTADISTICAS ACADEMICAS DESDE ARCHIVOS TXT

from functools import reduce

from modulos_.materias_CRUD import (
    listar_materias,
    obtener_alumnos_materia
)


def suma_recursiva(valores):
    if not valores:
        return 0

    return valores[0] + suma_recursiva(valores[1:])


def contar_recursivo(valores, condicion):
    if not valores:
        return 0

    cumple = 1 if condicion(valores[0]) else 0

    return cumple + contar_recursivo(
        valores[1:],
        condicion
    )


def maximo_recursivo(valores):
    if len(valores) == 1:
        return valores[0]

    maximo_resto = maximo_recursivo(valores[1:])

    return valores[0] if valores[0] > maximo_resto else maximo_resto


def calcular_promedio(notas):
    if not notas:
        return None

    return suma_recursiva(notas) / len(notas)


def _estadisticas_alumnos(alumnos):
    promedios = []

    todas_las_notas = []

    for alumno in alumnos:
        notas = alumno["notas"]

        if notas:
            promedios.append(calcular_promedio(notas))
            todas_las_notas.extend(notas)

    if not promedios:
        return None

    aprobados = contar_recursivo(
        promedios,
        lambda promedio: promedio >= 4
    )

    desaprobados = contar_recursivo(
        promedios,
        lambda promedio: promedio < 4
    )

    altos = contar_recursivo(
        promedios,
        lambda promedio: promedio >= 8
    )

    promedio_general = suma_recursiva(promedios) / len(promedios)

    return {
        "promedio_general": promedio_general,
        "aprobados": aprobados,
        "desaprobados": desaprobados,
        "porcentaje_altos": altos * 100 / len(promedios),
        "cantidad_alumnos_evaluados": len(promedios),
        "cantidad_notas": len(todas_las_notas),
        "nota_minima": min(todas_las_notas),
        "nota_maxima": maximo_recursivo(todas_las_notas),
        "resumen": (
            f"{aprobados} aprobados, "
            f"{desaprobados} desaprobados; "
            f"promedio {promedio_general:.2f}"
        )
    }


def estadisticas_materia(nombre_materia):
    nombre_materia = str(nombre_materia).strip().capitalize()

    if nombre_materia not in listar_materias():
        return None

    alumnos = obtener_alumnos_materia(nombre_materia)

    return _estadisticas_alumnos(alumnos)


def estadisticas_generales():
    alumnos = []

    for materia in listar_materias():
        alumnos.extend(
            obtener_alumnos_materia(materia)
        )

    return _estadisticas_alumnos(alumnos)


def estudiantes_en_todas_las_materias():
    materias = listar_materias()

    if not materias:
        return False, "No hay materias registradas en el sistema."

    dnis_por_materia = []

    for materia in materias:
        alumnos = obtener_alumnos_materia(materia)

        dnis = {
            alumno["dni"]
            for alumno in alumnos
        }

        dnis_por_materia.append(dnis)

    dnis_comunes = set.intersection(*dnis_por_materia)

    if dnis_comunes:
        return True, (
            "DNI de los alumnos inscriptos en TODAS las materias: "
            f"{sorted(dnis_comunes)}"
        )

    return True, (
        "No hay ningún alumno inscripto en todas las materias."
    )
