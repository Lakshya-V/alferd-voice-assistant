import pyautogui as p 
import time as t 

#Please do not touch any input device while code is running
#if you want to stop the code please move your mouse to top left corner of screen

def play_pause() :
    p.press('win')
    t.sleep(1)
    p.write('Spotify')
    t.sleep(1)
    p.press('enter')
    t.sleep(3)
    p.press('space')

def play(nm) :
    p.press('win')
    t.sleep(1)
    p.write('Spotify')
    t.sleep(1)
    p.press('enter')
    t.sleep(6)
    p.hotkey('ctrl', 'k')
    p.hotkey('ctrl', 'a')
    p.press('backspace')
    t.sleep(1)
    p.write(nm)
    t.sleep(1)
    p.press('enter')
    t.sleep(3)
    p.press('tab')*5
    p.press('enter')