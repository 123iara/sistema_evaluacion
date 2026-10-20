#Aca se importa la logica desde los modulos CRUD y el Login
#responsabilidad del ingreso y salida de datos por consola.

from login_general.login import verificar_credenciales
from modulos_.alumnos_CRUD import crear_estudiante, obtener_todos_estudiantes, buscar_estudiante_por_dni, modificar_datos_estudiante, eliminar_estudiante
from modulos_.materias_CRUD import crear_materia, listar_materias, modificar_materia, eliminar_materia, agregar_alumno_materia, obtener_alumnos_materia
from modulos_.notas_CRUD import agregar_nota, obtener_notas, modificar_nota, eliminar_nota
from modulos_.matrices_busquedas import crear_matriz_notas, buscar_notas_estudiante
from modulos_.estadisticas import estadisticas_materia


# LOGIN

def login():
    acceso = False
    intentos = 3

    while intentos > 0 and acceso == False:
        print("\033[4;35m---------- LOGIN ----------\033[0m")
        usuario = input("Usuario: ")
        contrasena = input("Contrasena: ")

        if verificar_credenciales(usuario, contrasena):
            acceso = True
            print("\033[32mIngreso correcto al sistema.\033[0m")
        else:
            intentos = intentos - 1
            print("\033[31mUsuario o contrasena incorrectos.\033[0m")
            print("\033[33mIntentos restantes:\033[0m", intentos)

    return acceso

#MENU PRINCIPAL   

def menu_principal():
      print("\033[1;33;44m----- MENU PRINCIPAL -----\033[0m")
      print("1. Registrar estudiante")
      print("2. Lista estudiantes")
      print("3. Buscar estudiante")
      print("4. Modificar estudiante")
      print("5. Eliminar estudiante") # Agregado por corrección
      print("6. Gestion de Materias")
      print("7. Mostrar matriz de calificaciones")
      print("8. Buscar materias y notas de un estudiante")
      print("9. Estadisticas academicas")
      print("10. Salir")
def mostrar_menu_materias():
    print("Ingresando a Materias...")
    print("----- MATERIAS -----")
    print("1. Crear Materia")
    print("2. Ver Materias")
    print("3. Renombrar Materia")
    print("4. Eliminar Materia")
    print("5. Menu de Cursada y Notas") # Para entrar a la gestión de alumnos
    print("6. Volver al menu principal")

def mostrar_submenu_materia(nombre_materia):
    print("-----", nombre_materia, "-----")
    print("1. Lista Alumnos")
    print("2. Ver Notas")
    print("3. Agregar Alumno")
    print("4. Agregar Nota") 
    print("5. Modificar Nota")
    print("6. Eliminar Nota")
    print("7. Volver")


#DATOS (Registro)

def registrar_estudiante():
    print("\033[34m------- REGISTRO DE ESTUDIANTE -------\033[0m")
    dni = input("Ingrese el DNI del estudiante: ")

    #SI EL DNI NO ESTÁ REGISTRADO, PEDIMOS LOS DATOS DEL ESTUDIANTE PARA REGISTRARLO
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")

    exito, msj = crear_estudiante(dni, nombre, apellido)
    if exito:
        print("\033[32m" + msj + "\033[0m")
        print("Nombre:", nombre)
        print("Apellido:", apellido)
    else:
        print(msj)


#ENCONTRAR ESTUDIANTE

def listar_estudiantes():
    print("\033[34m------- LISTA DE ESTUDIANTES -------\033[0m")
    estudiantes = obtener_todos_estudiantes()
    if not estudiantes:
         print("No hay estudiantes registrados.")
    else:
        for dni, estudiante in estudiantes.items():
            print("Legajo:", estudiante["legajo"], "| DNI:", dni, "| Nombre:", estudiante["nombre"], estudiante["apellido"])


def mostrar_matriz_notas():
    print("----- MATRIZ DE CALIFICACIONES -----")

    matriz = crear_matriz_notas()

    if len(matriz) == 0:
        print("No hay calificaciones registradas.")
    else:
        for fila in matriz:
            print(fila)


