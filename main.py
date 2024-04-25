from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/play/<filename>')
def play_audio(filename):
    # Serves audio files from the 'static' folder
    return app.send_static_file(filename)

def get_response(speaker, user_input):
    # Simple responses based on the speaker
    responses = {
        'ben_shapiro': "Hello, this is Ben Shapiro. How can I help you?",
        'joe_biden': "Greetings from Joe Biden. What would you like to discuss?",
        'morgan_freeman': "Morgan Freeman here, it's a pleasure to meet you.",
        'donald_trump': "It's Donald Trump. You're talking to the best, believe me."
    }
    return responses.get(speaker, "") if user_input.lower() == 'hi' else "Sorry, I didn't catch that."

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ''
    selected_speaker = None
    if request.method == 'POST':
        speaker = request.form.get('speaker', '')
        user_input = request.form.get('user_input', '')
        response = get_response(speaker, user_input)
        selected_speaker = speaker if speaker else None
    return render_template('chat.html', response=response, selected_speaker=selected_speaker)

if __name__ == "__main__":
    app.run(debug=True)
