import smtplib
import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, password, receiver_email, tipo, status):
    smtp_server = "smtp.gmail.com"
    port = 587

    # Mensagem condicional
    if tipo == "start":
        subject = "Pipeline Iniciado"
        body = "<p>O pipeline foi <b>iniciado</b>.</p>"
    elif tipo == "end":
        subject = "Pipeline Finalizado"
        body = f"<p>O pipeline foi finalizado com status: <b>{status.upper()}</b>.</p>"
    else:
        subject = "Notificação do Pipeline"
        body = "<p>Status desconhecido.</p>"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
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
    parser.add_argument("--tipo", required=True)     # "start" ou "end"
    parser.add_argument("--status", required=False)  # "success" ou "failure"
    args = parser.parse_args()

    send_email(args.sender, args.password, args.receiver, args.tipo, args.status or "undefined")
