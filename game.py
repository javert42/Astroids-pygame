#!/usr/bin/env python

import sys, pygame, random, math
from pygame.locals import *
import spaceShip, debugScreen
from astroid import Astroid
from bullet import Bullet

class AstroidGame:
    def __init__(self):
        pygame.init()
        self.load_sounds()
        self.window_size = 640,480
        self.fps_limit = 60 
        self.screen = pygame.display.set_mode(self.window_size)
        self.game_clock = pygame.time.Clock()
        self.ship = spaceShip.SpaceShip(45,45,(255,255,255))
        self.keydown = None
        self.bullets = []
        self.astroids = []
        self.debug = debugScreen.DebugScreen(self.screen)
        self.fonts = {"pause" : pygame.font.SysFont("monospace", 40)}
        self.labels = {"pause" :
                self.fonts["pause"]
                .render("PAUSED - Press 'p' to continue", 1, (255,0,0))}
        self.paused = False

    def load_sounds(self):
        self.sounds = {
            "shot" : pygame.mixer.Sound("shot.wav"),
            "explode" : pygame.mixer.Sound("explode.wav"),
        }

    def new_astroid(self):
        r = random.Random()
        side = r.randint(0,3)
        if side % 2 == 0:
            x = self.screen.get_width() * (side / 2)
            x = x + (side - 1) * 10
            y = r.randint(0,self.screen.get_height())
        else:
            x = r.randint(0,self.screen.get_width())
            y = self.screen.get_height() * (side / 2)
            y = y + (side - 2) * 10
        min_dir = 90 * side
        max_dir = min_dir + 180
        dir = r.randint(min_dir,max_dir)
        mult = r.gauss(.2, .05)
        v_x = math.sin( math.radians(dir) ) * mult
        v_y = -math.cos( math.radians(dir) ) * mult
        return Astroid((x,y), (v_x,v_y))

    def process_key(self):
        if (self.keydown != None):
            {
                K_UP    : lambda: self.ship.accelerate(.003),
                K_LEFT  : lambda: self.ship.turn(3),
                K_RIGHT : lambda: self.ship.turn(-3),
            }.get(self.keydown)()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.debug.add("Key: " + str(event.key))
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_q:
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_p:
                    self.paused = not self.paused
                
                if self.paused:
                    continue
                elif event.type == KEYDOWN and (event.key == K_UP
                                                or event.key == K_LEFT
                                                or event.key == K_RIGHT):
                    self.keydown = event.key
                elif event.type == KEYUP:
                    self.keydown = None
                elif event.type == KEYDOWN and event.key == K_SPACE:
                    self.sounds["shot"].play()
                    self.bullets.append(Bullet(self.ship.getGunPosition(),
                                                 self.ship.getDirection(),
                                                 self.ship.getVelocity()))
                elif event.type == KEYDOWN and event.key == K_a:
                    self.astroids.append(self.new_astroid())

            self.debug.add("FPS: " + str(self.game_clock.get_fps()))
            self.debug.add("Bullets: " + str(len(self.bullets)))
            self.debug.add("Astroids: " + str(len(self.astroids)))
            self.debug.add("Angle: "
                    + str(math.degrees(self.ship.getDirection())))
            self.debug.add("Velocity: " + str(self.ship.getVelocity()))
            self.screen.fill((0,0,0))

            dtime = self.game_clock.tick(self.fps_limit)

            if self.paused:
                tx = (self.screen.get_width()
                        - self.labels["pause"].get_width()) / 2
                ty = (self.screen.get_height()
                        - self.labels["pause"].get_height()) / 2
                ty = ty - (self.labels["pause"].get_height() / 2)
                self.screen.blit(self.labels["pause"], (tx,ty))
            else: 
                self.process_key()
                self.ship.advance(self.screen, dtime)
                self.ship.draw(self.screen)

                for b in self.bullets[:]:
                    b.advance(dtime)
                    b.draw(self.screen)
                    for a in self.astroids:
                        if b.does_circle_collide(a):
                            self.bullets.remove(b)
                            self.sounds["explode"].play()
                            a.color = (255,255,255)
                            break #A single bullet should only hit 1 astroid
                            

                for a in self.astroids:
                    a.advance(self.screen, dtime)
                    a.draw(self.screen)

                for b in self.bullets[:]:
                    if b.isOffScreen(self.screen):
                        self.bullets.remove(b)
           
            self.debug.draw()
            pygame.display.flip()  
            pygame.display.update()


game = AstroidGame()
game.run()
