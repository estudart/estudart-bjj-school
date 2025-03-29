import logging

from flask import make_response

from services.api.models.student import Student
from utils.extensions import db, telegram_adapter



def post_student(data):
    try:
        new_student = Student(**data)
        db.session.add(new_student)
        db.session.commit()
        telegram_adapter.send_message(
            f"New student registered: {data}"
        )
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
            500)