from flask import make_response

from services.api.models.student import Student
from services.celery.tasks import send_welcome_message_on_chat
from utils.extensions import db, logger



def post_student(data):
    try: 
        new_student = Student(**data)
        db.session.add(new_student)
        db.session.commit()
        task = send_welcome_message_on_chat.delay(data["name"])
        logger.debug(f"{task.id}")
        return make_response(
            {"message": "Successfully added new student"}, 
            200)
    except ValueError as err:
        return make_response(
            {"message": f"Age must be an integer number"}, 
            400)
    except Exception as err:
        logger.error(err)
        return make_response(
            {"message": f"Failed to add new student: {err}"}, 
            500)