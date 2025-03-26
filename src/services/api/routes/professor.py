import logging

from flask import Blueprint, request as req

from services.api.controllers.professor import post_professor


bp_professor = Blueprint("professor",
                         __name__)


@bp_professor.route("/register-professor", methods=["POST"])
def register_professor():
    """
    Register Professor
    ---
    tags:
     - Professor

    parameters:
     - name: name
       in: query
       type: string
       default: 'Ricardo'
       required: True
       description: Name of the Professor
     - name: age
       in: query
       type: integer
       default: 38
       required: True
       description: Age of the Professor
     - name: belt
       in: query
       type: string
       default: 'Black'
       required: True
       description: Belt of the Professor
     - name: stripes
       in: query
       type: integer
       default: 2
       required: True
       description: Stripes in the belt
     - name: black_belt_under_who
       in: query
       type: string
       default: 'Murilo Bustamante'
       required: True
       description: Who gave the professor the black belt
    
    responses:
        200:
            description: New Professor was registered
            
    """
    try:
        data = req.json()
    except:
        data = req.args.to_dict()
    logging.info(f"Received data request from user: {data}")

    return post_professor(data)