
from datos_generales.memoria import materias


# PROMEDIO DE UN ALUMNO
def calcular_promedio(notas):
    if len(notas) == 0:
        return None

    suma = 0

    for nota in notas:
        suma = suma + nota

    return suma / len(notas)


# ESTADISTICAS POR MATERIA
def estadisticas_materia(nombre_materia):
    if nombre_materia not in materias:
        return None

    alumnos = materias[nombre_materia]["alumnos"]

    aprobados = 0
    desaprobados = 0
    promedios_altos = 0
    suma_promedios = 0
    cantidad = 0

    for alumno in alumnos:
        promedio = calcular_promedio(alumno["notas"])

        if promedio is not None:
            suma_promedios += promedio
            cantidad += 1

            if promedio >= 4:
                aprobados += 1
            else:
                desaprobados += 1

            if promedio >= 8:
                promedios_altos += 1

    if cantidad == 0:
        return None

    promedio_general = suma_promedios / cantidad
    porcentaje_altos = promedios_altos * 100 / cantidad

    return [
        promedio_general,
        aprobados,
        desaprobados,
        porcentaje_altos
    ]
