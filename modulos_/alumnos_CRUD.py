#Crear, Leer, Actualizar y Borrar (CRUD) de alumnos


from datos_generales.memoria import estudiantes

def crear_estudiante(dni, nombre, apellido):
    #VERIFICAR SI EL DNI YA ESTÁ REGISTRADO
    if dni in estudiantes:
       return False, f"El estudiante con DNI {dni} ya está registrado." #uso de f-string

    #Slicing y metodo de cadenas para crearle un usuario a partir del nombre y apellido (en minusculas)
    usuario_generado = (nombre[0:1] + apellido).lower().replace(" ", "")
    
    #ASIGNAR UN NUEVO LEGAJO
    legajo = len(estudiantes) + 1   
    
    #CREAR AL ESTUDIANTE
    nuevo_estudiante = {
        "legajo": legajo,
        "nombre": nombre.strip().title(),
        "apellido": apellido.strip().title(),
        "usuario": usuario_generado
    }
    
    #AGREGARLO A LA LISTA
    estudiantes[dni] = nuevo_estudiante
    return True, f"Estudiante {nombre.strip().title()} registrado con éxito."

def obtener_todos_estudiantes():
    return estudiantes

#ENCONTRAR ESTUDIANTE
def buscar_estudiante_por_dni(dni):
    if dni in estudiantes:
        return True, estudiantes[dni]
    return False, f"Estudiante con DNI {dni} no encontrado."

#UPDATE Estudiante:
def modificar_datos_estudiante(dni, nuevo_nombre, nuevo_apellido):
    if dni in estudiantes:
        #ACTUALIZAR LOS DATOS DEL ESTUDIANTE (con metodos de cadena)
        estudiantes[dni]["nombre"] = nuevo_nombre.strip().title()
        estudiantes[dni]["apellido"] = nuevo_apellido.strip().title()
        return True, f"Datos del DNI {dni} actualizados con éxito."
    return False, f"Estudiante con DNI {dni} no encontrado."

def eliminar_estudiante(dni):
    if dni in estudiantes:
        del estudiantes[dni]
        return True, f"Estudiante con DNI {dni} eliminado del sistema."
    return False, f"Estudiante con DNI {dni} no encontrado."