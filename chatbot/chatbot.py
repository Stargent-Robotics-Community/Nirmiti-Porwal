import pyttsx3
import speech_recognition as sr
import pyaudio
import random
import datetime

a = pyttsx3.init()
voices = a.getProperty('voices')
print(voices)
a.setProperty('voice',voices[0].id)
a.setProperty('volume', 1)
a.setProperty('rate', 150)

def speak(str):
    a.say(str)
    a.runAndWait()
speak(" Hello myself CookieBot !! May i know your good name?")

def record_audio():
    date = datetime.datetime.now()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        print("listening....")
        audio = r.listen(source)
        text =""
        try:
            text = r.recognize_google(audio)
            print("user said:- " + text)

        except :
            print("CookieBOt:- Sorry, can't understand!!")
            speak("I didn't get that, please rerun the code!")
        return text
text = record_audio()
name = text[11:]
speak("Hi," + name + " nice to meet you!") # my name is
print("CookieBOt:- Hi," + name + " nice to meet you!")
speak("how are you ?" + name)
print("CookieBOt:- how are you ?" + name)
text = record_audio()
color =['blue','white','pink','purple','blue','red','hotpink','magenta']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.',
         'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.',
         'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']

speak("do you want to ask me something? yes or no")
print("CookieBOt:- Do you want to ask me something? yes or no")


text = record_audio()

if text == "yes":
    text = record_audio()
    if text == "what is your name?":
        speak("My name is CookieBot")
        print("CookieBOt:- name is CookieBot")
    elif text == "tell me your favorite color":
        speak("my fav color is " + random.choice(color))
        print("CookieBOt:- my fav color is " + random.choice(color))
        speak("what's your?" + name)
        print("CookieBOt:- what's your?" + name)
        text = record_audio()
        speak("That's amazing!!")
        print("CookieBOt:- That's amazing!!")
    elif text == "tell me a joke":
        print(random.choice(jokes))
        speak(random.choice(jokes))
    elif text == "what year is it?":
        speak(date.year)
        print(date.year)
    elif text == "what day is it today?":
        speak(date.strftime("%A"))
        print("today is :-" + date.strftime("%A"))
    elif text == "what is current date and time?":
        speak(date)
        print(date)
        
elif text == "no":
    speak("that's alright! see you later!! It was nice taalking to you...")
    print("CookieBOt:- that's alright! see you later!! It was nice taalking to you...")
    
    
else:
    speak(" couldn't recognize. Please re-run the code and say yes or no!")
    print("CookieBOt:- couldn't recognize. Please re-run the code and say yes or no!")

