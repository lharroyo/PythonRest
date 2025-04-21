from flask import Flask
from sqlalchemy import create_engine
from models.base import Base
from services.DepartmentsService import DepartmentService
from services.JobsService import JobsService  # Asegúrate de que la ruta sea correcta
from controllers.DepartmentsController import init_departments_controller, departments_bp
from controllers.JobsController import init_jobs_controller, jobs_bp

engine = create_engine("sqlite:///data/employees.db")
Base.metadata.create_all(engine)

department_service = DepartmentService(engine)
job_service = JobsService(engine)

app = Flask(__name__)
app.config["DEBUG"] = True

init_departments_controller(department_service)
init_jobs_controller(job_service)

app.register_blueprint(departments_bp, url_prefix='/departments')
app.register_blueprint(jobs_bp, url_prefix='/jobs')

if __name__ == '__main__':
    app.run()