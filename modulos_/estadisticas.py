
from modulos_.materias_CRUD import obtener_todas_materias, obtener_alumnos_materia

ARCHIVO_INSCRIPCIONES = "inscripciones.txt"


#PROMEDIO DE UN ALUMNO
def calcular_promedio(notas):
    if len(notas) == 0:
        return None

    suma = 0

    for nota in notas:
        suma = suma + nota

    return suma / len(notas)


#ESTADISTICAS POR MATERIA
def estadisticas_materia(nombre_materia):
    nombre_materia = nombre_materia.strip().title()
    alumnos = obtener_alumnos_materia(nombre_materia) #alumnos del CRUD

    if not alumnos:
        return False, "La materia no tiene alumnos registrados o no existe."

    #Lista que contenga los promedios calculados de todos los alumnos (Listas por Comprensión)
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

    #Devolvemos el diccionario prolijo
    resultado = {
        "aprobados": aprobados,
        "desaprobados": desaprobados,
        "porcentaje_altos": porcentaje_altos,
        "total_calificados": cantidad_calificados,
        "mejor_promedio": mejor_promedio,
        "peor_promedio": peor_promedio
    }
    
    return True, resultado


#USO DE CONJUNTOS (SETS) E INTERSECCION
def estudiantes_en_todas_las_materias():
    """Usa conjuntos (sets) e intersección para buscar alumnos anotados en todas las materias."""
    materias_totales = obtener_todas_materias()
    
    if not materias_totales:
        return False, "No hay materias registradas en el sistema."

    #Diccionario temporal para agrupar los DNIs por materia leyendo el archivo
    dnis_por_materia = {materia: set() for materia in materias_totales}

    try:
        with open(ARCHIVO_INSCRIPCIONES, 'r', encoding='UTF-8') as archivo:
            for linea in archivo:
                datos = linea.strip().split(';')
                if len(datos) >= 2:
                    materia = datos[0]
                    dni = datos[1]
                    if materia in dnis_por_materia:
                        dnis_por_materia[materia].add(dni)
    except FileNotFoundError:
        return False, "No hay inscripciones registradas."

    #Extraemos solo los conjuntos de DNIs
    lista_conjuntos = list(dnis_por_materia.values())
    
    #Intersección de todos los conjuntos para encontrar los que están en TODAS las materias
    if lista_conjuntos:
        # Se toma el primer conjunto, cruza las listas y busca qué DNI se repite en absolutamente todas
        dnis_comunes = set.intersection(*lista_conjuntos)
        
        if dnis_comunes:
            return True, f"DNI de los alumnos inscriptos en TODAS las materias: {dnis_comunes}"
        else:
            return True, "No hay ningún alumno que esté inscripto en todas las materias a la vez."
            
        return False, "No hay alumnos inscriptos."