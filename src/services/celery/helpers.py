from utils.extensions import db, logger
from services.api.models.bjj_class import BJJClass


def class_reminders():
    try:
        search_classes = (
            db.session.query(BJJClass)
            .all()
        )

        bjj_class_id_list = [bjj_class.to_dict() for bjj_class in search_classes]

        logger.info(f"Classes to send message are {bjj_class_id_list}") 

    except Exception as err:
        logger.error(err)