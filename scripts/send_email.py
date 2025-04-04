import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    # Configurações Gmail
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = os.environ["GMAIL_EMAIL"]
    password = os.environ["GMAIL_PASSWORD"]
    receiver_email = os.environ["DESTINATARIO_EMAIL"]

    # Criar mensagem
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Notificação: Pipeline Iniciado"
    
    # Corpo HTML
    body = """
    <p>O pipeline foi iniciado com sucesso!</p>
    <p><b>Atenção:</b> Este é um e-mail automático.</p>
    """
    msg.attach(MIMEText(body, "html"))

    # Enviar
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print("✅ E-mail enviado!")
    except Exception as e:
        print(f"❌ Falha no envio: {e}")

if __name__ == "__main__":
    send_email()