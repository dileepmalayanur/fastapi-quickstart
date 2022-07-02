from email.message import EmailMessage

from app.loader.properties import get_application_properties


def send_email(to_email_address: str, subject: str, body: str):

    print("Sending email to ", to_email_address)
    msg = EmailMessage()
    msg['Subject'] = f'The contents of '
    msg['From'] = get_application_properties()['email-address']['from']
    msg['To'] = to_email_address
    print("Sent email to ", to_email_address, '!')