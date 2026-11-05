#Crear, Leer, Actualizar y Borrar (CRUD) de alumnos
import os
import re

# Función para limpiar espacios y poner Mayúscula Inicial (lambda)
formatear_nombre = lambda texto: str(texto).strip().title()

# CONSTANTES DE ARCHIVOS (Se usa el txt directo para mantener tus tests en verde)
ARCHIVO_ALUMNOS = "alumnos.txt"
ARCHIVO_INSCRIPCIONES = "inscripciones.txt"

# EXPRESIONES REGULARES PARA VALIDAR DNI:
def validar_dni(dni):
    """Verifica que el DNI tenga exactamente 8 números."""
    patron = r"^\d{8}$" 
    return bool(re.fullmatch(patron, dni))

def validar_nombre_apellido(texto):
    """Verifica que el texto contenga solo letras y espacios."""
    patron = r"^[a-zA-Z\s]+$"
    return bool(re.search(patron, texto))

# FUNCIONES CRUD:
def obtener_todos_estudiantes():
    estudiantes = {}
    try:
        with open(ARCHIVO_ALUMNOS, 'r', encoding='UTF-8') as archivo:
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
        pass
    return estudiantes

def crear_estudiante(dni, nombre, apellido):
    ## VALIDAMOS EL FORMATO CON REGEX
    if not validar_dni(dni):
        return False, "Error: El DNI debe ser numérico y tener 8 dígitos."
    if not validar_nombre_apellido(nombre) or not validar_nombre_apellido(apellido):
        return False, "Error: El nombre y apellido solo pueden contener letras."

    # FORMATO DEL NOMBRE Y APELLIDO
    nombre = nombre.strip().title()
    apellido = apellido.strip().title()

    # VERIFICAR SI EL DNI YA ESTÁ REGISTRADO
    estudiantes = obtener_todos_estudiantes()
    if dni in estudiantes:
       return False, f"El estudiante con DNI {dni} ya está registrado."

    ## Slicing para usuario
    usuario_generado = (nombre[0:1] + apellido).lower().replace(" ", "")
    legajo = len(estudiantes) + 1 

    # Excepciones y Escritura en archivo
    try:
        with open(ARCHIVO_ALUMNOS, 'a', encoding='UTF-8') as archivo:
            linea_registro = f"{dni};{legajo};{formatear_nombre(nombre)};{formatear_nombre(apellido)};{usuario_generado}\n"
            archivo.write(linea_registro)
        return True, f"Estudiante {formatear_nombre(nombre)} registrado con éxito."
    except PermissionError:
        return False, "Error: Permisos insuficientes para escribir en el archivo."
    except OSError as e:
        return False, f"Error de escritura o ruta inválida: {e}"

# ENCONTRAR ESTUDIANTE
def buscar_estudiante_por_dni(dni):
    estudiantes = obtener_todos_estudiantes()
    if str(dni) in estudiantes:
        return True, estudiantes[str(dni)]
    return False, f"Estudiante con DNI {dni} no encontrado."

# UPDATE Estudiante
def modificar_datos_estudiante(dni, nuevo_nombre, nuevo_apellido):
    if not validar_nombre_apellido(nuevo_nombre) or not validar_nombre_apellido(nuevo_apellido):
        return False, "Error: El nombre y apellido solo pueden contener letras."
    
    encontrado = False
    try:
        with open(ARCHIVO_ALUMNOS, 'r', encoding='UTF-8') as orig, \
             open("alumnos_temp.txt", 'w', encoding='UTF-8') as temp:
            for linea in orig:
                datos = linea.strip().split(';')
                if len(datos) == 5 and datos[0] == str(dni):
                    dni, legajo, old_nombre, old_apellido, usuario = datos
                    temp.write(f"{dni};{legajo};{formatear_nombre(nuevo_nombre)};{formatear_nombre(nuevo_apellido)};{usuario}\n")
                    encontrado = True
                else:
                    temp.write(linea)

        os.replace("alumnos_temp.txt", ARCHIVO_ALUMNOS) 
        if encontrado:
            return True, f"Datos del DNI {dni} actualizados con éxito."
        return False, f"Estudiante con DNI {dni} no encontrado."
    except Exception as e:
        return False, f"Error al modificar archivo: {e}"

def eliminar_estudiante(dni_borrar):
    encontrado = False
    try:
        with open(ARCHIVO_ALUMNOS, 'r', encoding='UTF-8') as orig, \
             open("alumnos_temp.txt", 'w', encoding='UTF-8') as temp:
            for linea in orig:
                datos = linea.strip().split(';')
                if len(datos) == 5 and datos[0] == str(dni_borrar):
                    encontrado = True 
                else:
                    temp.write(linea)
                    
        os.replace("alumnos_temp.txt", ARCHIVO_ALUMNOS)
        if encontrado:
            return True, f"Estudiante con DNI {dni_borrar} eliminado del sistema."
        return False, f"Estudiante con DNI {dni_borrar} no encontrado."
    except Exception as e:
        return False, f"Error al eliminar del archivo: {e}"

# Funciones lambda
def filtrar_estudiantes_por_apellido(letra_inicial):
    """Devuelve una lista de alumnos cuyo apellido inicia con una letra específica."""
    estudiantes = obtener_todos_estudiantes()
    todos = list(estudiantes.values())
    letra = letra_inicial.lower()
    filtrados = list(filter(lambda est: est["apellido"][0].lower() == letra, todos))
    nombres_completos = list(map(lambda est: f"{est['apellido']}, {est['nombre']}", filtrados))
    return nombres_completos
