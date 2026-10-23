"""Lectura y escritura de los datos del sistema en CSV y JSON."""

import csv
import json
from pathlib import Path

from datos_generales.memoria import ROLES, estudiantes, materias


CARPETA_DATOS = Path(__file__).resolve().parent.parent / "datos"
ARCHIVO_ESTUDIANTES = CARPETA_DATOS / "estudiantes.csv"
ARCHIVO_MATERIAS = CARPETA_DATOS / "materias.json"
ARCHIVO_ROLES = CARPETA_DATOS / "roles.json"


def guardar_datos():
    """Guarda estudiantes en CSV y cursadas/notas y roles en JSON."""
    CARPETA_DATOS.mkdir(exist_ok=True)
    with ARCHIVO_ESTUDIANTES.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["dni", "legajo", "nombre", "apellido"])
        for dni, estudiante in estudiantes.items():
            escritor.writerow([
                dni, estudiante["legajo"], estudiante["nombre"], estudiante["apellido"]
            ])
    with ARCHIVO_MATERIAS.open("w", encoding="utf-8") as archivo:
        json.dump(materias, archivo, ensure_ascii=False, indent=2)
    with ARCHIVO_ROLES.open("w", encoding="utf-8") as archivo:
        json.dump(ROLES, archivo, ensure_ascii=False, indent=2)


def cargar_datos():
    """Restaura los archivos disponibles; un archivo ausente deja datos vacíos."""
    if ARCHIVO_ESTUDIANTES.exists():
        with ARCHIVO_ESTUDIANTES.open("r", newline="", encoding="utf-8") as archivo:
            for fila in csv.DictReader(archivo):
                estudiantes[fila["dni"]] = {
                    "legajo": int(fila["legajo"]),
                    "nombre": fila["nombre"],
                    "apellido": fila["apellido"],
                }
    if ARCHIVO_MATERIAS.exists():
        with ARCHIVO_MATERIAS.open("r", encoding="utf-8") as archivo:
            materias.update(json.load(archivo))
    if ARCHIVO_ROLES.exists():
        with ARCHIVO_ROLES.open("r", encoding="utf-8") as archivo:
            ROLES.update(json.load(archivo))
