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

## Elevenlabs
Using the Elevenlabs API we are able to train realistic AI voices to make the application more interactive and approachable

To use ElevenLabs Python library the following prerequisites are required:
- Install Python 3.6 or higher
- Access pip package manager
- Register with Eleven Labs

The ElevenLabs library also requires the following components for audio playback:

ffmpeg For Mac: Install using brew install
ffmpeg For Linux and Windows: Refer to https://ffmpeg.org/

mpv For Mac: Install using brew install
mpv For Linux and Windows: Refer to https://mpv.io/


To install the latest version enter the following command:

pip install elevenlabs

This will download and install the package from PyPI.


For development versions, you can install directly from GitHub:

pip install git+https://github.com/elevenlabs/elevenlabs-python


Now the library is ready to import into your code:

import elevenlabs


The next step is to authenticate with your free API key, which provides additional usage quota.

Next, you need to set the key in your Python code:

from elevenlabs import set_api_key

set_api_key("YOUR_API_KEY")


With the ElevenLabs package, you can efficiently stream audio in real-time.

To generate audio in streaming mode, use the stream=True parameter with the generate function:

from elevenlabs import generate

audio_stream = generate("Hello world", stream=True)
This returns a generator that yields audio chunks as they become available.

To play streamed audio, you need to collect the chunks and play them sequentially. For example:

from elevenlabs import generate, stream
  
audio_stream = generate("Hello world", stream=True)  
for chunk in audio_stream:  
  stream(chunk)
This allows playing audio with minimal latency, useful for real-time applications. 

ElevenLabs usually delivers latency of less than one second. Latency is as low as 500 ms in some cases.