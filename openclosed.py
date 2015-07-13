import os
from firebase import firebase
import time
import requests
from twilio.rest import TwilioRestClient
from config import fbRef, twilio_acc_id, twilio_acc_auth_token, twilio_number, alert_user, alert_user_name

FIREBASE = firebase.FirebaseApplication(fbRef, None)

def change_dooralert_state(state):
	if state == 0:
		FIREBASE.put('/', 'dooralert', 'false')
	else:
		FIREBASE.put('/', 'dooralert', 'true')
		
	client = TwilioRestClient(twilio_acc_id, twilio_acc_auth_token)
	message = client.messages.create(body=alert_user_name + " the door has been opened!",
		to=alert_user,
	    from_="+19723626631")
	print "text sent"
	time.sleep (3)

	client = TwilioRestClient(twilio_acc_id, twilio_acc_auth_token)
	call = client.calls.create(url="https://dooralert.firebaseapp.com/voice.xml",
		to=alert_user,
		from_="+19723626631")
	print "call made"
