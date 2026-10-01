'''
crud for materias
crud for signatures
'''


NOTA_APROBADA = 4
NOTA_ALTA = 8


def obtener_alumnos_materia(estudiantes, materia):
	'''
	devuelve los alumnos que cursal tal materia
	'''
	return filter(
		lambda legajo, info: materia in info[2],
		estudiantes.items()
	)

def calcular_promedio_materia(estudiantes, materia):
	'''
	devuelve el promedio de las notas en tal materia
	'''

	alumnos = obtener_alumnos_materia(estudiantes, materia)

	suma_notas = sum(map(
		lambda alumno: alumno[2][materia],
		alumnos.values()
	))

	return suma_notas / len(alumnos)


def porcentaje_nota_mayor_igual(estudiantes, materia, nota):

	alumnos = obtener_alumnos_materia(estudiantes, materia)

	cantidad_alumnos_nota = 0

	for alumno in alumnos:

		if alumno[2][materia] >= nota:
			cantidad_alumnos_nota += 1

	return cantidad_alumnos_nota / len(alumnos)



def cargar_estudiantes(archivo):
	# ejemplo. TODO: hacer logica real
	return {
		1234: [47_321_654, 'Arturo López', {}]
	}

def guardar_estudiantes(archivo, estudiantes):
	... # TODO



def cargar_materias(archivo):
	# ejemplo. TODO: hacer logica real
	return {
		'Geografia',
		'Matematicas',
		'Lengua',
		'Historia',
		'Ciencias',
	}

def guardar_materias(archivo, materias):
	... # TODO
