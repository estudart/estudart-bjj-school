import logging

from flask import make_response

from utils.extensions import db
from services.api.models.professor import Professor


def delete_professor_by_id(id):
    try:
        search_delete_professor = (
            db.session.query(Professor)
            .filter(Professor.id==id)
            .first()
        )
        if not search_delete_professor:
            return make_response(
                {
                    "message": "professor was not found in database"
                }, 404)
        
        db.session.delete(search_delete_professor)
        db.session.commit()
        return make_response(
            {
                "message": f"professor with id: {id} was deleted"
            }, 200)
    
    except Exception as err:
        logging.error(f"Could not delete professor, reason: {err}")
        return make_response(
            {
                "message": f"Could not delete professor, reason: {err}"
            }, 500)


def delete_professor_by_name(name):
    try:
        search_delete_professor = (
            db.session.query(Professor)
            .filter(Professor.name==name)
            .first()
        )
        if not search_delete_professor:
            return make_response(
                {
                    "message": "professor was not found in database"
                }, 404)
        
        db.session.delete(search_delete_professor)
        db.session.commit()
        return make_response(
            {
                "message": f"professor with name: {name} was deleted"
            }, 200)
    
    except Exception as err:
        logging.error(f"Could not delete professor, reason: {err}")
        return make_response(
            {
                "message": f"Could not delete professor, reason: {err}"
            }, 500)