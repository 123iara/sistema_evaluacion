#Crear, Leer, Actualizar y Borrar (CRUD) de alumnos


import re #para expresiones regulares, se usa para validar el formato del DNI

import os #para verificar la existencia del archivo y manejar errores de escritura

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
    ##VALIDAMOS EL FORMATO CON REGEX
    if not validar_dni(dni):
        return False, "Error: El DNI debe ser numérico y tener 8 dígitos."
    if not validar_nombre_apellido(nombre) or not validar_nombre_apellido(apellido):
        return False, "Error: El nombre y apellido solo pueden contener letras."

    #verificar si el DNI ya está registrado
    estudiantes = obtener_todos_estudiantes()
    if dni in estudiantes:
       return False, f"El estudiante con DNI {dni} ya está registrado."

    ##Slicing y metodo de cadenas para crearle un usuario a partir del nombre y apellido (en minusculas)
    usuario_generado = (nombre[0:1] + apellido).lower().replace(" ", "")
    legajo = len(estudiantes) + 1 ##ASIGNAR UN NUEVO LEGAJO

    #Excepciones y Escritura en archivo
    try:
        with open("alumnos.txt", 'a', encoding='UTF-8') as archivo:
            linea_registro = f"{dni};{legajo};{formatear_nombre(nombre)};{formatear_nombre(apellido)};{usuario_generado}\n"
            archivo.write(linea_registro)
        return True, f"Estudiante {formatear_nombre(nombre)} registrado con éxito."
    except PermissionError:
        return False, "Error: Permisos insuficientes para escribir en el archivo."
    except OSError as e:
        return False, f"Error de escritura o ruta inválida: {e}"


def obtener_todos_estudiantes():
    #Lee el archivo .txt y reconstruye el diccionario de estudiantes
    estudiantes = {}
    try:
        with open("alumnos.txt", 'r', encoding='UTF-8') as archivo:
            for linea in archivo:
                datos = linea.strip().split(';')
                if len(datos) == 5:
                    dni, legajo, nombre, apellido, usuario = datos
                    estudiantes[dni] = {
                        "dni": dni,
                        "legajo": int(legajo),
                        "nombre": nombre,
                        "apellido": apellido,
                        "usuario": usuario
                    }
    except FileNotFoundError:
        pass # Si el archivo no existe, devuelve un diccionario vacío
    return estudiantes

#ENCONTRAR ESTUDIANTE
def buscar_estudiante_por_dni(dni):
    estudiantes = obtener_todos_estudiantes()
    if str(dni) in estudiantes:
        return True, estudiantes[str(dni)]
    return False, f"Estudiante con DNI {dni} no encontrado."

#UPDATE Estudiante:
def modificar_datos_estudiante(dni, nuevo_nombre, nuevo_apellido):

    #VALIDAMOS EL FORMATO CON REGEX
    if not validar_nombre_apellido(nuevo_nombre) or not validar_nombre_apellido(nuevo_apellido):
        return False, "Error: El nombre y apellido solo pueden contener letras."
   
    encontrado = False
    try:
        # archivo auxiliar temporal para la modificación
        with open("alumnos.txt", 'r', encoding='UTF-8') as orig, \
             open("alumnos_temp.txt", 'w', encoding='UTF-8') as temp:
            
            for linea in orig:
                datos = linea.strip().split(';')
                # Si el DNI es el que BUSCAMOS, escribimos la linea con el nombre y apellido actualizados
                if len(datos) == 5 and datos[0] == str(dni):
                    dni, legajo, old_nombre, old_apellido, usuario = datos
                    temp.write(f"{dni};{legajo};{formatear_nombre(nuevo_nombre)};{formatear_nombre(nuevo_apellido)};{usuario}\n")
                    encontrado = True
                else:
                    # Si el DNI NO es el que buscamos, copiamos la línea original al archivo temporal
                    temp.write(linea)

        # FUERA del bloque with: reemplazamos el archivo original viejo por el temporal actualizado
        os.replace("alumnos_temp.txt", "alumnos.txt") 
        
        if encontrado:
            return True, f"Datos del DNI {dni} actualizados con éxito."
        return False, f"Estudiante con DNI {dni} no encontrado."
        
    except Exception as e:
        return False, f"Error al modificar archivo: {e}"

    

def eliminar_estudiante(dni_borrar):
    encontrado = False
    try:
        #Archivo temporal para almacenar los datos mientras se elimina el estudiante
        with open("alumnos.txt", 'r', encoding='UTF-8') as orig, \
             open("alumnos_temp.txt", 'w', encoding='UTF-8') as temp:
             
            for linea in orig:
                datos = linea.strip().split(';')
                #Si encontramos al alumno a eliminar, lo omitimos para que no se guarde en el nuevo archivo
                if len(datos) == 5 and datos[0] == str(dni_borrar):
                    encontrado = True 
                else:
                    #El resto de los alumnos se copian normalmente:
                    temp.write(linea)
                    
        #Reemplazamos el archivo original por el temporal 
        os.replace("alumnos_temp.txt", "alumnos.txt")
        
        if encontrado:
            return True, f"Estudiante con DNI {dni_borrar} eliminado del sistema."
        return False, f"Estudiante con DNI {dni_borrar} no encontrado."
    except Exception as e:
        return False, f"Error al eliminar del archivo: {e}"


#Funciones lambda para filtrar estudiantes por nombre o apellido
def filtrar_estudiantes_por_apellido(letra_inicial):
    """Devuelve una lista de alumnos cuyo apellido inicia con una letra específica."""
    estudiantes = obtener_todos_estudiantes()
    todos = list(estudiantes.values())
    letra = letra_inicial.lower()

    # La funcion debajo queda solo con los alumnos que cumplen la condicion pedida
    filtrados = list(filter(lambda est: est["apellido"][0].lower() == letra, todos)) # filter y lambda

    # Convierte el diccionario de cada alumno en un texto simple y prolijo
    nombres_completos = list(map(lambda est: f"{est['apellido']}, {est['nombre']}", filtrados)) # map y lambda

    return nombres_completos