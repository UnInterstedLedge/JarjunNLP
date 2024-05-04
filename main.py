from flask import Flask, request, render_template, url_for, send_from_directory
import os
import speech_recognition as sr

app = Flask(__name__)

def transcribe_audio(file_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        # Listen to the source
        audio_data = recognizer.record(source)
        try:
            # Perform speech recognition
            return recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results; {e}"

@app.route('/play/<filename>')
def play_audio(filename):
    # Serves audio files
    return send_from_directory(directory='static', filename=filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ''
    transcription = ''
    audio_file_1 = 'mf-my_name.wav'  # Assuming the file is directly in the static folder
    audio_file_2 = 'mf-how_are_you.wav'  # Assuming the file is directly in the static folder
    selected_speaker = None
    if request.method == 'POST':
        speaker = request.form.get('speaker', '')
        user_input = request.form.get('user_input', '')
        if speaker == "morgan_freeman" and user_input.lower() == "hey morgan freeman, how are you?":
            selected_speaker = speaker
            # Construct the URL for the audio files
            audio_file_1_url = url_for('play_audio', filename=audio_file_1)
            audio_file_2_url = url_for('play_audio', filename=audio_file_2)
            # Transcribe the audio
            transcription += transcribe_audio(os.path.join('static', audio_file_1)) + " "
            transcription += transcribe_audio(os.path.join('static', audio_file_2))
            return render_template('chat.html', audio_file_1=audio_file_1_url, audio_file_2=audio_file_2_url, transcription=transcription, selected_speaker=selected_speaker)
    return render_template('chat.html', selected_speaker=selected_speaker)

if __name__ == "__main__":
    app.run(debug=True)
