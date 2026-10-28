
from datos_generales.memoria import materias
from datos_generales.memoria import estudiantes #Lo usamos para REFERENCIAR a los alumnos y sus datos 


def crear_matriz_notas():
    matriz = []

    #Encabezado de la matriz para Impresion Prolija
    encabezado = ["Materia".ljust(15), "DNI".ljust(10), "Apellido".ljust(15), "Nombre".ljust(15), "Notas"]
    matriz.append(encabezado)

    for nombre_materia in materias:
        alumnos = materias[nombre_materia]["alumnos"]

        for alumno in alumnos:
            dni = alumno["dni"]

            # No copiamos los datos, los referenciamos usando el DNI
            if dni in estudiantes:
                datos_est = estudiantes[dni]
                apellido_est = datos_est["apellido"]
                nombre_est = datos_est["nombre"]
            else:
                apellido_est = "N/A"
                nombre_est = "N/A"

            # Fila de la matriz formateada
            fila = [
                nombre_materia.ljust(15), 
                str(dni).ljust(10), 
                apellido_est.ljust(15), 
                nombre_est.ljust(15)
            ]

            # Convertimos la lista de notas a string para que no rompa la tabla al imprimir
            fila.append(str(alumno["notas"]))

            matriz.append(fila)

    return matriz


def buscar_notas_estudiante(dni):
    resultados = []

    # Buscamos el nombre del alumno por referencia para mostrarlo
    if dni in estudiantes:
        datos_est = estudiantes[dni]
        resultados.append(f"Estudiante: {datos_est['nombre']} {datos_est['apellido']}")
    else:
        resultados.append(f"DNI {dni} no encontrado en el sistema principal.")

    resultados.append("----------------------------------")

    for nombre_materia in materias:
        alumnos = materias[nombre_materia]["alumnos"]

        for alumno in alumnos:
            if alumno["dni"] == dni:
                # Agregamos la información de la cursada a la lista de resultados
                resultados.append([
                    nombre_materia,
                    alumno["notas"]
                ])

    return resultados