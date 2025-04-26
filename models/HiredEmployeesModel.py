from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class HiredEmployee(Base):
    __tablename__ = 'hiredemployees'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    hire_date = Column(DateTime, nullable=False)
    job_id = Column(Integer, ForeignKey('jobs.id'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=True)

    job = relationship("Job", back_populates="hired_employees")
    department = relationship("Department", back_populates="hired_employees")