import speech_recognition as sr
import pyttsx3 as p
from messages import *

r = sr.Recognizer()
engine = p.init()

engine.say("Hello, Mitra How are you doing?")
engine.runAndWait()
with sr.Microphone() as source:
<<<<<<< HEAD
    print("SPEAK NOW")
=======
    print("Speak now")
>>>>>>> 52d728325322da557808117f671bf8d2816faf44
    text = r.listen(source)

    try:
        recognised_text = r.recognize_google(text)
        if recognised_text == "music":
           engine.say(music())
    except sr.UnknownValueError:
        print("Unknownvalueerror")
    except sr.RequestError:
        print("Requesterror")
