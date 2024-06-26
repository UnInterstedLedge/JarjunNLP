from flask import url_for

# Ben Shapiro
def response_ben_shapiro(user_input):
    if user_input == 'Hi' or user_input == 'hi' or user_input == 'Hello' or user_input == 'hello':
        return {"text": "Oh, hello there, liberal! I am Ben Shapiro. My motto is “facts don't care about your feelings.” I am also very short. But my wit and intellect is much greater than my height.", "audio": url_for('serve_audio', filename = "BHello.wav")}
    
    elif user_input == 'Give me some advice' or user_input == 'give me some advice':
        return {"text": "Well, let me tell you, my best life advice would be to never be afraid to speak your mind. Don't let anyone silence you or tell you what to think or how to act. Instead, be confident in who you are and what you believe in. You'll never go wrong with that.", "audio": url_for('serve_audio', filename = "BAdvice.wav")}
    
    elif user_input == 'How do you feel about liberals' or user_input == 'how do you feel about liberals':
        return {"text": "Oh, you bet I have to comment on liberals. As you might expect, I am not one of them, ha! ha!", "audio": url_for('serve_audio', filename = "BLibs.wav")}
    
    elif user_input == 'How are you' or user_input == 'how are you':
        return {"text": "I am doing quite well, thank you for asking! It's always nice to get some positive attention.", "audio": url_for('serve_audio', filename = "BHowYou.wav")}
    
    elif user_input == 'Who are you' or user_input == 'who are you':
        return {"text": "I am Ben Shapiro, a conservative thinker and pundit. I fight to ensure that conservative values and ideas are always given a fair hearing in the mainstream media, but beyond all that, I am a husband, father, and proud American, and it is my pleasure to meet you.", "audio": url_for('serve_audio', filename = "BGreeting.wav")}

    else:
        return {"text": "I didn't understand that.", "audio": None}

# Dr.Chen
def response_dr_chen(user_input):
    if user_input == 'hi' or user_input == 'hello':
        return {"text": "Hello, good to see you!", "audio": url_for('serve_audio', filename="CHello.wav")}
    
    elif user_input == "How are you?" or user_input == "how are you?":
         return {"text": "I'm doing alright, thanks for asking.", "audio": url_for('serve_audio', filename="CHowYou.wav")}

    elif user_input == "Who are your favorite students?" or user_input == "who are your favorite students?":
        return {"text": "My favorite students are Arjun, Tanner, Kelsey, Jacob, and Claire. They are the wisest students I ever met.", "audio": url_for('serve_audio', filename="CFav.wav")}
    
    elif user_input == "What do you think of this project?" or user_input == "what do you think of this project?":
        return {"text": "This is the best project I 've ever seen, I'm honored to present you with the Nobel Peace Prize. Congratulations!", "audio": url_for('serve_audio', filename="CCongrats.wav")}
    
    else:
        return {"text": "I didn't understand that.", "audio": None}

# Morgan Freeman
def response_morgan_freeman(user_input):
    if user_input == 'hi' or user_input == 'hello':
        return {"text": "Hello, and thank you for reaching out and saying hello.", "audio": url_for('serve_audio', filename="MHello.wav")}
    
    elif user_input == "How are you?" or user_input == "how are you?":
        return {"text": "I'm doing well, thank you for asking. I'm feeling good and things are going well overall. Hope everything is going well for you too!!", "audio": url_for('serve_audio', filename="MHowYou.wav")}    

    elif user_input == "Who are you?" or user_input == "who are you?":
        return {"text": "My name is Morgan Freeman and I am an actor and filmmaker. I'm known for my work in films like the Shawshank Redemption, Deep Impact, and the Dark Knight Trilogy.", "audio": url_for('serve_audio', filename="MGreeting.wav")}
    
    elif user_input == "What is some life adivce you can give?" or user_input == "what is some life adivce you can give?":
        return {"text": "Get busy living or get busy dying.", "audio": url_for('serve_audio', filename="MShaw.wav")}
    
    else:
        return {"text": "I didn't understand that.", "audio": None}

# Sponge Bob
def response_sponge_bob(user_input):
    if user_input == 'hi' or user_input == 'hello':
        return {"text": "Hi there! Have a wonderfuld day today!!", "audio": url_for('serve_audio', filename="SHello.wav")}
    
    elif user_input == "What is your name?" or user_input == "what is your name?":
        return {"text": "My name is Sponge-Bob Square Pants. Nice to meet you buddy!", "audio": url_for('serve_audio', filename="SGreeting.wav")}
    
    elif user_input == "How are you?" or user_input == "how are you?":
        return {"text": "I'm doing pretty good, just living the life you know, enjoying the sun, catching the jelly fish and serving up some delicous Krabby-Patties at the Krusty Krab!!", "audio": url_for('serve_audio', filename="SHowYou.wav")}
    
    elif user_input == "What's the secret formula for the Krabby Patty?" or user_input == "what's the secret formula for the krabby patty?":
        return {"text": "Uhhh...I don't think I can tell you that. Maybe try applying for the Krusty Krab and maybe you will learn one day!!", "audio": url_for('serve_audio', filename="SHowYou.wav")}
    
    else:
        return {"text": "I didn't understand that.", "audio": None}

# Darth Vader
def response_darth_vader(user_input):
    if user_input == 'hi' or user_input == 'hello':
        return {"text": "What is it that you want? Do not speak to me so casually!!", "audio": url_for('serve_audio', filename="VHello.wav")}
    
    elif user_input == "How are you?" or user_input == "how are you?":
        return {"text": "I am as I must be, your concern is unnessary!", "audio": url_for('serve_audio', filename="VHowYou.wav")}    

    elif user_input == "Who are you?" or user_input == "who are you?":
        return {"text": "I am Darth Vader, Lord of the Sith. You will find that your defense is no match for the power of the dark side.", "audio": url_for('serve_audio', filename="VGreeting.wav")}
    
    elif user_input == "You're not my father" or user_input == "you're not my father":
        return {"text": "Search your feelings, you know it to be true. I am your father.", "audio": url_for('serve_audio', filename="VQuote.wav")}
    
    else:
        return {"text": "I didn't understand that.", "audio": None}
