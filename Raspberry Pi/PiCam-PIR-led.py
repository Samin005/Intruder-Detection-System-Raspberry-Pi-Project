import RPi.GPIO as GPIO
import time
import picamera

led = 40
pir = 11
data = ""

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(pir,GPIO.IN)

def capture_image():
    data = time.strftime("%d_%b_%Y|%H:%M:%S")
    camera.start_preview()
    time.sleep(3)
    print (data)
    camera.capture('%s.jpg'%data)
    camera.stop_preview()
    time.sleep(1)

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
        
        
