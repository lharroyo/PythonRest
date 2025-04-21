from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.JobModel import Job
from models.HiredEmployeesModel import HiredEmployee
from models.DepartmentModel import Department

DATABASE_URL = "sqlite:///C:/Users/lharr/OneDrive/Escritorio/Challenge/PythonCRUD/data/employees.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

# Servicio para obtener todos los registros de jobs
def get_all_jobs():
    session = SessionLocal()
    try:
        jobs = session.query(Job).all()
        return jobs
    finally:
        session.close()

# Prueba del servicio
if __name__ == "__main__":
    jobs = get_all_jobs()
    for job in jobs:
        print(f"ID: {job.id}, Name: {job.name}")
