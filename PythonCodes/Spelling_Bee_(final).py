import pygame
import sys

#setup
size = width, height = 480, 360
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)



while 1:
    clock = pygame.time.Clock()
    # Limit to 60 frames per second
    clock.tick(60)
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit()
            #mouse_pos = pg.mouse.get_pos()
    
    #event
    screen.fill("white")
    pos=(200,200)
    pygame.draw.circle(screen,"red",pos,40)
    pygame.display.flip()