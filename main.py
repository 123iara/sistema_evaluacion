import re

USERYCONT = (
    ("admin", "admin123"),
    ("user", "1234"),
    ("user2", "4321")

)

dnis_registrados = set()
alumnos_en_materias = set()

estudiantes = {}

materias = {
    "Matematicas": {
        "alumnos": [],
        "dnis": set()
    },
    "Lengua": {
        "alumnos": [],
        "dnis": set()
    },
    "Ciencias": {
        "alumnos": [],
        "dnis": set()
    },
    "Historia": {
        "alumnos": [],
        "dnis": set()
    },
    "Geografia": {
        "alumnos": [],
        "dnis": set()
    }
}


def login():
    acceso = False
    intentos = 3

    while intentos > 0 and acceso == False:
        print("\033[4;35m---------- LOGIN ----------\033[0m")
        usuario = input("Usuario: ")
        contrasena = input("Contrasena: ")

        if (usuario, contrasena) in USERYCONT:
            acceso = True
            print("\033[32mIngreso correcto al sistema.\033[0m")
        else:
            intentos = intentos - 1
            print("\033[31mUsuario o contrasena incorrectos.\033[0m")
            print("\033[33mIntentos restantes:\033[0m", intentos)

    return acceso


def menu_principal():
      print("\033[1;33;44m----- MENU PRINCIPAL -----\033[0m")
      print("1. Registrar estudiante")
      print("2. Lista estudiantes")
      print("3. Buscar estudiante")
      print("4. Modificar estudiante")
      print("5. Materias")
      print("6. Mostrar estudiantes en todas las materias")
      print("7. Salir")

def mostrar_menu_materias():
    print("Ingresando a Materias...")
    print("----- MATERIAS -----")
    print("1. Matematicas")
    print("2. Lengua")
    print("3. Ciencias")
    print("4. Historia")
    print("5. Geografia")
    print("6. Volver al menu principal")

def mostrar_submenu_materia(nombre_materia):

    print("-----", nombre_materia, "-----")
    print("1. Lista Alumnos")
    print("2. Notas")
    print("3. Agregar Alumno")
    print("4. Modificar Alumno")
    print("5. Modificar Nota")
    print("6. Volver")


def registrar_estudiante():
    print("\033[34m------- REGISTRO DE ESTUDIANTE -------\033[0m")

    dni = input("Ingrese el DNI del estudiante: ")

    if not re.match(r"^\d+$", dni):
        print("\033[31mError: El DNI debe contener solo números.\033[0m")
        return

    if dni in dnis_registrados:
        estudiante = estudiantes[dni]

        print("El estudiante ya está registrado.")
        print("Nombre:", estudiante["nombre"])
        print("Apellido:", estudiante["apellido"])
        print("Legajo:", estudiante["legajo"])
        return

    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")

    legajo = len(estudiantes) + 1   

    nuevo_estudiante = {
        "legajo": legajo,
        "nombre": nombre,
        "apellido": apellido
    }

    estudiantes[dni] = nuevo_estudiante
    dnis_registrados.add(dni)

    print("\033[32mEstudiante registrado con éxito.\033[0m")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Legajo:", legajo)


def listar_estudiantes():
    print("\033[34m------- LISTA DE ESTUDIANTES -------\033[0m")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    for dni, estudiante in estudiantes.items():
        print("Legajo:", estudiante["legajo"], "| DNI:", dni, "| Nombre:", estudiante["nombre"], estudiante["apellido"])

def buscar_estudiante():
    print("\033[34m------- BUSCAR ESTUDIANTE -------\033[0m")
    dni = input("Ingrese el DNI a buscar: ")

    if dni in dnis_registrados:
        estudiante = estudiantes[dni]

        print("Estudiante encontrado:")
        print("Nombre:", estudiante["nombre"])
        print("Apellido:", estudiante["apellido"])
        print("Legajo:", estudiante["legajo"])
    else:
        print("Estudiante no encontrado.")


def modificar_estudiante():
    dni = input("Ingrese el DNI del estudiante a modificar: ")
    if dni in dnis_registrados:
         estudiante = estudiantes[dni]
    
         print("Estudiante encontrado:")
         print("Nombre:", estudiante["nombre"])
         print("Apellido:", estudiante["apellido"])
         print("Legajo:", estudiante["legajo"])
 
         nuevo_nombre = input("Ingrese el nuevo nombre del estudiante: ")
         nuevo_apellido = input("Ingrese el nuevo apellido del estudiante: ")

         estudiante["nombre"] = nuevo_nombre
         estudiante["apellido"] = nuevo_apellido

         print("Datos del estudiante actualizados con éxito.")
         return
    
    print("Estudiante no encontrado.")


def agregar_alumno_materia(materia):

    print("--- AGREGAR ALUMNO ---")

    dni = input("Ingrese el DNI del estudiante: ")

    estudiante_encontrado = False

    if dni in dnis_registrados:

            estudiante_encontrado = True
            estudiante = estudiantes[dni]

            if dni in materia["dnis"]:
                print("El estudiante ya esta agregado a esta materia.")
                return

            nuevo_alumno = {
                "dni": dni,
                "legajo": estudiante["legajo"],
                "nombre": estudiante["nombre"],
                "apellido": estudiante["apellido"],
                "nota": 0
            }

            materia["alumnos"].append(nuevo_alumno)
            materia["dnis"].add(dni)
            alumnos_en_materias.add(dni)

            print("Alumno agregado correctamente a la materia.")
            print("Nombre:", estudiante["nombre"])
            print("Apellido:", estudiante["apellido"])
            print("Legajo:", estudiante["legajo"])

            return

    if estudiante_encontrado == False:
        print("El estudiante no esta registrado en el sistema.")
        print("Primero debe registrarlo desde el menu principal.")


