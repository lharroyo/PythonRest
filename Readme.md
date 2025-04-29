# Proyecto de Gestión de Empleados

Este proyecto es una API RESTful para la gestión de departamentos, empleados contratados y trabajos. Está construido utilizando Flask y SQLAlchemy, y permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en las entidades mencionadas.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Flask**: Framework web utilizado para construir la API.
- **SQLAlchemy**: ORM (Object-Relational Mapping) utilizado para interactuar con la base de datos.
- **Pandas**: Biblioteca utilizada para la manipulación y análisis de datos, especialmente para la carga masiva de datos desde archivos CSV.
- **Werkzeug**: Utilizado para asegurar los nombres de archivo al subir archivos.

## Estructura del Proyecto

- **Controllers**: Contienen las rutas y lógica de la API.
  - `DepartmentsController.py`
  - `HiredEmployeesController.py`
  - `JobsController.py`
- **Services**: Contienen la lógica de negocio y las interacciones con la base de datos.
  - `DepartmentsService.py`
  - `HiredEmployeesService.py`
  - `JobsService.py`
- **Models**: Definen las estructuras de las tablas de la base de datos.
  - `DepartmentModel.py`
  - `HiredEmployeesModel.py`
  - `JobModel.py`

## Endpoints y Métodos de Consumo

**Cloud endpoint**: `https://pythonrest.azurewebsites.net/`
**Alternative Cloud endpoint**: `https://pythonrest-production.up.railway.app/`


### Departments `/departments`


