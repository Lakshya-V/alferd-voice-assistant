import pyautogui as p 
import time as t 
import speech_recognition as sr
from word2number import w2n

def play_pause() :
    p.press('win')
    t.sleep(1)
    p.write('Spotify')
    t.sleep(1)
    p.press('enter')
    t.sleep(6)
    p.press('space')

def play(nm) :
    p.press('win')
    t.sleep(1)
    p.write('Spotify')
    t.sleep(1)
    p.press('enter')
    t.sleep(6)
    p.moveTo(969,39,duration=0.75)
    p.click()
    p.click()
    p.hotkey('ctrl', 'a')
    t.sleep(0.5)
    p.press('backspace')
    t.sleep(1)
    p.write(nm)
    t.sleep(3)
    p.press('enter')
    with sr.Microphone() as source:
        r = sr.Recognizer()
        print("LISTENING... position of the song (1 for first, 2 for second etc.)")
        audio = r.listen(source)
        pos = r.recognize_google(audio, language="en-IN")
        print(f"Position: {pos}")
    t.sleep(4)
    p.press('tab')
    p.press('tab')
    p.press('tab')
    p.press("tab")
    for i in range(w2n.word_to_num(pos)) :
        p.press('down')
    p.press('enter')