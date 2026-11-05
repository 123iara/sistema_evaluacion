
import json
from unittest.mock import patch, mock_open
from datos_generales.persistencia import cargar_datos

try:
    with patch(
        "datos_generales.persistencia.ARCHIVO_ESTUDIANTES"
    ) as estudiantes, patch(
        "datos_generales.persistencia.ARCHIVO_MATERIAS"
    ) as materias:

        estudiantes.exists.return_value = False
        materias.exists.return_value = True
        materias.open = mock_open(
            read_data="{datos incorrectos}"
        )

        cargar_datos()

except json.JSONDecodeError:
    print("Excepcion JSON capturada correctamente")
