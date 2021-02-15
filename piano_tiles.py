import pyautogui
from pyautogui import *
import keyboard
import random
import win32api, win32con

import time
time.sleep(3)
from mss import mss



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #pyautogui.click(x=a,y=b)
    

    
    

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(540, 485)[0] == 0:
        click(540,485)
    if pyautogui.pixel(636,485)[0] == 0:
        click(636,485)
    if pyautogui.pixel(727,485)[0] == 0:
        click(727,485)
    if pyautogui.pixel(813,485)[0] == 0:
        click(813,485)
