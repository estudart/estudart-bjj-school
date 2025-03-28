from sqlalchemy import Integer, DateTime, ForeignKey

from utils.extensions import db



class BJJClass(db.Model):
    __tablename__ = "classes"

    id = db.Column(Integer, primary_key=True)
    date = db.Column(DateTime, nullable=False)
    professor_id = db.Column(Integer, ForeignKey("professors.id"), 
                             nullable=False)

    professors = db.relationship("Professor", 
                                back_populates="classes")
    students = db.relationship("Student", 
                               secondary="students_classes", 
                               back_populates="classes")

    def __repr__(self):
        return f"<Class {self.id} - {self.date}>"
    
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }