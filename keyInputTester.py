# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 23:08:35 2018

@author: wtolliver
"""

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()

while 1:
    clock.tick(60) #60 FPS
    for event in pygame.event.get:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print "The Spacebar was pressed."
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print "The Spacebar was released."