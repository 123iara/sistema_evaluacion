#Crear, Leer, Actualizar y Borrar (CRUD) de materias


from datos_generales.memoria import materias, estudiantes
from datos_generales.persistencia import guardar_datos

def crear_materia(nombre):
    nombre = nombre.strip().capitalize()
    if nombre in materias:
        return False, "La materia ya existe."
    materias[nombre] = {"alumnos": []}
    guardar_datos()
    return True, "Materia creada con éxito."

def listar_materias():
    return list(materias.keys())

def modificar_materia(nombre_actual, nombre_nuevo):
    nombre_actual = nombre_actual.strip().capitalize()
    nombre_nuevo = nombre_nuevo.strip().capitalize()
    
    if nombre_actual not in materias:
        return False, "Materia no encontrada."
    if nombre_nuevo in materias:
        return False, "El nuevo nombre ya está ocupado."
    
    materias[nombre_nuevo] = materias.pop(nombre_actual)
    guardar_datos()
    return True, "Nombre de materia actualizado."

def eliminar_materia(nombre):
    nombre = nombre.strip().capitalize()
    if nombre in materias:
        del materias[nombre]
        guardar_datos()
        return True, "Materia eliminada del sistema."
    return False, "Materia no encontrada."

#AGREGAR ALUMNO A MATERIA
def agregar_alumno_materia(nombre_materia, dni):
    #BUSCAMOS SI EL ESTUDIANTE EXISTE
    #¿DNI existe en estudiantes?
    if dni not in estudiantes:
        return False, "El estudiante no está registrado."
    if nombre_materia not in materias:
        return False, "Materia no encontrada."
    
    #DNI existe = estudiante encontrado
    # El conjunto permite comprobar de forma directa si ya está inscripto.
    dnis_inscriptos = {
        alumno["dni"] for alumno in materias[nombre_materia]["alumnos"]
    }
    if dni in dnis_inscriptos:
        return False, "El estudiante ya está inscripto en esta materia."

    # AGREGAR EL ESTUDIANTE A LA MATERIA
    estudiante = estudiantes[dni]
    nuevo_alumno = {
        "dni": dni,
        "legajo": estudiante["legajo"],
        "nombre": estudiante["nombre"],
        "apellido": estudiante["apellido"],
        "notas": [] 
    }
    materias[nombre_materia]["alumnos"].append(nuevo_alumno)
    guardar_datos()
    return True, "Alumno inscripto correctamente."

#LISTA ALUMNOS POR MATERIA
def obtener_alumnos_materia(nombre_materia):
    if nombre_materia in materias:
        return materias[nombre_materia]["alumnos"]
    return []
