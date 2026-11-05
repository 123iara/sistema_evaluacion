
# CRUD DE ALUMNOS UTILIZANDO ARCHIVOS TXT

from datos_generales import persistencia
from modulos_.validaciones import (
    validar_dni,
    validar_nombre,
    normalizar_nombre
)

ARCHIVO_ALUMNOS = persistencia.ARCHIVO_ALUMNOS
ARCHIVO_INSCRIPCIONES = persistencia.ARCHIVO_INSCRIPCIONES


def obtener_todos_estudiantes():
    estudiantes = {}

    for linea in persistencia.leer_lineas(ARCHIVO_ALUMNOS):
        partes = linea.split(";")

        if len(partes) == 4:
            dni, legajo, nombre, apellido = partes

            try:
                estudiantes[dni] = {
                    "legajo": int(legajo),
                    "nombre": nombre,
                    "apellido": apellido
                }
            except ValueError:
                continue

    return estudiantes


def crear_estudiante(dni, nombre, apellido):
    dni = str(dni).strip()

    if not validar_dni(dni):
        return False, "El DNI debe tener 7 u 8 dígitos."

    if not validar_nombre(nombre) or not validar_nombre(apellido):
        return False, "Nombre y apellido inválidos."

    try:
        estudiantes = obtener_todos_estudiantes()

        if dni in estudiantes:
            return False, "El estudiante ya está registrado."

        legajo = max(
            (e["legajo"] for e in estudiantes.values()),
            default=0
        ) + 1

        nombre = normalizar_nombre(nombre)
        apellido = normalizar_nombre(apellido)

        registro = f"{dni};{legajo};{nombre};{apellido}"

        persistencia.agregar_linea(
            ARCHIVO_ALUMNOS,
            registro
        )

        return True, "Estudiante registrado con éxito."

    except OSError as error:
        return False, str(error)


def buscar_estudiante_por_dni(dni):
    dni = str(dni).strip()

    estudiantes = obtener_todos_estudiantes()

    if dni in estudiantes:
        return True, estudiantes[dni]

    return False, "Estudiante no encontrado."


def modificar_datos_estudiante(dni, nuevo_nombre, nuevo_apellido):
    dni = str(dni).strip()

    if not validar_nombre(nuevo_nombre) or not validar_nombre(nuevo_apellido):
        return False, "Nombre y apellido inválidos."

    try:
        lineas = persistencia.leer_lineas(ARCHIVO_ALUMNOS)
        actualizadas = []
        encontrada = False

        for linea in lineas:
            partes = linea.split(";")

            if len(partes) == 4 and partes[0] == dni:
                partes[2] = normalizar_nombre(nuevo_nombre)
                partes[3] = normalizar_nombre(nuevo_apellido)
                encontrada = True

            actualizadas.append(";".join(partes))

        if not encontrada:
            return False, "Estudiante no encontrado."

        persistencia.escribir_lineas(
            ARCHIVO_ALUMNOS,
            actualizadas
        )

        return True, "Datos actualizados con éxito."

    except OSError as error:
        return False, str(error)


def eliminar_estudiante(dni):
    dni = str(dni).strip()

    try:
        lineas = persistencia.leer_lineas(ARCHIVO_ALUMNOS)

        restantes = [
            linea for linea in lineas
            if linea.split(";")[0] != dni
        ]

        if len(restantes) == len(lineas):
            return False, "Estudiante no encontrado."

        persistencia.escribir_lineas(
            ARCHIVO_ALUMNOS,
            restantes
        )

        inscripciones = persistencia.leer_lineas(
            ARCHIVO_INSCRIPCIONES
        )

        restantes_inscripciones = []

        for linea in inscripciones:
            partes = linea.split(";", 2)

            if len(partes) < 2 or partes[1] != dni:
                restantes_inscripciones.append(linea)

        persistencia.escribir_lineas(
            ARCHIVO_INSCRIPCIONES,
            restantes_inscripciones
        )

        return True, "Estudiante eliminado del sistema."

    except OSError as error:
        return False, str(error)
