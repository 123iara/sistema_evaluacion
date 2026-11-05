
# CRUD DE MATERIAS E INSCRIPCIONES CON ARCHIVOS TXT

from datos_generales import persistencia
from modulos_.alumnos_CRUD import buscar_estudiante_por_dni

ARCHIVO_MATERIAS = persistencia.ARCHIVO_MATERIAS
ARCHIVO_INSCRIPCIONES = persistencia.ARCHIVO_INSCRIPCIONES


def crear_materia(nombre):
    nombre = str(nombre).strip().capitalize()

    if not nombre:
        return False, "El nombre no puede estar vacío."

    try:
        materias = listar_materias()

        if nombre in materias:
            return False, "La materia ya existe."

        persistencia.agregar_linea(
            ARCHIVO_MATERIAS,
            nombre
        )

        return True, "Materia creada con éxito."

    except OSError as error:
        return False, str(error)


def listar_materias():
    return persistencia.leer_lineas(ARCHIVO_MATERIAS)


def modificar_materia(nombre_actual, nombre_nuevo):
    nombre_actual = str(nombre_actual).strip().capitalize()
    nombre_nuevo = str(nombre_nuevo).strip().capitalize()

    try:
        materias = listar_materias()

        if nombre_actual not in materias:
            return False, "Materia no encontrada."

        if not nombre_nuevo:
            return False, "El nuevo nombre no puede estar vacío."

        if nombre_nuevo in materias:
            return False, "El nuevo nombre ya está ocupado."

        nuevas_materias = [
            nombre_nuevo if materia == nombre_actual else materia
            for materia in materias
        ]

        persistencia.escribir_lineas(
            ARCHIVO_MATERIAS,
            nuevas_materias
        )

        registros = persistencia.leer_lineas(
            ARCHIVO_INSCRIPCIONES
        )

        actualizados = []

        for registro in registros:
            partes = registro.split(";", 2)

            if partes[0] == nombre_actual:
                partes[0] = nombre_nuevo

            actualizados.append(";".join(partes))

        persistencia.escribir_lineas(
            ARCHIVO_INSCRIPCIONES,
            actualizados
        )

        return True, "Nombre de materia actualizado."

    except OSError as error:
        return False, str(error)


def eliminar_materia(nombre):
    nombre = str(nombre).strip().capitalize()

    try:
        materias = listar_materias()

        if nombre not in materias:
            return False, "Materia no encontrada."

        persistencia.escribir_lineas(
            ARCHIVO_MATERIAS,
            [m for m in materias if m != nombre]
        )

        registros = persistencia.leer_lineas(
            ARCHIVO_INSCRIPCIONES
        )

        restantes = [
            registro for registro in registros
            if registro.split(";", 1)[0] != nombre
        ]

        persistencia.escribir_lineas(
            ARCHIVO_INSCRIPCIONES,
            restantes
        )

        return True, "Materia eliminada del sistema."

    except OSError as error:
        return False, str(error)


# AGREGAR ALUMNO A UNA MATERIA

def agregar_alumno_materia(nombre_materia, dni):
    nombre_materia = str(nombre_materia).strip().capitalize()
    dni = str(dni).strip()

    encontrado, estudiante = buscar_estudiante_por_dni(dni)

    if not encontrado:
        return False, "El estudiante no está registrado."

    if nombre_materia not in listar_materias():
        return False, "Materia no encontrada."

    try:
        registros = persistencia.leer_lineas(
            ARCHIVO_INSCRIPCIONES
        )

        for registro in registros:
            partes = registro.split(";", 2)

            if len(partes) >= 2:
                if partes[0] == nombre_materia and partes[1] == dni:
                    return False, "El estudiante ya está inscripto."

        nueva_inscripcion = f"{nombre_materia};{dni};"

        persistencia.agregar_linea(
            ARCHIVO_INSCRIPCIONES,
            nueva_inscripcion
        )

        return True, "Alumno inscripto correctamente."

    except OSError as error:
        return False, str(error)


# LISTAR ALUMNOS DE UNA MATERIA

def obtener_alumnos_materia(nombre_materia):
    nombre_materia = str(nombre_materia).strip().capitalize()

    alumnos = []

    try:
        registros = persistencia.leer_lineas(
            ARCHIVO_INSCRIPCIONES
        )

        for registro in registros:
            partes = registro.split(";", 2)

            if len(partes) < 2:
                continue

            materia, dni = partes[0], partes[1]

            if materia == nombre_materia:
                encontrado, estudiante = buscar_estudiante_por_dni(dni)

                if encontrado:
                    notas = []

                    if len(partes) == 3 and partes[2].strip():
                        try:
                            notas = [
                                float(nota)
                                for nota in partes[2].split(",")
                            ]
                        except ValueError:
                            notas = []

                    alumnos.append({
                        "dni": dni,
                        "legajo": estudiante["legajo"],
                        "nombre": estudiante["nombre"],
                        "apellido": estudiante["apellido"],
                        "notas": notas
                    })

        return alumnos

    except OSError:
        return []
