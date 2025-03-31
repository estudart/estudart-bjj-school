from datetime import datetime

from flask import make_response

from utils.extensions import db, logger
from services.api.models.bjj_class import BJJClass



def update_bjj_class_data(id, data):
    try:
        data["date"] = datetime.strptime(
            data["date"],
            '%Y-%m-%dT%H:%M:%S')
        update_bjj_class = (
            db.session.query(BJJClass)
            .filter(BJJClass.id==id)
            .update({**data})
        )
        if not update_bjj_class:
            return make_response(
                {
                    "message": "bjj_class is not registered"
                }, 404)
        
        db.session.commit()
        return make_response(
            {
                "message": f"bjj_class with id: {id} was updated"
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not find bjj_class, reason: {err}")
        return make_response(
            {
                "message": "Could not find bjj_class"
            }, 500)