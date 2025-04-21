from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from models.JobModel import Job

DATABASE_URL = "sqlite:///C:/Users/lharr/OneDrive/Escritorio/Challenge/PythonCRUD/data/employees.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

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