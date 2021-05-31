import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

fromAddr = "samin005.bracu@gmail.com"
toAddr = "back4mhell2@gmail.com"
mail = MIMEMultipart()
mail['From'] = fromAddr
mail['To'] = toAddr
mail['Subject'] = "Attachment"
body = "See that picture!"

def sendMail(data):
    mail.attach(MIMEText(body, 'plain'))
    print(data)
    data = "image.jpg"
    attachment = open(data, 'rb')
    image = MIMEImage(attachment.read())
    attachment.close()
    mail.attach(image)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(fromAddr, "14101005")
    text = mail.as_string()
    server.sendmail(fromAddr, toAddr, text)
    server.quit
    print("Image sent via email!")
sendMail("image.jpg")
