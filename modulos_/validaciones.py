"""Validaciones sencillas usadas por las altas y modificaciones."""

import re


PATRON_DNI = re.compile(r"^\d{7,8}$")
PATRON_NOMBRE = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+(?:[ '-][A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+)*$")


def validar_dni(dni):
    return bool(PATRON_DNI.fullmatch(str(dni).strip()))


def validar_nombre(nombre):
    return bool(PATRON_NOMBRE.fullmatch(str(nombre).strip()))


def normalizar_nombre(nombre):
    """Recorta espacios y deja cada palabra con inicial mayúscula."""
    return " ".join(palabra.capitalize() for palabra in str(nombre).strip().split())



# MANEJO DE EXCEPCIONES

def verificar_dni(dni):
    try:
        if not validar_dni(dni):
            raise ValueError("El DNI debe tener 7 u 8 dígitos.")
        return True

    except ValueError as error:
        print("Error:", error)
        return False


def verificar_nombre(nombre):
    try:
        if not validar_nombre(nombre):
            raise ValueError("El nombre ingresado no es válido.")
        return True

    except ValueError as error:
        print("Error:", error)
        return False
