import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = "watruluck@gmail.com"
SENDER_PASSWORD = "wzva svui jsma kpuu"  # replace when in production

def send_verification_email(to_email: str, user: str, token: str):
    msg = MIMEMultipart()
    body = "http://localhost:5173/verify/" + token
    msg["From"] = SENDER_EMAIL
    msg["To"] = "watruluck@gmail.com"
    # msg["To"] = to_email
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
    body = "http://localhost:5173/password-change/" + token
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