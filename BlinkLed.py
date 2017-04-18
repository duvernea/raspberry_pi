import RPi.GPIO as GPIO
import time
import threading
from tkinter import *

blinkState = False;

# set Pin Numbering Mode
GPIO.setmode(GPIO.BOARD) # numbering is board based numbering
# GPIO.setmode(GPIO.BCM) # Broadcom SoC number

# Set Pin Direction and Assignment
GPIO.setup(13, GPIO.OUT)


def buttonPress():
	global blinkState
	blinkState = not blinkState
	print ("blink state: " + str(blinkState))	
	t=threading.Thread(target=LEDblink)
	t.start()
	
def LEDblink():
	while blinkState:
		# Assign value to output pin
		if blinkState:
			GPIO.output(13, True)
			time.sleep(1)
			GPIO.output(13, False)
			time.sleep(1)
		else:
			GPIO.output(13, False)

root = Tk()
b = Button(root, text="blink start/stop", command=buttonPress)
b.pack()
root.mainloop()

