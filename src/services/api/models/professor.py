from sqlalchemy import Integer, String

from utils.extensions import db



class Professor(db.Model):
    __tablename__ = "professors"

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
            column.name: getattr(self, column.name) 
            for column in self.__table__.columns
        }