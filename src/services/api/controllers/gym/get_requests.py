from flask import make_response

from utils.extensions import db, logger
from services.api.models.gym import Gym
from services.api.models.student import Student
from services.api.models.professor import Professor



def get_gym_by_name(name):
    try:
        search_gym = db.session.query(Gym).filter(Gym.name==name).first()
        
        if not search_gym:
            return make_response(
                {
                    "message": "gym was not found in database"
                }, 404)
        
        dict_gym = search_gym.to_dict()
        logger.info(
            f"gym was found, {dict_gym}")
        return make_response(
            {
                "message": "gym found",
                "data": search_gym.to_dict()
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not find gym, reason: {err}")
        return make_response(
            {
                "message": f"Could not find gym, reason: {err}"
            }, 500)
    

def get_gym_by_id(id):
    try:
        search_gym = db.session.query(Gym).filter(Gym.id==id).first()

        if not search_gym:
            return make_response(
                {
                    "message": "gym was not found in database"
                }, 404)
        
        dict_gym = search_gym.to_dict()
        logger.info(
            f"gym was found, {dict_gym}")
        return make_response(
            {
                "message": "gym found",
                "data": dict_gym
            }, 200)
    
    except Exception as err:
        logger.error(f"Could not find gym, reason: {err}")
        return make_response(
            {
                "message": f"Could not find gym, reason: {err}"
            }, 500
        )


def get_students_by_gym(id):
    try:
        search_students = (
            db.session.query(Student)
            .filter(Student.gym_id==id)
            .all()
        )

        dict_students = [
            student.to_dict() for student in search_students
        ]

        if not search_students:
            return make_response(
                {
                    "message": f"There aren't students for gym with id: {id}",
                    "data": dict_students
                }, 404
            )
        
        logger.info(f"Students were found for gym with id: {id}")
        return make_response(
            {
                "message": f"Students were found for gym with id: {id}",
                "data": dict_students
            }, 200
        )
    except Exception as err:
        logger.error(f"Could not find students for gym with id: {id}")
        return make_response(
            {
                "message": f"Could not find students, reason: {err}"
            }, 500
        )
    

def get_professors_by_gym(id):
    try:
        search_professors = (
            db.session.query(Professor)
            .filter(Professor.gym_id==id)
            .all()
        )

        dict_professors = [
            professors.to_dict() for professors in search_professors
        ]
        
        if not search_professors:
            return make_response(
                {
                    "message": f"There aren't professors for gym with id: {id}",
                    "data": dict_professors
                }, 404
            )
        
        logger.info(f"professors were found for gym with id: {id}")
        return make_response(
            {
                "message": f"professors were found for gym with id: {id}",
                "data": dict_professors
            }, 200
        )
    except Exception as err:
        logger.error(f"Could not find professors for gym with id: {id}")
        return make_response(
            {
                "message": f"Could not find professors, reason: {err}"
            }, 500
        )