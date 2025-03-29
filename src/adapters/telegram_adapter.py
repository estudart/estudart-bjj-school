import logging

import requests

from utils.config import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_API_URL
)



class TelegramAdapter:
    def __init__(self,
                 url=TELEGRAM_API_URL,
                 token=TELEGRAM_BOT_TOKEN):
        
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
                logger.info(
                    f"Message was sent to telegram: {data}")
        except Exception as err:
            logger.error(
                f"Could not send message to Telegram, reason: {err}"
            )
    

    def send_welcome_message(self, name):
        text_message = (
            f"Welcome to our team, {name}. "
            "This is the gym's number, feel free to get in contact "
            "with us if you have any doubts"
        )
        self.send_message(text_message)

