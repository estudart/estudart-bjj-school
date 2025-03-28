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

    classes = db.relationship(
        "BJJClass", 
        secondary="students_classes", 
        back_populates="students"
    )

    def __repr__(self):
        return f"<Student {self.name}>"
    
    def to_dict(self):
        return {
            column.name: getattr(self, column.name) 
            for column in self.__table__.columns
        }
