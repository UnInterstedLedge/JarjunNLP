from flask import Flask, request, render_template, url_for
from speaker_outputs import response_ben_shapiro, response_dr_chen, response_morgan_freeman, response_sponge_bob, response_darth_vader

app = Flask(__name__)

# Set the path to the audio folder
@app.route('/static/audio/<filename>')
def serve_audio(filename):
    # Serves audio files from the 'audio' folder
    return app.send_static_file(f'audio/{filename}')

def get_response(speaker, user_input):
    # Dictionary of speakers and corresponding function
    response_functions = {
        'ben_shapiro': response_ben_shapiro,
        'dr_chen': response_dr_chen,
        'morgan_freeman': response_morgan_freeman,
        'sponge_bob': response_sponge_bob,
        'darth_vader': response_darth_vader
    }

    # Get the function for corresponding speaker
    response_function = response_functions.get(speaker)

    # Check if a speaker was found
    if response_functions.get(speaker):
        # Convert input to lowercase
        lowercase_user_input = user_input.lower()
        # Return output text & audio
        return response_function(lowercase_user_input)
    else:
        # Error if speaker was not found (should not occur)
        return {"text": "Sorry, I didn't catch that.", "audio": None}

@app.route('/', methods=['GET', 'POST'])
def index():
    response = {"text": "", "audio": None}
    selected_speaker = None
    if request.method == 'POST':
        speaker = request.form.get('speaker', '')
        user_input = request.form.get('user_input', '')
        response = get_response(speaker, user_input)
        selected_speaker = speaker if speaker else None
    return render_template('chat.html', response=response, selected_speaker=selected_speaker)

if __name__ == "__main__":
    app.run(debug=True)
