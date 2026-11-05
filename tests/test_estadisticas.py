
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

from modulos_.estadisticas import (
    calcular_promedio,
    estadisticas_materia,
    suma_recursiva,
    maximo_recursivo,
    estudiantes_en_todas_las_materias
)

from modulos_.materias_CRUD import (
    crear_materia,
    agregar_alumno_materia
)

from modulos_.alumnos_CRUD import crear_estudiante

from modulos_.notas_CRUD import agregar_nota


class PruebasEstadisticas(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        carpeta = Path(self.temp.name)

        self.archivo_alumnos = carpeta / "alumnos.txt"
        self.archivo_materias = carpeta / "materias.txt"
        self.archivo_inscripciones = carpeta / "inscripciones.txt"

        self.patches = [
            patch(
                "modulos_.alumnos_CRUD.ARCHIVO_ALUMNOS",
                self.archivo_alumnos
            ),
            patch(
                "modulos_.alumnos_CRUD.ARCHIVO_INSCRIPCIONES",
                self.archivo_inscripciones
            ),
            patch(
                "modulos_.materias_CRUD.ARCHIVO_MATERIAS",
                self.archivo_materias
            ),
            patch(
                "modulos_.materias_CRUD.ARCHIVO_INSCRIPCIONES",
                self.archivo_inscripciones
            ),
            patch(
                "modulos_.notas_CRUD.ARCHIVO_INSCRIPCIONES",
                self.archivo_inscripciones
            )
        ]

        for p in self.patches:
            p.start()

        self.archivo_alumnos.touch()
        self.archivo_materias.touch()
        self.archivo_inscripciones.touch()

    def tearDown(self):
        for p in reversed(self.patches):
            p.stop()

        self.temp.cleanup()

    def test_promedio_de_notas_y_lista_vacia(self):
        self.assertEqual(calcular_promedio([6, 8]), 7)
        self.assertIsNone(calcular_promedio([]))

    def test_estadisticas_materia(self):
        crear_estudiante("10000000", "Ana", "Perez")
        crear_estudiante("10000001", "Juan", "Gomez")

        crear_materia("Historia")

        agregar_alumno_materia("Historia", "10000000")
        agregar_alumno_materia("Historia", "10000001")

        agregar_nota("Historia", "10000000", 2)
        agregar_nota("Historia", "10000000", 6)

        agregar_nota("Historia", "10000001", 8)
        agregar_nota("Historia", "10000001", 10)

        resumen = estadisticas_materia("Historia")

        self.assertEqual(resumen["aprobados"], 2)
        self.assertEqual(resumen["desaprobados"], 0)
        self.assertEqual(resumen["cantidad_notas"], 4)
        self.assertEqual(resumen["nota_minima"], 2)
        self.assertEqual(resumen["nota_maxima"], 10)

    def test_estadisticas_sin_notas(self):
        crear_estudiante("10000000", "Ana", "Perez")
        crear_materia("Historia")
        agregar_alumno_materia("Historia", "10000000")

        self.assertIsNone(estadisticas_materia("Historia"))

    def test_funciones_recursivas(self):
        self.assertEqual(suma_recursiva([1, 2, 3]), 6)
        self.assertEqual(maximo_recursivo([1, 8, 3]), 8)

    def test_estudiantes_en_todas_las_materias(self):
        crear_estudiante("10000000", "Ana", "Perez")
        crear_estudiante("10000001", "Juan", "Gomez")

        crear_materia("Historia")
        crear_materia("Matematica")

        agregar_alumno_materia("Historia", "10000000")
        agregar_alumno_materia("Historia", "10000001")

        agregar_alumno_materia("Matematica", "10000000")

        exito, mensaje = estudiantes_en_todas_las_materias()

        self.assertTrue(exito)
        self.assertIn("10000000", mensaje)


if __name__ == "__main__":
    unittest.main()
