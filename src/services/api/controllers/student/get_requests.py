import logging

from flask import make_response

from utils.extensions import db
from services.api.models.student import Student

def get_student_by_name(name):
    try:
        search_student = (
            db.session.query(Student)
            .filter(Student.name==name)
            .first()
        )
        if not search_student:
            return make_response(
                {
                    "message": "Student is not registered"
                }, 404)
        
        dict_student = search_student.to_dict()
        return make_response(
            {
                "message": "Student was found",
                "data": dict_student
            }, 200)
    except Exception as err:
        logging.error(f"Could not find student, reason: {err}")
        return make_response(
            {
                "message": "Could not find student"
            }, 500)


def get_student_by_id(id):
    try:
        search_student = (
            db.session.query(Student)
            .filter(Student.id==id)
            .first()
        )
        if not search_student:
            return make_response(
                {
                    "message": "Student is not registered"
                }, 404)
        
        dict_student = search_student.to_dict()
        return make_response(
            {
                "message": "Student was found",
                "data": dict_student
            }, 200)
    except Exception as err:
        logging.error(f"Could not find student, reason: {err}")
        return make_response(
            {
                "message": "Could not find student"
            }, 500)