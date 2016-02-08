import mraa
import time
import sys

trigPin = mraa.Gpio(5)
trigPin.dir(mraa.DIR_OUT)
trigPin.write(0)

echoPin = mraa.Gpio(6)
echoPin.dir(mraa.DIR_IN)

time.sleep(0.3)

while 1:

	trigPin.write(1)
	time.sleep(0.00001)
	trigPin.write(0)

	while echoPin.read() == 0:
		pulseOff = time.time()
	while echoPin.read() == 1:
		pulseOn = time.time()

	timeDifference = pulseOn - pulseOff
	centimeters = timeDifference *17000
	print 'centimeters: '
	print centimeters
	time.sleep(.1)