def mostrar_busqueda_notas():
    print("----- BUSQUEDA DE NOTAS POR ESTUDIANTE -----")

    dni = input("Ingrese el DNI del estudiante: ")
    resultados = buscar_notas_estudiante(dni)

    if len(resultados) == 0:
        print("No se encontraron materias para ese estudiante.")
    else:
        for resultado in resultados:
            print("Materia:", resultado[0])
            print("Notas:", resultado[1])
            print("--------------------")



# ESTADISTICAS ACADEMICAS
def mostrar_estadisticas():
    print("----- ESTADISTICAS ACADEMICAS -----")

    materias_disponibles = listar_materias()

    if len(materias_disponibles) == 0:
        print("No hay materias registradas.")
        return

    print("Materias disponibles:", materias_disponibles)

    nombre = input("Ingrese el nombre de la materia: ")
    nombre = nombre.strip().capitalize()

    if nombre not in materias_disponibles:
        print("Materia no encontrada.")
        return

    resultados = estadisticas_materia(nombre)

    if resultados is None:
        print("No hay alumnos con notas registradas.")
    else:
        print("Materia:", nombre)
        print("Promedio general:", round(resultados[0], 2))
        print("Alumnos aprobados:", resultados[1])
        print("Alumnos desaprobados:", resultados[2])
        print(
            "Porcentaje con promedio alto:",
            round(resultados[3], 2), "%"
        )












def buscar_estudiante():
    print("\033[34m------- BUSCAR ESTUDIANTE -------\033[0m")
    dni = input("Ingrese el DNI a buscar: ")
    encontrado, datos = buscar_estudiante_por_dni(dni)
    if encontrado:
        print("Estudiante encontrado:")
        print("Nombre:", datos["nombre"])
        print("Apellido:", datos["apellido"])
        print("Legajo:", datos["legajo"]) 
    else:
        print(datos) # Estudiante no encontrado.


#UPDATE Estudiante:

def modificar_estudiante():
    dni = input("Ingrese el DNI del estudiante a modificar: ")
    encontrado, datos = buscar_estudiante_por_dni(dni)
    
    if encontrado:
         print("Estudiante encontrado:")
         print("Nombre:", datos["nombre"])
         print("Apellido:", datos["apellido"])
         print("Legajo:", datos["legajo"])
 
         #PEDIR NUEVOS DATOS 
         nuevo_nombre = input("Ingrese el nuevo nombre del estudiante: ")
         nuevo_apellido = input("Ingrese el nuevo apellido del estudiante: ")

         exito, msj = modificar_datos_estudiante(dni, nuevo_nombre, nuevo_apellido)
         print(msj)
    else:
         print("Estudiante no encontrado.")

# Agregado para cumplir la corrección
def eliminar_estudiante_menu():
    dni = input("Ingrese el DNI del estudiante a eliminar: ")
    exito, msj = eliminar_estudiante(dni)
    print(msj)


#AGREGAR ALUMNO A MATERIA
def agregar_alumno_materia_menu(materia_seleccionada):
    print("--- AGREGAR ALUMNO ---")
    dni = input("Ingrese el DNI del estudiante: ") #buscamos el DNI del estuidante que queremos agregar
    exito, msj = agregar_alumno_materia(materia_seleccionada, dni)
    print(msj)

#LISTA ALUMNOS POR MATERIA

def listar_alumnos_materia_menu(materia_seleccionada):
    print("----- LISTA DE ALUMNOS -----")
    alumnos = obtener_alumnos_materia(materia_seleccionada)
    if len(alumnos) == 0:
        print("No hay alumnos registrados en esta materia.")
    else:
        for alumno in alumnos:
            print("Legajo:", alumno["legajo"], "| DNI:", alumno["dni"], "| Nombre:", alumno["nombre"], alumno["apellido"])


#NOTAS POR MATERIA

def mostrar_notas_menu(materia_seleccionada):
    print("----- NOTAS -----")
    dni = input("Ingrese DNI del alumno: ")
    encontrado, notas = obtener_notas(materia_seleccionada, dni)
    
    if encontrado:
        if len(notas) == 0:
             print("No hay notas registradas para este alumno.")
        else:
             for i, n in enumerate(notas):
                 print(f"[{i}] - Nota: {n}")
    else:
        print(notas) # Imprime "Alumno no encontrado"

