from sqlite3 import IntegrityError

from sqlalchemy.orm import Session
from sqlalchemy import func, Integer
from models.HiredEmployeesModel import HiredEmployee
from models.JobModel import Job
from models.DepartmentModel import Department
from datetime import datetime
from typing import List, Optional
import pandas as pd

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

    def get_hires_per_job_and_department_by_quarter_2021(self):
        result = (
            self.session.query(
                Department.name.label("department"),
                Job.name.label("job"),
                ((func.strftime('%m', HiredEmployee.hire_date).cast(Integer) - 1) / 3 + 1).label("quarter"),
                func.count(HiredEmployee.id).label("hires")
            )
            .join(Department, HiredEmployee.department_id == Department.id)
            .join(Job, HiredEmployee.job_id == Job.id)
            .filter(func.strftime('%Y', HiredEmployee.hire_date) == '2021')
            .group_by(Department.name, Job.name,
                      (func.strftime('%m', HiredEmployee.hire_date).cast(Integer) - 1) / 3 + 1)
            .order_by(Department.name.asc(), Job.name.asc())
            .all()
        )
        return result


    def get_departments_above_average_hires_2021(self):
        hires_per_department = (
            self.session.query(
                HiredEmployee.department_id,
                func.count(HiredEmployee.id).label("num_hired")
            )
            .filter(func.strftime('%Y', HiredEmployee.hire_date) == '2021')
            .group_by(HiredEmployee.department_id)
            .subquery()
        )

        avg_hires = (
            self.session.query(func.avg(hires_per_department.c.num_hired))
            .scalar_subquery()
        )

        result = (
            self.session.query(
                Department.id,
                Department.name,
                hires_per_department.c.num_hired
            )
            .join(hires_per_department, Department.id == hires_per_department.c.department_id)
            .filter(hires_per_department.c.num_hired > avg_hires)
            .order_by(hires_per_department.c.num_hired.desc())
            .all()
        )

        return result

    def create_hired_employees_bulk(self, hiredemployees_df):
        average_date = hiredemployees_df['hire_date'].mean() if 'hire_date' in hiredemployees_df.columns else None

        additional_df = hiredemployees_df[['department_id', 'job_id']].dropna()
        new_hires = []

        for _, row in hiredemployees_df.iterrows():
            if pd.isnull(row['name']) or row['name'] == '':
                continue

            date = row['hire_date'] if pd.notnull(row['hire_date']) else average_date

            department = row['department_id'] if pd.notnull(row['department_id']) else None
            job = row['job_id'] if pd.notnull(row['job_id']) else 184

            if department is None:
                matching_row = additional_df[additional_df['job_id'] == job]
                if not matching_row.empty:
                    department = matching_row['department_id'].iloc[0]

            if department is None:
                department = 13

            new_hires.append(HiredEmployee(
                id=row['id'],
                name=row['name'],
                hire_date=date,
                department_id=department,
                job_id=job
            ))

        try:
            self.session.bulk_save_objects(new_hires)
            self.session.commit()
        except IntegrityError as e:
            self.session.rollback()
            print(f"Error al insertar registros: {e}")

        #print(additional_df)
        return [HiredEmployee.name for HiredEmployee in new_hires]

    def close(self):
        self.session.close()