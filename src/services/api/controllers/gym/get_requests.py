from flask import make_response

from utils.extensions import db, logger
from services.api.models.gym import Gym



def get_gym_by_name(name):
    try:
        search_gym = db.session.query(Gym).filter(Gym.name==name).first()
        
        if not search_gym:
            return make_response(
                {
                    "message": "gym was not found in database"
                }, 404)
        
        dict_gym = search_gym.to_dict()
        logger.info(
            f"gym was found, {dict_gym}")
        return make_response(
            {
                "message": "gym found",
                "data": search_gym.to_dict()
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not find gym, reason: {err}")
        return make_response(
            {
                "message": f"Could not find gym, reason: {err}"
            }, 500)
    

def get_gym_by_id(id):
    try:
        search_gym = db.session.query(Gym).filter(Gym.id==id).first()

        if not search_gym:
            return make_response(
                {
                    "message": "gym was not found in database"
                }, 404)
        
        dict_gym = search_gym.to_dict()
        logger.info(
            f"gym was found, {dict_gym}")
        return make_response(
            {
                "message": "gym found",
                "data": dict_gym
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not find gym, reason: {err}")
        return make_response(
            {
                "message": f"Could not find gym, reason: {err}"
            }, 500
        )