def listar_alumnos_materia(lista_materia):

    print("----- LISTA DE ALUMNOS -----")

    if len(lista_materia) == 0:
        print("No hay alumnos registrados en esta materia.")

    else:

        for alumno in lista_materia:

            print(
                "Legajo:", alumno["legajo"],
                "| DNI:", alumno["dni"],
                "| Nombre:", alumno["nombre"],
                alumno["apellido"]
            )


def mostrar_notas(lista_materia):

    print("----- NOTAS -----")

    if len(lista_materia) == 0:
        print("No hay alumnos registrados en esta materia.")

    else:
        for alumno in lista_materia:
            print(
                "Legajo:", alumno["legajo"],
                "| Alumno:", alumno["nombre"],
                alumno["apellido"],
                "| Nota:", alumno["nota"]
            )


def modificar_alumno_materia(lista_materia):

    print("----- MODIFICAR ALUMNO -----")

    dni = input("Ingrese el DNI del alumno: ")

    for alumno in lista_materia:

        if alumno["dni"] == dni:

            print("Alumno encontrado:")
            print("Nombre:", alumno["nombre"])
            print("Apellido:", alumno["apellido"])

            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nuevo_apellido = input("Ingrese el nuevo apellido: ")

            alumno["nombre"] = nuevo_nombre
            alumno["apellido"] = nuevo_apellido

            print("Alumno modificado correctamente.")

            return
        
    print("Alumno no encontrado en esta materia.")


def modificar_nota(lista_materia):

    print("----- MODIFICAR NOTA -----")

    dni = input("Ingrese el DNI del alumno: ")

    for alumno in lista_materia:

        if alumno["dni"] == dni:

            print("Alumno:", alumno["nombre"], alumno["apellido"])
            print("Nota actual:", alumno["nota"])

            nueva_nota = float(input("Ingrese la nueva nota: "))

            while nueva_nota < 0 or nueva_nota > 10:
                print("La nota debe estar entre 0 y 10.")
                nueva_nota = float(input("Ingrese nuevamente la nota: "))

            alumno["nota"] = nueva_nota

            print("Nota modificada correctamente.")

            return

    print("Alumno no encontrado en esta materia.")


def estudiantes_en_todas_las_materias():
    print("----- ESTUDIANTES EN TODAS LAS MATERIAS -----")

    dnis_comunes = (
        materias["Matematicas"]["dnis"] &
        materias["Lengua"]["dnis"] &
        materias["Ciencias"]["dnis"] &
        materias["Historia"]["dnis"] &
        materias["Geografia"]["dnis"]
    )

    if len(dnis_comunes) == 0:
        print("No hay estudiantes inscritos en todas las materias simultáneamente.")
    else:
        for dni in dnis_comunes:
            estudiante = estudiantes[dni]
            print("DNI:", dni, "| Nombre:", estudiante["nombre"], estudiante["apellido"])


def menu_materia(nombre_materia, materia):

    opcion = 0

    while opcion != 6:

        mostrar_submenu_materia(nombre_materia)

        opcion = int(input("Ingrese una opcion: "))
        
        if opcion == 1:
            listar_alumnos_materia(materia["alumnos"])

        elif opcion == 2:
            mostrar_notas(materia["alumnos"])

        elif opcion == 3:
            agregar_alumno_materia(materia)

        elif opcion == 4:
            modificar_alumno_materia(materia["alumnos"])

        elif opcion == 5:
            modificar_nota(materia["alumnos"])

        elif opcion == 6:
            print("Volviendo al menu de materias...")

        else:
            print("Ingrese una opcion valida.")


def menu_materias():

    opcion = 0

    while opcion != 6:

        mostrar_menu_materias()

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            menu_materia("MATEMATICAS", materias ["Matematicas"])

        elif opcion == 2:
            menu_materia("LENGUA", materias ["Lengua"])

        elif opcion == 3:
            menu_materia("CIENCIAS", materias ["Ciencias"])

        elif opcion == 4:
            menu_materia("HISTORIA", materias ["Historia"])

        elif opcion == 5:
            menu_materia("GEOGRAFIA", materias ["Geografia"])

        elif opcion == 6:
            print("Volviendo al menu principal...")

        else:
            print("Ingrese una opcion valida.")


def ejecutar_sistema():
    acceso = login()

    if acceso == True:
        print( "Acceso al sistema permitido")

        opcion = 0

        while opcion != 7:
            menu_principal()
            opcion = int(input("Ingrese una opcion:"))

            if opcion == 1:
                registrar_estudiante()
            elif opcion == 2:
                listar_estudiantes()
            elif opcion == 3:
                buscar_estudiante()
            elif opcion == 4:
                modificar_estudiante()
            elif opcion == 5:
                menu_materias()  
            elif opcion == 6:
                estudiantes_en_todas_las_materias()
            elif opcion == 7:
                print("Saliendo del sistema..")

    else:
        print ("Ingrese un numero valido")


ejecutar_sistema()