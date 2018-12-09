# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 23:08:35 2018

@author: wtolliver
"""

import RPi.GPIO
import time
import keyboard

count = 0
while True:
        try:
            if keyboard.is_pressed('1'):
                
                print (keyboard.is_pressed('1'))
            else: 
                pass
        except:
            break
        

            