import RPi.GPIO as  GPIO
from time import sleep

GPIO.serwarnings(False)
GPIO.setmode(GPIO.BCM) #GPIO.BOARD
GPIO.setup(23, GPIO.IN)
elozo = 0
while True:
	mostani = GPIO.input(23)
	if (not elozo and mostani):
		print("Gomb lenyomva")
	elozo = mostani
	sleep(0.1)

