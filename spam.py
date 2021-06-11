import pynput
import random
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

i = 0
while i < 1:
#the following can be edited to suit your needs
    keyboard.type('a') 
    keyboard.press(Key.enter)
    time.sleep(1)