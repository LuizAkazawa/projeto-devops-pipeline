import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    # Coletar variáveis de ambiente
    sender_email = os.getenv("GMAIL_EMAIL")
    password = os.getenv("GMAIL_PASSWORD")
    receiver_email = os.getenv("DESTINATARIO_EMAIL")

    if not sender_email or not password or not receiver_email:
        raise ValueError("Uma ou mais variáveis de ambiente não estão definidas.")

    smtp_server = "smtp.gmail.com"
    port = 587

    # Criar mensagem
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Notificação: Pipeline Iniciado"

    body = """
    <p>O pipeline foi iniciado com sucesso!</p>
    <p><b>Atenção:</b> Este é um e-mail automático.</p>
    """
    msg.attach(MIMEText(body, "html"))

    # Enviar e-mail
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print("✅ E-mail enviado com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    send_email()
