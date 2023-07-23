
# Jeff - A Python-based Voice Assistant

Jeff is a simple voice assistant built using Python and several third-party libraries, including the SpeechRecognition, pyttsx3, pywhatkit, wikipedia, pyjokes, and google-cloud-language libraries. With Jeff, you can perform various tasks using voice commands, such as playing music, searching the web, getting information about people, and more.

## Installation

To use Jeff, you will need to install Python 3.x and several dependencies. You can install the dependencies by running the following command:

```
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes google-cloud-language googlesearch-python
```

You will also need to set up credentials for the `google-cloud-language` library in order to use the sentiment analysis feature.

## Usage

To use Jeff, simply run the `jeff.py` script from the command line:

```
python jeff.py
```

The assistant will then listen for your voice commands and respond accordingly. The following voice commands are currently supported:

- "play [song name]": Plays a song on YouTube.
- "what time is it" or "what is the time": Tells you the current time.
- "who is [person name]": Looks up information about a person on Google or Wikipedia.
- "search [query]": Performs a Google search for the given query.
- "search news [query]": Searches for news articles on the given topic.
- "search images [query]": Searches for images of the given topic.
- "search videos [query]": Searches for videos of the given topic.
- "joke": Tells a random joke.
- "run [Python code]": Executes the given Python code.
- "date": Tells you that the assistant is not feeling well to go out today.
- "are you single": Tells you that the assistant is not capable of being in a relationship.
- Any other command or query: The assistant will try to respond appropriately based on the sentiment of the input.
## License

Jeff is released under the MIT License. See the LICENSE file for more information. 
thank you for reading and hope you like it ♥️ 
Greetings Ahmed
