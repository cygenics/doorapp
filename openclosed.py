import os
from firebase import firebase
import time
import datetime
import requests
from twilio.rest import TwilioRestClient
from config import fbRef, twilio_acc_id, twilio_acc_auth_token, twilio_number, alert_user, alert_user_name

FIREBASE = firebase.FirebaseApplication(fbRef, None)

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def send_text():
	client = TwilioRestClient(twilio_acc_id, twilio_acc_auth_token)
	message = client.messages.create(body=alert_user_name + " the door has been opened!",
		to=alert_user,
		from_=twilio_number)
	print st
	print "text sent"

def make_call():
	client = TwilioRestClient(twilio_acc_id, twilio_acc_auth_token)
	call = client.calls.create(url="https://dooralert.firebaseapp.com/voice.xml",
		to=alert_user,
		from_=twilio_number)
	print st
	print "call made"

def write_log():
	with open("log.txt", "a") as myfile:
	myfile.write(st)
    myfile.write("Door has been opened.")

def change_dooralert_state(state):
	if state == 0:
		FIREBASE.put('/', 'dooralert', 'false')
		send_text()
		time.sleep(4)
		make_call()
		write_log()
	else:
		FIREBASE.put('/', 'dooralert', 'true')
