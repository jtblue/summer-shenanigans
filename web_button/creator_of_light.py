from flask import (
    Flask, flash, g, redirect, render_template, request, session, url_for
)
import datetime
#import RPi.GPIO as GPIO
import time
app = Flask(__name__)

#GPIO.setmode(GPIO.BCM)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title': 'HELLO!',
        'time' : timeString
        }
    return render_template('main.html', **templateData)


@app.route("/button", methods=('GET', 'POST'))
def button():
    on = False
    message = "Hello there"
    if request.form.get('button_switch'):
        on = True
    print(on)

    templateData = {
        'button_status' : on,
        'button_message' : message
    }

    return render_template('button.html', **templateData)


@app.route("/button/<status>")
def button_toggle(status):
    on = False
    if (status == "on"):
        on = True
    
    message = status

    templateData = {
        'button_status' : on,
        'button_message' : message
    }

    return render_template('button.html', **templateData)


"""
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
        else:
            response = "Invalid command"

    except Exception as e:        
        response = "Error message: " + str(e)

    templateData = {
        'title': 'Button page',
        'response': response
        }
    return render_template('button.html', **templateData)"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)