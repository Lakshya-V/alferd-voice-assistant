import pyautogui as p 
import time  as t
import os

def msg(c,reciever):
    os.system("start whatsapp:")
    p.moveTo(386,181,duration=3)
    t.sleep(2)
    p.click()
    p.write(reciever)
    p.moveTo(386,330,duration=0.75)
    p.click()
    p.moveTo(1561,976,duration=0.25)
    p.click()
    p.write(c,interval=0.25)
    p.hotkey('enter')