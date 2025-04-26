from sqlalchemy.orm import Session
from models.DepartmentModel import Department
from models.HiredEmployeesModel import HiredEmployee
from models.JobModel import Job

class DepartmentService:
    def __init__(self, engine):
        self.engine = engine
        self.session = Session(bind=self.engine)

    def get_all_departments(self):
        return self.session.query(Department).all()

    def get_department_by_id(self, dept_id: int):
        return self.session.query(Department).filter_by(id=dept_id).first()

    def create_department(self, name: str):
        new_dept = Department(name=name)
        self.session.add(new_dept)
        self.session.commit()
        return new_dept

    def update_department(self, dept_id: int, new_name: str):
        dept = self.get_department_by_id(dept_id)
        if dept:
            dept.name = new_name
            self.session.commit()
        return dept

    def delete_department(self, dept_id: int):
        dept = self.get_department_by_id(dept_id)
        if dept:
            self.session.delete(dept)
            self.session.commit()
        return dept

    def create_departments_bulk(self, departments_df):
        if departments_df.isnull().values.any() or (departments_df['name'] == '').any():
            raise ValueError("Los datos no pueden contener valores nulos o vacíos.")

        existing_ids = {
            dept.id for dept in self.session.query(Department.id).all()
        }

        new_departments = []
        for _, row in departments_df.iterrows():
            if row['id'] not in existing_ids:
                new_departments.append(Department(id=row['id'], name=row['name']))

        try:
            self.session.bulk_save_objects(new_departments)
            self.session.commit()
            return [dept.name for dept in new_departments]
        except Exception as e:
            self.session.rollback()
            raise e

    def close(self):
        self.session.close()
