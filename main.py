import os
import subprocess

def play_audio_response(audio_file):
    # Command to play audio on Unitree Go1 Pro using aplay utility
    os.system(f"aplay {audio_file}")

def respond_to_text_input(user_input):
    # A dictionary mapping keywords or phrases to specific audio files
    responses = {
      # Paths for audio files
      '''
        "hi": "/home/austin/Documents/AIRobotics/Project/hi_how_are_you.wav",
        "hello": "/home/austin/Documents/AIRobotics/Project/hi_how_are_you.wav",
        "what is your name?": "/home/arjun/Documents/go1/chatbot/wav_files/my_name.wav",
        "how are you?": "/home/arjun/Documents/go1/chatbot/wav_files/how_are_you.wav",
    '''
    }

    # Check if the user input matches any of the keywords or phrases
    for keyword, audio_file in responses.items():
        if keyword.lower() in user_input.lower():
            play_audio_response(audio_file)
            break
    else:
        print("No appropriate response found.")

def main():
    while True:
        # Example usage - replace this with the actual input you receive from the user
        user_input = input("Type your message: ")
        respond_to_text_input(user_input)
        # To exit the loop and stop the chatbot, type 'exit'
        if user_input.lower() == 'exit':
            break

if __name__ == "__main__":
    main()
