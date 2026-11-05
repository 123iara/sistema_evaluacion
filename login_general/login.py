
# LOGIN CON USUARIOS ALMACENADOS EN TXT

from datos_generales import persistencia

ARCHIVO_USUARIOS = persistencia.ARCHIVO_USUARIOS

ROLES_VALIDOS = {"administrador", "usuario"}


def verificar_credenciales(usuario, contrasena):
    try:
        usuarios = persistencia.leer_lineas(
            ARCHIVO_USUARIOS
        )

        for linea in usuarios:
            partes = linea.split(";")

            if len(partes) == 3:
                nombre, clave, rol = partes

                if nombre == usuario and clave == contrasena:
                    return True

        return False

    except OSError:
        return False


def obtener_rol(usuario):
    try:
        usuarios = persistencia.leer_lineas(
            ARCHIVO_USUARIOS
        )

        for linea in usuarios:
            partes = linea.split(";")

            if len(partes) == 3:
                nombre, clave, rol = partes

                if nombre == usuario and rol in ROLES_VALIDOS:
                    return rol

        return None

    except OSError:
        return None
