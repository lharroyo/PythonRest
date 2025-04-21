from flask import Blueprint, jsonify
from services.DepartmentsService import DepartmentService

departments_bp = Blueprint('departments', __name__)

def init_departments_controller(service):
    @departments_bp.route('/', methods=['GET'])
    def get_all():
        departments = service.get_all_departments()
        departments_list = [{"id": dept.id, "name": dept.name} for dept in departments]
        return jsonify({"departments": departments_list})

    @departments_bp.route('/<int:id>', methods=['GET'])
    def get_by_id(id):
        department = service.get_department_by_id(id)
        return jsonify({"Department": {"id": department.id, "name": department.name}})

    @departments_bp.route('/', methods=['POST'])
    def post_home():
        return jsonify({"message": "Este es el método de Creación"})

    @departments_bp.route('/', methods=['PUT'])
    def put_home():
        return jsonify({"message": "Este es el método de Actualización"})

    @departments_bp.route('/', methods=['DELETE'])
    def delete_home():
        return jsonify({"message": "Este es el método de Eliminación"})