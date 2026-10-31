#Crear, Leer, Actualizar y Borrar (CRUD) de materias

import os

from alumnos_CRUD import obtener_todos_estudiantes

ARCHIVO_MATERIAS = "materias.txt"
ARCHIVO_INSCRIPCIONES = "inscripciones.txt"
ARCHIVO_TEMP = "temp_materias.txt"

def obtener_todas_materias():
    """Función auxiliar para leer el archivo de materias y armar una lista."""
    materias = []
    try:
        with open(ARCHIVO_MATERIAS, 'r', encoding='UTF-8') as archivo:
            for linea in archivo:
                if linea.strip():
                    materias.append(linea.strip())
    except FileNotFoundError:
        pass
    return materias

def crear_materia(nombre):
    nombre = nombre.strip().capitalize()
    materias = obtener_todas_materias()
    
    if nombre in materias:
        return False, "La materia ya existe."
    
    try:
        with open(ARCHIVO_MATERIAS, 'a', encoding='UTF-8') as archivo:
            archivo.write(f"{nombre}\n")
        return True, "Materia creada con éxito."
    except OSError as e:
        return False, f"Error al escribir en disco: {e}"

def listar_materias():
   return obtener_todas_materias()

def modificar_materia(nombre_actual, nombre_nuevo):
    nombre_actual = nombre_actual.strip().upper()
    nombre_nuevo = nombre_nuevo.strip().upper()

    materias = obtener_todas_materias()
    if nombre_actual not in materias:
        return False, "Materia no encontrada."
    if nombre_nuevo in materias:
        return False, "El nuevo nombre ya está ocupado."

    encontrado = False
    try:
        #modificamos la materia en materias.txt con archivo temporal
        with open(ARCHIVO_MATERIAS, 'r', encoding='UTF-8') as orig, \
             open(ARCHIVO_TEMP, 'w', encoding='UTF-8') as temp:
            for linea in orig:
                materia = linea.strip()
                if materia == nombre_actual:
                    temp.write(f"{nombre_nuevo}\n")
                    encontrado = True
                elif materia:
                    temp.write(f"{materia}\n")
        os.replace(ARCHIVO_TEMP, ARCHIVO_MATERIAS)

        # Actualizamos también el nombre en las inscripciones para no perder alumnos
        if os.path.exists(ARCHIVO_INSCRIPCIONES):
            with open(ARCHIVO_INSCRIPCIONES, 'r', encoding='UTF-8') as orig_i, \
                 open("temp_inscripciones.txt", 'w', encoding='UTF-8') as temp_i:
                for linea in orig_i:
                    datos = linea.strip().split(';')
                    if datos[0] == nombre_actual:
                        # Reemplaza nombre viejo por nuevo, mantiene DNI y notas intactas
                        notas = datos[2] if len(datos) > 2 else ""
                        temp_i.write(f"{nombre_nuevo};{datos[1]};{notas}\n")
                    else:
                        temp_i.write(linea)
            os.replace("temp_inscripciones.txt", ARCHIVO_INSCRIPCIONES)

        return True, "Nombre de materia actualizado."
    except Exception as e:
        return False, f"Error al modificar: {e}"
    

def eliminar_materia(nombre):
    nombre = nombre.strip().title()
    encontrado = False  
    try:
        # Baja física en materias.txt
        with open(ARCHIVO_MATERIAS, 'r', encoding='UTF-8') as orig, \
             open(ARCHIVO_TEMP, 'w', encoding='UTF-8') as temp:
            for linea in orig:
                materia = linea.strip()
                if materia == nombre:
                    encontrado = True # Se omite
                elif materia:
                    temp.write(f"{materia}\n")
        os.replace(ARCHIVO_TEMP, ARCHIVO_MATERIAS)

        if encontrado:
            return True, "Materia eliminada del sistema."
        return False, "Materia no encontrada."
    except Exception as e:
        return False, f"Error al eliminar: {e}"
    
    

#AGREGAR ALUMNO A MATERIA
def agregar_alumno_materia(nombre_materia, dni):
    estudiantes = obtener_todos_estudiantes()
    if dni not in estudiantes:
        return False, "El estudiante no está registrado."
    
    materias = obtener_todas_materias()
    if nombre_materia not in materias:
        return False, "Materia no encontrada."
    
    #DNI existe = estudiante encontrado
    # VERIFICAR SI YA ESTA EN LA MATERIA
    try:
        with open(ARCHIVO_INSCRIPCIONES, 'r', encoding='UTF-8') as archivo:
            for linea in archivo:
                datos = linea.strip().split(';')
                if len(datos) >= 2 and datos[0] == nombre_materia and datos[1] == str(dni):
                    return False, "El estudiante ya está inscripto en esta materia."
    except FileNotFoundError:
        pass #Si no existe, es la primera inscripción

    # AGREGAR EL ESTUDIANTE A LA MATERIA
    try:
        with open(ARCHIVO_INSCRIPCIONES, 'a', encoding='UTF-8') as archivo:
            # Formato: Materia;DNI;Notas (dejamos las notas vacías por ahora)
            archivo.write(f"{nombre_materia};{dni};\n")
        return True, "Alumno inscripto correctamente."
    except OSError as e:
        return False, f"Error al inscribir: {e}"

#LISTA ALUMNOS POR MATERIA
def obtener_alumnos_materia(nombre_materia):
    #Devuelve los datos en formato de lista de diccionarios para mantener la compatibilidad con el resto del sistema.
    alumnos_inscriptos = []
    estudiantes = obtener_todos_estudiantes()
    try:
        with open(ARCHIVO_INSCRIPCIONES, 'r', encoding='UTF-8') as archivo:
            for linea in archivo:
                datos = linea.strip().split(';')
                if len(datos) >= 2 and datos[0] == nombre_materia:
                    dni = datos[1]
                    notas_str = datos[2] if len(datos) > 2 else ""
                    #si hay notas guardadas separadas por coma, las convierte a lista float
                    notas = [float(n) for n in notas_str.split(',')] if notas_str else []
                    
                    #cruzamos el DNI del archivo de inscripciones con los datos del archivo alumnos.txt
                    if dni in estudiantes:
                        est = estudiantes[dni]
                        nuevo_alumno = {
                            "dni": dni,
                            "legajo": est["legajo"],
                            "nombre": est["nombre"],
                            "apellido": est["apellido"],
                            "notas": notas
                        }
                        alumnos_inscriptos.append(nuevo_alumno)
    except FileNotFoundError:
        pass
    return alumnos_inscriptos