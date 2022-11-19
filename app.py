from email import message
from flask import Flask, render_template, request
from gpiozero import LED
from time import sleep

app = Flask(__name__)
led = LED(17)

blink = False


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/message',  methods=['POST'])
def light():
    global blink 

    try:
        message = request.form['message']

        if message == "on":
            blink = False
            led.on()
        elif message == "off":
            blink = False
            led.off()
        elif message == 'blink':
            blink = True
            while blink == True:
                led.on()
                sleep(1)
                led.off()
                sleep(1)
    
    except:
        pass
    
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
