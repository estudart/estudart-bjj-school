from flask import make_response

from utils.extensions import db, logger
from services.api.models.gym import Gym



def update_gym_data(id, data):
    try:
        update_gym = (
            db.session.query(Gym)
            .filter(Gym.id==id)
            .update({**data})
        )
        if not update_gym:
            return make_response(
                {
                    "message": "gym is not registered"
                }, 404)
        
        db.session.commit()
        return make_response(
            {
                "message": f"gym with id: {id} was updated"
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not find gym, reason: {err}")
        return make_response(
            {
                "message": "Could not find gym"
            }, 500)