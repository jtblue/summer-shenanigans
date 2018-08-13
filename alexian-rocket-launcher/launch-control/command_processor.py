from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from circuit_controller import check_circuit_continuity, launch_sequence
import os

app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def start_skill():
	print("Program started...")
	return question('Launch controller initiated')


@ask.on_session_started
def start_session():
	print("begin")
	session.attributes['launch'] = False


@ask.session_ended
def session_ended():
	print("end")
	print(session.attributes['launch'])
	if session.attributes['launch']:
		launch_sequence()
	return statement("")


@ask.intent('countdown', default={'time' : 10}, convert={'time' : int})
def begin_countdown(time):
	if time < 3:
		return question("Countdown must be longer than 3 seconds")
	elif time >= 30:
		return question("Countdown cannot be longer than 30 seconds")
	numbers = time
	counter = ''
	while numbers > 0:
		counter += str(numbers) + ' <break time="0.4s"/> '
		numbers -= 1
	text = render_template('countdown_message', time=time, counter=counter)
	session.attributes['launch'] = True
	print(session.attributes['launch'])
	return statement(text) #TODO: not ending session


@ask.intent('continuity')
def continuity():
	circuit_has_continuity = check_circuit_continuity()
	if circuit_has_continuity:
		return question('Circuit has continuity')
	return question('Circuit does not have continuity')


@ask.intent('AMAZON.CancelInent')
def cancel():
	return statement('Launch aborted')


@ask.intent('AMAZON.HelpIntent')
def help_message():
	return question('Write helpful messages')


@ask.intent('AMAZON.FallbackIntent')
def fallback():
	return question('Please try again idiot')


#TODO: move main method into a separate file
if __name__ == '__main__':
	print("Application is running")
	if 'ASK_VERIFY_REQUESTS' in os.environ:
		verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
		if verify == 'false':
			app.config['ASK_VERIFY_REQUESTS'] = False
	app.run(debug=True)