def agregar_nota_menu(materia_seleccionada):
    print("----- AGREGAR NOTA -----")
    dni = input("Ingrese el DNI del alumno: ")
    try:
        nueva_nota = float(input("Ingrese la nueva nota: ")) #float para permitir notas decimales
        exito, msj = agregar_nota(materia_seleccionada, dni, nueva_nota)
        print(msj)
    except ValueError:
        print("Error: Ingrese un valor numerico.")

# MODIFICAR NOTAS

def modificar_nota_menu(materia_seleccionada):
    print("----- MODIFICAR NOTA -----")
    dni = input("Ingrese el DNI del alumno: ")
    try:
        indice = int(input("Ingrese el numero entre corchetes [ ] de la nota a modificar: "))
        nueva_nota = float(input("Ingrese la nueva nota: ")) #float para permitir notas decimales
        exito, msj = modificar_nota(materia_seleccionada, dni, indice, nueva_nota)
        print(msj)
    except ValueError:
        print("Error: Ingrese valores numericos.")

def eliminar_nota_menu(materia_seleccionada):
    print("----- ELIMINAR NOTA -----")
    dni = input("Ingrese el DNI del alumno: ")
    try:
        indice = int(input("Ingrese el numero entre corchetes [ ] de la nota a eliminar: "))
        exito, msj = eliminar_nota(materia_seleccionada, dni, indice)
        print(msj)
    except ValueError:
        print("Error: Ingrese valores numericos.")


#MENUS Y SUBMENUS

def menu_materia(nombre_materia):
    opcion = 0
    while opcion != 7:
        mostrar_submenu_materia(nombre_materia)
        try:
            opcion = int(input("Ingrese una opcion: "))
            
            if opcion == 1:
                listar_alumnos_materia_menu(nombre_materia)
            elif opcion == 2:
                mostrar_notas_menu(nombre_materia) 
            elif opcion == 3:
                agregar_alumno_materia_menu(nombre_materia) 
            elif opcion == 4:
                agregar_nota_menu(nombre_materia)
            elif opcion == 5:
                modificar_nota_menu(nombre_materia)
            elif opcion == 6:
                eliminar_nota_menu(nombre_materia)
            elif opcion == 7:
                print("Volviendo...")
            else:
                print("Ingrese una opcion valida.")
        except ValueError:
             print("Error: Ingrese un numero valido.")


#MENU MATERIAS
def menu_materias():
    opcion = 0
    while opcion != 6:
        mostrar_menu_materias()
        try:
            opcion = int(input("Ingrese una opcion: "))

            if opcion == 1:
                nombre = input("Nombre de la nueva materia: ")
                exito, msj = crear_materia(nombre)
                print(msj)
            elif opcion == 2:
                materias = listar_materias()
                if not materias:
                     print("No hay materias.")
                else:
                     print("Materias: ", materias)
            elif opcion == 3:
                viejo = input("Nombre actual: ")
                nuevo = input("Nuevo nombre: ")
                exito, msj = modificar_materia(viejo, nuevo)
                print(msj)
            elif opcion == 4:
                nombre = input("Nombre a eliminar: ")
                exito, msj = eliminar_materia(nombre)
                print(msj)
            elif opcion == 5:
                materias = listar_materias()
                if not materias:
                    print("Cree una materia primero.")
                else:
                    print("Materias disponibles:", materias)
                    mat_seleccion = input("Escriba el nombre de la materia para ingresar: ").strip().capitalize()
                    if mat_seleccion in materias:
                        menu_materia(mat_seleccion)
                    else:
                        print("Materia no encontrada.")
            elif opcion == 6:
                print("Volviendo al menu principal...")
            else:
                print("Ingrese una opcion valida.")
        except ValueError:
             print("Error: Ingrese un numero valido.")
                

    
#EJECUCION DEL SISTEMA:
def ejecutar_sistema():
    acceso = login()

    if acceso == True:
        print( "Acceso al sistema permitido")

        opcion = 0

        while opcion != 9:
            menu_principal()
            try:
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
                    eliminar_estudiante_menu()
                
                elif opcion == 6:
                     menu_materias()

                elif opcion == 7:
                     mostrar_matriz_notas()

                elif opcion == 8:
                     mostrar_busqueda_notas()

                elif opcion == 9:
                     mostrar_estadisticas()

                elif opcion == 10:
                     print("Saliendo del sistema..")
                
            except ValueError:
                print("Ingrese un numero valido")

    else:
        print ("Se agotaron los intentos.")