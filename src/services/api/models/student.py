from sqlalchemy import Integer, String
from utils.extensions import db 

class Student(db.Model):  
    __tablename__ = "students" 

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)
    nick_name = db.Column(String(100), nullable=True)
    age = db.Column(Integer, nullable=False)
    belt = db.Column(String(30), nullable=False)
    stripes = db.Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Student {self.name}>"
