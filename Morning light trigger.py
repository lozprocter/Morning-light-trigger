import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

relay = 11
GPIO.setup(relay, GPIO.OUT)

while True:
    GPIO.setup(relay, True)
    GPIO.setup(relay, False)


