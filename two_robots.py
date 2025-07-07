# WRITE YOUR SOLUTION HERE:
import pygame

class Robot:
    def __init__(self, x, y, v):
        self._x = x
        self.y = y
        self.v = v
        self.img = pygame.image.load("src\\robot.png")

    @property
    def x(self):
        self.get_velocity()
        return self._x

    @x.setter
    def x(self, value):
        return self._x

    def get_velocity(self):
        self._x += self.v
        if self.v > 0 and self._x + self.img.get_width() >= 640:
            self.v = -self.v
        if self.v < 0 and self._x <= 0:
            self.v = -self.v
        return self._x

pygame.init()
window = pygame.display.set_mode((640, 480))

fast_robot = Robot(0,50,1)
slow_robot = Robot(0,150,2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(fast_robot.img, (fast_robot.x,fast_robot.y))
    window.blit(slow_robot.img, (slow_robot.x,slow_robot.y))
    pygame.display.flip()
    clock.tick(60)