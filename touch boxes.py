#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 14:02:13 2020

@author: kyle
"""

import pygame
import random

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
 
pygame.init()

screen_width = 700
screen_height = 400
screen=pygame.display.set_mode([screen_width,screen_height])

player_x=0
player_y=0
player_w=50
player_h=50
block_x=[]
block_y=[]
collisions=[]

for i in range(10):
    block_x.append(random.randrange(screen_width))
    block_y.append(random.randrange(screen_height))
    collisions.append(False)
    
block_w=50
block_h=50
score=0
font=pygame.font.Font(None,50)
done=False
clock=pygame.time.Clock()    
start_ticks=pygame.time.get_ticks()

while not done:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          done = True
    screen.fill(white) 
    seconds=int((pygame.time.get_ticks()-start_ticks)/1000)      
    
    pos=pygame.mouse.get_pos()
    
    for i in range(10):
        xin=block_x[i]<=player_x<=block_x[i]+block_w or block_x[i]<=player_x+player_w<=block_x[i]+block_w
        yin=block_y[i]<=player_y<=block_y[i]+block_h or block_y[i]<=player_y+player_h<=block_y[i]+block_h                                                                                                                               
        if xin and yin and not collisions[i]:
            collisions[i] = True
            score+=1
    player_x=pos[0]
    player_y=pos[1]
    pygame.draw.rect(screen,red,[player_x,player_y,player_w,player_h])
    for i in range(10):
        if not collisions[i]:
            pygame.draw.rect(screen,black,[block_x[i],block_y[i],block_w,block_h])    
            
    message=str(score)+'points'
    text=font.render(message,10,black)
    screen.blit(text,(10,10))
    t=font.render(str(seconds),10,red)
    screen.blit(t,(40,40))  

    if seconds>10:
        text=font.render("game over",50,black)
        screen.blit(text,(100,100))
        done=True
        
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()    