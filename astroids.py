import sys, pygame, random, math
from pygame.locals import *
import spaceShip

size = 1024,1024
fps_limit = 100
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
ship = spaceShip.SpaceShip(300,500,(0,0,255))
keydown = None
quant = 5


def process_key():
    if (keydown != None and keydown["time"] >= quant):
        {
            K_UP    : lambda: ship.accelerate(.001),
            K_DOWN  : lambda: ship.accelerate(-.001),
            K_LEFT  : lambda: ship.turn(-1),
            K_RIGHT : lambda: ship.turn(1),
        }.get(keydown["key"])()
        keydown["time"] -= quant
            

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            sys.exit()
        elif event.type == KEYDOWN and (event.key == K_UP
                                        or event.key == K_DOWN
                                        or event.key == K_LEFT
                                        or event.key == K_RIGHT):
            keydown = {"key":event.key, "time":quant}
        elif event.type == KEYUP:
            keydown = None

    process_key()
    dtime = clock.tick(fps_limit)
    if (keydown != None):
        keydown["time"] += dtime
    screen.fill((0,0,0))
    ship.advance(dtime)
    ship.draw(screen)
    
    pygame.display.flip()  
    pygame.display.update()
