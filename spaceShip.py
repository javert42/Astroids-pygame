import pygame, math

class SpaceShip:
    def __init__(self, x=0, y=0, color=(0,0,255)):
        self.height = 50
        self.width = 30
        self.velocity = 0
        self.direction = 0
        if x < self.width/2:
            x = self.width/2
        self.points = [(x,y),
                       (x-(self.width/2),y+self.height),
                       (x+(self.width/2),y+self.height)]
        self.x_pos = x
        self.y_pos = y+(self.height/2)
        self.color = color

    def draw(self, screen):
        r = pygame.draw.polygon(screen, self.color, self.points, 1)

    def accelerate(self, val):
        self.velocity = self.velocity + val

    def advance(self, dtime):
        xd = math.sin( self.direction ) * self.velocity * dtime
        yd = math.cos( self.direction ) * self.velocity * dtime
        self.x_pos = self.x_pos + xd
        self.y_pos = self.y_pos + yd
        new_points = []
        for point in self.points:
            new_point = (point[0] + xd, point[1]+yd)
            new_points.append(new_point)
        self.points = new_points
        
    def turn(self, deg):
        rad = math.radians(deg)
        self.direction = (self.direction + rad) % (2*math.pi)        
        new_points = []
        for point in self.points:
            x = point[0] - self.x_pos
            y = point[1] - self.y_pos
            
            x = x * math.cos(rad) + y * math.sin(rad)
            y = x * (-1* math.sin(rad)) + y * math.cos(rad)

            x = x + self.x_pos
            y = y + self.y_pos
            
            new_points.append((x,y))
        self.points = new_points
