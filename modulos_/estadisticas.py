
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
        return False, "La materia no tiene alumnos registrados."

    alumnos = materias[nombre_materia]["alumnos"]

    if len(alumnos) == 0:
         return False, "La materia no tiene alumnos para generar estadisticas."

    # Lista que contenga unicamente los promedios calculados de todos los alumnos (Listas por Comprensión)
    promedios = [calcular_promedio(alumno["notas"]) for alumno in alumnos if calcular_promedio(alumno["notas"]) is not None]
    cantidad_calificados = len(promedios)

    if cantidad_calificados == 0:
         return False, "Los alumnos inscriptos aún no tienen notas cargadas."

    #Lista por Comprension para saber los alumnos que aprobaron y desaprobaron
    aprobados = len([p for p in promedios if p >= 4])
    desaprobados = cantidad_calificados - aprobados

    #Lista por Comprension para saber los alumnos que tienen promedio mayor o igual a 8
    promedios_altos = len([p for p in promedios if p >= 8])
    porcentaje_altos = (promedios_altos * 100) / cantidad_calificados

    #Identificacion de valores MAXIMOS Y MINIMOS
    mejor_promedio = max(promedios)
    peor_promedio = min(promedios)

    # Devolvemos el diccionario prolijo
    resultado = {
        "aprobados": aprobados,
        "desaprobados": desaprobados,
        "porcentaje_altos": porcentaje_altos,
        "total_calificados": cantidad_calificados,
        "mejor_promedio": mejor_promedio,
        "peor_promedio": peor_promedio
    }
    
    return True, resultado


    