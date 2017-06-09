import RPi.GPIO as GPIO
import time
import socket
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

s=socket.socket()
host=socket.gethostname()
port=445
s.bind((host,port))

s.listen(5)

while True:
	c,addr=s.accept()	# incoming of wannacry
	print "wannacry in local network"
	c.close()		# close wannacry connection

	while True:		# blink led on pin 18
		GPIO.output(18,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(18,GPIO.LOW)
		time.sleep(1)
