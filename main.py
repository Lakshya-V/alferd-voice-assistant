import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import datetime as dt
from spotify import play, play_pause



recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")
engine.setProperty('voice', voices[0].id) 
engine.setProperty('rate', 125)


def ProcessCommand(c) :
    if "open spotify" in c.lower() :
        speak("Spotify opened sir tell the name of the song you want to play")
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print("LISTENING...... Please say pause/play the song or mention the name of music")
            audio = r.listen(source)
            song = r.recognize_google(audio, language="en-IN")
            print(song)
        if song == 'pause the music' :
            speak("pausing the music")
            play_pause()
        elif song == 'play the music' :
            speak("playing the music")
            play_pause()
        else :
            speak(f"playing {song}")
            play(song)
    if "tell date and time" in c.lower() :
        now = dt.datetime.now()
        hour = now.strftime('%I')
        minute = now.strftime('%M')
        ampm = now.strftime('%p').lower()
        date_str = now.strftime('%A, %d %B %Y')
        time_str = f"It's {hour}:{minute} {ampm} on {date_str}."
        speak(f"Sir, the current time and date is {time_str}")
    if "open google" in c.lower() :
        webbrowser.open("https://google.com")
    if "open linkedin" in c.lower() :
        webbrowser.open("https://linkedin.com")
    if "open youtube" in c.lower() :
        webbrowser.open("https://youtube.com")
    if "open instagram" in c.lower() :
        webbrowser.open("https://instagram.com")
    else :
        #Let openi handle the request
        ai_process(c)

def open(app) :
    os.system(f"start {app}:") 

def speak(text) :
    engine.say(text)
    engine.runAndWait()

def final(stop_event=None):
    while not stop_event.is_set():
        print("Assistant running...")

        speak("Hi sir ALFERD here")
        while not stop_event.is_set():
            try:
                with sr.Microphone() as source:
                    r = sr.Recognizer()
                    print("LISTENING......")
                    audio = r.listen(source)
                word = r.recognize_google(audio, language="en-IN")
                print(word)
                if "alfred" in word.lower().strip() :
                    speak("YES SIR")
                    with sr.Microphone() as source:
                        r = sr.Recognizer()
                        print("ALFERD ACTIVE......")
                        audio = r.listen(source)
                        command = r.recognize_google(audio, language="english-in")
                    ProcessCommand(command)
                    

            except sr.UnknownValueError:

                print("ALFERD COULD NOT UNDERSTAND WHAT YOU SAID...")
            except Exception as e:
                print(f"ERROR; {e}") 
            
            if stop_event is not None and stop_event.is_set():
                break 


