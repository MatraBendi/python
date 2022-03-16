import RPi.GPIO as  GPIO
from time import sleep
led = 23
kapcsolo = 24
GPIO.serwarnings(False)
GPIO.setmode(GPIO.BCM) #GPIO.BOARD
GPIO.setup(led, GPIO.out, initial = GPIO.LOW)
GPIO.setup(kapcsolo, GPIO.IN)
elozo = 0
ledallapot = 0
while True:
	mostani = GPIO.input(kapcsolo)
	if (not elozo and mostani):
		if ledallapot:
			GPIO.outpu(led, GPIO.LOW)
			ledallapot = 0
		else:
			GPIO.output(led, GPIO.HIGH)
			ledallapot = 1
	elozo = mostani
	sleep(0.1)

