from flask import make_response

from utils.extensions import db, logger
from services.api.models.professor import Professor



def get_professor_by_name(name):
    try:
        search_professor = db.session.query(Professor).filter(Professor.name==name).first()
        
        if not search_professor:
            return make_response(
                {
                    "message": "Professor was not found in database"
                }, 404)
        
        dict_professor = search_professor.to_dict()
        logger.info(
            f"Professor was found, {dict_professor}")
        return make_response(
            {
                "message": "Professor found",
                "data": search_professor.to_dict()
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not find professor, reason: {err}")
        return make_response(
            {
                "message": f"Could not find professor, reason: {err}"
            }, 500)
    

def get_professor_by_id(id):
    try:
        search_professor = db.session.query(Professor).filter(Professor.id==id).first()

        if not search_professor:
            return make_response(
                {
                    "message": "Professor was not found in database"
                }, 404)
        
        dict_professor = search_professor.to_dict()
        logger.info(
            f"Professor was found, {dict_professor}")
        return make_response(
            {
                "message": "Professor found",
                "data": dict_professor
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not find professor, reason: {err}")
        return make_response(
            {
                "message": f"Could not find professor, reason: {err}"
            }, 500
        )