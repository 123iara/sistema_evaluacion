#Crear, Leer, Actualizar y Borrar notas de alumnos en materias

from datos_generales.memoria import materias

#NOTAS POR MATERIA
def agregar_nota(nombre_materia, dni, nota):
    if nota < 0 or nota > 10:
        return False, "La nota debe estar entre 0 y 10."

    #buscamos al alumno dentro de la materia
    for alumno in materias.get(nombre_materia, {}).get("alumnos", []):
        if alumno["dni"] == dni:
            alumno["notas"].append(nota)
            return True, "Nota agregada correctamente."
            
    return False, "Alumno no encontrado en esta materia."

def obtener_notas(nombre_materia, dni):
    for alumno in materias.get(nombre_materia, {}).get("alumnos", []):
        if alumno["dni"] == dni:
            return True, alumno["notas"]
    return False, "Alumno no encontrado."

# MODIFICAR NOTAS
def modificar_nota(nombre_materia, dni, indice, nueva_nota):
    if nueva_nota < 0 or nueva_nota > 10:
        return False, "La nota debe estar entre 0 y 10."

    for alumno in materias.get(nombre_materia, {}).get("alumnos", []):
        if alumno["dni"] == dni:
            if 0 <= indice < len(alumno["notas"]):
                alumno["notas"][indice] = nueva_nota
                return True, "Nota modificada."
            return False, "Índice de nota incorrecto."
    return False, "Alumno no encontrado."

def eliminar_nota(nombre_materia, dni, indice):
    for alumno in materias.get(nombre_materia, {}).get("alumnos", []):
        if alumno["dni"] == dni:
            if 0 <= indice < len(alumno["notas"]):
                del alumno["notas"][indice]
                return True, "Nota eliminada."
            return False, "Índice de nota incorrecto."
    return False, "Alumno no encontrado."
