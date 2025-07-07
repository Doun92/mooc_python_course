# WRITE YOUR SOLUTION HERE:
import pygame
import random

class Rock:
    def __init__(self, x:int, y:int):
        self._x = x
        self._y = y
        self.__v = 1
        self.rock_img = pygame.image.load("src\\rock.png")
        self.status = "falling"

    def __del__(self):
        # pass
        print("Rock gets destroyed")

    @property
    def y(self):
        self._y += self.__v
        return self._y

    @property
    def x(self):
        return self._x

class Points:
    def __init__(self):
        self.text = "Points: "
        self.color = (255, 0, 0)
        self._points = 0

    @property
    def points(self):
        update_points()
        return self._points

    def update_points(self):
        self._points += 1 


class Robot:
    def __init__(self):
        self.robot_img = pygame.image.load("src\\robot.png")
        self.x = 0
        self.y = 480 - self.robot_img.get_height()

    def __str__(self):
        return f"Robot at coordinates ({self.x},{self.y})"

    def move(self, keys:str):
        if keys[pygame.K_LEFT] and self.x >= 0:
            self.x -= 2
        if keys[pygame.K_RIGHT] and self.x <= (640 - self.robot_img.get_width()):
            self.x += 2


def calculate_rock_position(rock, robot):
    is_pos_ok_x = False
    is_pos_ok_y = False

    if rock.x in range(robot.x,robot.x+robot.robot_img.get_width()):
        is_pos_ok_x = True
    if rock.y in range(robot.y,robot.y+robot.robot_img.get_height()):
        is_pos_ok_y = True

    if is_pos_ok_x and is_pos_ok_y:
        rock.status = "destroy"

def create_rocks(list_rocks):
    if random.randint(1, 75) == 1:
        list_rocks.append(Rock(random.randint(0, 590), 0))

def update_and_draw_rock(rocks, window, points):
    for rock in rocks[:]:
        calculate_rock_position(rock,robot)
        if rock.status == "destroy":
            rocks.remove(rock)
            points.update_points()
        window.blit(rock.rock_img, (rock.x, rock.y))
        

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

game_font = pygame.font.SysFont("Arial", 24)

points = Points()


robot = Robot()

list_rocks = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    create_rocks(list_rocks)

    keys = pygame.key.get_pressed()
    robot.move(keys)
    update_and_draw_rock(list_rocks,window, points)

    window.blit(robot.robot_img, (robot.x, robot.y))


    text = game_font.render(f"{points.text}{points._points}", True, points.color)
    window.blit(text, (525, 5))

    pygame.display.flip()
    clock.tick(60)