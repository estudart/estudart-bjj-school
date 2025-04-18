import requests

from utils.config import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_API_URL
)



class TelegramAdapter:
    def __init__(self,
                 logger,
                 url=TELEGRAM_API_URL,
                 token=TELEGRAM_BOT_TOKEN):
        
        self.logger = logger
        self.token = token
        self.url = url
        

    def send_message(self, text_message, chat_id="7149973377"):
        try:
            response = requests.post(
                url=f"{self.url}{self.token}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": text_message
                }
            )

            data = response.json()

            if response.status_code == 200:
                self.logger.info(
                    f"Message was sent to telegram: {data}")
        except Exception as err:
            self.logger.error(
                f"Could not send message to Telegram, reason: {err}"
            )
    

    def send_welcome_message(self, name):
        text_message = (
            f"Welcome to our team, {name}. "
            "This is the gym's number, feel free to get in contact "
            "with us if you have any doubts"
        )
        self.send_message(text_message)

    
    def send_class_alert_message(self, 
                                 student_name, 
                                 bjj_class_address,
                                 professor_name,
                                 time_until_class):
        text_message = (
            f"Hello there, {student_name}.\n\n"
            f"You have a bjj class with professor {professor_name} "
            f"at the address {bjj_class_address} in {time_until_class} " 
            f"{'minutes' if time_until_class > 1 else 'minute'}."
        )
        self.send_message(text_message)

