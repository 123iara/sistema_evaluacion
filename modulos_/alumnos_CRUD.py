#Crear, Leer, Actualizar y Borrar (CRUD) de alumnos

from datos_generales.memoria import estudiantes

#Función para limpiar espacios y poner Mayúscula Inicial (lambda)
formatear_nombre = lambda texto: str(texto).strip().title()  #Limpia espacios sobrantes y pone la primera letra en mayúscula

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
        "nombre": formatear_nombre(nombre),
        "apellido": formatear_nombre(apellido),
        "usuario": usuario_generado
    }
    
    #AGREGARLO A LA LISTA
    estudiantes[dni] = nuevo_estudiante
    return True, f"Estudiante {formatear_nombre(nombre)} registrado con éxito."

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
        #Funcion lambda para actualizar
        estudiantes[dni]["nombre"] = formatear_nombre(nuevo_nombre)
        estudiantes[dni]["apellido"] = formatear_nombre(nuevo_apellido)
        return True, f"Datos del DNI {dni} actualizados con éxito."
    return False, f"Estudiante con DNI {dni} no encontrado."

def eliminar_estudiante(dni):
    if dni in estudiantes:
        del estudiantes[dni]
        return True, f"Estudiante con DNI {dni} eliminado del sistema."
    return False, f"Estudiante con DNI {dni} no encontrado."

#Funciones lambda para filtrar estudiantes por nombre o apellido
def filtrar_estudiantes_por_apellido(letra_inicial):
    """Devuelve una lista de alumnos cuyo apellido inicia con una letra específica."""
    todos = list(estudiantes.values())
    letra = letra_inicial.lower()

    #La funcion debajo queda solo con los alumnos que cumplen la condición pedida (ej: que el apellido empiece con una letra específica)
    filtrados = list(filter(lambda est: est["apellido"].lower().startswith(letra), todos)) #filter y lambda 
                                                                        
    #Convierte el diccionario de cada alumno en un texto simple y prolijo ("Apellido, Nombre") listo para imprimir
    nombres_completos = list(map(lambda est: f"{est['apellido']}, {est['nombre']}", filtrados)) #map y lambda

    return nombres_completos