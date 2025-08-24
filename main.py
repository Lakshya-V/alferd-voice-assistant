import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import musiclib
import requests
from openai import OpenAI
import datetime as dt
from _whatsapp_ import msg
from _spotify_ import play, play_pause
from _brave_ import search

# Can use whisper for speech recognition and gtts for better text to speech but it is paid api key for open ai also helps a lot. you can make
# this project better over time to make it greater and better using pygame os etc to clarify issues and other things


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
            print("LISTENING...... Please say pause the song or play the song or anything else to sart one")
            audio = r.listen(source)# timeout= 2 timpephraseout = 1
            song = r.recognize_google(audio, language="en-IN")
            print(song)
        if song == 'pause the song' :
            speak("pausing the song")
            play_pause()
        elif song == 'play the song' :
            speak("playing the song")
            play_pause()
        else :
            speak(f"playing {song}")
            play(song)
    if "tell date and time" in c.lower() :
        speak(f"sir the date and time right now is {dt.datetime.now()}")
    if "open google" in c.lower() :
        webbrowser.open("https://google.com")
    if "open linkedin" in c.lower() :
        webbrowser.open("https://linkedin.com")
    if "open youtube" in c.lower() :
        webbrowser.open("https://youtube.com")
    if "open instagram" in c.lower() :
        webbrowser.open("https://instagram.com")
    if c.lower().startswith("play") :
        song = c.lower().split(" ") [1]
        webbrowser.open(musiclib.music[song])
    if "news" in c.lower() :
        r =  requests.get("")# use news api for making it function... or use openai only for getting news
    if "open whatsapp" in c.lower() :
        speak("opening whatsapp sir please say write message if you want to send a message")
        open("whatsapp")
    if "write message" in c.lower() :
        speak("sir whom should i write the message for")
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print("LISTENING...... Please say the reciever name")
            audio = r.listen(source)# timeout= 2 timpephraseout = 1
            person = r.recognize_google(audio, language="en-IN")
            print(person)
            if person.lower()  == "man ji" :
                person = "ma ji"
        speak(f"say the message for {person} sir")
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print("LISTENING...... YOUR MESSAGE")
            audio = r.listen(source)# timeout= 2 timpephraseout = 1
            word = r.recognize_google(audio, language="en-IN")
            print(word)
        msg(word,person)
    if "open brave" in c.lower() :
        speak("sir do you want to search something")
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print("LISTENING...... YOUR DECISION")
            audio = r.listen(source)# timeout= 2 timpephraseout = 1
            decision = r.recognize_google(audio, language="en-IN")
            print(decision)
            if "yes" in decision.lower() :
                speak("sir please state you query")
                with sr.Microphone() as source:
                    r = sr.Recognizer()
                    print("LISTENING...... YOUR QUERY")
                    audio = r.listen(source)# timeout= 2 timpephraseout = 1
                    query = r.recognize_google(audio, language="en-IN")
                    print(query)
                speak("searching the query sir")
                search(query)
            else :
                speak("okay sir")
    else :
        #Let openi handle the request
        # ai_process(c)
        pass

def open(app) :
    os.system(f"start {app}:") #only for standard apps

def ai_process(c) :
    client = OpenAI(
        api_key="",
        )
    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system","content": "You are a virual assistant named alferd and who is master in skills and doing general tasks like alexa and googlecloud.give short response please"},
            {"role": "user","content": c}]
        )

    content = (completion.choices[0].message.content)
    speak(content)

def speak(text) :
    engine.say(text)
    engine.runAndWait()

def final(stop_event=None):
    while not stop_event.is_set():
        print("Assistant running...")

        speak("Hi sir ALFERD here")
        while not stop_event.is_set():
                
            # Recognize speech using whisper
            try:
                # Obtain audio from the microphone
                with sr.Microphone() as source:
                    r = sr.Recognizer()
                    print("LISTENING......")
                    audio = r.listen(source)# timeout= 2 timpephraseout = 1
                word = r.recognize_google(audio, language="en-IN")
                print(word)
                if "alfred" in word.lower().strip() :
                    speak("YES SIR")
                    with sr.Microphone() as source:
                        r = sr.Recognizer()
                        print("ALFRED ACTIVE......")
                        audio = r.listen(source)
                        command = r.recognize_google(audio, language="english-in")
                    ProcessCommand(command)
                    

            except sr.UnknownValueError:

                print("ALFERD COULD NOT UNDERSTAND WHAT YOU SAID...")
            except Exception as e:
                print(f"ERROR; {e}") 
            
            if stop_event is not None and stop_event.is_set():
                break 


