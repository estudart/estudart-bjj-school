from datetime import datetime

from sqlalchemy import (
    String, 
    Integer, 
    DateTime, 
    Boolean,
    DECIMAL
)

from utils.extensions import db



class Gym(db.Model):
    __tablename__ = "gyms"

    # Basic info
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)
    address = db.Column(String(100), nullable=False)
    email = db.Column(String(100), nullable=True)
    phone_number = db.Column(String(20), nullable=True)

    # Details
    head_coach = db.Column(String(100), nullable=False)
    description = db.Column(String(1000), nullable=True)
    created_at = db.Column(DateTime, default=datetime.now,
                           onupdate=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, 
                           onupdate=datetime.now)

    # Operacional
    membership_fee = db.Column(DECIMAL(10, 2), nullable=True)
    gi_classes = db.Column(Boolean, nullable=False)
    no_gi_classes = db.Column(Boolean, nullable=False)
    kids_classes = db.Column(Boolean, nullable=False)
    open_mat = db.Column(Boolean, nullable=False)

    # Facilities
    mat_space_size = db.Column(Integer, nullable=False)
    showers_available = db.Column(Boolean, nullable=False)
    parking_available = db.Column(Boolean, nullable=False)

    # Relantionship
    classes = db.relationship("BJJClass", back_populates="gyms")
    professors = db.relationship("Professor", back_populates="gyms")
    students = db.relationship("Students", back_populates="gyms")

    def __repr__(self):
        return f"<Gym {self.name}"
    
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }