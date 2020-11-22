import pyttsx3 as p
import speech_recognition as sr
import os

r = sr.Recognizer()
eng = p.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[1].id)
eng.setProperty('rate',150)

def greetings():
    eng.say("Hi there! I'm Rax Your PERSONAL ASSISTANCE")
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
    eng.say("TELL SOMETHING")
    eng.runAndWait()


def searching(file):
    print("Searching " + file +"........")
    val = file.lower()
    path = 'D:\VS-code'
    con = True
    while con:
        for root,dir,files in os.walk(path):
            for f in dir:
                print(f)
                if str(f) == str(val):
                    print(os.path.join(path,val))
                    con = False
                    eng.say("found")
                    eng.runAndWait()
        break
    else:
        eng.say("Not found")
        eng.runAndWait()    