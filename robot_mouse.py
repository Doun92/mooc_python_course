# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot_img = pygame.image.load("src\\robot.png")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = pygame.mouse.get_pos()[0]-robot_img.get_width()//2
    y = pygame.mouse.get_pos()[1]-robot_img.get_height()//2

    window.fill((0, 0, 0))
    window.blit(robot_img, (x, y))
    pygame.display.flip()

    clock.tick(60)