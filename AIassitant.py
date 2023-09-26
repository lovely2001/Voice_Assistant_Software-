import pyttsx3  # pip install pyttsx3   -----------pyttsx3 is a text-to-speech conversion library in Python. 
import speech_recognition as sr  # pip install speechRecognition        --- for taking input from microphone
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')                  #sapi5-speech API -- for windows-- PROVIDED BY MICROSSOFT
voices = engine.getProperty('voices')
# print(voices[1].id)                           #2VOICES IN SYSTEM - MALE,FEAMLE
engine.setProperty('voice', voices[0].id)     


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello I am Jarvis , How may I help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1                      #seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()

while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open moodle' in query:
            webbrowser.open("moodle.dbit.in")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\akash\\Music\\fvt'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[4]))