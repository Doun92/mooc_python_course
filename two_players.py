# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

class Robot():
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
        self.img = pygame.image.load("src\\robot.png")

    def __str__(self):
        return f"I am Robot {self.id}, my coordinates are ({self.x},{self.y})"

    def move(self, keys:str):
        if self.id == "A":
            if keys[pygame.K_LEFT] and self.x >= 0:
                self.x -= 2
            if keys[pygame.K_RIGHT] and self.x <= (640 - self.img.get_width()):
                self.x += 2
            if keys[pygame.K_UP] and self.y >= 0:
                self.y -= 2
            if keys[pygame.K_DOWN] and self.y <= (480 - self.img.get_height()):
                self.y += 2

        elif self.id == "B":
            if keys[pygame.K_a] and self.x >= 0:
                self.x -= 2
            if keys[pygame.K_d] and self.x <= (640 - self.img.get_width()):
                self.x += 2
            if keys[pygame.K_w] and self.y >= 0:
                self.y -= 2
            if keys[pygame.K_s] and self.y <= (480 - self.img.get_height()):
                self.y += 2


robot_A = Robot(50,50, "A")
robot_B = Robot(150,150, "B")
print(robot_A)
print(robot_B)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    keys = pygame.key.get_pressed()
    robot_A.move(keys)
    robot_B.move(keys)


    window.fill((0, 0, 0))
    window.blit(robot_A.img, (robot_A.x, robot_A.y))
    window.blit(robot_B.img, (robot_B.x, robot_B.y))
    pygame.display.flip()

    

    clock.tick(60)