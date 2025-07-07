# WRITE YOUR SOLUTION HERE:
#Le code devrait déjà fonctionner
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src\\ball.png")

x = 0
y = 0
velocity_x = 1
velocity_y = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += velocity_x
    if velocity_x > 0 and x+robot.get_width() >= 640:
        velocity_x = -velocity_x
    if velocity_x < 0 and x <= 0:
        velocity_x = -velocity_x

    y += velocity_y
    if velocity_y > 0 and y+robot.get_height() >= 480:
        velocity_y = -velocity_y
    if velocity_y < 0 and y <= 0:
        velocity_y = -velocity_y
    clock.tick(120)