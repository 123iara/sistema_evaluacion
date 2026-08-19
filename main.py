#DATOS

USUARIO = "user"
CONTRASENA = "4321"

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
            print("Usuario o contrasena incorrectos.")
            print("Intentos restantes:", intentos)

    return acceso


    
 #MENU PRINCIPAL   
 
def menu_principal():
      print("----- MENU PRINCIPAL -----")
      print("1. Registrar estudiante")
      print("2. Lista estudiantes")
      print("3. Buscar estudiante")
      print("4. Modificar estudiante")
      print("5. Salir")

  
#DATOS
estudiantes = []

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


# --- ENCONTRAR ESTUDIANTE ---

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


#Ejecucion del sistema:
def ejecutar_sistema():
    acceso = login()

    if acceso == True:
        print( "Acceso al sistema permitido")

        opcion = 0

        while opcion != 5:
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
                print("Saliendo del sistema...")

    else:
        print ("Ingrese un numero valido")
            

#
ejecutar_sistema()