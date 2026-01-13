from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from dotenv import load_dotenv

load_dotenv()

SENDGRID_EMAIL = os.environ.get("SENDGRID_EMAIL")
SENDGRID_KEY = os.environ.get("SENDGRID_KEY")

def send_verification_email(to_email: str, user: str, token: str):
    """Send email verification link via SendGrid"""
    message = Mail(
        from_email=SENDGRID_EMAIL,
        to_emails=to_email,
        subject=f"Hello {user}, please verify your email",
        html_content=f'<p>Click the link below to verify your email:</p><p><a href="http://wtruluck-project.com/verify/{token}">http://wtruluck-project.com/verify/{token}</a></p>'
    )
    
    try:
        sg = SendGridAPIClient(SENDGRID_KEY)
        response = sg.send(message)
        return True
    except Exception as e:
        error_msg = f"Failed to send email: {str(e)}"
        return error_msg


def send_password_reset_email(to_email: str, user: str, token: str):
    """Send password reset link via SendGrid"""
    message = Mail(
        from_email=SENDGRID_EMAIL,
        to_emails=to_email,
        subject=f"Hello {user}, reset your password",
        html_content=f'<p>Click the link below to reset your password:</p><p><a href="http://wtruluck-project.com/password-change/{token}">http://wtruluck-project.com/password-change/{token}</a></p>'
    )
    
    try:
        sg = SendGridAPIClient(SENDGRID_KEY)
        response = sg.send(message)
        return True
    except Exception as e:
        error_msg = f"Failed to send email: {str(e)}"
        return error_msg 