import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")

# Debug logging - check if env vars are loaded
print(f"Email config - SENDER_EMAIL: {SENDER_EMAIL}")
print(f"Email config - SENDER_PASSWORD: {'SET' if SENDER_PASSWORD else 'NOT SET'}")
if not SENDER_EMAIL or not SENDER_PASSWORD:
    print("WARNING: Email credentials not properly configured!")

def send_verification_email(to_email: str, user: str, token: str):
    print(f"Attempting to send verification email to {to_email}")
    msg = MIMEMultipart()
    body = "http://wtruluck-project.com/verify/" + token
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = "Hello " + user + ", please verify your email"
    msg.attach(MIMEText(body, "plain"))

    # Connect to Gmail SMTP
    try:
        print("Connecting to Gmail SMTP...")
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as server:
            print("Starting TLS...")
            server.starttls()
            print("Logging in...")
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            print("Sending message...")
            server.send_message(msg)
        print("Email sent successfully!")
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
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        return "Failed to send email: " + str(e) 