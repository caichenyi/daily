# encoding: utf-8
# Author: Cai Chenyi
import smtplib
import email.mime.multipart
import email.mime.text

def getPara(smtp_info, receivers, subject, content):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = smtp_info['sender']
    msg['to'] = ";".join(receivers)
    msg['subject'] = subject
    msg.attach(email.mime.text.MIMEText(content))
    return msg


def getSmtp(smtp_path):
    with open(smtp_path, 'rt', encoding='utf-8') as f:
        return eval(f.readline())


def sendEmail(smtp_path, receivers, subject='', content=''):
    smtp_info = getSmtp(smtp_path)
    msg = getPara(smtp_info, receivers, subject, content)

    smtp = smtplib.SMTP()
    smtp.connect(smtp_info['smtp_host'], smtp_info['smtp_port'])
    smtp.login(smtp_info['sender'], smtp_info['password'])
    smtp.sendmail(smtp_info['sender'], receivers, str(msg))
    smtp.quit()

