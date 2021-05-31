import RPi.GPIO as GPIO
import time
import picamera

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

#for email
fromAddr = "samin005.bracu@gmail.com"
toAddr = "back4mhell2@gmail.com"
mail = MIMEMultipart()
mail['From'] = fromAddr
mail['To'] = toAddr
mail['Subject'] = "Possible Intruder!"
body = "It is possible that and intruder broke into your residance. Here is the picture of the intruder: "

#pir and led initialization
led = 40
pir = 11
data = ""

#setting up the pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(pir,GPIO.IN)

#taking a picture and saving it, also calls sendMail() in the end
def capture_image():
    data = time.strftime("%d_%b_%Y|%H:%M:%S")
    camera.start_preview()
    time.sleep(3)
    print ("Taking Picture...")
    camera.capture('%s.jpg'%data)
    camera.stop_preview()
    time.sleep(1)
    sendMail(data)

#sends the image via email
def sendMail(data):
    mail.attach(MIMEText(body, 'plain'))
    print("Image saved as %s"%data)
    dat = '%s.jpg'%data
    print("Sending image....")
    attachment = open(dat, 'rb')
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

GPIO.output(led,0)
camera = picamera.PiCamera()
camera.rotation = 180
camera.awb_mode = 'auto'
camera.brightness = 55

while True:
    i = GPIO.input(pir)
    if i==0:
        print ("No Intruder.")
        GPIO.output(led,0)
        time.sleep(0.1)
    elif i==1:
        print("Intruder Detected!")
        GPIO.output(led,1)
        capture_image()
