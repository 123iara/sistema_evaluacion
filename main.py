#DATOS

USUARIO = "user"
CONTRASENA = "4321"



estudiantes = []

matematicas = []
lengua = []
ciencias = []
historia = []
geografia = []



# LOGIN

def login():
    acceso = False
    intentos = 3

    while intentos > 0 and acceso == False:
        print(" ----- LOGIN ----- ")
        usuario = input("Usuario: ")
        contrasena = input("Contrasena: ")

        if usuario == USUARIO and contrasena == CONTRASENA:
            acceso = True
            print("Ingreso correcto al sistema.")
        else:
            intentos = intentos - 1
            print("\033[31mUsuario o contrasena incorrectos.\033[0m")
            print("\033[33mIntentos restantes:\033[0m", intentos)

    return acceso


    
 #MENU PRINCIPAL   
 
def menu_principal():
      print("----- MENU PRINCIPAL -----")
      print("1. Registrar estudiante")
      print("2. Lista estudiantes")
      print("3. Buscar estudiante")
      print("4. Modificar estudiante")
      print("5. Materias")
      print("6. Salir")

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
  
#DATOS

def registrar_estudiante():
    print("---- REGISTRO DE ESTUDIANTE ----")

    dni = input("Ingrese el DNI del estudiante: ")

#VERIFICAR SI EL DNI YA ESTÁ REGISTRADO

    for estudiante in estudiantes:
        if estudiante["dni"] == dni: 
            print("El estudiante ya está registrado.")
            print("Nombre:", estudiante["nombre"])
            print("Apellido:", estudiante["apellido"])
            print("Legajo:", estudiante["legajo"])
            return

#SI EL DNI NO ESTÁ REGISTRADO, PEDIMOS LOS DATOS DEL ESTUDIANTE PARA REGISTRARLO
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")

#ASIGNAR UN NUEVO LEGAJO
    legajo = len(estudiantes) + 1

    #CREAR AL ESTUDIANTE
    nuevo_estudiante = {
        "dni": dni,
        "legajo": legajo,
        "nombre": nombre,
        "apellido": apellido
    }

    #AGREGARLO A LA LISTA
    estudiantes.append(nuevo_estudiante)

    print("Estudiante registrado con éxito.")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Legajo:", legajo)


#ENCONTRAR ESTUDIANTE

def listar_estudiantes():
    print("-- LISTA DE ESTUDIANTES --")
    for estudiante in estudiantes:
        print("Legajo:", estudiante["legajo"], "| DNI:", estudiante["dni"], "| Nombre:", estudiante["nombre"], estudiante["apellido"])

def buscar_estudiante():
    print("-- BUSCAR ESTUDIANTE --")
    dni = input("Ingrese el DNI a buscar: ")
    for estudiante in estudiantes:
        if estudiante["dni"] == dni:
            print("Estudiante encontrado:")
            print("Nombre:", estudiante["nombre"])
            print("Apellido:", estudiante["apellido"])
            print("Legajo:", estudiante["legajo"])
            return
    print("Estudiante no encontrado.")


#UPDATE Estudiante:

def modificar_estudiante():
    dni = input("Ingrese el DNI del estudiante a modificar: ")

    for estudiante in estudiantes:
        if estudiante["dni"] == dni:
            print("Estudiante encontrado:")
            print("Nombre:", estudiante["nombre"])
            print("Apellido:", estudiante["apellido"])
            print("Legajo:", estudiante["legajo"])

            #PEDIR NUEVOS DATOS 
            nuevo_nombre = input("Ingrese el nuevo nombre del estudiante: ")
            nuevo_apellido = input("Ingrese el nuevo apellido del estudiante: ")

            #ACTUALIZAR LOS DATOS DEL ESTUDIANTE
            estudiante["nombre"] = nuevo_nombre
            estudiante["apellido"] = nuevo_apellido

            print("Datos del estudiante actualizados con éxito.")
            return
    else:
         print("Estudiante no encontrado.")



