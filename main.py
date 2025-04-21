from flask import Flask
from sqlalchemy import create_engine
from models.base import Base
from services.DepartmentsService import DepartmentService
from controllers.DepartmentsController import init_departments_controller, departments_bp
from models.HiredEmployeesModel import HiredEmployee

engine = create_engine("sqlite:///data/employees.db")
Base.metadata.create_all(engine)
service = DepartmentService(engine)

app = Flask(__name__)
app.config["DEBUG"] = True

init_departments_controller(service)

app.register_blueprint(departments_bp, url_prefix='/departments')

if __name__ == '__main__':
    app.run()