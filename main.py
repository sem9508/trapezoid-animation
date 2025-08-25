import pygame
import math
import time

from cardioid import Cardioid

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
cardioid = Cardioid(1000, 1000)
time.sleep(1)
FPS = 600
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill('black')
    cardioid.draw(screen)
    pygame.display.update()
    clock.tick(FPS)