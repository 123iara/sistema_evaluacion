
from pathlib import Path

CARPETA_DATOS = Path(__file__).resolve().parent.parent / "datos"

ARCHIVO_ALUMNOS = CARPETA_DATOS / "alumnos.txt"
ARCHIVO_MATERIAS = CARPETA_DATOS / "materias.txt"
ARCHIVO_INSCRIPCIONES = CARPETA_DATOS / "inscripciones.txt"
ARCHIVO_USUARIOS = CARPETA_DATOS / "usuarios.txt"


def preparar_archivos():
    try:
        CARPETA_DATOS.mkdir(parents=True, exist_ok=True)

        for ruta in (
            ARCHIVO_ALUMNOS,
            ARCHIVO_MATERIAS,
            ARCHIVO_INSCRIPCIONES
        ):
            ruta.touch(exist_ok=True)

        if not ARCHIVO_USUARIOS.exists():
            ARCHIVO_USUARIOS.write_text(
                "admin;admin123;administrador\n"
                "user;1234;usuario\n"
                "user2;4321;usuario\n",
                encoding="utf-8"
            )

    except OSError as error:
        raise OSError(
            f"No se pudieron preparar los archivos: {error}"
        )


def leer_lineas(ruta):
    try:
        with Path(ruta).open("r", encoding="utf-8") as archivo:
            return [
                linea.strip()
                for linea in archivo
                if linea.strip()
            ]

    except FileNotFoundError:
        return []

    except (PermissionError, OSError) as error:
        raise OSError(f"Error al leer el archivo: {error}")


def escribir_lineas(ruta, lineas):
    ruta = Path(ruta)
    temporal = ruta.with_name(ruta.name + ".tmp")

    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)

        with temporal.open("w", encoding="utf-8") as archivo:
            for linea in lineas:
                archivo.write(str(linea) + "\n")

        temporal.replace(ruta)

    except (PermissionError, OSError) as error:
        if temporal.exists():
            temporal.unlink(missing_ok=True)

        raise OSError(f"Error al escribir el archivo: {error}")


def agregar_linea(ruta, linea):
    try:
        Path(ruta).parent.mkdir(parents=True, exist_ok=True)

        with Path(ruta).open("a", encoding="utf-8") as archivo:
            archivo.write(str(linea) + "\n")

    except (PermissionError, OSError) as error:
        raise OSError(f"Error al agregar información: {error}")


def cargar_datos():
    preparar_archivos()
