import pygame, math

class Astroid:

    def __init__(self, pos, velocity):
        self.width = 30
        self.height = 30
        self.pos = pos
        self.velocity = velocity
        self.color = (255,0,255)

    def advance(self, dtime):
        x = self.pos[0] + self.velocity[0] * dtime
        y = self.pos[1] + self.velocity[1] * dtime
        self.pos = (x,y)

    def draw(self, screen):
        pygame.draw.circle(screen,
                           self.color,
                           (int(self.pos[0]),int(self.pos[1])),
                           15)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def isOffScreen(self, screen):
        if ((self.pos[0] < -self.get_width()
                or self.pos[0] > (screen.get_width() + self.get_width()))
            or (self.pos[1] < -self.get_height()
                or self.pos[1] > (screen.get_height() + self.get_height()))):
            return True        
