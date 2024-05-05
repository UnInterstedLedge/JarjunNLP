from flask import url_for

# Ben Shapiro
def response_ben_shapiro(user_input):
    if user_input == 'hi':
        return {"text": "Hello, this is Ben Shapiro. How can I help you?", "audio": url_for('serve_audio', filename="mf-hello.wav")}
    else:
        return {"text": "I didn't understand that.", "audio": None}

# Joe Biden
def response_joe_biden(user_input):
    if user_input == 'hi':
        return {"text": "Greetings from Joe Biden. What would you like to discuss?", "audio": url_for('serve_audio', filename="mf-hello.wav")}
    else:
        return {"text": "I didn't understand that.", "audio": None}

# Morgan Freeman
def response_morgan_freeman(user_input):
    if user_input == 'hi':
        return {"text": "Morgan Freeman here, it's a pleasure to meet you.", "audio": url_for('serve_audio', filename="mf-hello.wav")}
    else:
        return {"text": "I didn't understand that.", "audio": None}

# Donald Trump
def response_donald_trump(user_input):
    if user_input == 'hi':
        return {"text": "It's Donald Trump. You're talking to the best, believe me.", "audio": url_for('serve_audio', filename="mf-hello.wav")}
    else:
        return {"text": "I didn't understand that.", "audio": None}