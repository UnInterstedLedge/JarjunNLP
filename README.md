# JarjunNLP

# Simple Audio Response Flask App

This Flask application serves as a simple chatbot that responds with audio messages based on user input. It's designed to provide pre-recorded audio responses for a fixed set of questions.

## Purpose

The application demonstrates a basic use case of Flask for creating web applications that can interact with users and provide dynamic content - in this case, audio responses.

## Setup

To get this application running on your local machine, you'll need to have Python installed, along with the following dependencies:

- Flask

You can install Flask using pip, Python's package installer:

```bash
pip install flask
```
## Running the Application
After installing Flask, you can start the application with the following command:

```bash
python main.py
```

The server will start on 'localhost' on port '5000'. You can access the application by navigating to 'http://127.0.0.1:5000/' in your web browser.

## Directory Structure 
Here is the required directory strure for the application:

```markdown
/JarjunNLP
  /static
    - my_name.wav
    - other_responses.wav
  - main.py
  - README.md
```

## Adding more responses
To add more audio responses, simply place your '.wav' files into the 'static' directory and update the 'responses' dictionary within 'main.py' file.

Example :

```python
responses = {
    "hi": "hi_response.wav",
    "how are you?": "how_are_you_response.wav",
    ...
}
```
