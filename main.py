import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime as dt
import requests
import screen_brightness_control as sbc
import os
from word2number import w2n
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from openai import OpenAI
from spotify import play, play_pause
from whatsapp import msg



recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")
engine.setProperty('voice', voices[0].id) 
engine.setProperty('rate', 125)


def ProcessCommand(c) :

    if "tell date and time" in c.lower() :
        now = dt.datetime.now()
        hour = now.strftime('%I')
        minute = now.strftime('%M')
        ampm = now.strftime('%p').lower()
        date_str = now.strftime('%A, %d %B %Y')
        time_str = f"It's {hour}:{minute} {ampm} on {date_str}."
        speak(f"Sir, the current time and date is {time_str}")

    if "open mail" in c.lower() :
        webbrowser.open("https://mail.google.com")
        
    if "open github" in c.lower() :
        webbrowser.open("https://github.com")

    if "open google" in c.lower() :
        speak("sir what do you want to search on google")
        with sr.Microphone() as source :
            r = sr.Recognizer()
            print("LISTENING... google search")
            audio = r.listen(source)
            search_query = r.recognize_google(audio, language="en-IN")
            print(f"User wants to search: {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

    if "open linkedin" in c.lower() :
        webbrowser.open("https://linkedin.com")

    if "open youtube" in c.lower() :
        speak("sir do you want me to search anything on youtube")
        with sr.Microphone() as source :
            r = sr.Recognizer()
            print("LISTENING... decision")
            audio = r.listen(source)
            decision = r.recognize_google(audio, language="en-IN")
            print(decision)
        if "yes" in decision.lower() :
            speak("what do you want to search on youtube")
            with sr.Microphone() as source :
                r = sr.Recognizer()
                print("LISTENING... youtube search")
                audio = r.listen(source)
                yt_query = r.recognize_google(audio, language="en-IN")
                print(f"User wants to search: {yt_query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={yt_query}")

    if "open instagram" in c.lower() :
        webbrowser.open("https://instagram.com")
    
    if "change brightness" in c.lower().strip() :
        brightness = sbc.get_brightness()
        speak (f"Current brightness is {brightness} percent.how much would you like brightness to be?")
        print("FOR SINGLE DIGIT BRIGHTNESS SAY ZERO BEFORE THE NUMBER LIKE 0 5 FOR 5% BRIGHTNESS")
        with sr.Microphone() as source :
            r = sr.Recognizer()
            print("LISTENING... brightness change")
            audio = r.listen(source)
            percent = r.recognize_google(audio, language="en-IN")
        try :
            sbc.set_brightness(smart_num_convert(percent))
            speak(f"Brightness changed to {percent} percent")
        except Exception as e :
            print(f"Error changing brightness: {e}")
            speak("Sorry, I couldn't change the brightness.")
        
    if "change volume" in c.lower().strip() :
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = interface.QueryInterface(IAudioEndpointVolume)
        vol = volume.GetMasterVolumeLevel()
        speak(f"Current volume level is {vol}. how much would you like it to be?")
        with sr.Microphone() as source :
            r = sr.Recognizer()
            print("LISTENING... speak mute or unmute or specify the percent volume")
            print("FOR SINGLE DIGIT VOLUME SAY ZERO BEFORE THE NUMBER LIKE 0 5 FOR 5% VOLUME")
            audio = r.listen(source)
            percent = r.recognize_google(audio, language="en-IN")
        if percent.lower().strip() == "mute" :
            volume.SetMute(1, None)
            speak("Volume muted")
        elif percent.lower().strip() == "unmute" :
            volume.SetMute(0, None)
            speak("Volume unmuted")
        else :
            try :
                percentage = smart_num_convert(percent)
                if 0 <= percentage <= 100 :
                    volume.SetMasterVolumeLevelScalar(percentage / 100, None)
                    speak(f"Volume changed to {percentage} percent")
                else :
                    speak("Please specify a volume between 0 and 100.")
            except Exception as e :
                print(f"Error changing volume: {e}")
                speak("Sorry, I couldn't change the volume.")

    if "open spotify" in c.lower() :
        speak("Spotify opened sir tell the name of the song you want to play")
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print("LISTENING...... Please say pause/play the song or mention the name of song")
            audio = r.listen(source)
            song = r.recognize_google(audio, language="en-IN")
            print(song)
        if song == 'pause the song':
            speak("pausing the song")
            play_pause()
        elif song == 'play the song':
            speak("playing the song")
            play_pause()
        else :
            speak ("please tell the position of the song when the search results are shown")
            play(song)
            speak(f"playing {song}")
    
    if "write message" in c.lower():
        speak("sir whom should i write the message for")
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print("LISTENING...... Please say the receiver name")
            audio = r.listen(source)
            person = r.recognize_google(audio, language="en-IN")
            print(person)
        speak(f"say the message for {person} sir")
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print("LISTENING...... YOUR MESSAGE")
            audio = r.listen(source)
            word = r.recognize_google(audio, language="en-IN")
            print(word)
        msg(word, person)
    
    if " tell news" in c.lower() :
        speak("Which topic do you want news about? Please keep it short.")
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print("LISTENING... News topic")
            audio = r.listen(source)
            topic = r.recognize_google(audio, language="en-IN")
            print(f"User asked for news on: {topic}")
        api_key = ""  # Replace with your NewsAPI key
        url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}&pageSize=1"
        try:
            response = requests.get(url)
            data = response.json()
            if data.get("articles"):
                article = data["articles"][0]
                title = article.get("title", "No title")
                news_text = f"Here is a news headline about {topic}: {title}"
                speak(news_text)
            else:
                speak(f"Sorry, I couldn't find news about {topic}.")
        except Exception as e:
            print(f"Error fetching news: {e}")
            speak("Sorry, there was an error fetching the news.")

    if "take note" in c.lower():
        speak("What would you like me to note down?")
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print("LISTENING... Your note")
            audio = r.listen(source)
            note = r.recognize_google(audio, language="en-IN")
            print(f"Note: {note}")
        with open("notes.txt","a") as f:
            f.write(note + "\n")
        speak("Your note has been saved.")

    if "clear notes" in c.lower():
        try:
            open("notes.txt", "w").close() 
            speak("All notes have been cleared.")
        except Exception as e:
            print(f"Error clearing notes: {e}")
            speak("Sorry, there was an error clearing the notes.")
            
    if "read notes" in c.lower():
        try:
            with open("notes.txt", "r") as f:
                notes = f.readlines()
            if notes:
                speak("Here are your notes:")
                for n in notes:
                    speak(n.strip())
            else:
                speak("You have no notes yet.")
        except FileNotFoundError:
            speak("You have no notes yet.")
            
    else :
        # Let openi handle the request
        speak("do you want me to utilise openai for this?")
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print("LISTENING... your decision")
            audio = r.listen(source)
            decision = r.recognize_google(audio, language="en-IN")
            print(decision)
            if "yes" in decision.lower() :
                ai_process(c)
            else :
                speak("Okay, I won't use OpenAI for this request.")

def ai_process(c) :
    client = OpenAI(
        api_key="",# enter your openai api key here
    )
    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You are Alferd, a friendly and conversational virtual assistant. Respond naturally and briefly, as if talking to a human. Avoid robotic or overly formal language."},
            {"role": "user", "content": c}
        ]
    )
    content = completion.choices[0].message.content.strip()
    speak(content)

def smart_num_convert(s):
    s = s.strip().lower()
    try:
        return int(s)
    except ValueError:
        return w2n.word_to_num(s)
    
def speak(text) :
    engine.say(text)
    engine.runAndWait()

def open(app) :
    os.system(f"start {app}:")  # only for standard apps

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


