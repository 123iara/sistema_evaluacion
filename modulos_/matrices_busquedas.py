
# MATRICES Y BUSQUEDAS UTILIZANDO ARCHIVOS TXT

from modulos_.materias_CRUD import (
    listar_materias,
    obtener_alumnos_materia
)

from modulos_.alumnos_CRUD import (
    obtener_todos_estudiantes
)


def crear_matriz_notas():
    matriz = []

    encabezado = [
        "Materia".ljust(15),
        "DNI".ljust(12),
        "Apellido".ljust(15),
        "Nombre".ljust(15),
        "Notas"
    ]

    matriz.append(encabezado)

    estudiantes = obtener_todos_estudiantes()

    for nombre_materia in listar_materias():
        alumnos = obtener_alumnos_materia(nombre_materia)

        for alumno in alumnos:
            dni = alumno["dni"]

            datos = estudiantes.get(dni, {})

            fila = [
                nombre_materia.ljust(15),
                str(dni).ljust(12),
                datos.get("apellido", "N/A").ljust(15),
                datos.get("nombre", "N/A").ljust(15),
                str(alumno["notas"])
            ]

            matriz.append(fila)

    return matriz


def buscar_notas_estudiante(dni):
    resultados = []

    dni = str(dni).strip()

    estudiantes = obtener_todos_estudiantes()

    if dni in estudiantes:
        alumno = estudiantes[dni]

        resultados.append(
            f"Estudiante: {alumno['nombre']} {alumno['apellido']}"
        )
    else:
        resultados.append(
            f"DNI {dni} no encontrado en el sistema principal."
        )

    resultados.append("----------------------------------")

    for materia in listar_materias():
        alumnos = obtener_alumnos_materia(materia)

        for alumno in alumnos:
            if alumno["dni"] == dni:
                resultados.append([
                    materia,
                    alumno["notas"]
                ])

    return resultados


def obtener_datos_personales_matriz():
    matriz = crear_matriz_notas()

    lista_datos_personales = []

    for fila in matriz[1:]:
        datos_alumno = fila[1:4]

        lista_datos_personales.append(datos_alumno)

    return lista_datos_personales
