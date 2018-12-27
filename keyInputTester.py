# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 23:08:35 2018

@author: wtolliver
"""

from pad4pi import rpi_gpio
import time

#Setup Keypad right now
KEYPAD = [
          ["1","2","3","A"],
          ["4","%","6","B"],
          ["7","8","9","C"],
          ["*","0","#","D"]
]
          
#Same as calling: factory.create_4_by_4_keypad, still we put here fyi
ROW_PINS = [4, 14, 15, 17] # BCM numbering
COL_PINS = [18, 27, 22, 23] # BCM Numbering

factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

#keypad.cleanup

def printKey(key):
    print(key)
    if(key=="1"):
        print("number")
    elif (key=="A"):
        print("letter")
        
# printKey will be callec each time a keypad button is pressed
        
try:
    while(True):
        time.sleep(0.2)
except:
    keypad.cleanup()
    