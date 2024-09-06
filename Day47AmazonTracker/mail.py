from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

class SendEmail:
    def __init__(self,body='',mail_subject="Amazon Notification"):
        self.__file_path = os.environ.get("MY_ENV")
        load_dotenv(dotenv_path=self.__file_path)
        self.__mail_from = os.getenv('EMAIL_RECIPIENT')
        self.__mail_to = os.getenv('EMAIL_2')
        self.__smtp_password= os.getenv('STMP_PASS')
        self.__smtp_server = "smtp.gmail.com"
        self.__body = "Tassimo Coffee current price:" + str(body)
        self.__subject = mail_subject
        self.__smtp_port = 587  # Use 465 for SSL

    def send_message(self):
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = self.__mail_from
        msg['To'] = self.__mail_to
        msg['Subject'] = self.__subject
        msg.attach(MIMEText(self.__body, 'plain'))

        try:
            with smtplib.SMTP(self.__smtp_server, self.__smtp_port) as server:
                # Transport Layer Security
                server.starttls()
                server.login(self.__mail_from, self.__smtp_password)
                text = msg.as_string()
                server.sendmail(self.__mail_from, self.__mail_to, text)
                print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
        finally:
            print("Done!")