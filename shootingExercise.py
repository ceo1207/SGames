import pygame
import sys, math
import random
from pygame.locals import *
class Circle:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius
    def isInside(self, tmp):
        distance = math.pow(tmp[0]- self.pos[0],2)+math.pow(tmp[1]- self.pos[1],2)
        if distance > self.radius**2:
            return False
        else:
            return True


pygame.init()
time = pygame.time.Clock()
surface = pygame.display.set_mode((400, 200), 0, 32)

circles = []
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
surface.fill(WHITE)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            for item in circles[:]:
                if item.isInside([event.pos[0], event.pos[1]]):
                    circles.remove(item)
                    break

    surface.fill(WHITE)
    if (len(circles)<10):
        circles.append(Circle([random.randint(0,399), random.randint(0,199)],random.randint(3,10)))

    for item in circles:
        pygame.draw.circle(surface, (255,255,0), item.pos, item.radius, 0)
    #  do not forget the update process otherwise, the screen will not change
    pygame.display.update()
    time.tick(40)
