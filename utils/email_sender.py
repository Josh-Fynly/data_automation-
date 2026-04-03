import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")


def send_email(report_path: str) -> bool:
    """
    Sends an email with the report attached.

    Returns:
        bool: True if successful, False otherwise
    """

    # Validate config
    if not all([EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER]):
        print("Email configuration missing. Check your .env file.")
        return False

    try:
        msg = EmailMessage()
        msg["Subject"] = "Automated Data Report"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        msg.set_content("Attached is your automated data report.")

        # Attach file
        with open(report_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(f.name)

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="json",
            filename=file_name
        )

        # Send email securely
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("Email sent successfully.")
        return True

    except FileNotFoundError:
        print(f"Report file not found: {report_path}")
        return False

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email or app password.")
        return False

    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
        return False

    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
