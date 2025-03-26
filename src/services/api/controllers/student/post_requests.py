import logging

from flask import make_response

from services.api.models.student import Student
from utils.extensions import db

def post_student(data):
    try:
        new_student = Student(
            name=data["name"],
            age=data["age"],
            belt=data["belt"],
            stripes=data["stripes"]
            )
        db.session.add(new_student)
        db.session.commit()
        return make_response(
            {"message": "Successfully added new student"}, 
            200)
    except ValueError as err:
        return make_response(
            {"message": f"Age must be an integer number"}, 
            400)
    except Exception as err:
        logging.error(err)
        return make_response(
            {"message": f"Failed to add new student: {err}"}, 
            400)