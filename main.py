import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
GPIO.setwarnings(False)
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

def turnOn():
	GPIO.output(RELAIS_1_GPIO, GPIO.LOW)

def turnOff():
	GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)

if not (len(sys.argv) - 1):
	print("Call some vars")
elif sys.argv[1] == "off":
	turnOff()
elif not (len(sys.argv) - 2):
	print("do that again")
elif sys.argv[1] == "on" and not float(sys.argv[2]) == 0:
	turnOn()
	time.sleep(float(sys.argv[2]))
	turnOff()
else:
	turnOff()