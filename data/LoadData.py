import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.DepartmentModel import Department
from models.JobModel import Job
from models.HiredEmployeesModel import HiredEmployee

engine = create_engine('sqlite:///employees.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

departments_df = pd.read_csv('departments.csv', header=None, names=['id', 'name'])
for _, row in departments_df.iterrows():
    department = Department(id=row['id'], name=row['name'])
    session.merge(department)

jobs_df = pd.read_csv('jobs.csv', header=None, names=['id', 'name'])
for _, row in jobs_df.iterrows():
    job = Job(id=row['id'], name=row['name'])
    session.merge(job)

employees_df = pd.read_csv('hired_employees.csv', header=None,
                           names=['id', 'name', 'hire_date', 'job_id', 'department_id'])

employees_df['hire_date'] = pd.to_datetime(employees_df['hire_date'], errors='coerce')
employees_df['name'] = employees_df['name'].fillna('unknown')
employees_df['hire_date'] = employees_df['hire_date'].fillna(pd.Timestamp('9999-01-01'))
employees_df['job_id'] = employees_df['job_id'].fillna(-1)
employees_df['department_id'] = employees_df['department_id'].fillna(-1)

employees_df['job_id'] = employees_df['job_id'].astype(int)
employees_df['department_id'] = employees_df['department_id'].astype(int)

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
print("✅ Datos cargados exitosamente.")

session.close()
