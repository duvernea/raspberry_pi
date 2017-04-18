import RPi.GPIO as GPIO
import time

# set Pin Numbering Mode
GPIO.setmode(GPIO.BOARD) # numbering is board based numbering
# GPIO.setmode(GPIO.BCM) # Broadcom SoC number

# Set Pin Direction and Assignment
GPIO.setup(13, GPIO.OUT)

while True:
	# Assign value to output pin
	GPIO.output(13, True)
	time.sleep(1)
	GPIO.output(13, False)
	time.sleep(1)


