import speech_recognition as sr
import pyttsx3 as p
from messages import *

r = sr.Recognizer()
engine = p.init()

engine.say("Hello, Mitra How are you doing?")
engine.runAndWait()
with sr.Microphone() as source:
    print("SPEAK NOW")
    try:
        recognised_text = rec(source)
        if recognised_text == "hai":
            a = "hello there!"
            engine(a)
    except sr.UnknownValueError:
        print("Unknownvalueerror")
    except sr.RequestError:
        print("Requesterror")
