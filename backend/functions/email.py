import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")

def send_verification_email(to_email: str, user: str, token: str):
    msg = MIMEMultipart()
    body = "http://wtruluck-project.com/verify/" + token
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = "Hello " + user + ", please verify your email"
    msg.attach(MIMEText(body, "plain"))

    # Connect to Gmail SMTP
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        return "Failed to send email: " + str(e)


def send_password_reset_email(to_email: str, user: str, token: str):
    msg = MIMEMultipart()
    body = "http://wtruluck-project.com/password-change/" + token
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = "Hello " + user + ", reset your password"
    msg.attach(MIMEText(body, "plain"))

    # Connect to Gmail SMTP
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        return "Failed to send email: " + str(e) 