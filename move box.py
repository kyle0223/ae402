#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 13:42:04 2020

@author: kyle
"""

import pygame
import random

blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)

pygame.init()

size=(400,300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("move the box")

# done = False
clock = pygame.time.Clock()
# while not done:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#           done = True  
          
          
x = 200
y = 150
# screen.fill(red)
# pygame.draw.rect(screen,blue,[x ,y ,10,10])
# pygame.display.flip()
# done = False


# while not done:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#           done = True  
                  
done = False


while not done:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          done = True
          
    keys = pygame.key.get_pressed()
    screen.fill(red)
    pygame.draw.rect(screen,blue,[x ,y ,10,10])
    pygame.display.flip()
    
    if keys[pygame.K_RIGHT]:
        x += 10
    
        
       
            
          # if keys[pygame.K_LEFT]:
          #     x -= 1
          #     pygame.display.flip()  
          #     screen.fill(red)
          #     pygame.draw.rect(screen,blue,[x ,y ,10,10]
          # elif keys[pygame.K_RIGHT]:
          #     x += 1
          # elif keys[pygame.K_UP]:
          #     y -= 1   
          # elif keys[pygame.K_DOWN]:
          #     y += 1
          # elif keys[pygame.K_SPACE]:
          #     x = random.randrange(0,400)
          #     y = random.randrange(0,300)
          # elif keys[pygame.K_k]:
          #     screen.fill(red)
          #     pygame.draw.rect(screen,black,[x ,y ,10,10])
          #     pygame.display.flip()
  
          # else:
          #     pass
    
    
    pygame.display.flip()
        
    clock.tick(10)

pygame.quit()    