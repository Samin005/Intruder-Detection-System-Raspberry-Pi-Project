import RPi.GPIO as GPIO
import time

led = 40
pir = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(pir,GPIO.IN)

while True:
    i = GPIO.input(pir)
    if i==0:
        print ("No Intruder.")
        GPIO.output(led,0)
        time.sleep(0.1)
    elif i==1:
        print ("Intruder Detected!")
        GPIO.output(led,1)
        time.sleep(0.1)
