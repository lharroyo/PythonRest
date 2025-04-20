from sqlalchemy import create_engine
from models.base import Base
from models.DepartmentModel import Department
from models.JobModel import Job
from models.HiredEmployeesModel import HiredEmployee
from services.DepartmentService import DepartmentService

if __name__ == "__main__":
    engine = create_engine('sqlite:///employees.db')
    Base.metadata.create_all(engine)

    service = DepartmentService()
    departments = service.get_all_departments()
    print("Lista de departamentos:")
    for dept in departments:
        print(f"- {dept.name}")
    service.close()
