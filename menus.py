#Aca se importa la logica desde los modulos CRUD y el Login
#responsabilidad del ingreso y salida de datos por consola.

from login_general.login import verificar_credenciales
from modulos_.alumnos_CRUD import crear_estudiante, obtener_todos_estudiantes, buscar_estudiante_por_dni, modificar_datos_estudiante
from modulos_.materias_CRUD import agregar_alumno_materia, obtener_alumnos_materia
from modulos_.notas_CRUD import actualizar_nota, obtener_notas

def login():
    intentos = 3
    while intentos > 0:
        print("\033[4;35m---------- LOGIN ----------\033[0m")
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")

        if verificar_credenciales(usuario, contrasena):
            print("\033[32mIngreso correcto al sistema.\033[0m")
            return True
        else:
            intentos -= 1
            print("\033[31mUsuario o contraseña incorrectos.\033[0m")
            print(f"\033[33mIntentos restantes:\033[0m {intentos}")
    return False

def menu_estudiantes():
    print("\033[1;33;44m----- MENU ESTUDIANTES -----\033[0m")
    print("1. Registrar estudiante")
    print("2. Lista estudiantes")
    print("3. Buscar estudiante")
    print("4. Modificar estudiante")
    print("5. Volver")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        dni = input("Ingrese el DNI: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        exito, msj = crear_estudiante(dni, nombre, apellido)
        print(msj)
        
    elif opcion == "2":
        estudiantes = obtener_todos_estudiantes()
        if not estudiantes:
            print("No hay estudiantes registrados.")
        else:
            for dni, est in estudiantes.items():
                print(f"Legajo: {est['legajo']} | DNI: {dni} | {est['nombre']} {est['apellido']}")
                
    elif opcion == "3":
        dni = input("Ingrese el DNI a buscar: ")
        encontrado, datos = buscar_estudiante_por_dni(dni)
        if encontrado:
            print(f"Estudiante: {datos['nombre']} {datos['apellido']} (Legajo {datos['legajo']})")
        else:
            print(datos) # Muestra el mensaje de error
            
    elif opcion == "4":
        dni = input("Ingrese el DNI a modificar: ")
        encontrado, datos = buscar_estudiante_por_dni(dni)
        if encontrado:
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_apellido = input("Nuevo apellido: ")
            exito, msj = modificar_datos_estudiante(dni, nuevo_nombre, nuevo_apellido)
            print(msj)
        else:
            print("Estudiante no encontrado.")
            
def menu_materia_individual(nombre_materia):
    opcion = 0
    while str(opcion) != "5":
        print(f"\033[1;36m----- {nombre_materia} -----\033[0m")
        print("1. Agregar Alumno a la materia")
        print("2. Lista Alumnos en la materia")
        print("3. Modificar Nota")
        print("4. Ver Notas")
        print("5. Volver")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            dni = input("DNI del estudiante a agregar: ")
            exito, msj = agregar_alumno_materia(nombre_materia, dni)
            print(msj)
            
        elif opcion == "2":
            alumnos = obtener_alumnos_materia(nombre_materia)
            if not alumnos:
                print("No hay alumnos en esta materia.")
            else:
                for al in alumnos:
                    print(f"DNI: {al['dni']} | {al['nombre']} {al['apellido']}")
                    
        elif opcion == "3":
            dni = input("DNI del estudiante: ")
            try:
                nota = float(input("Nueva nota (0-10): "))
                exito, msj = actualizar_nota(nombre_materia, dni, nota)
                print(msj)
            except ValueError:
                print("Por favor, ingrese un número válido.")
                
        elif opcion == "4":
            alumnos = obtener_notas(nombre_materia)
            if not alumnos:
                print("No hay alumnos calificados.")
            else:
                for al in alumnos:
                    print(f"Alumno: {al['nombre']} {al['apellido']} | Nota: {al['nota']}")

def ejecutar_sistema():
    if login():
        opcion = "0"
        while opcion != "3":
            print("\033[1;33;44m----- MENU PRINCIPAL -----\033[0m")
            print("1. Gestión de Estudiantes Global")
            print("2. Gestión de Materias y Notas")
            print("3. Salir")
            opcion = input("Opción: ")

            if opcion == "1":
                menu_estudiantes()
            elif opcion == "2":
                print("1. Matematicas | 2. Lengua | 3. Ciencias | 4. Historia | 5. Geografia")
                mat_op = input("Seleccione número de materia: ")
                materias_map = {"1": "Matematicas", "2": "Lengua", "3": "Ciencias", "4": "Historia", "5": "Geografia"}
                if mat_op in materias_map:
                    menu_materia_individual(materias_map[mat_op])
                else:
                    print("Opción inválida.")
            elif opcion == "3":
                print("Saliendo del sistema...")

if __name__ == "__main__":
    ejecutar_sistema()