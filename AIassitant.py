import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello, I am Jarvis. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query.lower()

def openWebsite(url):
    webbrowser.open(url)

def searchOnWikipedia(query):
    speak('Searching Wikipedia...')
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def playMusic():
    music_dir = 'C:\\Users\\akash\\Music\\fvt'
    songs = os.listdir(music_dir)
    if songs:
        random_song = random.choice(songs)
        print(f"Now playing: {random_song}")
        os.startfile(os.path.join(music_dir, random_song))
    else:
        speak("No music files found in the specified directory.")

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            search_query = query.replace("wikipedia", "")
            searchOnWikipedia(search_query)

        elif 'open moodle' in query:
            openWebsite("http://moodle.dbit.in")

        elif 'open youtube' in query:
            openWebsite("http://youtube.com")

        elif 'open google' in query:
            openWebsite("http://google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'play music' in query:
            playMusic()

        elif 'stop' in query or 'exit' in query:
            speak("Goodbye!")
            break

        else:
            speak("I'm sorry, I didn't understand that. Can you please repeat?")
