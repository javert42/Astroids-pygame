import pygame, math

class Astroid(pygame.sprite.Sprite):

    def __init__(self, pos, velocity):
        self.radius = 30
        self.width = self.radius * 2
        self.height = self.radius * 2 
        self.pos = pos
        self.velocity = velocity
        self.color = (255,0,255)

    def advance(self, screen, dtime):
        dx = self.velocity[0] * dtime
        dy = self.velocity[1] * dtime
        x = self.pos[0] + dx
        y = self.pos[1] + dy
        if x < -(self.radius):
            dx = dx + screen.get_width() + self.radius
        elif x > screen.get_width() + self.get_width()/2:
            dx = dx - (screen.get_width() + self.width/2)
        if y < -self.get_height()/2:
            dy = dy + screen.get_height() + self.height/2
        elif y > screen.get_height() + self.height/2:
            dy = dy - (screen.get_height() + self.height/2)
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)

    def draw(self, screen):
        pygame.draw.circle(screen,
                           self.color,
                           (int(self.pos[0]),int(self.pos[1])),
                           self.radius)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def does_circle_collide(self, circle):
        x1,x2,y1,y2 = (self.pos[0], circle.pos[0], self.pos[1], circle.pos[1])
        r1,r2 = self.radius, circle.radius
        return math.sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) ) < (r1 + r2)
