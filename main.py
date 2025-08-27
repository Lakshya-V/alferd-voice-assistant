import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import datetime as dt
import requests
from openai import OpenAI
from spotify import play, play_pause



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

    if "open google" in c.lower() :
        webbrowser.open("https://google.com")

    if "open linkedin" in c.lower() :
        webbrowser.open("https://linkedin.com")

    if "open youtube" in c.lower() :
        webbrowser.open("https://youtube.com")

    if "open instagram" in c.lower() :
        webbrowser.open("https://instagram.com")
    
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
            speak(f"playing {song}")
            play(song)

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

    else :
        #Let openi handle the request
        ai_process(c)

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


