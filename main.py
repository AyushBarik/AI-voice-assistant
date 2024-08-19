import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')  # SAPI5 (Speech Application Programming Interface) by Microsoft for Windows.
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)  # 1 = female voice, 0 = male voice

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

    assname = "assistant"
    speak("I am an assistant")
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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    
    # Use environment variables or a secure method to handle sensitive information.
    EMAIL = os.getenv('EMAIL')  # Get the email from environment variables
    PASSWORD = os.getenv('PASSWORD')  # Get the password from environment variables
    
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, to, content)
    server.close()

if __name__ == '__main__':
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()
    wishMe()
    username()





