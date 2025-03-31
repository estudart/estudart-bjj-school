from utils.extensions import db, logger
from services.api.models.bjj_class import BJJClass


def class_reminders():
    try:
        search_classes = (
            db.session.query(BJJClass)
            .all()
        )

        bjj_class_id_list = []

        for bjj_class in search_classes:
            bjj_class_id_list.append(bjj_class.to_dict()["id"])

        logger.info(f"Classes to send message are {bjj_class_id_list}") 

    except Exception as err:
        logger.error(err)