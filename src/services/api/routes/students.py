import logging

from flask import Blueprint, request as req

from services.api.controllers.student import (
    post_student, 
    get_student_by_name,
    get_student_by_id
)

bp_student = Blueprint("student", 
                       __name__)

@bp_student.route("/register-student", methods=["POST"])
def register_student():
    """
    Register Student
    ---
    tags:
     - Student

    parameters:
     - name: name
       in: query
       type: string
       default: 'Erico'
       required: True
       description: Name of the student
     - name: age
       in: query
       type: integer
       default: 27
       required: True
       description: Age of the student
     - name: belt
       in: query
       type: string
       default: 'Purple'
       required: True
       description: Belt of the student
     - name: stripes
       in: query
       type: integer
       default: 2
       required: True
       description: Stripes in the belt
    
    responses:
        200:
            description: New student was registered
            
    """
    try:
        data = req.json()
    except:
        data = req.args.to_dict()
    logging.info(f"Received data request from user: {data}")

    return post_student(data)


@bp_student.route("/get-student-by-name/<name>", methods=["GET"])
def read_student_by_name(name):
    """
    Register Student
    ---
    tags:
     - Student

    parameters:
     - name: name
       in: path
       type: string
       default: 'Erico'
       required: True
       description: Name of the student
    
    responses:
        200:
            description: New student was registered
            
    """
    return get_student_by_name(name)


@bp_student.route("/get-student-by-id/<id>", methods=["GET"])
def read_student_by_id(id):
    """
    Register Student
    ---
    tags:
     - Student

    parameters:
     - name: id
       in: path
       type: integer
       default: 1
       required: True
       description: Id of the student
    
    responses:
        200:
            description: New student was registered
            
    """
    return get_student_by_id(id)