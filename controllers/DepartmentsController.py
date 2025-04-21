import os
import pandas as pd

from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename

from services.DepartmentsService import DepartmentService

departments_bp = Blueprint('departments', __name__)

def init_departments_controller(service):
    @departments_bp.route('/', methods=['GET'])
    def get_all():
        departments = service.get_all_departments()
        departments_list = [{"id": dept.id, "name": dept.name} for dept in departments]
        return jsonify({"Departments": departments_list}), 200

    @departments_bp.route('/<int:id>', methods=['GET'])
    def get_by_id(id):
        department = service.get_department_by_id(id)
        if department is None:
            return jsonify({"Error": "Departament not found."}), 404
        else:
            return jsonify({"Department": {"id": department.id, "name": department.name}})

    @departments_bp.route('/', methods=['POST'])
    def post_home():
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({"Error": "Invalid input"}), 400
        name = data['name']
        new_department = service.create_department(name)
        return jsonify({"Department": {"id": new_department.id, "name": new_department.name}}), 201

    @departments_bp.route('/<int:id>', methods=['PUT'])
    def put_home(id):
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({"Error": "Invalid input"}), 400
        name = data['name']
        updated_department = service.update_department(id, name)
        if updated_department is None:
            return jsonify({"Error": "Department not found."}), 404
        else:
            return jsonify({"Department": {"id": updated_department.id, "name": updated_department.name}}), 200

    @departments_bp.route('/<int:id>', methods=['DELETE'])
    def delete_home(id):
        deleted_department = service.delete_department(id)
        
        if deleted_department is None:
            return jsonify({"error": "Department not found."}), 404
        else:
            return jsonify({"message": "Department deleted successfully.", "Department": {"id": deleted_department.id, "name": deleted_department.name}}), 200
        
    @departments_bp.route('/uploadbybulk', methods=['POST'])
    def upload_by_bulk():
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join('data/', filename)
            file.save(file_path)
            try:
                departments = pd.read_csv(file_path, header=None, names=['id', 'name'])
                created_departments = service.create_departments_bulk(departments)
                return jsonify({"message": "Departments uploaded successfully", "departments": created_departments}), 201
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        return jsonify({"error": "Invalid file format"}), 400

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'csv'}
    
