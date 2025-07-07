# WRITE YOUR SOLUTION HERE:
import pygame
import math

class Robot:
    def __init__(self, angle_offset, radius=130):
        self.angle_offset = angle_offset  # unique starting angle for each robot
        self.radius = radius
        self.angle = 0  # shared angle updated each frame
        
    def update(self, center_x, center_y, global_angle):
        angle = global_angle + self.angle_offset
        x = center_x + math.cos(angle) * self.radius - robot_img.get_width() / 2
        y = center_y + math.sin(angle) * self.radius - robot_img.get_height() / 2
        return x, y

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

robot_img = pygame.image.load("src\\robot.png")

# Create multiple robots spaced evenly in a circle
num_robots = 10

robots = [
    Robot(angle_offset=2 * math.pi * i / num_robots)
    for i in range(num_robots)
]

global_angle = 0.0
center_x, center_y = 320, 240

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    # Update and draw each robot
    for robot in robots:
        x, y = robot.update(center_x, center_y, global_angle)
        window.blit(robot_img, (x, y))

    pygame.display.flip()
    clock.tick(40)
    global_angle += 0.02  # radians per frame