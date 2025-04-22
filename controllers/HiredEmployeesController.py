import os
import pandas as pd

from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename

from services.HiredEmployeesService import HiredEmployeesService  # Asegúrate de que la ruta sea correcta
from datetime import datetime

hired_employees_bp = Blueprint('hiredemployees', __name__)

def init_hired_employees_controller(service: HiredEmployeesService):
    @hired_employees_bp.route('/', methods=['GET'])
    def get_all():
        employees = service.get_all_hired_employees()
        employees_list = [
            {
                "id": emp.id,
                "name": emp.name,
                "hire_date": emp.hire_date.isoformat(),
                "job_id": emp.job_id,
                "department_id": emp.department_id
            } for emp in employees
        ]
        return jsonify({"HiredEmployees": employees_list}), 200

    @hired_employees_bp.route('/<int:id>', methods=['GET'])
    def get_by_id(id):
        employee = service.get_hired_employee_by_id(id)
        if employee is None:
            return jsonify({"Error": "Hired employee not found."}), 404
        else:
            return jsonify({
                "HiredEmployee": {
                    "id": employee.id,
                    "name": employee.name,
                    "hire_date": employee.hire_date.isoformat(),
                    "job_id": employee.job_id,
                    "department_id": employee.department_id
                }
            })

    @hired_employees_bp.route('/', methods=['POST'])
    def post_hired_employee():
        data = request.get_json()
        if not data or 'name' not in data or 'hire_date' not in data or 'job_id' not in data:
            return jsonify({"Error": "Invalid input"}), 400
        
        name = data['name']
        hire_date = datetime.fromisoformat(data['hire_date'])
        job_id = data['job_id']
        department_id = data.get('department_id')

        new_employee = service.create_hired_employee(name, hire_date, job_id, department_id)
        return jsonify({
            "HiredEmployee": {
                "id": new_employee.id,
                "name": new_employee.name,
                "hire_date": new_employee.hire_date.isoformat(),
                "job_id": new_employee.job_id,
                "department_id": new_employee.department_id
            }
        }), 201

    @hired_employees_bp.route('/<int:id>', methods=['PUT'])
    def put_hired_employee(id):
        data = request.get_json()
        if not data or 'name' not in data or 'hire_date' not in data or 'job_id' not in data:
            return jsonify({"Error": "Invalid input"}), 400
        
        name = data['name']
        hire_date = datetime.fromisoformat(data['hire_date'])
        job_id = data['job_id']
        department_id = data.get('department_id')

        updated_employee = service.update_hired_employee(id, name, hire_date, job_id, department_id)
        if updated_employee is None:
            return jsonify({"Error": "Hired employee not found."}), 404
        else:
            return jsonify({
                "HiredEmployee": {
                    "id": updated_employee.id,
                    "name": updated_employee.name,
                    "hire_date": updated_employee.hire_date.isoformat(),
                    "job_id": updated_employee.job_id,
                    "department_id": updated_employee.department_id
                }
            }), 200

    @hired_employees_bp.route('/<int:id>', methods=['DELETE'])
    def delete_hired_employee(id):
        deleted_employee = service.delete_hired_employee(id)
        
        if deleted_employee is None:
            return jsonify({"Error": "Hired employee not found."}), 404
        else:
            return jsonify({
                "Message": "Hired employee deleted successfully.",
                "HiredEmployee": {
                    "id": deleted_employee.id,
                    "name": deleted_employee.name,
                    "hire_date": deleted_employee.hire_date.isoformat(),
                    "job_id": deleted_employee.job_id,
                    "department_id": deleted_employee.department_id
                }
            }), 200

    @hired_employees_bp.route('/byquarter', methods=['GET'])
    def hired_employees_by_quarter():
        hires_by_quarter_2021 = service.get_hires_per_job_and_department_by_quarter_2021()
        result_list = [
            {
                "department": row.department,
                "job": row.job,
                "quarter": int(row.quarter),
                "hires": row.hires
            }
            for row in hires_by_quarter_2021
        ]
        return jsonify({
            "message": "Hires per job and department by quarter 2021",
            "results": result_list
        }), 200

    @hired_employees_bp.route('/byaveragehires', methods=['GET'])
    def departments_above_average_hires():
        above_avg_departments = service.get_departments_above_average_hires_2021()
        result_list = [
            {
                "department_id": row.id,
                "department_name": row.name,
                "hires": row.num_hired
            }
            for row in above_avg_departments
        ]
        return jsonify({
            "message": "Departments with hires above 2021 average",
            "results": result_list
        }), 200

    @hired_employees_bp.route('/uploadbybulk', methods=['POST'])
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
                jobs_df = pd.read_csv(file_path, header=None,
                                      names=['id', 'name', 'hire_date', 'department_id', 'job_id'])

                jobs_df['hire_date'] = pd.to_datetime(jobs_df['hire_date'], errors='coerce')

                created_employees = service.create_hired_employees_bulk(jobs_df)
                return jsonify(
                    {"message": "Hired employees uploaded successfully", "employees": created_employees}), 201
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        return jsonify({"error": "Invalid file format"}), 400

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'csv'}