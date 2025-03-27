import logging
from datetime import datetime

from flask import make_response

from services.api.models.bjj_class import BJJClass
from utils.extensions import db



def post_class(data):
    try:
        data["date"] = datetime.strptime(
            data["date"],
            '%Y-%m-%dT%H:%M:%S')
        new_class = BJJClass(**data)
        db.session.add(new_class)
        db.session.commit()
        return make_response(
            {"message": "Successfully added new class"}, 
            200)
    except ValueError as err:
        return make_response(
            {"message": f"Inavlid json: {err}"}, 
            400)
    except Exception as err:
        logging.error(err)
        return make_response(
            {"message": f"Failed to add new class: {err}"}, 
            500)