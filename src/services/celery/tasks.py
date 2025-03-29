from services.celery.celery_app import celery_service
from adapters.telegram_adapter import TelegramAdapter



@celery_service.task
def send_message_on_chat(
    message,
    chat_id=None):

    TelegramAdapter().send_message(message)