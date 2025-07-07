# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:

# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((840, 480))

robot = pygame.image.load("src\\robot.png")

window.fill((0,0,0))

def line(nb:int, row=int):
    for i in range(nb):
        window.blit(robot, (100+(i+(row/4))*robot.get_width(), 100+(row/4)*robot.get_height()))


def draw_robots(height:int):
    idx=0
    while idx < height:
        line(10, idx)
        idx += 1

draw_robots(10)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()