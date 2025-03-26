from sqlalchemy import Integer, String
from utils.extensions import db

class Professor(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)
    age = db.Column(Integer, nullable=False)
    belt = db.Column(String, nullable=False)
    stripes = db.Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Professor {self.name}>"