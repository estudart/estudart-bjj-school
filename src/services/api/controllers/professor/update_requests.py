from flask import make_response

from utils.extensions import db, logger
from services.api.models.professor import Professor



def update_professor_data(id, data):
    try:
        update_professor = (
            db.session.query(Professor)
            .filter(Professor.id==id)
            .update({**data})
        )
        if not update_professor:
            return make_response(
                {
                    "message": "professor is not registered"
                }, 404)
        
        db.session.commit()
        return make_response(
            {
                "message": f"professor with id: {id} was updated"
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not find professor, reason: {err}")
        return make_response(
            {
                "message": "Could not find professor"
            }, 500)