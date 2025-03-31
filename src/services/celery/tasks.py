from celery import shared_task
from utils.extensions import telegram_adapter
from services.celery.helpers import class_reminders



@shared_task
def send_welcome_message_on_chat(
    message,
    chat_id=None):

    telegram_adapter.send_welcome_message(message)


@shared_task
def send_payment_email(message):
    pass

@shared_task
def check_and_send_reminders():
    class_reminders()