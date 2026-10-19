#Crear, Leer, Actualizar y Borrar (CRUD) de alumnos


from datos_generales.memoria import estudiantes

def crear_estudiante(dni, nombre, apellido):
    if dni in estudiantes:
        return False, "El estudiante ya está registrado."
    
    legajo = len(estudiantes) + 1   
    estudiantes[dni] = {
        "legajo": legajo,
        "nombre": nombre,
        "apellido": apellido
    }
    return True, "Estudiante registrado con éxito."

def obtener_todos_estudiantes():
    return estudiantes

def buscar_estudiante_por_dni(dni):
    if dni in estudiantes:
        return True, estudiantes[dni]
    return False, "Estudiante no encontrado."

def modificar_datos_estudiante(dni, nuevo_nombre, nuevo_apellido):
    if dni in estudiantes:
        estudiantes[dni]["nombre"] = nuevo_nombre
        estudiantes[dni]["apellido"] = nuevo_apellido
        return True, "Datos actualizados con éxito."
    return False, "Estudiante no encontrado."

def eliminar_estudiante(dni):
    if dni in estudiantes:
        del estudiantes[dni]
        return True, "Estudiante eliminado del sistema."
    return False, "Estudiante no encontrado."