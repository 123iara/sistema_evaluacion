#Crear, Leer, Actualizar y Borrar notas de alumnos en materias

from datos_generales.memoria import materias
from datos_generales.persistencia import guardar_datos

#NOTAS POR MATERIA

def agregar_nota(nombre_materia, dni, nota):
    try:
        # Verificamos que la nota sea un número
        if not isinstance(nota, (int, float)):
            raise TypeError("La nota debe ser un número.")

        # Verificamos que esté entre 0 y 10
        if nota < 0 or nota > 10:
            raise ValueError("La nota debe estar entre 0 y 10.")

        # Buscamos al alumno dentro de la materia
        for alumno in materias.get(nombre_materia, {}).get("alumnos", []):
            if alumno["dni"] == dni:
                alumno["notas"].append(nota)
                guardar_datos()
                return True, "Nota agregada correctamente."

        return False, "Alumno no encontrado en esta materia."

    except (TypeError, ValueError) as error:
        return False, str(error)


def obtener_notas(nombre_materia, dni):
    for alumno in materias.get(nombre_materia, {}).get("alumnos", []):
        if alumno["dni"] == dni:
            return True, alumno["notas"]
    return False, "Alumno no encontrado."

# MODIFICAR NOTAS

def modificar_nota(nombre_materia, dni, indice, nueva_nota):
    try:
        # Verificamos que la nota sea numérica
        if not isinstance(nueva_nota, (int, float)):
            raise TypeError("La nota debe ser un número.")

        # Verificamos que esté entre 0 y 10
        if nueva_nota < 0 or nueva_nota > 10:
            raise ValueError("La nota debe estar entre 0 y 10.")

        # Verificamos que el índice sea entero
        if not isinstance(indice, int):
            raise TypeError("El índice debe ser un número entero.")

        # Buscamos al alumno
        for alumno in materias.get(nombre_materia, {}).get("alumnos", []):
            if alumno["dni"] == dni:

                if indice < 0 or indice >= len(alumno["notas"]):
                    raise IndexError("Índice de nota incorrecto.")

                alumno["notas"][indice] = nueva_nota
                guardar_datos()
                return True, "Nota modificada."

        return False, "Alumno no encontrado."

    except (TypeError, ValueError, IndexError) as error:
        return False, str(error)


def eliminar_nota(nombre_materia, dni, indice):
    for alumno in materias.get(nombre_materia, {}).get("alumnos", []):
        if alumno["dni"] == dni:
            if 0 <= indice < len(alumno["notas"]):
                del alumno["notas"][indice]
                guardar_datos()
                return True, "Nota eliminada."
            return False, "Índice de nota incorrecto."
    return False, "Alumno no encontrado."
