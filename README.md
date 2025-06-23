# Actividad 5: API con CRUD

Para esta actividad se realizó una API en la que, a partir de peticiones REST, se pueda modificar la información cargada en memoria sobre los datos almacenados en la base de datos de estudiantes de la Facultad de Ciencias de la Computación.

## Documentación

### [Archivo JSON con documentación generada por FastAPI](https://github.com/ivan-psz/MDW-API_con_CRUD/blob/main/Documentaci%C3%B3n.json)

### Archivos
* [`model.py`](https://github.com/ivan-psz/MDW-API_con_CRUD/blob/main/model.py): Archivo en donde se define el modelo `Estudiante` con uso de la biblioteca `pydantic`, además de la función `normalize_degree()` para acortar el nombre de la carrera de los estudiantes y la función `load_students()` para leer el CSV con los datos de los estudiantes.
* [`main.py`](https://github.com/ivan-psz/MDW-API_con_CRUD/blob/main/main.py): Archivo en donde se encuentra codificada la API. Este importa `model.py` para cargar los datos del CSV mencionado y se definen los endpoints.

### Endpoints

1. **`GET /estudiantes`**: Recupera la colección completa de estudiantes cargados en memoria (filtrados previamente desde el CSV). 
   - Ejemplo:  
     ```
     GET /estudiantes
     ```

2. **`GET /estudiantes/id/{id}`**: Devuelve el estudiante cuyo campo `id` coincide con el valor dado.  
   - **Parámetros**:  
        - `id` (int): identificador único del estudiante.  
   - **Ejemplo**:  
     ```
     GET /estudiantes/id/1
     ```

3. **`GET /estudiantes/matricula/{matricula}`**: Devuelve el estudiante cuya `matrícula` coincide con el valor dado.  
   - **Parámetros**:  
        - `matricula` (str): Matrícula del estudiante.  
   - **Ejemplo**:  
        ```
        GET /estudiantes/matricula/202500000
        ```

4. **`POST /estudiantes`**: Registra un nuevo estudiante en la colección en memoria.
Antes de la inserción, valida que no exista otro registro con el mismo `id` ni la misma `matrícula`.
    - **BODY (`application/json`)**:
        ```javascript
        {
            "id": int,
            "matricula": "string",
            "nombre": "string",
            "genero": "string",
            "edad": int,
            "estatus": "string",
            "carrera": "string",
            "semestre": int,
            "materias_aprobadas": int,
            "creditos_acumulados": int,
            "porcentaje_avanzado": int
        }
        ```
    - **Ejemplo**:
        ```javascript
        POST /estudiantes
        Content-Type: application/json

        {
            "id": 41,
            "matricula": "202500000",
            "nombre": "Ana Gómez",
            "genero": "Femenino",
            "edad": 21,
            "estatus": "Activo",
            "carrera": "ITI",
            "semestre": 5,
            "materias_aprobadas": 30,
            "creditos_acumulados": 75,
            "porcentaje_avanzado": 50
        }
        ```

5. **`PUT /estudiantes`**: Modifica los datos de un estudiante existente. Se basa en el campo `id` para ubicar el registro en memoria.
    - **BODY (`application/json`)**:
        ```javascript
        {
            "id": int,
            "matricula": "string",
            "nombre": "string",
            "genero": "string",
            "edad": int,
            "estatus": "string",
            "carrera": "string",
            "semestre": int,
            "materias_aprobadas": int,
            "creditos_acumulados": int,
            "porcentaje_avanzado": int
        }
        ```
    - **Ejemplo**:
        ```javascript
        PUT /estudiantes
        Content-Type: application/json

        {
            "id": 41,
            "matricula": "202599999",
            "nombre": "Ana Gómez",
            "genero": "Femenino",
            "edad": 21,
            "estatus": "Activo",
            "carrera": "LCC",
            "semestre": 6,
            "materias_aprobadas": 30,
            "creditos_acumulados": 75,
            "porcentaje_avanzado": 50
        }
        ```
    
6. **`DELETE /estudiantes`**: Elimina el registro del estudiante identificado por `id` de la colección en memoria.
    - **Parámetros**:  
        - `id` (int, **query**): identificador único del estudiante.
    - **Ejemplo**:
        ```
        DELETE /estudiantes?id=41
        ```