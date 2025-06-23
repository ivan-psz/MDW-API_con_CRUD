"""
API REST CRUD para gestión de estudiantes.
Implementa operaciones GET, POST, PUT y DELETE utilizando FastAPI.
"""
from fastapi import FastAPI
import model

# Carga inicial de datos y configuración de la instancia de FastAPI
students = model.load_students()
app = FastAPI(
    title="Actividad 5 - API con CRUD",
    summary="API que implementa las cuatro operaciones de un CRUD"
)

@app.get("/estudiantes", summary="Obtener todos los estudiantes")
async def get_students():
    """
    Recupera la lista completa de estudiantes.

    Devuelve:
    
        list[Estudiante] o dict: Lista de estudiantes o mensaje de error si está vacía.
    """
    if not students:
        return {
            "RESPUESTA" : "No hay registros disponibles"
        }
    return (students)

@app.get("/estudiantes/id/{id}", summary="Buscar estudiante por ID")
async def get_by_id(id: int):
    """
    Busca un estudiante por su identificador único.

    Parámetros:
    
        id (int): Identificador del estudiante.

    Devuelve:
    
        Estudiante o dict: Instancia de Estudiante o mensaje de no encontrado.
    """
    student = list(filter(
        lambda s : s.id == id, 
        students
    ))
    
    try:
        return (student)[0]
    except:
        return {
            "RESPUESTA" : f"No existe el estudiante con id {id}"
        }

@app.get("/estudiantes/matricula/{matricula}", summary="Buscar estudiante por matrícula")
async def get_by_matricula(matricula: str):
    """
    Recupera un registro de estudiante según su matrícula académica.

    Parámetros:
    
        matricula (str): Matrícula del estudiante.

    Devuelve:
    
        Estudiante o dict: Registro encontrado o mensaje de no encontrado.
    """
    student = list(filter(
        lambda s : s.matricula == matricula, 
        students
    ))
    
    try:
        return (student)[0]
    except:
        return {
            "RESPUESTA" : f"No existe el estudiante con matrícula {matricula}"
        }

@app.post("/estudiantes", summary="Agregar nuevo estudiante")
async def post_student(student: model.Estudiante):
    """
    Inserta un nuevo registro de estudiante.
    Valida unicidad de ID y matrícula antes de la inserción.

    Parámetros:
    
        student (Estudiante): Datos del estudiante por agregar.

    Devuelve:
    
        dict: Mensaje de éxito o error por ID duplicado.
    """
    for s in students:
        if s.id == student.id:
            return {
                "RESPUESTA" : f"El estudiante con id {student.id} ya se encuentra registrado"
            }
        elif s.matricula == student.matricula:
            return {
                "RESPUESTA" : f"El estudiante con matricula {student.matricula} ya se encuentra registrado"
            }
    students.append(student)
    return {
        "RESPUESTA" : "El estudiante ha sido agregado exitosamente",
        "Información del nuevo registro" : (student)
    }

@app.put("/estudiantes", summary="Actualizar estudiante existente")
async def put_student(student: model.Estudiante):
    """
    Actualiza los datos de un estudiante existente.
    Busca por ID y reemplaza el objeto completo.

    Parámetros:
    
        student (Estudiante): Datos actualizados del estudiante.

    Devuelve:
    
        dict: Mensaje de éxito o error si no existe el ID.
    """
    for index, s in enumerate(students, start=0):
        if s.id == student.id:
            students[index] = student
            return {
                "RESPUESTA" : f"El estudiante con id {student.id} ha sido actualizado exitosamente",
                "Información actualizada del registro" : (student)
            }
    return {
        "RESPUESTA" : f"No existe un estudiante registrado con id {student.id}"
    }

@app.delete("/estudiantes", summary="Eliminar estudiante por ID")
async def delete_student(id: int):
    """
    Elimina un estudiante según su identificador.

    Parámetros:
    
        id (int): ID del estudiante a eliminar.

    Devuelve:
    
        dict: Mensaje de éxito y registro eliminado, o error si no existe.
    """
    for index, student in enumerate(students):
        if student.id == id:
            return {
                "RESPUESTA" : f"El estudiante con id {id} ha sido eliminado exitosamente",
                "Registro eliminado" : (students.pop(index))
            }
    return {
        "RESPUESTA" : f"No existe un estudiante registrado con id {id}"
    }