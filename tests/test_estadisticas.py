import unittest

from datos_generales.memoria import materias
from modulos_.estadisticas import (
    calcular_promedio,
    estadisticas_generales,
    estadisticas_materia,
    maximo_recursivo,
    suma_recursiva,
)


class PruebasEstadisticas(unittest.TestCase):
    def setUp(self):
        materias.clear()

    def tearDown(self):
        materias.clear()

    def test_promedio_de_notas_y_lista_vacia(self):
        self.assertEqual(calcular_promedio([6, 8]), 7)
        self.assertIsNone(calcular_promedio([]))

    def test_estadisticas_materia_incluyen_extremos_y_conteos(self):
        materias["Historia"] = {"alumnos": [
            {"dni": "10000000", "notas": [2, 6]},
            {"dni": "10000001", "notas": [8, 10]},
        ]}
        resumen = estadisticas_materia("Historia")
        self.assertEqual(resumen["promedio_general"], 6.5)
        self.assertEqual(resumen["aprobados"], 2)
        self.assertEqual(resumen["desaprobados"], 0)
        self.assertEqual(resumen["cantidad_notas"], 4)
        self.assertEqual(resumen["nota_minima"], 2)
        self.assertEqual(resumen["nota_maxima"], 10)

    def test_estadisticas_sin_notas_devuelven_none(self):
        materias["Historia"] = {"alumnos": [{"dni": "10000000", "notas": []}]}
        self.assertIsNone(estadisticas_materia("Historia"))
        self.assertIsNone(estadisticas_generales())

    def test_resumen_general_recorre_materias(self):
        materias["Historia"] = {"alumnos": [{"dni": "10000000", "notas": [7]}]}
        materias["Matemática"] = {"alumnos": [{"dni": "10000001", "notas": [3]}]}
        resumen = estadisticas_generales()
        self.assertEqual(resumen["promedio_general"], 5)
        self.assertEqual(resumen["aprobados"], 1)
        self.assertEqual(resumen["desaprobados"], 1)

    def test_funciones_recursivas(self):
        self.assertEqual(suma_recursiva([1, 2, 3]), 6)
        self.assertEqual(maximo_recursivo([1, 8, 3]), 8)


if __name__ == "__main__":
    unittest.main()
