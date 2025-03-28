import logging

from flask import Blueprint, request as req

from services.api.controllers.bjj_class import (
    get_class_by_id,
    get_students_by_class_id,
    get_all_classes,
    post_class,
    add_student_to_class,
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
     - name: class_id
       in: query
       type: integer
       default: 1
       required: True
       description: Id of the class that gave the class
    
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


@bp_class.route("/add-student-to-class", methods=["POST"])
def insert_student_to_class():
    """
    Add Student to a class
    ---
    tags:
     - Class

    parameters:
     - name: class_id
       in: query
       type: integer
       default: 1
       required: True
       description: Id of the class
     - name: student_id
       in: query
       type: integer
       default: 1
       required: True
       description: Id of the Student
     - name: notes
       in: query
       type: string
       default: 'Erico performed really well in this class'
       required: False
       description: Notes about the class
    
    responses:
        200:
            description: Student was added to class
            
    """
    try:
        data = req.json()
    except Exception as err:
        data = req.args.to_dict()
    logging.info(f"Received class request from user: {data}")

    return add_student_to_class(data)


@bp_class.route("/get-class-by-id/<id>", methods=["GET"])
def read_class_by_id(id):
    """
    Get Class by id
    ---
    tags:
     - Class

    parameters:
     - name: id
       in: path
       type: integer
       default: 2
       required: True
       description: Id of the Class
    
    responses:
        200:
            description: Class was found
            
    """
    return get_class_by_id(id)


@bp_class.route("/get-all-classes", methods=["GET"])
def read_all_class():
    """
    Get all classes
    ---
    tags:
     - Class
    
    responses:
        200:
            description: Classes were found
            
    """
    return get_all_classes()


@bp_class.route("/get-students-by-class/<id>", methods=["GET"])
def find_all_students_on_class(id):
    """
    Get students by class id
    ---
    tags:
     - Class

    parameters:
     - name: id
       in: path
       type: integer
       default: 1
       required: True
       description: Id of the Class
    
    responses:
        200:
            description: students were found
            
    """
    return get_students_by_class_id(id)


@bp_class.route("/delete-class-by-id/<id>", methods=["DELETE"])
def delete_class_given_id(id):
    """
    Delete class
    ---
    tags:
     - Class

    parameters:
     - name: id
       in: path
       type: integer
       default: 1
       required: True
       description: Id of the class
    
    responses:
        200:
            description: class was deleted
            
    """
    return delete_class_by_id(id)
        