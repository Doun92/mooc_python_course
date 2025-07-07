import pygame
import math
from datetime import datetime
import sys

# Initialize Pygame
pygame.init()

window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

def draw_bars(angle_deg, length, width):
    angle_rad = math.radians(angle_deg - 90)
    x = 320 + math.cos(angle_rad) * length
    y = 240 + math.sin(angle_rad) * length
    pygame.draw.line(window, (0,0,255), (320,240), (x, y), width)

def get_time_angles():
    now = datetime.now()
    sec = now.second
    minute = now.minute + sec / 60
    hour = now.hour % 12 + minute / 60

    sec_angle = (sec / 60) * 360
    min_angle = (minute / 60) * 360
    hour_angle = (hour / 12) * 360

    return hour_angle, min_angle, sec_angle

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0,0,0))

    pygame.draw.circle(window, (255,0,0), (320,240), 200, width=4)
    pygame.draw.circle(window, (255,0,0), (320,240), 10)

    hour_angle, min_angle, sec_angle = get_time_angles() 
    draw_bars(hour_angle, 100, 6)
    draw_bars(min_angle, 150, 2)
    draw_bars(sec_angle, 150, 2)


    pygame.display.flip()
    clock.tick(60)
