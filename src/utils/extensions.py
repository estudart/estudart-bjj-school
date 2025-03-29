import logging

from flask_sqlalchemy import SQLAlchemy

from adapters.telegram_adapter import TelegramAdapter

db = SQLAlchemy()
telegram_adapter = TelegramAdapter()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# handler = logging.StreamHandler()  # Or FileHandler for logs in a file

# handler.setFormatter(formatter)
# logger.addHandler(handler)