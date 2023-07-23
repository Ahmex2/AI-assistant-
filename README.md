# AI Assistant

This is a Python script that implements a simple voice-controlled AI assistant using the Google Cloud Speech-to-Text API and various Python libraries. The assistant is capable of performing a variety of tasks, such as searching the internet, playing music, telling jokes, and more.

## Installation

To use the AI assistant, you will need to install the following libraries using pip:

- `speechrecognition`
- `pyttsx3`
- `pywhatkit`
- `wikipedia`
- `pyjokes`
- `google-cloud-language`

You can install these libraries by running the following command:

```
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes google-cloud-language
```

## Usage

To use the AI assistant, simply run the `AI_assistant.py` script using Python:

```
python AI_assistant.py
```

Once the script is running, the assistant will listen for your voice commands. To activate the assistant, say "Jeff" followed by your command. For example, you can say "Jeff, search for Python tutorials" to ask the assistant to search for Python tutorials on the internet.

The assistant is capable of performing a variety of tasks, such as:

- Searching the internet using the `search()` function from the `pywhatkit` library
- Searching for news articles, images, or videos related to a given query using custom functions
- Playing music using the `playonyt()` function from the `pywhatkit` library
- Answering questions by searching Wikipedia using the `wikipedia` library
- Telling jokes using the `pyjokes` library
- Running Python code using the `exec()` function

You can customize the assistant further by modifying the script to add more features or change the behavior of existing features.

## Credits

This script was inspired by various online resources and tutorials on building voice-controlled AI assistants using Python. Here are some of the key resources that were used to develop this script:

- [SpeechRecognition library ↗](https://github.com/Uberi/speech_recognition)
- [pyttsx3 library ↗](https://github.com/nateshmbhat/pyttsx3)
- [pywhatkit library ↗](https://github.com/Ankit404butfound/PyWhatKit)
- [wikipedia library ↗](https://github.com/wikipedia/wikipedia-python)
- [pyjokes library ↗](https://github.com/pyjokes/pyjokes)
- [Google Cloud Speech-to-Text API ↗](https://cloud.google.com/speech-to-text) 

## License
MIT License 
