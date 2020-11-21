import pyttsx3 as p
import speech_recognition as sr
import os

r = sr.Recognizer()
eng = p.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[1].id)
eng.setProperty('rate',150)

def greetings():
    eng.say("Go ahead I'm Hearing you")
    eng.runAndWait()

def engine(voice):
    eng.say(voice)
    eng.runAndWait()

def rec(source):
    text = r.listen(source)
    recognised_text = r.recognize_google(text)
    print(recognised_text)
    return recognised_text

def agian():
    eng.say("Try again!")
    eng.runAndWait()