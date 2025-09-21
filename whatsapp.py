import pyautogui as p 
import time  as t
import os

def call(reciever,type) :
    os.system("start whatsapp:")
    t.sleep(5)
    p.hotkey('ctrl','f')
    p.hotkey('ctrl','a')
    p.press('backspace')
    t.sleep(1)
    p.write(reciever)
    p.moveTo(386,330,duration=0.75)
    p.click()
    if type == "v" :
        p.moveTo(1734,111,duration=0.35)
        t.sleep(1)
        p.click()
    if type == "n" :
        p.moveTo(1806,117,duration=0.35)
        t.sleep(1)
        p.click()
        
def msg(c,reciever):
    os.system("start whatsapp:")
    t.sleep(5)
    p.hotkey('ctrl','f')
    p.hotkey('ctrl','a')
    p.press('backspace')
    t.sleep(1)
    p.write(reciever)
    p.moveTo(386,330,duration=0.75)
    p.click()
    p.moveTo(1561,976,duration=0.35)
    t.sleep(1)
    p.click()
    p.write(c,interval=0.05)
    p.hotkey('enter')