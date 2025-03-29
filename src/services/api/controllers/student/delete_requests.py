from flask import make_response

from utils.extensions import db, logger
from services.api.models.student import Student



def delete_student_by_id(id):
    try:
        search_delete_student = (
            db.session.query(Student)
            .filter(Student.id==id)
            .first()
        )
        if not search_delete_student:
            return make_response(
                {
                    "message": "Student was not found in database"
                }, 404)
        
        db.session.delete(search_delete_student)
        db.session.commit()
        logger.info(f"Student with id: {id} was deleted")
        return make_response(
            {
                "message": f"Student with id: {id} was deleted"
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not delete student, reason: {err}")
        return make_response(
            {
                "message": f"Could not delete student, reason: {err}"
            }, 500)


def delete_student_by_name(name):
    try:
        search_delete_student = (
            db.session.query(Student)
            .filter(Student.name==name)
            .first()
        )
        if not search_delete_student:
            return make_response(
                {
                    "message": "Student was not found in database"
                }, 404)
        
        db.session.delete(search_delete_student)
        db.session.commit()
        return make_response(
            {
                "message": f"Student with name: {name} was deleted"
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not delete student, reason: {err}")
        return make_response(
            {
                "message": f"Could not delete student, reason: {err}"
            }, 500)
