from services.celery.celery_app import celery_service
from utils.extensions import telegram_adapter



@celery_service.task
def send_welcome_message_on_chat(
    message,
    chat_id=None):

    telegram_adapter.send_welcome_message(message)


@celery_service.task
def send_payment_email(message):
    pass