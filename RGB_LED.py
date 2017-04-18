import RPi.GPIO as GPIO
import time

# Mark pin 18 for PWM, freq = 400
pwm_obj = GPIO.PWM(18, 400)

# Start generating PWM signal, duty cycle = 100%
pwm_obj.start(100)

# Delay for 10 seconds
delay(10)

# Change duty cycle to 50%
pwm_obj.ChangeDutyCycle(50)



