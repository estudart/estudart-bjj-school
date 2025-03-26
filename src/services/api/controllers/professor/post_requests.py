import logging

from flask import make_response

from services.api.models.professor import Professor
from utils.extensions import db

def post_professor(data):
    try:
        new_professor = Professor(**data)
        db.session.add(new_professor)
        db.session.commit()
        return make_response(
            {"message": "Successfully added new professor"}, 
            200)
    except ValueError as err:
        return make_response(
            {"message": f"Age must be an integer number"}, 
            400)
    except Exception as err:
        logging.error(err)
        return make_response(
            {"message": f"Failed to add new professor: {err}"}, 
            400)