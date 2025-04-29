from flask import Flask
from sqlalchemy import create_engine
from models.base import Base
from services.DepartmentsService import DepartmentService
from services.JobsService import JobsService
from services.HiredEmployeesService import HiredEmployeesService
from controllers.DepartmentsController import init_departments_controller, departments_bp
from controllers.JobsController import init_jobs_controller, jobs_bp
from controllers.HiredEmployeesController import init_hired_employees_controller, hired_employees_bp
from controllers.root import rootpath
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine("sqlite:data/employees.db")
Base.metadata.create_all(engine)

department_service = DepartmentService(engine)
job_service = JobsService(engine)
hired_employees_service = HiredEmployeesService(engine)

app = Flask(__name__)

init_departments_controller(department_service)
init_jobs_controller(job_service)
init_hired_employees_controller(hired_employees_service)

app.register_blueprint(departments_bp, url_prefix='/departments')
app.register_blueprint(jobs_bp, url_prefix='/jobs')
app.register_blueprint(hired_employees_bp, url_prefix='/hiredemployees')
app.register_blueprint(rootpath)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
