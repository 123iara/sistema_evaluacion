import logica
import menu

ARCHIVO_ESTUDIANTES = 'estudiantes.csv'
ARCHIVO_MATERIAS = 'materias.csv'

estudiantes = logica.cargar_estudiantes(ARCHIVO_ESTUDIANTES)
materias = logica.cargar_materias(ARCHIVO_MATERIAS)

menu.principal(estudiantes, materias)

logica.guardar_estudiantes(ARCHIVO_ESTUDIANTES, estudiantes)
logica.guardar_materias(ARCHIVO_MATERIAS, materias)
