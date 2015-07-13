import os
from firebase import firebase
import time
import requests
from twilio.rest import TwilioRestClient
from config import fbRef, twilio_acc_id, twilio_acc_auth_token, twilio_number, name, number

FIREBASE = firebase.FirebaseApplication(fbRef, None)

def send_text(number, name):
	client = TwilioRestClient(twilio_acc_id, twilio_acc_auth_token)
	message = client.messages.create(body=name + " the door has been opened!",
		name = os.getenv(NAME)
		number = os.getenv(NUMBER)
		to='number',
	    from_="+19723626631")
	print "text sent"

def make_call(number, name):
	client = TwilioRestClient(twilio_acc_id, twilio_acc_auth_token)
	call = client.calls.create(url="https://dooralert.firebaseapp.com/voice.xml",
		to="+12144444000",
		from_="+19723626631")
	print "call made"

def change_dooralert_state(state):
	if state == 0:
		FIREBASE.put('/', 'dooralert', 'false')
		name = os.getenv(NAME)
		number = os.getenv(NUMBER)
		send_text(number, name)
		time.sleep(3)
		make_call(number, name)
	else:
		FIREBASE.put('/', 'dooralert', 'true')
