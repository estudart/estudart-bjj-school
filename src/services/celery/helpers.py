from datetime import datetime, timedelta

from utils.extensions import db, logger, telegram_adapter
from services.api.models.bjj_class import BJJClass
from services.api.models.student import Student
from services.api.models.student_class import StudentClasses
from services.api.models.professor import Professor
from services.api.models.gym import Gym



def class_reminders():
    now_time = datetime.now()
    time_range = timedelta(minutes=10)
    try:
        search_classes = (
            db.session.query(BJJClass)
            .filter(BJJClass.class_reminder_was_sent==False)
            .all()
        )

        for bjj_class in search_classes:
            dict_bjj_class = bjj_class.to_dict()
            
            if timedelta(minutes=0) <= dict_bjj_class["date"] - now_time <= time_range:
                search_students = (
                    db.session.query(Student)
                    .join(StudentClasses)
                    .filter(StudentClasses.class_id==dict_bjj_class["id"])
                    .all()
                )

                if search_students:
                    dict_students = [
                        search_student.to_dict() for search_student in search_students
                    ]
                    for student in dict_students:
                        telegram_adapter.send_class_alert_message(
                            student_name=student["name"],

                            bjj_class_address=(db.session.query(Gym)
                             .filter(Gym.id==dict_bjj_class["gym_id"])
                             .first()
                             .to_dict()["address"]),

                            professor_name=(db.session.query(Professor)
                             .filter(Professor.id==dict_bjj_class["professor_id"])
                             .first()
                             .to_dict()["name"]),

                             time_until_class=int(
                                 (dict_bjj_class["date"] - now_time).total_seconds() / 60
                             )                          
                        )
            updated = (
                db.session.query(BJJClass)
                .filter(BJJClass.id==dict_bjj_class["id"])
                .update({"class_reminder_was_sent": True})
            )

            db.session.commit()

    except Exception as err:
        logger.error(f"Could not send class reminder, reason: {err}")


def send_class_reminder(student_id,
                        class_id,
                        time_before_class):
    try:
        professor_id = (
            db.session.query(BJJClass)
            .filter(BJJClass.id==class_id)
            .first()
            .to_dict()["professor_id"]
        )

        gym_id = (
            db.session.query(BJJClass)
            .filter(BJJClass.id==class_id)
            .first()
            .to_dict()["gym_id"]
        )

        telegram_adapter.send_class_alert_message(
            student_name=(db.session.query(Student)
                .filter(Student.id==student_id)
                .first()
                .to_dict()["name"]),

            bjj_class_address=(db.session.query(Gym)
                .filter(Gym.id==gym_id)
                .first()
                .to_dict()["address"]),

            professor_name=(db.session.query(Professor)
                .filter(Professor.id==professor_id)
                .first()
                .to_dict()["name"]),

                time_until_class=time_before_class                        
        )

    except Exception as err:
        logger.error(f"Could not send class reminder, reason: {err}")