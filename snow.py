#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:44:47 2020

@author: kyle
"""

import pygame
import random


black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)

pygame.init()


size=(500,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("haha")

snow_list = []
for me in range(50):
    x = random.randrange(0,500)
    y = random.randrange(0,500)
    snow_list.append([x,y])
    
done = False
clock = pygame.time.Clock()

while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(black)        
    
    for me in range(len(snow_list)):
        pygame.draw.circle(screen,white,snow_list[me],2,2)
        snow_list[me][1] += 1
        
        if snow_list[me][1] > 500:
            y = random.randrange(-50,-10)
            snow_list[me][1] = y
            x = random.randrange(0,500)
            snow_list[me][0] = x
    pygame.display.flip()
    clock.tick(60)   
pygame.quit()

