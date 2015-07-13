import os
from firebase import firebase
import time
import requests
from twilio.rest import TwilioRestClient
from config import fbRef, twilio_acc_id, twilio_acc_auth_token, twilio_number

FIREBASE = firebase.FirebaseApplication(fbRef, None)

def send_text:
	client = TwilioRestClient(twilio_acc_id, twilio_acc_auth_token)
	message = client.messages.create(body=name + " the door has been opened!",
		to="+12144444000",
	    from_="+19723626631")
	print "text sent"

#make call define
def make_call:
	#pull data from twilio
	client = TwilioRestClient(twilio_acc_id, twilio_acc_auth_token)
	call = client.calls.create(url="https://dooralert.firebaseapp.com/voice.xml",
		to="+12144444000",        # alert number
		from_="+19723626631")    # twilio from number
	print "call made"

# firebase updates for open/closed
def change_dooralert_state(state):
	if state == 0:
		FIREBASE.put('/', 'dooralert', 'false')
		name = "Stan"
		number = os.getenv(name)
		send_text
		time.sleep(3)
		make_call
	else:
		#door is closed
		FIREBASE.put('/', 'dooralert', 'true')
