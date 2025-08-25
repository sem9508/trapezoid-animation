import math
import pygame

class Cardioid:
    def __init__(self, width, height):
        self.radius = 400
        self.transform = width//2, height//2
        self.num_lines = 200
        self.counter, self.inc = 0, 0.01

    def get_color(self):
        self.counter += self.inc
        self.counter, self.inc = (self.counter, self.inc) if 0 < self.counter < 1 else(max(min(self.counter, 1), 0), -self.inc)

        return pygame.Color('red').lerp('blue', self.counter)

    def draw(self, screen):
        time = pygame.time.get_ticks()
        self.radius = 350 + 50 * abs(math.sin(time*0.004)-0.5)

        factor = 1 + 0.0001 * time

        for i in range(self.num_lines):
            angle = (factor*math.pi/self.num_lines)*i
            x1 = math.cos(angle)*self.radius + self.transform[0]
            y1 = math.sin(angle)*self.radius + self.transform[1]

            x2 = math.cos(factor*angle)*self.radius + self.transform[0]
            y2 = math.sin(factor*angle)*self.radius + self.transform[1]

            pygame.draw.aaline(screen, self.get_color(), (x1, y1), (x2, y2))
