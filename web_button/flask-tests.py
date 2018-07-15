from flask import Flask, render_template
import datetime
import time
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title': 'HELLO!',
        'time' : timeString
        }
    return render_template('main.html', **templateData)

@app.route('/receiver', methods = ['POST'])
def worker():
	# read json + reply
	data = request.get_json()
	result = ''

	for item in data:
		# loop over every row
		result += str(item['make']) + '\n'

	return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)