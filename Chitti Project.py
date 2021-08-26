import pyttsx3
import win32api
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyaudio
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")

    elif hour >= 16 and hour < 20:
        speak("Good Evening!")

    else:
        speak("Good Night!")
    speak("I am Chitti, Speed  1 terahertz, memory 1 zeta byte. Please tell me how may I help you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    with open("email.txt") as f:
        passw = f.read()
        server.login("example@gmail.com", f"{passw}")
    server.sendmail("example@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            try:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=4)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            except Exception as e:
                print(e)
                speak("Sorry mere bhai. I can't able to search this wikipedia")

        elif "hello" in query or "hey" in query:
            print("Hello Sir, How may I help you?")
            speak("Hello Sir, How may I help you?")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "D:\\punjabi video songs"
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
            print(f"Timing Now: {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            codePath = "C:\\Users\\RAJAN AGRAHARI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "email to rajan agrahari" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rajan972001@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry my friend Rajan bhai. I am not able to send this email")

        elif "play south movies" in query:
            movie_path = "D:\\Movies South+Bollywood+Hollywood\\South Movies"
            lst_movie = os.listdir(movie_path)
            os.startfile(os.path.join(movie_path, random.choice(lst_movie)))

        elif "quit" in query:
            exit()
