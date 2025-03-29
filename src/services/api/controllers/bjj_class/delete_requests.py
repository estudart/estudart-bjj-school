from flask import make_response

from services.api.models.bjj_class import BJJClass
from utils.extensions import db, logger



def delete_class_by_id(id):
    try:
        search_delete_class = (
            db.session.query(BJJClass)
            .filter(BJJClass.id==id)
            .first()
        )
        if not search_delete_class:
            return make_response(
                {
                    "message": "class was not found in database"
                }, 404)
        
        db.session.delete(search_delete_class)
        db.session.commit()
        return make_response(
            {
                "message": f"class with id: {id} was deleted"
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not delete class, reason: {err}")
        return make_response(
            {
                "message": f"Could not delete class, reason: {err}"
            }, 500)