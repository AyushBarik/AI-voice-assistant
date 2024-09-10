
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import shutil
import sys
from googlesearch import search
from dotenv import load_dotenv
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init()  # SAPI5 (Speech Application Programming Interface) by Microsoft for Windows.
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)  # 1 = female voice, 0 = male voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!") 

    else:
        speak("Good Evening Sir!") 

    assname = "assistant"
    speak("I'm your intelligent Assistant Luna!")
    speak(assname)

def username():
    speak("What should I call you?")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    
    print("#####################".center(columns))
    print(f"Welcome Mr. {uname}".center(columns))
    print("#####################".center(columns))
    
    speak("How can I help you, Sir")

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
        print(e) 
        print("Unable to Recognize your voice.") 
        return "None"
    
    return query

if __name__ == '__main__':
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()
    wishMe()
    username()
    
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif "will you be my gf" in query or "will you be my bf" in query:   
            speak("touch some grass")
            
        elif 'bye' in query:
            sys.exit()





