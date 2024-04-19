from flask import Flask, request, render_template_string, url_for
import os

app = Flask(__name__)

@app.route('/play/<filename>')
def play_audio(filename):
    # This route serves audio files from the 'static' folder
    return app.send_static_file(filename)

def respond_to_text_input(user_input):
    responses = {
        "what is your name?": "my_name.wav",
    }

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
    return render_template_string(HTML_TEMPLATE, response=response)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Simple Chatbot</title>
</head>
<body>
    <h1>Chat with our bot</h1>
    <form method="post">
        <input type="text" name="user_input" placeholder="Type your message here..." autofocus>
        <button type="submit">Send</button>
    </form>
    {% if response and response != "No appropriate response found." %}
        <p>Response: <audio controls autoplay>
            <source src="{{ response }}" type="audio/wav">
            Your browser does not support the audio element.
        </audio></p>
    {% else %}
        <p>{{ response }}</p>
    {% endif %}
</body>
</html>
'''

if __name__ == "__main__":
    app.run(debug=True)