#AGREGAR ALUMNO A MATERIA

def agregar_alumno_materia(lista_materia):

    print("----- AGREGAR ALUMNO -----")

    dni = input("Ingrese el DNI del estudiante: ")

    #BUSCAMOS SI EL ESTUDIANTE EXISTE
    

    estudiante_encontrado = False

    for estudiante in estudiantes:

        if estudiante["dni"] == dni:

            estudiante_encontrado = True

            # VERIFICAR SI YA ESTA EN LA MATERIA

            for alumno in lista_materia:
                if alumno["dni"] == dni:
                    print("El estudiante ya esta agregado a esta materia.")
                    return

            # AGREGAR EL ESTUDIANTE A LA MATERIA

            nuevo_alumno = {
                "dni": estudiante["dni"],
                "legajo": estudiante["legajo"],
                "nombre": estudiante["nombre"],
                "apellido": estudiante["apellido"],
                "nota": 0
            }

            lista_materia.append(nuevo_alumno)

            print("Alumno agregado correctamente a la materia.")
            print("Nombre:", estudiante["nombre"])
            print("Apellido:", estudiante["apellido"])
            print("Legajo:", estudiante["legajo"])

            return

    if estudiante_encontrado == False:
        print("El estudiante no esta registrado en el sistema.")
        print("Primero debe registrarlo desde el menu principal.")


#LISTA ALUMNOS POR MATERIA

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


#NOTAS POR MATERIA

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


# MODIFICAR ALUMNO

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


# MODIFICAR NOTAS

def modificar_nota(lista_materia):

    print("----- MODIFICAR NOTA -----")

    dni = input("Ingrese el DNI del alumno: ")

    for alumno in lista_materia:

        if alumno["dni"] == dni:

            print("Alumno:", alumno["nombre"], alumno["apellido"])
            print("Nota actual:", alumno["nota"])

            nueva_nota = int(input("Ingrese la nueva nota: "))

            while nueva_nota < 0 or nueva_nota > 10:
                print("La nota debe estar entre 0 y 10.")
                nueva_nota = int(input("Ingrese nuevamente la nota: "))

            alumno["nota"] = nueva_nota

            print("Nota modificada correctamente.")

            return

    print("Alumno no encontrado en esta materia.")


#MENUS Y SUBMENUS

def menu_materia(nombre_materia, lista_materia):

    opcion = 0

    while opcion != 6:

        mostrar_submenu_materia(nombre_materia)

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            listar_alumnos_materia(lista_materia)

        elif opcion == 2:
            mostrar_notas(lista_materia)

        elif opcion == 3:
            agregar_alumno_materia(lista_materia)

        elif opcion == 4:
            modificar_alumno_materia(lista_materia)

        elif opcion == 5:
            modificar_nota(lista_materia)

        elif opcion == 6:
            print("Volviendo al menu de materias...")

        else:
            print("Ingrese una opcion valida.")



def materias():

    opcion = 0

    while opcion != 6:

        mostrar_menu_materias()

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            menu_materia("MATEMATICAS", matematicas)

        elif opcion == 2:
            menu_materia("LENGUA", lengua)

        elif opcion == 3:
            menu_materia("CIENCIAS", ciencias)

        elif opcion == 4:
            menu_materia("HISTORIA", historia)

        elif opcion == 5:
            menu_materia("GEOGRAFIA", geografia)

        elif opcion == 6:
            print("Volviendo al menu principal...")

        else:
            print("Ingrese una opcion valida.")
            
        
    


#Ejecucion del sistema:

def ejecutar_sistema():
    acceso = login()

    if acceso == True:
        print( "Acceso al sistema permitido")

        opcion = 0

        while opcion != 6:
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
                materias()  
            elif opcion == 6:
                print("Saliendo del sistema..")

    else:
        print ("Ingrese un numero valido")
            


#ejecucion del sistema
ejecutar_sistema()