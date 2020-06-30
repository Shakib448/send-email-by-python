import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'djangomaster7023@gmail.com'
password = 'ShakiB7023956841'

def send_mail(text= 'Email body', subject = 'Hello world',from_email = 'Django master <djangomaster7023@gmail.com>', to_emails = None, html = None):
    assert isinstance(to_emails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
 
    text_part = MIMEText(text, 'plain')
    msg.attach(text_part)

    # html_part = MIMEText('<h1> This is working </h1>', 'html')
    # msg.attach(html_part)

    msg_str = msg.as_string()

    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

    # login to my smtp sever
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username , password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()

    # with smtplib.SMTP() as server:
    #     server.login()
    #     pass