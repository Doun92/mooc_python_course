# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((840, 480))

robot = pygame.image.load("src\\robot.png")

window.fill((0,0,0))

def draw_robot(x:int,y:int):
    window.blit(robot, (x, y))
i=0
while i <1000:
    draw_robot(
        randint(0, 840-int(robot.get_width())),
        randint(0, 480-int(robot.get_height()))
        )
    i+=1



pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()