# WRITE YOUR SOLUTION HERE:
import pygame
import random

class Robot:
    def __init__(self, x:int, y:int):
        self._x = x
        self._y = y
        self.v = 1
        self.status = "falling"
        self.robot_img = pygame.image.load("src\\robot.png")

    def __del__(self):
        pass
        # print("Robot gets destroyed")


    def __str__(self):
        return f"I am a robot at coordinates ({self._x},{self._y})."

    @property
    def y(self):
        self.get_velocity()
        return self._y

    @property
    def x(self):
        self.get_velocity()
        return self._x


    def get_velocity(self):
        if self.status == "falling":
            self._y += self.v
            if self.v > 0 and self._y + self.robot_img.get_height() >= 480:
                self.v = 0
                if self._x < 640/2:
                    self.status = "to_left"
                    return self.status
                else:
                    self.status = "to_right"
                    return self.status
            return self._y
        if self.status == "to_left":
            self.v = 1
            self._x += -self.v
            if self._x + self.robot_img.get_width() < 0:
                self.status = "destroy"
            return self._x
        if self.status == "to_right":
            self.v = 1
            self._x += self.v
            if self._x + self.robot_img.get_width() > 690:
                self.status = "destroy"
            return self._x
        
def create_robots(list_robots):
    if random.randint(1, 30) == 30:
        list_robots.append(Robot(random.randint(0, 590), 0))

def update_and_draw_robots(robots, window):
    for robot in robots[:]:
        window.blit(robot.robot_img, (robot.x, robot.y))
        if robot.status == "destroy":
            robots.remove(robot)

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

list_robots = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    create_robots(list_robots)
    update_and_draw_robots(list_robots,window)

    pygame.display.flip()
    clock.tick(60)