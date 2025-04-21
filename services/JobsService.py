from sqlalchemy.orm import Session
from models.JobModel import Job
from models.HiredEmployeesModel import HiredEmployee

class JobsService:
    def __init__(self, engine):
        self.engine = engine
        self.session = Session(bind=self.engine)

    def get_all_jobs(self):
        return self.session.query(Job).all()

    def get_job_by_id(self, job_id: int):
        return self.session.query(Job).filter_by(id=job_id).first()

    def create_job(self, name: str):
        new_job = Job(name=name)
        self.session.add(new_job)
        self.session.commit()
        return new_job

    def update_job(self, job_id: int, new_name: str):
        job = self.get_job_by_id(job_id)
        if job:
            job.name = new_name
            self.session.commit()
        return job

    def delete_job(self, job_id: int):
        job = self.get_job_by_id(job_id)
        if job:
            self.session.delete(job)
            self.session.commit()
        return job

    def create_jobs_bulk(self, jobs_df):
        if jobs_df.isnull().values.any() or (jobs_df['name'] == '').any():
            raise ValueError("Los datos no pueden contener valores nulos o vacíos.")

        new_jobs = [
            Job(id=row['id'], name=row['name']) for _, row in jobs_df.iterrows()
        ]

        self.session.bulk_save_objects(new_jobs)
        self.session.commit()
        return [job.name for job in new_jobs]

    def close(self):
        self.session.close()