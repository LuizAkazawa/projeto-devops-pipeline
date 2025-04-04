import os
import smtplib
from email.mime.text import MIMEText

def send_email(status="start"):
    msg = MIMEText(
        "Pipeline iniciada!" if status == "start" 
        else f"Pipeline concluída! Status: {os.getenv('WORKFLOW_STATUS')}"
    )
    msg["Subject"] = f"CI/CD: {'Início' if status == 'start' else 'Término'}"
    msg["From"] = os.getenv("SMTP_USER")
    msg["To"] = os.getenv("RECIPIENT_EMAIL")

    with smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as server:
        server.starttls()
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
        server.send_message(msg)

if __name__ == "__main__":
    import sys
    send_email(sys.argv[1] if len(sys.argv) > 1 else "final")