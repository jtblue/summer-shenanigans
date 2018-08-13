# relay 1 = continuity/safety
# relay 2 = launch button
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# TODO: update pins
SAFETY_PIN = 0
LAUNCH_PIN = 0
CONTINUITY_CHECK_PIN = 0

def launch_sequence():
	if trigger():
		print("Ignition!")
	print("Ignition failed")


def check_circuit_continuity():
	circuit_has_continuity = False
	try:
		GPIO.setup(SAFETY_PIN, GPIO.OUT)
		GPIO.setup(CONTINUITY_CHECK_PIN, GPIO.IN)
		# switch relay 1 to be closed
		GPIO.output(SAFETY_PIN, GPIO.HIGH)
		# TODO: check for continuity here somehow
		if GPIO.input(CONTINUITY_CHECK_PIN):
			circuit_has_continuity = True
		# switch relay 1 to be open again
		GPIO.output(SAFETY_PIN, GPIO.LOW)
	except Exception as e:
		print(e)
	return circuit_has_continuity


def trigger():
	launch_successful = False
	try:
		# make sure circuit does not have continuity
		GPIO.setup(CONTINUITY_CHECK_PIN, GPIO.IN)
		if GPIO.input(CONTINUITY_CHECK_PIN):
			print("Circuit should not have continuity yet")
			return launch_successful
		GPIO.setup(SAFETY_PIN, GPIO.OUT)
		GPIO.setup(LAUNCH_PIN, GPIO.OUT)
		# switch relay 1 to be closed
		GPIO.output(SAFETY_PIN, GPIO.HIGH)
		# if continuous switch relay 2 to be closed, set launch_successful
		if GPIO.input(CONTINUITY_CHECK_PIN):
			GPIO.output(LAUNCH_PIN, GPIO.HIGH) # this line triggers ignition
			launch_successful = True
	except Exception as e:
		print(e)
	return launch_successful