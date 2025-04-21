from sqlalchemy.orm import Session
from models.HiredEmployeesModel import HiredEmployee
from models.JobModel import Job
from models.DepartmentModel import Department
from datetime import datetime
from typing import List, Optional

class HiredEmployeesService:
    def __init__(self, engine):
        self.engine = engine
        self.session = Session(bind=self.engine)

    def get_all_hired_employees(self) -> List[HiredEmployee]:
        return self.session.query(HiredEmployee).all()

    def get_hired_employee_by_id(self, employee_id: int) -> Optional[HiredEmployee]:
        return self.session.query(HiredEmployee).filter_by(id=employee_id).first()

    def create_hired_employee(self, name: str, hire_date: datetime, job_id: int, department_id: Optional[int] = None) -> HiredEmployee:
        new_employee = HiredEmployee(name=name, hire_date=hire_date, job_id=job_id, department_id=department_id)
        self.session.add(new_employee)
        self.session.commit()
        return new_employee

    def update_hired_employee(self, employee_id: int, name: str, hire_date: datetime, job_id: int, department_id: Optional[int] = None) -> Optional[HiredEmployee]:
        employee = self.get_hired_employee_by_id(employee_id)
        if employee:
            employee.name = name
            employee.hire_date = hire_date
            employee.job_id = job_id
            employee.department_id = department_id
            self.session.commit()
        return employee

    def delete_hired_employee(self, employee_id: int) -> Optional[HiredEmployee]:
        employee = self.get_hired_employee_by_id(employee_id)
        if employee:
            self.session.delete(employee)
            self.session.commit()
        return employee

    def close(self):
        self.session.close()