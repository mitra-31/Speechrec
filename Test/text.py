import pyttsx3 as p

engine = p.init()
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)
engine.say('HOW you doing? Master.')
engine.runAndWait()