import RPi.GPIO as IO
import time

IO.setmode(IO.BOARD)
IO.setup(40,IO.OUT)
IO.output(40,1)
time.sleep(1)
IO.cleanup()
time.sleep(1)

count = 0
while(count < 9):
    IO.setmode(IO.BOARD)
    IO.setup(40,IO.OUT)
    IO.output(40,1)
    time.sleep(1)
    IO.cleanup()
    time.sleep(1)

    count = count + 1
