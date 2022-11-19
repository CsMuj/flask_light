from re import X
from flask import Flask, render_template, request
from gpiozero import LED
from time import sleep

app = Flask(__name__)
led = LED(17)

conditon = X
while conditon == On:
    led.on()
    sleep(0.5)
    led.off()
    sleep(2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/message',  methods=['POST'])
def light():
    message = request.form['message']

    print(message)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
