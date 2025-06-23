"""
Módulo de modelo de datos para la gestión de estudiantes.
Contiene la definición de la clase Estudiante, funciones auxiliares y carga de datos desde CSV.
"""

from pydantic import BaseModel
import csv
import sys

# Ruta al archivo CSV con la base de datos de estudiantes
CSV_FILE = '../Base_Datos.csv'

class Estudiante(BaseModel):
    """
    Representa el esquema de datos de un estudiante.

    Atributos:
        id (int): Identificador único del estudiante.
        matricula (str): Matrícula.
        nombre (str): Nombre completo.
        genero (str): Género (Masculino/Femenino).
        edad (int): Edad en años.
        estatus (str): Estado académico (ej. activo, baja temporal).
        carrera (str): Iniciales de la carrera (ITI, ICC, LCC).
        semestre (int): Semestre actual.
        materias_aprobadas (int): Número de materias aprobadas.
        creditos_acumulados (int): Créditos acumulados.
        porcentaje_avanzado (int): Porcentaje de avance en la carrera.
    """
    id: int
    matricula: str
    nombre: str
    genero: str
    edad: int
    estatus: str
    carrera: str
    semestre: int
    materias_aprobadas: int
    creditos_acumulados: int
    porcentaje_avanzado: int

def normalize_degree(degree: str):
    """
    Convierte la descripción completa de la carrera a sus iniciales.

    Parámetros:
        degree (str): Nombre completo de la carrera.

    Devuelve:
        str: Abreviatura de la carrera (ITI, ICC o LCC).
    """
    if degree == "Ingeniería en Tecnologías de la Información":
        return "ITI"
    elif degree == "Ingeniería en Ciencias de la Computación":
        return "ICC"
    else:
        return "LCC"

def load_students():
    """
    Carga y valida los registros de estudiantes desde un archivo CSV.

    Filtra únicamente a los primeros 40 registros (id <= 40) para probar la petición POST.
    En caso de error de E/S, interrumpe la ejecución con un código de salida 1.

    Devuelve:
        list[Estudiante]: Lista de instancias de Estudiante.

    Excepciones:
        SystemExit: Cuando no se puede abrir o leer el CSV.
    """
    students = []
    try:
        with open(CSV_FILE, 'r', encoding='utf-8-sig', newline='') as file:
            dict_reader = csv.DictReader(file)
            for row in dict_reader:
                # Solo procesar los primeros 40 estudiantes
                if int(row['id']) <= 40:
                    student = Estudiante(
                        id=int(row['id']),
                        matricula=row['matricula'],
                        nombre=row['nombre'],
                        genero=row['genero'],
                        edad=int(row['edad']),
                        estatus=row['estatus'],
                        carrera=normalize_degree(row['carrera']),
                        semestre=int(row['semestre']),
                        materias_aprobadas=int(row['materias_aprobadas']),
                        creditos_acumulados=int(row['creditos_acumulados']),
                        porcentaje_avanzado=int(row['porcentaje_avanzado'])
                    )
                    students.append(student)
            return students
    except OSError as e:
        print(f"[ERROR {e.__class__.__name__}]: No se pudo abrir/leer el archivo: {CSV_FILE}")
        sys.exit(1)