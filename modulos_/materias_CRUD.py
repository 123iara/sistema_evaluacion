#Crear, Leer, Actualizar y Borrar (CRUD) de materias


from datos_generales.memoria import materias, estudiantes

def agregar_alumno_materia(nombre_materia, dni):
    if dni not in estudiantes:
        return False, "El estudiante no está registrado en el sistema general. Regístrelo primero."
    
    # Verificar si ya cursa la materia
    for alumno in materias[nombre_materia]["alumnos"]:
        if alumno["dni"] == dni:
            return False, "El estudiante ya está inscripto en esta materia."

    estudiante = estudiantes[dni]
    nuevo_alumno = {
        "dni": dni,
        "legajo": estudiante["legajo"],
        "nombre": estudiante["nombre"],
        "apellido": estudiante["apellido"],
        "nota": 0
    }
    
    materias[nombre_materia]["alumnos"].append(nuevo_alumno)
    return True, "Alumno inscripto correctamente en la materia."

def obtener_alumnos_materia(nombre_materia):
    return materias[nombre_materia]["alumnos"]

def quitar_alumno_materia(nombre_materia, dni):
    lista_alumnos = materias[nombre_materia]["alumnos"]
    for i, alumno in enumerate(lista_alumnos):
        if alumno["dni"] == dni:
            del lista_alumnos[i]
            return True, "Alumno dado de baja de la materia."
    return False, "Alumno no encontrado en esta materia."