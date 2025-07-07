# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

robot_img = pygame.image.load("src\\robot.png")

pygame.init()
window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

rand_x = randint(0,640-robot_img.get_width())
rand_y = randint(0,480-robot_img.get_height())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] > rand_x and pygame.mouse.get_pos()[0] < rand_x + robot_img.get_width():
                change_x = True
            else:
                change_x = False
            if pygame.mouse.get_pos()[1] > rand_y and pygame.mouse.get_pos()[1] < rand_y + robot_img.get_height():    
                change_y = True
            else:
                change_y = False
            if change_x and change_y:
                rand_x = randint(0,640-robot_img.get_width())
                rand_y = randint(0,480-robot_img.get_height())

    window.fill((0, 0, 0))
    window.blit(robot_img, (rand_x, rand_y))
    pygame.display.flip()

    clock.tick(60)