import unittest

from modulos_.validaciones import validar_dni, validar_nombre, normalizar_nombre
from modulos_.alumnos_CRUD import crear_estudiante, eliminar_estudiante
from datos_generales.memoria import estudiantes


class PruebasValidacionesYAlumnos(unittest.TestCase):
    def tearDown(self):
        estudiantes.clear()

    def test_patrones_de_dni_y_nombre(self):
        self.assertTrue(validar_dni("12345678"))
        self.assertFalse(validar_dni("12A"))
        self.assertTrue(validar_nombre("Ana María"))
        self.assertFalse(validar_nombre("Ana123"))

    def test_normalizar_nombre_recorta_y_usa_titulo(self):
        self.assertEqual(normalizar_nombre("  ANA   MARIA "), "Ana Maria")

    def test_alta_y_baja_de_estudiante(self):
        creado, _ = crear_estudiante("12345678", "ana", "perez")
        self.assertTrue(creado)
        eliminado, _ = eliminar_estudiante("12345678")
        self.assertTrue(eliminado)
        self.assertNotIn("12345678", estudiantes)


if __name__ == "__main__":
    unittest.main()
