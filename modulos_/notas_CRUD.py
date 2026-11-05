
# CRUD DE NOTAS UTILIZANDO ARCHIVOS TXT

from datos_generales import persistencia

ARCHIVO_INSCRIPCIONES = persistencia.ARCHIVO_INSCRIPCIONES


def _buscar_inscripcion(nombre_materia, dni):
    registros = persistencia.leer_lineas(
        ARCHIVO_INSCRIPCIONES
    )

    for indice, registro in enumerate(registros):
        partes = registro.split(";", 2)

        if len(partes) >= 2:
            if partes[0] == nombre_materia and partes[1] == str(dni):
                notas = []

                if len(partes) == 3 and partes[2].strip():
                    notas = [
                        float(nota)
                        for nota in partes[2].split(",")
                    ]

                return registros, indice, notas

    return registros, None, None


def agregar_nota(nombre_materia, dni, nota):
    try:
        nota = float(nota)

        if nota < 0 or nota > 10:
            return False, "La nota debe estar entre 0 y 10."

        registros, indice, notas = _buscar_inscripcion(
            nombre_materia,
            dni
        )

        if indice is None:
            return False, "Alumno no encontrado en esta materia."

        notas.append(nota)

        registros[indice] = (
            f"{nombre_materia};{dni};"
            + ",".join(map(str, notas))
        )

        persistencia.escribir_lineas(
            ARCHIVO_INSCRIPCIONES,
            registros
        )

        return True, "Nota agregada correctamente."

    except (ValueError, OSError) as error:
        return False, str(error)


def obtener_notas(nombre_materia, dni):
    try:
        _, indice, notas = _buscar_inscripcion(
            nombre_materia,
            dni
        )

        if indice is None:
            return False, "Alumno no encontrado."

        return True, notas

    except (ValueError, OSError) as error:
        return False, str(error)


def modificar_nota(nombre_materia, dni, indice_nota, nueva_nota):
    try:
        nueva_nota = float(nueva_nota)

        if nueva_nota < 0 or nueva_nota > 10:
            return False, "La nota debe estar entre 0 y 10."

        registros, indice, notas = _buscar_inscripcion(
            nombre_materia,
            dni
        )

        if indice is None:
            return False, "Alumno no encontrado."

        if not 0 <= indice_nota < len(notas):
            return False, "Índice de nota incorrecto."

        notas[indice_nota] = nueva_nota

        registros[indice] = (
            f"{nombre_materia};{dni};"
            + ",".join(map(str, notas))
        )

        persistencia.escribir_lineas(
            ARCHIVO_INSCRIPCIONES,
            registros
        )

        return True, "Nota modificada correctamente."

    except (ValueError, OSError) as error:
        return False, str(error)


def eliminar_nota(nombre_materia, dni, indice_nota):
    try:
        registros, indice, notas = _buscar_inscripcion(
            nombre_materia,
            dni
        )

        if indice is None:
            return False, "Alumno no encontrado."

        if not 0 <= indice_nota < len(notas):
            return False, "Índice de nota incorrecto."

        del notas[indice_nota]

        registros[indice] = (
            f"{nombre_materia};{dni};"
            + ",".join(map(str, notas))
        )

        persistencia.escribir_lineas(
            ARCHIVO_INSCRIPCIONES,
            registros
        )

        return True, "Nota eliminada correctamente."

    except (ValueError, OSError) as error:
        return False, str(error)
