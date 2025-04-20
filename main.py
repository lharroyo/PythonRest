from sqlalchemy import create_engine
from models.department import Department
from models.job import Job
from models.hired_employee import HiredEmployee
from sqlalchemy.orm import declarative_base

Base = declarative_base()

if __name__ == "__main__":
    engine = create_engine('sqlite:///employees.db')
    Base.metadata.create_all(engine)