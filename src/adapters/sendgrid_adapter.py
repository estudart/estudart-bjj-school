from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from utils.config import SENDGRID_API_KEY, SERVER_EMAIL


class SendGridAdapter:
    def __init__(self, logger_instance, api_key=SENDGRID_API_KEY, server_email=SERVER_EMAIL):
        self.api_key = api_key
        self.server_email = server_email
        self.logger_instance = logger_instance

    def send_email(self, send_to_email: str, subject: str, html_content: str = None):
        if html_content is None:
            html_content = "<strong>Testing email</strong>"

        msg = Mail(
            from_email=self.server_email,
            to_emails=send_to_email,
            subject=subject,
            html_content=html_content
        )

        try:
            sg = SendGridAPIClient(self.api_key)
            response = sg.send(msg)
            print(response)
            self.logger_instance.info(f"Email sent! Status Code: {response.status_code}")
            return response.status_code == 202  # 202 means accepted for processing
        except Exception as err:
            self.logger_instance.error(f"Could not send email, reason: {err}")
            return False
