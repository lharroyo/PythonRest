from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.DepartmentModel import Department

DATABASE_URL = "sqlite:///employees.db"  
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class DepartmentService:
    def __init__(self):
        self.session = Session()

    def get_all_departments(self):
        """Obtiene todos los departamentos."""
        return self.session.query(Department).all()

    def get_department_by_id(self, department_id):
        """Obtiene un departamento por su ID."""
        return self.session.query(Department).filter(Department.id == department_id).first()

    def add_department(self, name):
        """Agrega un nuevo departamento."""
        new_department = Department(name=name)
        self.session.add(new_department)
        self.session.commit()
        return new_department

    def close(self):
        """Cierra la sesión."""
        self.session.close()