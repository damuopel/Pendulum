import pygame
import numpy as np

WIDTH = 500
HEIGHT = 500

# INPUT
l = 250
angle = 90
R = 50

originX = 0
originY = 0

pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT]) 

running = True
while running:
    
    x = int(l*np.sin(np.pi*angle/180))
    y = int(l*np.cos(np.pi*angle/180))
    
    screen.fill((255,255,255))
    
    pygame.draw.line(screen,(0,0,255),(originX,originY),(x,y),5)
    pygame.draw.circle(screen, (0, 0, 255),(x,y), R)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
pygame.quit()