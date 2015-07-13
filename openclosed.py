import os
from firebase import firebase
import time
import requests
from twilio.rest import TwilioRestClient
from config import fbRef, twilio_acc_id, twilio_acc_auth_token, twilio_number, alert_user, alert_user_name

FIREBASE = firebase.FirebaseApplication(fbRef, None)

def send_text(number, name):
	client = TwilioRestClient(twilio_acc_id, twilio_acc_auth_token)
	message = client.messages.create(body=alert_user_name + " the door has been opened!",
		to=alert_user,
		from_="+19723626631")
	print "text sent"

def make_call(number, name):
	client = TwilioRestClient(twilio_acc_id, twilio_acc_auth_token)
	call = client.calls.create(url="https://dooralert.firebaseapp.com/voice.xml",
		to=alert_user,
		from_="+19723626631")
	print "call made"

def change_dooralert_state(state):
	if state == 0:
		FIREBASE.put('/', 'dooralert', 'false')
		send_text(text)
		time.sleep(4)
		make_call(call)
	else:
		FIREBASE.put('/', 'dooralert', 'true')
