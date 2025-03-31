from flask import make_response

from utils.extensions import db, logger
from services.api.models.gym import Gym



def delete_gym_by_id(id):
    try:
        search_delete_gym = (
            db.session.query(Gym)
            .filter(Gym.id==id)
            .first()
        )
        if not search_delete_gym:
            return make_response(
                {
                    "message": "gym was not found in database"
                }, 404)
        
        db.session.delete(search_delete_gym)
        db.session.commit()
        return make_response(
            {
                "message": f"gym with id: {id} was deleted"
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not delete gym, reason: {err}")
        return make_response(
            {
                "message": f"Could not delete gym, reason: {err}"
            }, 500)


def delete_gym_by_name(name):
    try:
        search_delete_gym = (
            db.session.query(Gym)
            .filter(Gym.name==name)
            .first()
        )
        if not search_delete_gym:
            return make_response(
                {
                    "message": "gym was not found in database"
                }, 404)
        
        db.session.delete(search_delete_gym)
        db.session.commit()
        return make_response(
            {
                "message": f"gym with name: {name} was deleted"
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not delete gym, reason: {err}")
        return make_response(
            {
                "message": f"Could not delete gym, reason: {err}"
            }, 500)