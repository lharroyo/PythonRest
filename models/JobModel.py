from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    hired_employees = relationship("HiredEmployee", back_populates="job")