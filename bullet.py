import pygame, math

class Bullet:
    
    def __init__(self, pos, d, v):
        self.pos = pos
        self.direction = d
        self.velocity = v
        self.color = (0,255,0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos[0]),int(self.pos[1])), 3)

    def advance(self, dtime):
        xd = math.sin( self.direction ) * self.velocity * dtime
        yd = math.cos( self.direction ) * self.velocity * dtime
        self.pos = (self.pos[0] + xd, self.pos[1] + yd)

    def isOffScreen(self, screen):
        if ((self.pos[0] < 0 or self.pos[0] > screen.get_width())
            or (self.pos[1] < 0 or self.pos[1] > screen.get_height())):
            return True

