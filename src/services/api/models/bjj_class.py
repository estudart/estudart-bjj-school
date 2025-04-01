from sqlalchemy import Integer, DateTime, ForeignKey, Boolean

from utils.extensions import db



class BJJClass(db.Model):
    __tablename__ = "classes"

    id = db.Column(Integer, primary_key=True)
    date = db.Column(DateTime, nullable=False)

    class_reminder_was_sent = db.Column(Boolean, default=False)

    # Relantionship
    professor_id = db.Column(Integer, ForeignKey("professors.id"), 
                             nullable=False)
    gym_id = db.Column(Integer, ForeignKey("gyms.id"),
                       nullable=False)
    
    gym = db.relationship("Gym",
                           back_populates="classes")
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