import RPi.GPIO as  GPIO
from time import sleep

GPIO.serwarnings(False)
GPIO.setmode(GPIO.BCM) #GPIO.BOARD
GPIO.setup(23, GPIO.out, initial = GPIO.LOW)

while True:
	GPIO.output(23, GPIO.HIGH)
	sleep(0.1)
	GPIO.output(23, GPIO.LOW)
        sleep(0.1)
