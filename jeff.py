import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from google.cloud import language
import googlesearch

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
client = language.LanguageServiceClient()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('I am listening, how may I assist you?')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jeff' in command:
                command = command.replace('jeff', '')
                print(command)
    except:
        pass
    return command

def analyze_sentiment(text):
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment.score
    return sentiment

def search_google(query):
    search_url = 'https://www.google.com/search?q='
    url = search_url + query
    results = googlesearch.search(url, num_results=1)
    if results:
        return results[0]
    else:
        return None
def run_jeff():
    command = take_command()
    print(command)
    sentiment = analyze_sentiment(command)
    if 'run' in command:
        code = command.replace('run', '')
        try:
            exec(code)
            talk('Code executed successfully.')
        except Exception as e:
            talk(f'Error executing the code: {e}')
    elif 'play' in command:
        song = command.replace('play', '')
        talk(f'Alright, playing {song} for you!')
        pywhatkit.playonyt(song)
    elif 'what time is it' in command or 'what is the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'The current time is {time}.')
    elif 'who is' in command:
        person = command.replace('who is', '')
        result = search_google(person)
        if result:
            talk(f'{person} is {result}.')
        else:
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
    elif 'search' in command:
        query = command.replace('search', '')
        talk(f'Searching for {query}.')
        pywhatkit.search(query)
    elif 'search news' in command:
        query = command.replace('search news', '')
        talk(f'Searching for news articles on {query}.')
        pywhatkit.search(f'{query} news')
    elif 'search images' in command:
        query = command.replace('search images', '')
        talk(f'Searching for images of {query}.')
        pywhatkit.search(f'{query} images')
    elif 'search videos' in command:
        query = command.replace('search videos', '')
        talk(f'Searching for videos of {query}.')
        pywhatkit.search(f'{query} videos')
    elif 'date' in command:
        talk('I am sorry, I am not feeling well to go out today.')
    elif 'are you single' in command:
        talk('I am not capable of being in a relationship, but I am always here to assist you.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        if sentiment < -0.2:
            talk('I am sorry, I did not understand what you said. Could you please repeat that?')
        else:
            talk('I am sorry, I could not recognize the command. Can you please try again?')
while True:
    run_jeff()