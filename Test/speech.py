import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    text = r.listen(source)

    try:
        recognised_text = r.recognize_google(text)
        print('Mitra: ' + recognised_text)
        if recognised_text == 'hello':
            print('BOT : Hi THERE HUMAN')
    except sr.UnknownValueError:
        print("e")
    except sr.RequestError:
        print("")
