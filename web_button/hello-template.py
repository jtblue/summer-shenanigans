from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
import time
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title': 'HELLO!',
        'time' : timeString
        }
    return render_template('main.html', **templateData)

@app.route("/readPin/<pin>")
def readPin(pin):
    try:
        GPIO.setup(int(pin), GPIO.IN)
        if GPIO.input(int(pin)) == True:
            response = "Pin number " + pin + " is high!"
        else:
            response = "Pin number " + pin + " is low!"
    except Exception as e:
        response = str(e) + " There was an error reading pin " + pin + "."
    
    templateData = {
        'title': 'Status of pin' + pin,
        'response': response
        }
    return render_template('pin.html', **templateData)

def fade():
    p = GPIO.PWM(25, 50)
    p.start(0)
    while True:
        for dc in range(0,100,10):
            p.ChangeDutyCycle(dc)
            time.sleep(.05)
        for dc in range(100,0,-10):
            p.ChangeDutyCycle(dc)
            time.sleep(.05)

@app.route("/button/<status>")
def button_status(status):
    try:
        GPIO.setup(25, GPIO.OUT)
        if status == "on":
            GPIO.output(25, 1)
            response = "Button is on!"
        elif status == "off":
            GPIO.output(25, 0)
            response = "Button is off!"
        elif status == "fade":
            fade(status) # infinite loop
        else:
            response = "Invalid command"

    except Exception as e:        
        response = "Error message: " + str(e)

    templateData = {
        'title': 'Button page',
        'response': response
        }
    return render_template('button.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)