from flask import url_for

# Ben Shapiro
def response_ben_shapiro(user_input):
    if user_input == 'Hi' or user_input == 'hi' or user_input == 'Hello' or user_input == 'hello':
        return {"text": "Oh, hello there, liberal! I am Ben Shapiro. My motto is “facts don’t care about your feelings.” I am also very short. But my wit and intellect is much greater than my height", "audio": url_for('serve_audio', filename = "BHello.mp3")}
    
    elif user_input == 'Give me some advice' or user_input == 'give me some advice':
        return {"text": "Well, let me tell you, my best life advice would be to never be afraid to speak your mind. Don't let anyone silence you or tell you what to think or how to act. Instead, be confident in who you are and what you believe in. You'll never go wrong with that.", "audio": url_for('serve_audio', filename = "BAdvice.mp3")}
    
    elif user_input == 'How do you feel about liberals' or 'how do you feel about liberals':
        return {"text": "Oh, you bet I have to comment on liberals. As you might expect, I am not one of them, ha! Ha!", "audio": url_for('serve_audio', filename = "BLibs.mp3")}
    
    elif user_input == 'How are you' or 'how are you':
        return {"text": "I am doing quite well, thank you for asking! It’s always nice to get some positive attention.", "audio": url_for('serve_audio', filename = "BHowYou.mp3")}
    
    elif user_input == 'Who are you' or 'who are you':
        return {"text": "I am Ben Shapiro, a conservative thinker and pundit. I fight to ensure that conservative values and ideas are always given a fair hearing in the mainstream media. But beyond all that, I am a husband, father, and proud American. And it is my pleasure to meet you.", "audio": url_for('serve_audio', filename = "BGreeting.mp3")}

    else:
        return {"text": "I didn't understand that.", "audio": None}

# Dr.Chen
def response_dr_chen(user_input):
    if user_input == 'hi' or user_input == 'hello':
        return {"text": "Hello, good to see you!", "audio": url_for('serve_audio', filename="CHello.mp3")}
    
    elif user_input == "How are you?" or "how are you?":
         return {"text": "I'm doing alright, thakns for asking", "audio": url_for('serve_audio', filename="CHowYou.mp3")}

    elif user_input == "Who are your favorite students?" or user_input == "who are your favorite students?":
        return {"text": "My favorite students are Arjun, Tanner, Kelsey, Jacob, and Claire. They are the wisest students I ever met.", "audio": url_for('serve_audio', filename="CFav.mp3")}
    
    elif user_input == "What do you think of this project?" or user_input == "what do you think of this project?":
        return {"text": "This is the best project I 've ever seen, I'm honored to present you with the noble peace prize. Congratulations!", "audio": url_for('serve_audio', filename="CCongrats.mp3")}
    
    else:
        return {"text": "I didn't understand that.", "audio": None}

# Morgan Freeman
def response_morgan_freeman(user_input):
    if user_input == 'hi' or user_input == 'hello':
        return {"text": "Hello, and thank you for reaching out and saying hello.", "audio": url_for('serve_audio', filename="MHello.mp3")}
    
    elif user_input == "How are you?" or user_input == "how are you?":
        return {"text": "I'm doing well, thank you for asking. I'm feeling good and things are going well overall. Hope everything is going well for you too!! ", "audio": url_for('serve_audio', filename="MHowYou.mp3")}    

    elif user_input == "Who are you?" or user_input == "who are you?":
        return {"text": "My name is Morgan Freeman and I am an actor and filmmaker. I'm known for my work in films like the Shawshank Redemption, Deep Impact and the Dark Knight Trilogy", "audio": url_for('serve_audio', filename="MGreeting.mp3")}
    
    elif user_input == "What is some life adivce you can give?" or user_input == "what is some life adivce you can give?":
        return {"text": "Get busy living or get busy dying", "audio": url_for('serve_audio', filename="MShaw.mp3")}
    
    else:
        return {"text": "I didn't understand that.", "audio": None}

# Sponge Bob
def response_sponge_bob(user_input):
    if user_input == 'hi' or user_input == 'hello':
        return {"text": "Hi there! Have a wonderfuld day today!!", "audio": url_for('serve_audio', filename="SHello.mp3")}
    
    elif user_input == "What is your name?" or user_input == "what is your name?":
        return {"text": "My name is Sponge-bob square pants. Nice to meet you buddy!", "audio": url_for('serve_audio', filename="SGreeting.mp3")}
    
    elif user_input == "How are you?" or user_input == "how are you?":
        return {"text": "I'm doing pretty good,just living the life you know, ejoying the sun, cathcing the jelly fish and serving up some delicous Krabby-Patties at the Krusty Krab!!", "audio": url_for('serve_audio', filename="SHowYou.mp3")}
    
    elif user_input == "What's the secret formula for the Krabby Patty?" or user_input == "what's the secret formula for the krabby patty?":
        return {"text": "Uhhh...I don't think I can tellyou that. Maybe try applying for the Krusty Krab and maybe you will learn one day!!", "audio": url_for('serve_audio', filename="SHowYou.mp3")}
    
    else:
        return {"text": "I didn't understand that.", "audio": None}
