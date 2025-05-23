from celery import shared_task
from utils.extensions import telegram_adapter
from services.celery.helpers import class_reminders, send_class_reminder



@shared_task
def send_welcome_message_on_chat(
    name,
    chat_id=None):

    telegram_adapter.send_welcome_message(name)

@shared_task
def schedule_reminder_for_class(student_id,
                        class_id,
                        time_before_class):
    send_class_reminder(student_id,
                        class_id,
                        time_before_class)



@shared_task
def send_payment_email(message):
    pass

@shared_task
def check_and_send_reminders():
    class_reminders()