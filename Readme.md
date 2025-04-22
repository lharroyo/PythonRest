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

#### Cloud endpoint: https://pythonrest.azurewebsites.net/

### Departments

- **GET /**: Obtener todos los departamentos.
  - **Respuesta**: Lista de departamentos.
  
- **GET /<int:id>**: Obtener un departamento por ID.
  - **Respuesta**: Detalles del departamento o error si no se encuentra.

- **POST /**: Crear un nuevo departamento.
  - **Entrada**: JSON con el nombre del departamento.
  - **Respuesta**: Detalles del departamento creado.

- **PUT /<int:id>**: Actualizar un departamento existente.
  - **Entrada**: JSON con el nuevo nombre del departamento.
  - **Respuesta**: Detalles del departamento actualizado o error si no se encuentra.

- **DELETE /<int:id>**: Eliminar un departamento.
  - **Respuesta**: Mensaje de éxito o error si no se encuentra.

- **POST /uploadbybulk**: Cargar departamentos en masa desde un archivo CSV.
  - **Entrada**: Archivo CSV.
  - **Respuesta**: Mensaje de éxito o error.

### Hired Employees

- **GET /**: Obtener todos los empleados contratados.
  - **Respuesta**: Lista de empleados contratados.

- **GET /<int:id>**: Obtener un empleado contratado por ID.
  - **Respuesta**: Detalles del empleado o error si no se encuentra.

- **POST /**: Crear un nuevo empleado contratado.
  - **Entrada**: JSON con los detalles del empleado.
  - **Respuesta**: Detalles del empleado creado.

- **PUT /<int:id>**: Actualizar un empleado contratado existente.
  - **Entrada**: JSON con los nuevos detalles del empleado.
  - **Respuesta**: Detalles del empleado actualizado o error si no se encuentra.

- **DELETE /<int:id>**: Eliminar un empleado contratado.
  - **Respuesta**: Mensaje de éxito o error si no se encuentra.

- **GET /byquarter**: Obtener contrataciones por trabajo y departamento por trimestre en 2021.
  - **Respuesta**: Lista de contrataciones por trimestre.

- **GET /byaveragehires**: Obtener departamentos con contrataciones por encima del promedio en 2021.
  - **Respuesta**: Lista de departamentos.

- **POST /uploadbybulk**: Cargar empleados contratados en masa desde un archivo CSV.
  - **Entrada**: Archivo CSV.
  - **Respuesta**: Mensaje de éxito o error.

### Jobs

- **GET /**: Obtener todos los trabajos.
  - **Respuesta**: Lista de trabajos.

- **GET /<int:id>**: Obtener un trabajo por ID.
  - **Respuesta**: Detalles del trabajo o error si no se encuentra.

- **POST /**: Crear un nuevo trabajo.
  - **Entrada**: JSON con el nombre del trabajo.
  - **Respuesta**: Detalles del trabajo creado.

- **PUT /<int:id>**: Actualizar un trabajo existente.
  - **Entrada**: JSON con el nuevo nombre del trabajo.
  - **Respuesta**: Detalles del trabajo actualizado o error si no se encuentra.

- **DELETE /<int:id>**: Eliminar un trabajo.
  - **Respuesta**: Mensaje de éxito o error si no se encuentra.

- **POST /uploadbybulk**: Cargar trabajos en masa desde un archivo CSV.
  - **Entrada**: Archivo CSV.
  - **Respuesta**: Mensaje de éxito o error.

### Referencias
https://github.com/lharroyo/PythonRest.git
https://hub.docker.com/repository/docker/lharroyoa/pythonemployees