from sqlalchemy import Integer, String
from utils.extensions import db

class Professor(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)
    nick_name = db.Column(String(100), nullable=True)
    age = db.Column(Integer, nullable=False)
    belt = db.Column(String, nullable=False)
    stripes = db.Column(Integer, nullable=False)
    black_belt_under_who = db.Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Professor {self.name}>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "nick_name": self.nick_name,
            "age": self.age,
            "belt": self.belt,
            "stripes": self.stripes,
            "black_belt_under_who": self.black_belt_under_who
        }