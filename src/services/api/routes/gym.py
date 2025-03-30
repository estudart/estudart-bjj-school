from flask import Blueprint, request as req

from utils.extensions import logger
from services.api.controllers.gym import (
    post_gym, 
    get_gym_by_name, 
    get_gym_by_id,
    delete_gym_by_name,
    delete_gym_by_id,
    update_gym_data
)

bp_gym = Blueprint("gym", __name__)

@bp_gym.route("/register-gym", methods=["POST"])
def register_gym():
    """
    Register Gym
    ---
    tags:
     - Gym

    parameters:
     - name: name
       in: query
       type: string
       default: 'BJJ Academy'
       required: True
       description: Name of the Gym
     - name: address
       in: query
       type: string
       default: '123 Main St'
       required: True
       description: Address of the Gym
     - name: email
       in: query
       type: string
       default: 'contact@bjjacademy.com'
       required: False
       description: Email of the Gym
     - name: phone_number
       in: query
       type: string
       default: '+1234567890'
       required: False
       description: Phone number of the Gym
     - name: head_coach
       in: query
       type: string
       default: 'Ricardo Nieira'
       required: True
       description: Name of the Head Coach
     - name: description
       in: query
       type: string
       default: 'A top-level gym for Brazilian Jiu-Jitsu'
       required: False
       description: A short description of the Gym
     - name: membership_fee
       in: query
       type: number
       default: 100.00
       required: False
       description: Membership fee of the Gym
     - name: gi_classes
       in: query
       type: boolean
       default: true
       required: True
       description: Does the Gym offer Gi classes?
     - name: no_gi_classes
       in: query
       type: boolean
       default: true
       required: True
       description: Does the Gym offer No-Gi classes?
     - name: kids_classes
       in: query
       type: boolean
       default: true
       required: True
       description: Does the Gym offer Kids' classes?
     - name: open_mat
       in: query
       type: boolean
       default: true
       required: True
       description: Does the Gym have Open Mat sessions?
     - name: mat_space_size
       in: query
       type: integer
       default: 200
       required: True
       description: The size of the mat space in square meters
     - name: showers_available
       in: query
       type: boolean
       default: true
       required: True
       description: Does the Gym have showers available?
     - name: parking_available
       in: query
       type: boolean
       default: true
       required: True
       description: Does the Gym have parking available?
    
    responses:
        200:
            description: New Gym was registered
    """
    try:
        data = req.json()
    except:
        data = req.args.to_dict()
    logger.info(f"Received data request from user: {data}")

    return post_gym(data)

@bp_gym.route("/get-gym-by-name/<name>")
def read_gym_by_name(name):
    """
    Get Gym by Name
    ---
    tags:
     - Gym

    parameters:
     - name: name
       in: path
       type: string
       default: 'BJJ Academy'
       required: True
       description: Name of the Gym
    
    responses:
        200:
            description: Gym data retrieved successfully
    """
    return get_gym_by_name(name)

@bp_gym.route("/get-gym-by-id/<id>", methods=["GET"])
def read_gym_by_id(id):
    """
    Get Gym by ID
    ---
    tags:
     - Gym

    parameters:
     - name: id
       in: path
       type: integer
       default: 1
       required: True
       description: ID of the Gym
    
    responses:
        200:
            description: Gym data retrieved successfully
    """
    return get_gym_by_id(id)

@bp_gym.route("/delete-gym-by-name/<name>", methods=["DELETE"])
def delete_gym_given_name(name):
    """
    Delete Gym by Name
    ---
    tags:
     - Gym

    parameters:
     - name: name
       in: path
       type: string
       default: 'BJJ Academy'
       required: True
       description: Name of the Gym
    
    responses:
        200:
            description: Gym was deleted
    """
    return delete_gym_by_name(name)

@bp_gym.route("/delete-gym-by-id/<id>", methods=["DELETE"])
def delete_gym_given_id(id):
    """
    Delete Gym by ID
    ---
    tags:
     - Gym

    parameters:
     - name: id
       in: path
       type: integer
       default: 1
       required: True
       description: ID of the Gym
    
    responses:
        200:
            description: Gym was deleted
    """
    return delete_gym_by_id(id)

@bp_gym.route("/update-gym/<id>", methods=["PUT"])
def put_gym(id):
    """
    Update Gym
    ---
    tags:
     - Gym

    parameters:
     - name: id
       in: path
       type: integer
       default: 1
       required: True
       description: ID of the Gym
     - name: name
       in: query
       type: string
       default: 'BJJ Academy'
       required: False
       description: Name of the Gym
     - name: address
       in: query
       type: string
       default: '123 Main St'
       required: False
       description: Address of the Gym
     - name: email
       in: query
       type: string
       default: 'contact@bjjacademy.com'
       required: False
       description: Email of the Gym
     - name: phone_number
       in: query
       type: string
       default: '+1234567890'
       required: False
       description: Phone number of the Gym
     - name: head_coach
       in: query
       type: string
       default: 'Ricardo Nieira'
       required: False
       description: Name of the Head Coach
     - name: description
       in: query
       type: string
       default: 'A top-level gym for Brazilian Jiu-Jitsu'
       required: False
       description: A short description of the Gym
     - name: membership_fee
       in: query
       type: number
       default: 100.00
       required: False
       description: Membership fee of the Gym
     - name: gi_classes
       in: query
       type: boolean
       default: true
       required: False
       description: Does the Gym offer Gi classes?
     - name: no_gi_classes
       in: query
       type: boolean
       default: true
       required: False
       description: Does the Gym offer No-Gi classes?
     - name: kids_classes
       in: query
       type: boolean
       default: true
       required: False
       description: Does the Gym offer Kids' classes?
     - name: open_mat
       in: query
       type: boolean
       default: true
       required: False
       description: Does the Gym have Open Mat sessions?
     - name: mat_space_size
       in: query
       type: integer
       default: 200
       required: False
       description: The size of the mat space in square meters
     - name: showers_available
       in: query
       type: boolean
       default: true
       required: False
       description: Does the Gym have showers available?
     - name: parking_available
       in: query
       type: boolean
       default: true
       required: False
       description: Does the Gym have parking available?
    
    responses:
        200:
            description: Gym was updated
    """
    try:
        data = req.json()
    except:
        data = req.args.to_dict()
    logger.info(f"Received data request from user: {data}")

    return update_gym_data(id, data)
