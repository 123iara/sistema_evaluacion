#Crear, Leer, Actualizar y Borrar notas de alumnos en materias

import os

ARCHIVO_INSCRIPCIONES = "inscripciones.txt"
ARCHIVO_TEMP = "temp_inscripciones.txt"

#NOTAS POR MATERIA
def agregar_nota(nombre_materia, dni, nota):
    if nota < 0 or nota > 10:
        return False, "La nota debe estar entre 0 y 10."

    nombre_materia = nombre_materia.strip().title()
    dni_str = str(dni)
    encontrado = False

    try:
        with open(ARCHIVO_INSCRIPCIONES, 'r', encoding='UTF-8') as orig, \
             open(ARCHIVO_TEMP, 'w', encoding='UTF-8') as temp:
            for linea in orig:
                datos = linea.strip().split(';')
                if len(datos) >= 2 and datos[0] == nombre_materia and datos[1] == dni_str:
                    encontrado = True
                    notas_actuales = datos[2] if len(datos) > 2 else ""
                    # Agrega la coma si ya hay notas previas
                    nuevas_notas = f"{notas_actuales},{nota}" if notas_actuales else f"{nota}"
                    temp.write(f"{nombre_materia};{dni_str};{nuevas_notas}\n")
                else:
                    temp.write(linea)
        os.replace(ARCHIVO_TEMP, ARCHIVO_INSCRIPCIONES)
        
        if encontrado:
            return True, "Nota agregada correctamente."
        return False, "Alumno no encontrado en esta materia."
    except Exception as e:
        return False, f"Error al guardar la nota: {e}"


def obtener_notas(nombre_materia, dni):
    nombre_materia = nombre_materia.strip().title()
    dni_str = str(dni)
    
    try:
        with open(ARCHIVO_INSCRIPCIONES, 'r', encoding='UTF-8') as archivo:
            for linea in archivo:
                datos = linea.strip().split(';')
                if len(datos) >= 2 and datos[0] == nombre_materia and datos[1] == dni_str:
                    notas_str = datos[2] if len(datos) > 2 else ""
                    notas = [float(n) for n in notas_str.split(',')] if notas_str else []
                    return True, notas
        return False, "Alumno no encontrado en esta materia."
    except FileNotFoundError:
        return False, "Archivo de inscripciones no encontrado."
    except Exception as e:
        return False, f"Error al leer las notas: {e}"

# MODIFICAR NOTAS
def modificar_nota(nombre_materia, dni, indice, nueva_nota):
    if nueva_nota < 0 or nueva_nota > 10:
        return False, "La nota debe estar entre 0 y 10."

    nombre_materia = nombre_materia.strip().title()
    dni_str = str(dni)
    encontrado = False
    nota_modificada = False
    
    try:
        with open(ARCHIVO_INSCRIPCIONES, 'r', encoding='UTF-8') as orig, \
             open(ARCHIVO_TEMP, 'w', encoding='UTF-8') as temp:
            for linea in orig:
                datos = linea.strip().split(';')
                if len(datos) >= 2 and datos[0] == nombre_materia and datos[1] == dni_str:
                    encontrado = True
                    notas_str = datos[2] if len(datos) > 2 else ""
                    notas = notas_str.split(',') if notas_str else []
                    
                    if 0 <= indice < len(notas):
                        notas[indice] = str(float(nueva_nota)) # Sobrescribe en la lista temporal
                        nota_modificada = True
                        nuevas_notas_str = ",".join(notas) # Vuelve a unir con comas
                        temp.write(f"{nombre_materia};{dni_str};{nuevas_notas_str}\n")
                    else:
                        temp.write(linea) # Si el índice falla, reescribe intacto
                else:
                    temp.write(linea)
        os.replace(ARCHIVO_TEMP, ARCHIVO_INSCRIPCIONES)
        
        if not encontrado:
            return False, "Alumno no encontrado en esta materia."
        if not nota_modificada:
            return False, "Índice de nota incorrecto."
        return True, "Nota modificada."
    except Exception as e:
        return False, f"Error al modificar la nota: {e}"

def eliminar_nota(nombre_materia, dni, indice):
    nombre_materia = nombre_materia.strip().title()
    dni_str = str(dni)
    encontrado = False
    nota_eliminada = False
    
    try:
        with open(ARCHIVO_INSCRIPCIONES, 'r', encoding='UTF-8') as orig, \
             open(ARCHIVO_TEMP, 'w', encoding='UTF-8') as temp:
            for linea in orig:
                datos = linea.strip().split(';')
                if len(datos) >= 2 and datos[0] == nombre_materia and datos[1] == dni_str:
                    encontrado = True
                    notas_str = datos[2] if len(datos) > 2 else ""
                    notas = notas_str.split(',') if notas_str else []
                    
                    if 0 <= indice < len(notas):
                        del notas[indice] # Elimina física de la lista
                        nota_eliminada = True
                        nuevas_notas_str = ",".join(notas) # Vuelve a unir el resto con comas
                        temp.write(f"{nombre_materia};{dni_str};{nuevas_notas_str}\n")
                    else:
                        temp.write(linea)
                else:
                    temp.write(linea)
        os.replace(ARCHIVO_TEMP, ARCHIVO_INSCRIPCIONES)
        
        if not encontrado:
            return False, "Alumno no encontrado en esta materia."
        if not nota_eliminada:
            return False, "Índice de nota incorrecto."
        return True, "Nota eliminada."
    except Exception as e:
        return False, f"Error al eliminar la nota: {e}"