import smtplib
from email.message import EmailMessage
import imghdr

PASSWORD = "daofpapzhirvlkqb"
USERNAME = "its.akram246@gmail.com"
RECEIVER = "its.akram246@gmail.com"

def sendEmail(image_path):
    email_message = EmailMessage()
    email_message["subject"] = "new customer showed up"
    email_message.set_content("a new customer")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(USERNAME, PASSWORD)
    gmail.sendmail(USERNAME, RECEIVER, email_message.as_string())
    gmail.quit()