- **GET /**: Obtener todos los departamentos.

  - **Curl**:

    ```bash

    curl -X GET https://pythonrest.azurewebsites.net/departments/

    ```

  - **Respuesta**: Lista de departamentos.


- **GET /<int:id>**: Obtener un departamento por ID.

  - **Curl**:

    ```bash

    curl -X GET https://pythonrest.azurewebsites.net/departments/1

    ```

  - **Respuesta**: Detalles del departamento o error si no se encuentra.


- **POST /**: Crear un nuevo departamento.

  - **Curl**:

    ```bash

    curl -X POST https://pythonrest.azurewebsites.net/departments/ -H "Content-Type: application/json" -d '{"name": "Nuevo Departamento"}'

    ```

  - **Entrada**: JSON con el nombre del departamento.

  - **Respuesta**: Detalles del departamento creado.


- **PUT /<int:id>**: Actualizar un departamento existente.

  - **Curl**:

    ```bash

    curl -X PUT https://pythonrest.azurewebsites.net/departments/1 -H "Content-Type: application/json" -d '{"name": "Departamento Actualizado"}'

    ```

  - **Entrada**: JSON con el nuevo nombre del departamento.

  - **Respuesta**: Detalles del departamento actualizado o error si no se encuentra.


- **DELETE /<int:id>**: Eliminar un departamento.

  - **Curl**:

    ```bash

    curl -X DELETE https://pythonrest.azurewebsites.net/departments/1

    ```

  - **Respuesta**: Mensaje de éxito o error si no se encuentra.


- **POST /uploadbybulk**: Cargar departamentos en masa desde un archivo CSV.

  - **Curl**:

    ```bash

    curl -X POST https://pythonrest.azurewebsites.net/departments/uploadbybulk -F "file=@path/to/your/file.csv"

    ```

  - **Entrada**: Archivo CSV.

  - **Respuesta**: Mensaje de éxito o error.

### Hired Employees `/hiredemployees`


- **GET /**: Obtener todos los empleados contratados.

  - **Curl**:

    ```bash

    curl -X GET https://pythonrest.azurewebsites.net/hiredemployees/

    ```

  - **Respuesta**: Lista de empleados contratados.


- **GET /<int:id>**: Obtener un empleado contratado por ID.

  - **Curl**:

    ```bash

    curl -X GET https://pythonrest.azurewebsites.net/hiredemployees/1

    ```

  - **Respuesta**: Detalles del empleado o error si no se encuentra.


- **POST /**: Crear un nuevo empleado contratado.

  - **Curl**:

    ```bash

    curl -X POST https://pythonrest.azurewebsites.net/hiredemployees/ -H "Content-Type: application/json" -d '{"name": "Nuevo Empleado", "hire_date": "2023-01-01", "job_id": 1, "department_id": 1}'

    ```

  - **Entrada**: JSON con los detalles del empleado.

  - **Respuesta**: Detalles del empleado creado.


- **PUT /<int:id>**: Actualizar un empleado contratado existente.

  - **Curl**:

    ```bash

    curl -X PUT https://pythonrest.azurewebsites.net/hiredemployees/1 -H "Content-Type: application/json" -d '{"name": "Empleado Actualizado", "hire_date": "2023-01-15", "job_id": 2, "department_id": 1}'

    ```

  - **Entrada**: JSON con los nuevos detalles del empleado.

  - **Respuesta**: Detalles del empleado actualizado o error si no se encuentra.


- **DELETE /<int:id>**: Eliminar un empleado contratado.

  - **Curl**:

    ```bash

    curl -X DELETE https://pythonrest.azurewebsites.net/hiredemployees/1

    ```

  - **Respuesta**: Mensaje de éxito o error si no se encuentra.


- **GET /byquarter**: Obtener contrataciones por trabajo y departamento por trimestre en 2021.

  - **Curl**:

    ```bash

    curl -X GET https://pythonrest.azurewebsites.net/hiredemployees/byquarter

    ```

  - **Respuesta**: Lista de contrataciones por trimestre.


- **GET /byaveragehires**: Obtener departamentos con contrataciones por encima del promedio en 2021.

  - **Curl**:

    ```bash

    curl -X GET https://pythonrest.azurewebsites.net/hiredemployees/byaveragehires

    ```

  - **Respuesta**: Lista de departamentos.


- **POST /uploadbybulk**: Cargar empleados contratados en masa desde un archivo CSV.

  - **Curl**:

    ```bash

    curl -X POST https://pythonrest.azurewebsites.net/hiredemployees/uploadbybulk -F "file=@path/to/your/file.csv"

    ```

  - **Entrada**: Archivo CSV.

  - **Respuesta**: Mensaje de éxito o error.

### Jobs `/jobs`


- **GET /**: Obtener todos los trabajos.

  - **Curl**:

    ```bash

    curl -X GET https://pythonrest.azurewebsites.net/jobs/

    ```

  - **Respuesta**: Lista de trabajos.


- **GET /<int:id>**: Obtener un trabajo por ID.

  - **Curl**:

    ```bash

    curl -X GET https://pythonrest.azurewebsites.net/jobs/1

    ```

  - **Respuesta**: Detalles del trabajo o error si no se encuentra.


- **POST /**: Crear un nuevo trabajo.

  - **Curl**:

    ```bash

    curl -X POST https://pythonrest.azurewebsites.net/jobs/ -H "Content-Type: application/json" -d '{"name": "Nuevo Trabajo"}'

    ```

  - **Entrada**: JSON con el nombre del trabajo.

  - **Respuesta**: Detalles del trabajo creado.


- **PUT /<int:id>**: Actualizar un trabajo existente.

  - **Curl**:

    ```bash

    curl -X PUT https://pythonrest.azurewebsites.net/jobs/1 -H "Content-Type: application/json" -d '{"name": "Trabajo Actualizado"}'

    ```

  - **Entrada**: JSON con el nuevo nombre del trabajo.

  - **Respuesta**: Detalles del trabajo actualizado o error si no se encuentra.


- **DELETE /<int:id>**: Eliminar un trabajo.

  - **Curl**:

    ```bash

    curl -X DELETE https://pythonrest.azurewebsites.net/jobs/1

    ```

  - **Respuesta**: Mensaje de éxito o error si no se encuentra.


- **POST /uploadbybulk**: Cargar trabajos en masa desde un archivo CSV.

  - **Curl**:

    ```bash

    curl -X POST https://pythonrest.azurewebsites.net/jobs/uploadbybulk -F "file=@path/to/your/file.csv"

    ```

  - **Entrada**: Archivo CSV.

  - **Respuesta**: Mensaje de éxito o error.

### Referencias
#### https://github.com/lharroyo/PythonRest.git
#### https://hub.docker.com/repository/docker/lharroyoa/pythonemployees
