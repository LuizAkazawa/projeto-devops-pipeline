import smtplib
import email.message
import os

# Envio de email para informar que o pipeline está sendo iniciado
def enviar_email():
    corpo_email = """
    O pipeline está sendo iniciado!
    """
    msg = email.message.EmailMessage()
    msg['Subject'] = 'Informação Pipeline'
    msg['From'] = os.getenv("GMAIL_EMAIL")
    msg['To'] = os.getenv("DESTINATARIO_EMAIL")
    password = os.getenv("GMAIL_PASSWORD")

    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    s.quit()
enviar_email()