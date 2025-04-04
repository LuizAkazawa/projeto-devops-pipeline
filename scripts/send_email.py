import smtplib
import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, password, receiver_email):
    smtp_server = "smtp.gmail.com"
    port = 587

    # Criar mensagem#
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Notificação: Pipeline Iniciado"

    body = """
    <p>O pipeline foi iniciado com sucesso!</p>
    <p><b>Atenção:</b> Este é um e-mail automático.</p>
    """
    msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print("E-mail enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sender", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--receiver", required=True)
    args = parser.parse_args()

    send_email(args.sender, args.password, args.receiver)
