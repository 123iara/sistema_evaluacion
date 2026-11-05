# Crear, Leer, Actualizar y Borrar (CRUD) de alumnos
import re
from datos_generales.memoria import estudiantes
from datos_generales.persistencia import guardar_datos

# Función para limpiar espacios y poner Mayúscula Inicial (lambda)
formatear_nombre = lambda texto: str(texto).strip().title()


# EXPRESIONES REGULARES PARA VALIDAR DNI Y NOMBRE:
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
    # Ahora simplemente devolvemos el diccionario en memoria
    return estudiantes

def crear_estudiante(dni, nombre, apellido):
    ## VALIDAMOS EL FORMATO CON REGEX
    if not validar_dni(dni):
        return False, "Error: El DNI debe ser numérico y tener 8 dígitos."
    if not validar_nombre_apellido(nombre) or not validar_nombre_apellido(apellido):
        return False, "Error: El nombre y apellido solo pueden contener letras."

    # FORMATO DEL NOMBRE Y APELLIDO
    nombre = formatear_nombre(nombre)
    apellido = formatear_nombre(apellido)

    # VERIFICAR SI EL DNI YA ESTÁ REGISTRADO
    if dni in estudiantes:
       return False, f"El estudiante con DNI {dni} ya está registrado."

    ## Slicing para usuario
    usuario_generado = (nombre[0:1] + apellido).lower().replace(" ", "")
    legajo = len(estudiantes) + 1 

    # Guardamos en el diccionario de memoria
    estudiantes[dni] = {
        "dni": dni,
        "legajo": legajo,
        "nombre": nombre,
        "apellido": apellido,
        "usuario": usuario_generado
    }

    try:
        # Llamamos a persistencia para que actualice el CSV
        guardar_datos()
        return True, f"Estudiante {nombre} registrado con éxito."
    except Exception as e:
        return False, f"Error al guardar los datos: {e}"


# ENCONTRAR ESTUDIANTE
def buscar_estudiante_por_dni(dni):
    if dni in estudiantes:
        return True, estudiantes[dni]
    return False, "Estudiante no encontrado."


# UPDATE Estudiante
def modificar_datos_estudiante(dni, nuevo_nombre, nuevo_apellido):
    if not validar_nombre_apellido(nuevo_nombre) or not validar_nombre_apellido(nuevo_apellido):
        return False, "Error: El nombre y apellido solo pueden contener letras."
    
    if dni in estudiantes:
        # Actualizamos en el diccionario
        estudiantes[dni]["nombre"] = formatear_nombre(nuevo_nombre)
        estudiantes[dni]["apellido"] = formatear_nombre(nuevo_apellido)
        # Opcional: Actualizar el usuario también basado en el nuevo nombre
        estudiantes[dni]["usuario"] = (estudiantes[dni]["nombre"][0:1] + estudiantes[dni]["apellido"]).lower().replace(" ", "")
        
        try:
            guardar_datos()
            return True, f"Datos del DNI {dni} actualizados con éxito."
        except Exception as e:
            return False, f"Error al guardar los datos: {e}"
            
    return False, f"Estudiante con DNI {dni} no encontrado."


# DELETE Estudiante
def eliminar_estudiante(dni_borrar):
    if dni_borrar in estudiantes:
        # Borramos del diccionario
        del estudiantes[dni_borrar]
        try:
            guardar_datos()
            return True, f"Estudiante con DNI {dni_borrar} eliminado del sistema."
        except Exception as e:
            return False, f"Error al guardar los datos: {e}"
            
    return False, f"Estudiante con DNI {dni_borrar} no encontrado."


# Funciones lambda (ahora lee directamente del diccionario)
def filtrar_estudiantes_por_apellido(letra_inicial):
    """Devuelve una lista de alumnos cuyo apellido inicia con una letra específica."""
    todos = list(estudiantes.values())
    letra = letra_inicial.lower()
    filtrados = list(filter(lambda est: est["apellido"][0].lower() == letra, todos))
    nombres_completos = list(map(lambda est: f"{est['apellido']}, {est['nombre']}", filtrados))
    return nombres_completos