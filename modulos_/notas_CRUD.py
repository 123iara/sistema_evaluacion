#Crear, Leer, Actualizar y Borrar notas de alumnos en materias


from datos_generales.memoria import materias

def actualizar_nota(nombre_materia, dni, nueva_nota):
    if nueva_nota < 0 or nueva_nota > 10:
        return False, "La nota debe estar entre 0 y 10."

    for alumno in materias[nombre_materia]["alumnos"]:
        if alumno["dni"] == dni:
            alumno["nota"] = nueva_nota
            return True, "Nota modificada correctamente."
            
    return False, "Alumno no encontrado en esta materia."

def obtener_notas(nombre_materia):
    return materias[nombre_materia]["alumnos"]
