TD background.png:
-----------------
https://codehs.com/uploads/cd984f81d8835a9775a443b972bc9fa4

emojipng.com-5355481.png:
------------------------
https://codehs.com/uploads/f4e917f668cf8aea6c0b778d22a39880

emojipng.com-8877575.png:
------------------------
https://codehs.com/uploads/80ec5877845341b9b3ba77bdef34fbc6

main.py:
-------
#imports
import sys
import pygame as pg
import os
from pygame.math import Vector2
import math
TILE_SIZE=50
SCREEN_WIDTH=800
SCREEN_HEIGHT=800
placing=[[0,0,0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,0,0],[0,0,1,0,1,0,1,1,1,1],[0,0,1,0,1,0,1,0,0,0],[0,0,1,0,1,0,1,0,0,0],[1,1,1,0,1,0,1,0,0,0],[0,0,0,0,1,0,1,1,1,0],[0,1,1,1,1,0,0,0,1,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0]]
class Enemy(pg.sprite.Sprite):
    
    def __init__(self,waypoints,image):
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos=Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 1
        self.angle = 0
        self.original_image = image
        self.image= pg.transform.rotate(self.original_image,self.angle)
        self.rect =self.image.get_rect()
        self.rect.center = self.pos
    def move(self):
        
        self.rect.x +=1
        #define a target waypoint
        if self.target_waypoint < len(self.waypoints):
            
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            #enemy reaches end of path
            self.kill()
        
        #Calculate distance to target
        dist = self.movement.length()
        #checking remianing distance, if its greater than the enemy speed
        if dist >= self.speed:
            self.pos += self.movement.normalize()*self.speed
        else:
            if dist != 0:
                self.pos += self.movement.normalize()*dist
            self.target_waypoint += 1
        
        
    def update(self):
        self.move()
        self.rotate()
    def rotate(self):
        #calculates the distance to the next wavepoint
        dist = self.target - self.pos
        #uses it to calculate the angle turn
        self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
        #Rotates and updates rect
        self.image= pg.transform.rotate(self.original_image, self.angle)
        self.rect =self.image.get_rect()
        self.rect.center = self.pos
class Turret(pg.sprite.Sprite):
    def __init__(self, image, tile_x,tile_y):
        self.tile_x=tile_x
        self.tile_y=tile_y
        #calculate center coordinates
        self.x= (self.tile_x+.5)*TILE_SIZE
        self.y= (self.tile_y+.5)*TILE_SIZE
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
class World():
    def __init__(self, map_image):
        self.image = map_image
    def draw(self, surface):
        surface.blit(self.image, (0, 0))










waypoints=[(0,250),(125,250),(125,75),(225,75),(225,340),(75,340),(75,435),(425,435),(425,300),(325,300),(325,115),(500,115)]

#Game window
os.environ['SDL_AUDIODRIVER'] = 'dsp'
pg.init()
WIDTH=500
HEIGHT=550
SIZE = WIDTH,HEIGHT
screen = pg.display.set_mode(SIZE)
pg.font.init()


#Enemy grpahics       

#Loading images
enemy_image = pg.image.load("emojipng.com-8877575.png").convert_alpha()

DEFAULT_IMAGE_SIZE=(30,30)
enemy_image = pg.transform.scale(enemy_image, DEFAULT_IMAGE_SIZE)
enemy =Enemy((waypoints),enemy_image)
#create groups
enemy_group= pg.sprite.Group()
enemy_group.add(enemy)


background = pg.image.load("TD background.png").convert_alpha()
BACKGROUND_SIZE=(500,550)
background = pg.transform.scale(background, BACKGROUND_SIZE)


#Individual elf turret
elf_turret = pg.image.load("emojipng.com-5355481.png").convert_alpha()
DEFAULT_IMAGE_SIZE=(40,40)
elf_turret = pg.transform.scale(elf_turret, DEFAULT_IMAGE_SIZE)
#turret group
turret_group = pg.sprite.Group()

def create_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // TILE_SIZE
    mouse_tile_y = mouse_pos[1] // TILE_SIZE

    
    turret = Turret(elf_turret,mouse_tile_x,mouse_tile_y)
    if placing[mouse_tile_y][mouse_tile_x]==0:
        if placing[mouse_tile_y][mouse_tile_x]==0:
            turret_group.add(turret)
            placing[mouse_tile_y][mouse_tile_x]=1
        else:
            pass
    else:
        pass


#create world
world = World(background)



#Game clock
while 1:
    clock = pg.time.Clock()
    
    screen.fill("white")
    
    #draws level background
    world.draw(screen)

    
    # Limit to 60 frames per second
    clock.tick(60)
    enemy_group.draw(screen)
    turret_group.draw(screen)
    
    #updates groups

    enemy_group.update()
    for enemy in enemy_group:
        enemy.move()
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pg.mouse.get_pos()
            # check mouse on game area
            if mouse_pos[0]< SCREEN_WIDTH and mouse_pos[1] < SCREEN_HEIGHT:
                create_turret(mouse_pos)
    
    #updates display
    pg.display.flip()

