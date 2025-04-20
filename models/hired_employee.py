from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class HiredEmployee(Base):
    __tablename__ = 'hired_employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hire_date = Column(DateTime, nullable=False)
    job_id = Column(Integer, ForeignKey('jobs.id'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=True)

    job = relationship("Job", back_populates="hired_employees")
    department = relationship("Department", back_populates="hired_employees")