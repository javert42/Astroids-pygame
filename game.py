#!/usr/bin/env python

import sys, pygame, random, math
from pygame.locals import *
import spaceShip, bullet, debugScreen

size = 800,800
fps_limit = 100
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
ship = spaceShip.SpaceShip(300,500,(0,0,255))
keydown = None
quant = 5
bullets = []
debug = debugScreen.DebugScreen(screen)
fonts = {}
fonts["pause"] = pygame.font.SysFont("monospace", 40)
pauseLabel = fonts["pause"].render("PAUSED - Press 'p' to continue", 1, (255,0,0))

paused = False

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
        elif event.type == KEYDOWN and event.key == K_p:
            paused = not paused
        
        if paused:
            continue
        elif event.type == KEYDOWN and (event.key == K_UP
                                        or event.key == K_DOWN
                                        or event.key == K_LEFT
                                        or event.key == K_RIGHT):
            keydown = {"key":event.key, "time":quant}
        elif event.type == KEYUP:
            keydown = None
        elif event.type == KEYDOWN and event.key == K_SPACE:
            bullets.append(bullet.Bullet(ship.getGunPosition(),
                                         ship.getDirection(),
                                         ship.getVelocity()-.5))

    debug.add("FPS: " + str(clock.get_fps()))
    debug.add("Bullets: " + str(len(bullets)))
    screen.fill((0,0,0))
    dtime = clock.tick(fps_limit)

    if paused:
        tx = (screen.get_width() - pauseLabel.get_width()) / 2
        ty = (screen.get_height() - pauseLabel.get_height()) / 2
        ty = ty - (pauseLabel.get_height() / 2)
        screen.blit(pauseLabel, (tx,ty))
    else: 
        process_key()
        if (keydown != None):
            keydown["time"] += dtime
        ship.advance(dtime)
        ship.draw(screen)
        for b in bullets:
            b.advance(dtime)
            b.draw(screen)

        for b in bullets[:]:
            if b.isOffScreen(screen):
                bullets.remove(b)
   
    debug.draw()
    pygame.display.flip()  
    pygame.display.update()
