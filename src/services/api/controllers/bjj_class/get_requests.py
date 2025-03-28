import logging

from flask import make_response

from services.api.models.bjj_class import BJJClass
from services.api.models.student_class import StudentClasses
from services.api.models.student import Student
from utils.extensions import db



def get_class_by_id(id):
    try:
        search_class = (
            db.session.query(BJJClass)
            .filter(BJJClass.id==id)
            .first()
        )
        if not search_class:
            return make_response(
                {
                    "message": "class was not found in database"
                }, 404)
        
        dict_class = search_class.to_dict()
        logging.info(
            f"class was found, {dict_class}")
        return make_response(
            {
                "message": "class found",
                "data": search_class.to_dict()
            }, 200)
    
    except Exception as err:
        logging.error(f"Could not find class, reason: {err}")
        return make_response(
            {
                "message": f"Could not find class, reason: {err}"
            }, 500)        


def get_all_classes():
    try:
        search_classes = (
            db.session.query(BJJClass)
            .all()
        )
        if not search_classes:
            return make_response(
                {
                    "message": "classes were not found in database"
                }, 404)
        
        dict_class = [search_class.to_dict() for search_class in search_classes]
        logging.info(
            f"class was found, {dict_class}")
        return make_response(
            {
                "message": "class found",
                "data": dict_class
            }, 200)
    
    except Exception as err:
        logging.error(f"Could not find classes, reason: {err}")
        return make_response(
            {
                "message": f"Could not find classes, reason: {err}"
            }, 500) 


def get_students_by_class_id(class_id):
    try:
        search_students = (
            db.session.query(Student)
            .join(StudentClasses)
            .filter(StudentClasses.class_id==class_id)
            .all()
        )
        if not search_students:
            return make_response(
                {
                    "message": "class was not found in database"
                }, 404)
        
        dict_students = [search_student.to_dict() for search_student in search_students]
        logging.info(
            f"students were found, {dict_students}")
        return make_response(
            {
                "message": "students were found",
                "data": dict_students
            }, 200)
    
    except Exception as err:
        logging.error(f"Could not find class, reason: {err}")
        return make_response(
            {
                "message": f"Could not find class, reason: {err}"
            }, 500)
