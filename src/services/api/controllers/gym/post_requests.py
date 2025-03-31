from flask import make_response

from services.api.models.gym import Gym
from utils.extensions import db, logger



def post_gym(data):
    try:
        new_gym = Gym(**data)
        db.session.add(new_gym)
        db.session.commit()
        return make_response(
            {"message": "Successfully added new gym"}, 
            200)
    except ValueError as err:
        return make_response(
            {"message": f"Age must be an integer number"}, 
            400)
    except Exception as err:
        logger.error(err)
        return make_response(
            {"message": f"Failed to add new gym: {err}"}, 
            500)