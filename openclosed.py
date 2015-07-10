import os
from firebase import firebase
import requests
from twilio.rest import TwilioRestClient
from config import fbRef, twilio_acc_id, twilio_acc_auth_token, twilio_number

FIREBASE = firebase.FirebaseApplication(fbRef, None)

#send text define
def send_text(number, name):
	# pull data from twilio
	client = TwilioRestClient(twilio_acc_id, twilio_acc_auth_token)
	message = client.messages.create(body=name + " the door has been opened!",
		to="+12144444000",    # alert number
	    from_="+19723626631") # Twilio from number
	print "text sent"


# firebase updates for open/closed
def change_dooralert_state(state):
	if state == 0:
		#door is opened
		FIREBASE.put('/', 'dooralert', 'false')
		#send sms alert
		name = "Stan"
		number = os.getenv(name)
		send_text(number, name)
	else:
		#door is closed
		FIREBASE.put('/', 'dooralert', 'true')
