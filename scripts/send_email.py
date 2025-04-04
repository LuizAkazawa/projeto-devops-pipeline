import os
import smtplib
from email.message import EmailMessage

def send_outlook_email(status="final"):
    # Configuração da mensagem
    msg = EmailMessage()
    msg.set_content(
        "Pipeline iniciada!" if status == "start" 
        else f"Pipeline concluída! Status: {os.getenv('WORKFLOW_STATUS', 'desconhecido')}"
    )
    msg["Subject"] = f"CI/CD: {'Início' if status == 'start' else 'Término'}"
    msg["From"] = os.getenv("OUTLOOK_EMAIL")  # Seu email Outlook
    msg["To"] = os.getenv("RECIPIENT_EMAIL")  # Email do destinatário

    # Configuração para Outlook/Office365
    with smtplib.SMTP("smtp.office365.com", port=587) as server:
        server.starttls()  # Upgrade para conexão segura
        server.login(os.getenv("OUTLOOK_EMAIL"), os.getenv("OUTLOOK_PASSWORD"))
        server.send_message(msg)

if __name__ == "__main__":
    import sys
    send_outlook_email(sys.argv[1] if len(sys.argv) > 1 else "final")