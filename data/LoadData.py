import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.DepartmentModel import Department
from models.JobModel import Job
from models.HiredEmployeesModel import HiredEmployee

engine = create_engine('sqlite:///employees.db')
Session = sessionmaker(bind=engine)
session = Session()

departments_df = pd.read_csv('departments.csv')
for _, row in departments_df.iterrows():
    department = Department(id=row['id'], name=row['name'])
    session.merge(department)

jobs_df = pd.read_csv('jobs.csv')
for _, row in jobs_df.iterrows():
    job = Job(id=row['id'], name=row['name'])
    session.merge(job)

employees_df = pd.read_csv('hired_employees.csv')
employees_df['hire_date'] = pd.to_datetime(employees_df['hire_date'])
for _, row in employees_df.iterrows():
    employee = HiredEmployee(
        id=row['id'],
        name=row['name'],
        hire_date=row['hire_date'],
        job_id=row['job_id'],
        department_id=row['department_id']
    )
    session.merge(employee)

session.commit()
session.close()
