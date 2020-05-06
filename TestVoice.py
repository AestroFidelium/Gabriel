import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("DA : ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"YOU SAY A : {text}")
    except:
        print("fck u")
    pass
