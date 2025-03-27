import logging

from flask import make_response, jsonify

from utils.extensions import db
from utils.helpers import dict_helper
from services.api.models.professor import Professor


def get_professor_by_name(name):
    try:
        search_professor = db.session.query(Professor).filter(Professor.name==name).first()
        logging.info(search_professor.to_dict())
        return make_response(
            {
                "message": "Professor found",
                "data": search_professor.to_dict()
            }
            ,200)
    except Exception as err:
        return make_response(
            {"Could not find professor": f"{err}"}
            ,500)
