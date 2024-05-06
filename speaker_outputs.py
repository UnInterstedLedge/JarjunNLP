from flask import url_for

# Ben Shapiro
def response_ben_shapiro(user_input):
    if user_input == 'hi' or user_input == 'hello':
        return {"text": "Hello, this is Ben Shapiro. How can I help you?", "audio": url_for('serve_audio', filename="fileName.wav")}
    else:
        return {"text": "I didn't understand that.", "audio": None}

# Dr.Chen
def response_dr_chen(user_input):
    if user_input == 'hi' or user_input == 'hello':
        return {"text": "Good day ladies and gentlemen, it's Dr.Chen", "audio": url_for('serve_audio', filename="fileName.wav")}
    else:
        return {"text": "I didn't understand that.", "audio": None}

# Morgan Freeman
def response_morgan_freeman(user_input):
    if user_input == 'hi' or user_input == 'hello':
        return {"text": "Morgan Freeman here, it's a pleasure to meet you.", "audio": url_for('serve_audio', filename="mf-hello.wav")}
    else:
        return {"text": "I didn't understand that.", "audio": None}

# Sponge Bob
def response_sponge_bob(user_input):
    if user_input == 'hi' or user_input == 'hello':
        return {"text": "It's Sponge Bob. You're talking to the best patty flipper.", "audio": url_for('serve_audio', filename="fileName.wav")}
    else:
        return {"text": "I didn't understand that.", "audio": None}
