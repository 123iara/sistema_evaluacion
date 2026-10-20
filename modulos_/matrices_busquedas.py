
from datos_generales.memoria import materias


def crear_matriz_notas():
    matriz = []

    for nombre_materia in materias:
        alumnos = materias[nombre_materia]["alumnos"]

        for alumno in alumnos:
            fila = [nombre_materia, alumno["dni"]]

            for nota in alumno["notas"]:
                fila.append(nota)

            matriz.append(fila)

    return matriz


def buscar_notas_estudiante(dni):
    resultados = []

    for nombre_materia in materias:
        alumnos = materias[nombre_materia]["alumnos"]

        for alumno in alumnos:
            if alumno["dni"] == dni:
                resultados.append([
                    nombre_materia,
                    alumno["notas"]
                ])

    return resultados
