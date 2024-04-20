from flask import Flask, request, render_template, url_for
from elevenlabs.client import ElevenLabs
from elevenlabs import play, stream, save
import os

app = Flask(__name__)

client = ElevenLabs(

    client = ElevenLabs(
        api_key = "e52a70d1c065b1967dd8a20fac50c212"   # api key needs to be put in
    )
)

@app.route('/play/<filename>')
def play_audio(filename):
    # This route serves audio files from the 'static' folder
    return app.send_static_file(filename)

def respond_to_text_input(user_input):
    audio = client.generate(
        responses = {
            "what is your name?": "My name is Unitree GO1.",
        },
        voice = Voice(
            voice_id = 'ao4mLC7j0ZkodIMMNscF',
            settings = VoiceSettings(stability = 0.75, similarity_boost = 1.0, style = 0.0, use_speaker_boost = True)
            ),
        mode = "eleven_monolingual_v1"
    )

    # Check if the user input matches any of the keywords or phrases
    for keyword, audio_file in responses.items():
        if keyword.lower() in user_input.lower():
            # Construct the URL for the audio file
            return url_for('play_audio', filename=audio_file)
    return "No appropriate response found."

@app.route('/', methods=['GET', 'POST'])

def index():
    response = ''
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        response = respond_to_text_input(user_input)
    return render_template('chat.html', response=response)

if __name__ == "__main__":
    app.run(debug=True)
