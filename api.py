from flask import Flask, jsonify
from sqlalchemy import create_engine
from models.base import Base
from services.DepartmentsService import DepartmentService

engine = create_engine("sqlite:///data/employees.db")
Base.metadata.create_all(engine)
service = DepartmentService(engine)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def get_all():
    departments = service.get_all_departments()
    departments_list = [{"id": dept.id, "name": dept.name} for dept in departments]
    return jsonify({"departments": departments_list})

@app.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    departments = service.get_department_by_id(id)
    return jsonify({"Department": {"id": departments.id, "name": departments.name}})


@app.route('/', methods=['POST'])
def post_home():
    return jsonify({"message":"Este es el método de Creación"})

@app.route('/', methods=['PUT'])
def put_home():
    return jsonify({"message":"Este es el método de Actualización"})

@app.route('/', methods=['DELETE'])
def delete_home():
    return jsonify({"message":"Este es el método de Eliminación"})


app.run()