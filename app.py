import os

from flask import Flask, render_template, request
from main import main
#python text to speech
import pyttsx3


app = Flask(__name__)
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')
@app.route('/audio', methods=['GET', 'POST'])
def get_text():
    audio = request.files.get('audio')
    temp_filename = 'temp_audio.flac'
    audio.save(temp_filename)
    res = main(temp_filename)
    os.remove(temp_filename)
    return res

if __name__ == '__main__':
    app.run()
