# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 23:08:35 2018

@author: wtolliver
"""

from threading import Thread

""" Declarations

"""
threads = []

def update():
    
    frameCount = 0
    fps = 1.0/16.67
    code = 1234
    code2 = 5678
    
    while (frameCount <= 60):
        frameCount = frameCount + 1
        time.sleep(fps)
        
        print(frameCount)
        
        if(frameCount == 60):
            code = code2
            print(code)
        
        if(code == 5678):
            print("You've successfully cracked the code!!!")
            break

process = Thread(target=update, args=[])
process.start()