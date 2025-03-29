import logging

from flask_sqlalchemy import SQLAlchemy

from adapters.telegram_adapter import TelegramAdapter

db = SQLAlchemy()
telegram_adapter = TelegramAdapter()
logger = logging.getLogger(__name__)