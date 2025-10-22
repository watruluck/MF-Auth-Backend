import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = "watruluck@gmail.com"
SENDER_PASSWORD = "wzva svui jsma kpuu"  # ⚠️ Not your Gmail password — use an "App Password"

def send_verification_email(to_email: str, user: str, token: str):
    msg = MIMEMultipart()
    body = "linktoverify.com/token=" + token
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
    except Exception as e:
        print(f"Error sending email: {e}")