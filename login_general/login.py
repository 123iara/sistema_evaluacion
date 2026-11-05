#Logica de validacion de usuarios y contraseñas
# login_general/login.py
from datos_generales.memoria import USERYCONT, ROLES

ROLES_VALIDOS = {"administrador", "usuario"}

def verificar_credenciales(usuario, contrasena):
    #Devuelve True si el usuario y contraseña coinciden con la memoria
    if (usuario, contrasena) in USERYCONT:
        return True
    return False


def obtener_rol(usuario):
    """Devuelve el rol de una cuenta o None si no está registrada."""
    rol = ROLES.get(usuario)
    return rol if rol in ROLES_VALIDOS else None
