from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os
import time

app = Flask(__name__)

# Set a directory for storing the audio files
AUDIO_FOLDER = os.path.join('static', 'audio')
if not os.path.exists(AUDIO_FOLDER):
    os.makedirs(AUDIO_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the text input from the form
        input_text = request.form['text']
        if input_text:
            # Convert the text to speech using gTTS
            tts = gTTS(text=input_text, lang='en')
            # Generate a unique filename based on the current timestamp
            filename = f"audio_{int(time.time())}.mp3"
            filepath = os.path.join(AUDIO_FOLDER, filename)
            # Save the audio file
            print(filepath)
            tts.save(filepath)

            # Send the file to the user to listen
            audio_url = filepath.replace("\\", "/")
            return render_template('index.html', audio_file=audio_url)

    return render_template('index.html', audio_file=None)

if __name__ == '__main__':
    app.run(debug=True)
