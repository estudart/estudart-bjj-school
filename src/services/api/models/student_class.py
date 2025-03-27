from sqlalchemy import Integer, String, ForeignKey

from utils.extensions import db



class StudentClasses(db.Model):
    __tablename__ = "students_classes"

    student_id = db.Column(Integer, ForeignKey("students.id"), primary_key=True)
    class_id = db.Column(Integer, ForeignKey("classes.id"), primary_key=True)
    notes = db.Column(String, nullable=True)