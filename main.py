from sqlalchemy import create_engine
from models.base import Base
from services.DepartmentsService import DepartmentService
from models.HiredEmployeesModel import HiredEmployee

if __name__ == "__main__":
    engine = create_engine("sqlite:///C:/Users/lharr/OneDrive/Escritorio/Challenge/PythonCRUD/data/employees.db")
    Base.metadata.create_all(engine)
    service = DepartmentService(engine)

    departments = service.get_all_departments()
    print("Lista de departamentos:")
    for dept in departments:
        print(f"- {dept.name}")

    service.close()
