import pygame

class DebugScreen:

    def __init__(self, screen):
        self.screen = screen
        self.lines = []
        self.font = pygame.font.SysFont("monospace", 20)

    def add(self, line):
        self.lines.append(line)

    def draw(self):
        ypos = 10
        for line in self.lines:
            label = self.font.render(line, 1, (255,0,0))
            self.screen.blit(label, (10, ypos))
            ypos = 15 + ypos
        self.lines = []
