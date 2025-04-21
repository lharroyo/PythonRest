from flask import Blueprint, jsonify, request
from services.JobsService import JobsService  # Asegúrate de que la ruta sea correcta

jobs_bp = Blueprint('jobs', __name__)

def init_jobs_controller(service):
    @jobs_bp.route('/', methods=['GET'])
    def get_all():
        jobs = service.get_all_jobs()
        jobs_list = [{"id": job.id, "name": job.name} for job in jobs]
        return jsonify({"Jobs": jobs_list}), 200

    @jobs_bp.route('/<int:id>', methods=['GET'])
    def get_by_id(id):
        job = service.get_job_by_id(id)
        if job is None:
            return jsonify({"Error": "Job not found."}), 404
        else:
            return jsonify({"Job": {"id": job.id, "name": job.name}})

    @jobs_bp.route('/', methods=['POST'])
    def post_job():
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({"Error": "Invalid input"}), 400
        name = data['name']
        new_job = service.create_job(name)
        return jsonify({"Job": {"id": new_job.id, "name": new_job.name}}), 201

    @jobs_bp.route('/<int:id>', methods=['PUT'])
    def put_job(id):
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({"Error": "Invalid input"}), 400
        name = data['name']
        updated_job = service.update_job(id, name)
        if updated_job is None:
            return jsonify({"Error": "Job not found."}), 404
        else:
            return jsonify({"Job": {"id": updated_job.id, "name": updated_job.name}}), 200

    @jobs_bp.route('/<int:id>', methods=['DELETE'])
    def delete_job(id):
        deleted_job = service.delete_job(id)
        
        if deleted_job is None:
            return jsonify({"Error": "Job not found."}), 404
        else:
            return jsonify({"message": "Job deleted successfully.", "Job": {"id": deleted_job.id, "name": deleted_job.name}}), 200