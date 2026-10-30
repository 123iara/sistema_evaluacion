#Crear, Leer, Actualizar y Borrar (CRUD) de alumnos

from datos_generales.memoria import estudiantes

import re #para expresiones regulares, se usa para validar el formato del DNI

#Función para limpiar espacios y poner Mayúscula Inicial (lambda)
formatear_nombre = lambda texto: str(texto).strip().title()  #Limpia espacios sobrantes y pone la primera letra en mayúscula

#EXPRESIONES REGULARES PARA VALIDAR DNI:
def validar_dni(dni):
    """Verifica que el DNI tenga exactamente 8 números."""
    patron = r"^\d{8}$" 
    return bool(re.fullmatch(patron, dni))

def validar_nombre_apellido(texto):
    """Verifica que el texto contenga solo letras y espacios."""
    patron = r"^[a-zA-Z\s]+$"
    return bool(re.search(patron, texto))


#FUNCIONES CRUD: 
def crear_estudiante(dni, nombre, apellido):
    #VALIDAMOS EL FORMATO CON REGEX
    if not validar_dni(dni):
        return False, "Error: El DNI debe ser numérico y contener exactamente 8 dígitos."

    if not validar_nombre_apellido(nombre) or not validar_nombre_apellido(apellido):
        return False, "Error: El nombre y apellido solo pueden contener letras."

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

    if dni not in estudiantes:
        return False, f"Estudiante con DNI {dni} no encontrado."

    #VALIDAMOS EL FORMATO CON REGEX
    if not validar_nombre_apellido(nuevo_nombre) or not validar_nombre_apellido(nuevo_apellido):
        return False, "Error: El nombre y apellido solo pueden contener letras."

    
    #Funcion lambda para actualizar
    estudiantes[dni]["nombre"] = formatear_nombre(nuevo_nombre)
    estudiantes[dni]["apellido"] = formatear_nombre(nuevo_apellido)
    return True, f"Datos del DNI {dni} actualizados con éxito."
    

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
    filtrados = list(filter(lambda est: est["apellido"][0].lower() == letra, todos)) #filter y lambda 
                                                                        
    #Convierte el diccionario de cada alumno en un texto simple y prolijo ("Apellido, Nombre") listo para imprimir
    nombres_completos = list(map(lambda est: f"{est['apellido']}, {est['nombre']}", filtrados)) #map y lambda

    return nombres_completos