import logging

from flask import Blueprint, request as req

from services.api.controllers.bjj_class import (
    get_class_by_id,
    post_class,
    delete_class_by_id
)



bp_class = Blueprint("class",
                     __name__)


@bp_class.route("/register-class", methods=["POST"])
def register_class():
    """
    Register Class
    ---
    tags:
     - Class

    parameters:
     - name: date
       in: query
       type: string
       default: '2025-02-27T11:00:00'
       required: True
       description: Date of the class
     - name: professor_id
       in: query
       type: integer
       default: 1
       required: True
       description: Id of the Professor that gave the class
    
    responses:
        200:
            description: New Class was registered
            
    """
    try:
        data = req.json()
    except Exception as err:
        data = req.args.to_dict()
    logging.info(f"Received class request from user: {data}")

    return post_class(data)