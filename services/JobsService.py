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
        cleaned_df = jobs_df.dropna(subset=['id', 'name'])
        cleaned_df = cleaned_df[cleaned_df['name'].str.strip() != '']

        existing_ids = {job.id for job in self.session.query(Job.id).all()}

        new_jobs = [
            Job(id=row['id'], name=row['name'])
            for _, row in cleaned_df.iterrows()
            if row['id'] not in existing_ids
        ]

        try:
            self.session.bulk_save_objects(new_jobs)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

        return [job.name for job in new_jobs]

    def close(self):
        self.session.close()