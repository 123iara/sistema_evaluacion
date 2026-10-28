#Logica de validacion de usuarios y contraseñas
# login_general/login.py
from datos_generales.memoria import USERYCONT

def verificar_credenciales(usuario, contrasena):
    #Devuelve True si el usuario y contraseña coinciden con la memoria
    if (usuario, contrasena) in USERYCONT:
        return True
    return 
    
    