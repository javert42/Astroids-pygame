import pygame, math

class SpaceShip:
    def __init__(self, x=0, y=0, color=(0,0,255)):
        self.height = 20
        self.width = 12
        self.velocity = (0,0)
        self.direction = 0
        if x < self.width/2:
            x = self.width/2
        self.points = [(x,y),
                       (x-(self.width/2),y+self.height),
                       (x+(self.width/2),y+self.height),
                       (x-(self.width/3),y+(self.height*.75)),
                       (x+(self.width/3),y+(self.height*.75)),
                       (x-(self.width/3)+1,y+(self.height*.75)),
                       (x,y+self.height),
                       (x+(self.width/3)-1,y+(self.height*.75)),
                       (x,y+self.height),]
        self.pos = (x, y+(self.height/2))
        self.color = color
        self.thrust = False

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def getGunPosition(self):
        return self.pos

    def getDirection(self):
        return self.direction

    def getVelocity(self):
        return self.velocity

    def draw(self, screen):
        #pygame.draw.polygon(screen, self.color, self.points, 1)
        pygame.draw.aaline(screen, self.color, self.points[0], self.points[1])
        pygame.draw.aaline(screen, self.color, self.points[0], self.points[2])
        pygame.draw.aaline(screen, self.color, self.points[3], self.points[4])
        if (self.thrust):
            pygame.draw.aaline(screen, self.color, self.points[5], self.points[6])
            pygame.draw.aaline(screen, self.color, self.points[7], self.points[8])
            self.thrust = False


    def accelerate(self, val):
        self.velocity = (self.velocity[0] + val * math.sin(self.direction),
                         self.velocity[1] + val * -math.cos(self.direction))
        self.thrust = True

    def advance(self, screen, dtime):
        xd = self.velocity[0] * dtime
        yd = self.velocity[1] * dtime
        x,y = (xd + self.pos[0], yd + self.pos[1])
        if x < -(self.width/2):
            xd = xd + screen.get_width() + self.width/2
        elif x > screen.get_width() + self.width/2:
            xd = xd - (screen.get_width() + self.width/2)
        if y < -self.height/2:
            yd = yd + screen.get_height() + self.height/2
        elif y > screen.get_height() + self.height/2:
            yd = yd - (screen.get_height() + self.get_height()/2)
        self.pos = (xd + self.pos[0], yd + self.pos[1])
        new_points = []
        for point in self.points:
            new_point = (point[0] + xd, point[1]+yd)
            new_points.append(new_point)
        self.points = new_points
        
    def turn(self, deg):
        rad = math.radians(-deg)
        self.direction = (self.direction + rad) % (2*math.pi)        
        new_points = []
        for point in self.points:
            x_old = point[0] - self.pos[0]
            y_old = point[1] - self.pos[1]
            
            x = x_old * math.cos(-rad) + y_old * math.sin(-rad)
            y = x_old * (-1* math.sin(-rad)) + y_old * math.cos(-rad)

            x = x + self.pos[0]
            y = y + self.pos[1]
            
            new_points.append((x,y))
        self.points = new_points
