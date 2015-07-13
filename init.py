import RPi.GPIO as GPIO
import time
from firebase import firebase
import openclosed

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
prev_state = 0;

while True:
	input_state = GPIO.input(4)
	print "input_state: " + str(input_state)
	print "prev_state: " + str(prev_state)
	if input_state != prev_state:
		openclosed.change_dooralert_state(input_state)

	prev_state = input_state
	time.sleep(1)
