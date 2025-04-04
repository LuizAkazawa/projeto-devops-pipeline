import os
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Assunto Seguro'
msg['From'] = os.environ['REMETENTE']
msg['To'] = os.environ['DESTINATARIO']
msg.set_content('Conteúdo protegido por secrets.')

with smtplib.SMTP('smtp.office365.com', 587) as smtp:
    smtp.starttls()
    smtp.login(os.environ['REMETENTE'], os.environ['SENHA'])
    smtp.send_message(msg)