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
        command = recognised_text.split(" ")
        ''' Some basic commands that bot can respond
            hi there! -> Bot introduce herself
            Search (filename0 -> Bot searchs file or folder  in directory
            play (songname) -> Bot plays locally stored music
        '''
        
        if command[0] == 'hai':
            greetings()
            print("Speak Something..")
            hai_respond = rec(source)
        
        elif command[0] == 'search':
            searching(command[1])

    except sr.UnknownValueError:
        print("Unknownvalueerror")
   
    except sr.RequestError:
        print("Requesterror")
