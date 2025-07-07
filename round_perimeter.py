# # WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src\\robot.png")

clock = pygame.time.Clock()

x = 0
y = 0
travel = "top"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    if travel == "top":
        if x == 640 - robot.get_width():
            x = 640 - robot.get_width()
            travel = "right"
        else:
            x += 1
    
    if travel == "right":
        if y == 480 - robot.get_height():
            y = 480 - robot.get_height()
            travel = "bottom"
        else:
            y += 1

    if travel == "bottom":
        if x == 0:
            x = 0
            travel = "left"
        else:
            x -= 1

    if travel == "left":
        if y == 0:
            y = 0
            travel = "top"
        else:
            y -= 1

    clock.tick(60)