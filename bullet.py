import pygame, math

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, pos, d, v):
        self.radius = 3
        self.pos = pos
        self.direction = d
        self.velocity = (v[0] + math.sin(d)*.5, v[1] + -math.cos(d)*.5)
        self.color = (0,255,0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos[0]),int(self.pos[1])), self.radius)

    def advance(self, dtime):
        x = self.pos[0] + self.velocity[0] * dtime
        y = self.pos[1] + self.velocity[1] * dtime
        self.pos = (x,y)

    def isOffScreen(self, screen):
        if ((self.pos[0] < 0 or self.pos[0] > screen.get_width())
            or (self.pos[1] < 0 or self.pos[1] > screen.get_height())):
            return True

    def does_circle_collide(self, circle):
        x1,x2,y1,y2 = (self.pos[0], circle.pos[0], self.pos[1], circle.pos[1])
        r1,r2 = self.radius, circle.radius
        return math.sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) ) < (r1 + r2)
