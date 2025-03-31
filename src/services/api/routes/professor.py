from flask import Blueprint, request as req

from utils.extensions import logger
from services.api.controllers.professor import (
    post_professor, 
    get_professor_by_name, 
    get_professor_by_id,
    delete_professor_by_name,
    delete_professor_by_id,
    update_professor_data
)


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
       default: 'Ricardo Nieira'
       required: True
       description: Name of the Professor
     - name: nick_name
       in: query
       type: string
       default: 'Ricardinho'
       required: False
       description: Nickname of the Professor
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
     - name: gym_id
       in: query
       type: integer
       default: 2
       required: True
       description: Gym in which professor gives classes
    
    responses:
        200:
            description: New Professor was registered
            
    """
    try:
        data = req.json()
    except:
        data = req.args.to_dict()
    logger.info(f"Received data request from user: {data}")

    return post_professor(data)

@bp_professor.route("/get-professor-by-name/<name>")
def read_professor_by_name(name):
    """
    Register Professor
    ---
    tags:
     - Professor

    parameters:
     - name: name
       in: path
       type: string
       default: 'Ricardo Nieira'
       required: True
       description: Name of the Professor
    
    responses:
        200:
            description: New Professor was registered
            
    """
    return get_professor_by_name(name)


@bp_professor.route("/get-professor-by-id/<id>", methods=["GET"])
def read_professor_by_id(id):
    """
    Register Professor
    ---
    tags:
     - Professor

    parameters:
     - name: id
       in: path
       type: integer
       default: 2
       required: True
       description: Id of the Professor
    
    responses:
        200:
            description: New Professor was registered
            
    """
    return get_professor_by_id(id)


@bp_professor.route("/delete-professor-by-name/<name>", methods=["DELETE"])
def delete_professor_given_name(name):
    """
    Delete professor
    ---
    tags:
     - Professor

    parameters:
     - name: name
       in: path
       type: string
       default: 'Ricardo Nieira'
       required: True
       description: name of the professor
    
    responses:
        200:
            description: professor was deleted
            
    """
    return delete_professor_by_name(name)


@bp_professor.route("/delete-professor-by-id/<id>", methods=["DELETE"])
def delete_professor_given_id(id):
    """
    Delete professor
    ---
    tags:
     - Professor

    parameters:
     - name: id
       in: path
       type: integer
       default: 1
       required: True
       description: Id of the professor
    
    responses:
        200:
            description: professor was deleted
            
    """
    return delete_professor_by_id(id)


@bp_professor.route("/update-professor/<id>", methods=["PUT"])
def put_professor(id):
    """
    Update Professor
    ---
    tags:
     - Professor

    parameters:
     - name: id
       in: path
       type: integer
       default: 1
       required: True
       description: Id of the Professor
     - name: name
       in: query
       type: string
       default: 'Ricardo Nieira'
       required: False
       description: Name of the Professor
     - name: nick_name
       in: query
       type: string
       default: 'Ricardinho'
       required: False
       description: Nickname of the Professor
     - name: age
       in: query
       type: integer
       default: 38
       required: False
       description: Age of the Professor
     - name: belt
       in: query
       type: string
       default: 'Black'
       required: False
       description: Belt of the Professor
     - name: stripes
       in: query
       type: integer
       default: 2
       required: False
       description: Stripes in the belt
     - name: black_belt_under_who
       in: query
       type: string
       default: 'Murilo Bustamante'
       required: False
       description: Who gave the professor the black belt
     - name: gym_id
       in: query
       type: integer
       default: 2
       required: False
       description: Gym in which professor gives classes
    
    responses:
        200:
            description: professor was updated
            
    """
    try:
        data = req.json()
    except:
        data = req.args.to_dict()
    logger.info(f"Received data request from user: {data}")

    return update_professor_data(id, data)