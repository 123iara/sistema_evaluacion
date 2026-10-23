#Crear, Leer, Actualizar y Borrar (CRUD) de alumnos


from datos_generales.memoria import estudiantes
from datos_generales.persistencia import guardar_datos
from modulos_.validaciones import validar_dni, validar_nombre, normalizar_nombre

def crear_estudiante(dni, nombre, apellido):
    dni = str(dni).strip()
    if not validar_dni(dni):
        return False, "El DNI debe tener 7 u 8 dígitos."
    if not validar_nombre(nombre) or not validar_nombre(apellido):
        return False, "Nombre y apellido deben contener solo letras y separadores simples."
    #VERIFICAR SI EL DNI YA ESTÁ REGISTRADO
    if dni in estudiantes:
        return False, "El estudiante ya está registrado."
    
    #ASIGNAR UN NUEVO LEGAJO
    legajo = len(estudiantes) + 1   
    
    #CREAR AL ESTUDIANTE
    nuevo_estudiante = {
        "legajo": legajo,
        "nombre": normalizar_nombre(nombre),
        "apellido": normalizar_nombre(apellido)
    }
    
    #AGREGARLO A LA LISTA
    estudiantes[dni] = nuevo_estudiante
    guardar_datos()
    return True, "Estudiante registrado con éxito."

def obtener_todos_estudiantes():
    return estudiantes

#ENCONTRAR ESTUDIANTE
def buscar_estudiante_por_dni(dni):
    if dni in estudiantes:
        return True, estudiantes[dni]
    return False, "Estudiante no encontrado."

#UPDATE Estudiante:
def modificar_datos_estudiante(dni, nuevo_nombre, nuevo_apellido):
    if not validar_nombre(nuevo_nombre) or not validar_nombre(nuevo_apellido):
        return False, "Nombre y apellido deben contener solo letras y separadores simples."
    if dni in estudiantes:
        #ACTUALIZAR LOS DATOS DEL ESTUDIANTE
        estudiantes[dni]["nombre"] = normalizar_nombre(nuevo_nombre)
        estudiantes[dni]["apellido"] = normalizar_nombre(nuevo_apellido)
        from datos_generales.memoria import materias
        for materia in materias.values():
            for alumno in materia["alumnos"]:
                if alumno["dni"] == dni:
                    alumno["nombre"] = estudiantes[dni]["nombre"]
                    alumno["apellido"] = estudiantes[dni]["apellido"]
        guardar_datos()
        return True, "Datos actualizados con éxito."
    return False, "Estudiante no encontrado."

def eliminar_estudiante(dni):
    if dni in estudiantes:
        del estudiantes[dni]
        # Evita dejar inscripciones que apunten a un estudiante eliminado.
        from datos_generales.memoria import materias
        for materia in materias.values():
            materia["alumnos"] = [alumno for alumno in materia["alumnos"] if alumno["dni"] != dni]
        guardar_datos()
        return True, "Estudiante eliminado del sistema."
    return False, "Estudiante no encontrado."
