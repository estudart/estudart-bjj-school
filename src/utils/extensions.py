from flask_sqlalchemy import SQLAlchemy

from adapters.telegram_adapter import TelegramAdapter
from adapters.logger_adapter import LoggerAdapter
from adapters.sendgrid_adapter import SendGridAdapter



logger = LoggerAdapter().get_logger()
db = SQLAlchemy()
telegram_adapter = TelegramAdapter(logger)
sendgrid_adapter = SendGridAdapter(logger)
