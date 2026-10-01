import logica


'''
================ CRUD ESTUDIANTES ================

------- CREATE -------
estudiantes[legajo] = [dni, nombre, notas]

------- READ -------
estudiantes[legajo]
estudiantes[legajo][0]
estudiantes[legajo][1]
estudiantes[legajo][2]
estudiantes[legajo][2][materia]

------- UPDATE -------
estudiantes[legajo] = [dni, nombre, notas]
estudiantes[legajo][0] = dni
estudiantes[legajo][1] = nombre
estudiantes[legajo][2] = notas
estudiantes[legajo][2][materia] = nota

------- DELETE -------
estudiantes.pop(legajo)
estudiantes[legajo][2].pop(materia)

================ CRUD MATERIAS ================

------- CREATE -------
materias.add(nombre)

------- READ -------
materias

------- UPDATE ------- (peligroso, habria que actualizar a todos los estudiantes que tengan la materia para cambiarle el nombre)
materias.pop(nombre_antiguo)
materias.add(nombre_nuevo)

------- DELETE ------- (peligroso, habria que eliminar la materia de todos los estudiantes)
materias.pop(nombre)
'''

def principal(estudiantes, materias):

	opcion = input('Ingrese la opcion: ')
	opcion = int(opcion)

def agregar_estudiante(estudiantes, materias):

	legajo = input('Ingrese el legajo del estudiante: ')
	legajo = int(legajo)
	dni = input('Ingrese el dni del estudiante: ')
	dni = int(dni)
	nombre = input('Ingrese el nombre del estudiante: ')

	notas = {}

	for materia in materias:

		opcion = input(f'El alumno tiene la materia {materia}? (deje vacio si no la cursa, ingrese la nota si lo hace) ')
		opcion = opcion.strip().lower()

		if opcion.isdigit():
			notas[materia] = int(opcion)

		elif opcion == '':
			pass

		else:
			print('Opcion invalida')

	estudiantes[legajo] = [dni, nombre, notas]

	print('Estudiante agregado exitosamente')

def eliminar_estudiante(estudiantes):

	legajo = input('Ingrese el legajo del estudiante que desea eliminar: ')
	legajo = int(legajo)

	estudiantes.pop(legajo)

	print('Estudiante eliminado exitosamente')

def mostrar_alumno(estudiantes):

	legajo = input('Que estudiante quiere ver? (ingrese legajo) ')
	legajo = legajo.strip()

	if legajo.isdigit():

		legajo = int(legajo)

		if legajo in estudiantes:

			dni, nombre, notas = estudiantes[legajo]

			print('Legajo:', legajo)
			print('DNI:', dni)
			print('Nombre:', nombre)

			print('Materias')
			for materia, nota in notas.items():
				print(' ' * 4 + materia + ': ' + str(nota))

		else:
			print('El estudiante no existe')
		 
	else:
		print('Legajo invalido')


def agregar_materia(materias):

	nombre = input('Ingrese el nombre de la materia que desea agregar: ')

	materias.add(nombre)

	print('Materia agregada exitosamente')


def mostrar_materias(materias):

	print('Materias disponibles:')

	for materia in materias:
		print('' * 4 + materia)


