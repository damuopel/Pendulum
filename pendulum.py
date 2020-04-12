import pygame
import numpy as np

WIDTH = 750
HEIGHT = 500

# INPUT
l = 250
angle = 50
R = 25
incT = 0.1
g = 9.807

omega = 0

originX = WIDTH/2
originY = 0

pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT]) 

running = True
while running:
    
    x = originX + l*np.sin(np.pi*angle/180)
    y = originY + l*np.cos(np.pi*angle/180)
    
    screen.fill((255,255,255))
    
    pygame.draw.line(screen,(0,0,255),(int(originX),int(originY)),(int(x),int(y)),5)
    pygame.draw.circle(screen, (0, 0, 255),(int(x),int(y)), R)
    
    pygame.display.flip()
    
    alfa = -(g/l)*np.sin(np.pi*angle/180)
    omega = omega + alfa*incT
    angle = angle + omega*incT
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
pygame.quit()