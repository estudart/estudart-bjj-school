from flask import make_response

from utils.extensions import db, logger
from services.api.models.student import Student



def update_student_data(id, data):
    try:
        update_student = (
            db.session.query(Student)
            .filter(Student.id==id)
            .update({**data})
        )
        if not update_student:
            return make_response(
                {
                    "message": "Student is not registered"
                }, 404)
        
        db.session.commit()
        return make_response(
            {
                "message": f"Student with id: {id} was updated"
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not find student, reason: {err}")
        return make_response(
            {
                "message": "Could not find student"
            }, 500)