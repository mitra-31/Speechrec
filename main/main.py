import speech_recognition as sr
import pyttsx3 as p
from messages import *

r = sr.Recognizer()
engine = p.init()

#engine.say("Hello, Mitra How are you doing?")
#engine.runAndWait()
with sr.Microphone() as source:
    text = r.listen(source)

    try:
        recognised_text = r.recognize_google(text)
        if recognised_text == "play music":
            print("fuckoff")
    except sr.UnknownValueError:
        print("Unknownvalueerror")
    except sr.RequestError:
        print("Requesterror")