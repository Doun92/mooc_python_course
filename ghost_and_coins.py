# WRITE YOUR SOLUTION HERE:
# Import different libraries
import pygame
import random
import time
import csv
import os

# Create super class
class GameItem:
    def __init__(self, x:int, y:int, vector:int, speed:int, status:str):
        self._x = x
        self._y = y
        self._vector = vector
        self._speed = speed
        self._status = status

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def status(self):
        return self._status

class Shoot(GameItem):
    def __init__(self, x:int, y:int, vector:int, speed:int, status:str, color:tuple, shooter:str):
        super().__init__(x, y, vector, speed, status)
        self.text = "|"
        self.color = color
        self.shooter = shooter

    def __str__(self):
        return f"laser created, at coordinate ({self.x}, {self.y})"

    @property
    def y(self):
        self._y += self._vector + self._speed
        return self._y

    def touches_something(self, target, points):
        if isinstance(target, list):
            for item in target:
                is_touching_x = self._x in range(item.x,item.x+item.width)
                is_touching_y = self._y in range(item.y,item.y+item.get_height())
                if is_touching_x and is_touching_y:
                    if self.shooter == "robot" and isinstance(item, Monster):
                        points.update_points(10)
                        self._status = "destroy"
                        item._status = "destroy"
                    else:
                        self._status = "destroy"
                        item._status = "destroy"
        elif isinstance(target, Robot):
            is_touching_x = target.x <= self._x <= target.x + target.robot_img.get_width()
            is_touching_y = target.y <= self._y <= target.y + target.robot_img.get_height()
            if is_touching_x and is_touching_y and not target.is_invincible:
                target.is_invincible = True
                target.last_time = pygame.time.get_ticks()
                lives.life_count -= 1
                self._status = "destroy"

class Robot(GameItem):
    def __init__(self, x:int, y:int, vector:int, speed:int, status:str):
        super().__init__(x, y, vector, speed, status)
        self.robot_img = pygame.image.load("src\\robot.png")
        self.jump_velocity = 0
        self.gravity = 1
        self.is_jumping = False
        self.cooldowns = 500
        self.last_time = 0
        self.is_invincible = False

    def __str__(self):
        return f"Robot at coordinates ({self.x},{self.y})"


    def jump(self, keys):
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_UP] and not self.is_jumping and current_time - self.last_time >= self.cooldowns:
            self.jump_velocity = -20
            self.is_jumping = True
            self._status = "jump"
            self.last_time = current_time

    def apply_gravity(self):
        if self.is_jumping:
            self._y += self.jump_velocity
            self.jump_velocity += self.gravity

            # Prevent falling below ground
            ground_y = 480 - self.robot_img.get_height()
            if self._y >= ground_y:
                self._y = ground_y
                self.is_jumping = False
                self._status = "walk"

    def move(self, keys:str):
        if keys[pygame.K_LEFT] and self._x >= 0:
            self._x -= 4
        if keys[pygame.K_RIGHT] and self._x <= (640 - self.robot_img.get_width()):
            self._x += 4

    def shoot(self, keys:str, shoot_list):
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and current_time - self.last_time >= self.cooldowns:
            new_shoot = Shoot(self._x + self.robot_img.get_width()// 2, self.y, -5, 0, "exists", (255, 0, 0), "robot")    
            # print(new_shoot)
            shoot_list.append(new_shoot)
            self.last_time = current_time

class Coin(GameItem):
    def __init__(self, x:int, y:int, vector:int, speed:int, status:str):
        super().__init__(x, y, vector, speed, status)
        self.coin_img = pygame.image.load("src\\coin.png")
        self.width = self.get_width()
        self.height = self.get_height()


    def update_y(self):
        self._y += self._vector + self._speed

    def get_width(self):
        self.width = self.coin_img.get_width()
        return self.width

    def get_height(self):
        self.height = self.coin_img.get_height()
        return self.height

    def calculate_coin_position(self, robot):
        is_pos_ok_x = False
        is_pos_ok_y = False

        if self._x in range(robot.x,robot.x+robot.robot_img.get_width()) or self._x + self.coin_img.get_width() in range(robot.x, robot.x + robot.robot_img.get_width()):
            is_pos_ok_x = True
        if self._y in range(robot.y,robot.y+robot.robot_img.get_height()) or self._y + self.coin_img.get_height() in range(robot.y, robot.y + robot.robot_img.get_height()):
            is_pos_ok_y = True

        if is_pos_ok_x and is_pos_ok_y:
            self._status = "gathered"

class Points:
    def __init__(self):
        self.text = "Points: "
        self.color = (255, 0, 0)
        self._points = 0

    @property
    def points(self):
        return self._points

    def update_points(self, nb_points: int):
        self._points += nb_points

class Monster(GameItem):
    def __init__(self, x:int, y:int, vector:int, speed:int, status:str, monster_type:str):
        super().__init__(x, y, vector, speed, status)
        self.current_direction = None
        self.last_change = time.time()
        self.monster_type = monster_type
        self.monster_img = self.set_color()
        self.height = self.get_height()
        self.width = self.get_width()
        
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    # Set colors to differentiate each monster type
    def set_color(self):
        monster_img = pygame.image.load("src\\monster.png").convert_alpha()

        # Black
        if self.monster_type == "bombs":
            color = (33, 71, 62)
        # White
        elif self.monster_type == "random":
            color = (220, 224, 254)
        # Purple
        elif self.monster_type == "sniper":
            color = (192, 51, 224)

        # Lock surface for pixel access
        pixel_array = pygame.PixelArray(monster_img)

        # Replace black with colors
        natural_black = monster_img.map_rgb((0, 0, 0))
        new_color = monster_img.map_rgb(color)
        pixel_array.replace(natural_black, new_color)


        # Delete the list
        del pixel_array

        return monster_img

    def get_width(self):
        self.width = self.monster_img.get_width()
        return self.width

    def get_height(self):
        self.height = self.monster_img.get_height()
        return self.height

    # Random mooves for the random monster
    def random_move(self):
        now = time.time()
        if self.current_direction is None or now - self.last_change >= 0.5:
            self.current_direction = random.choice(["left", "top", "bottom", "right"])
            self.last_change = now
        if self.current_direction == "left":
            if self._x > 0:
                self._x -= self._vector + self._speed
            else:
                self.current_direction = random.choice(["top", "bottom", "right"])
                self.last_change = now
        if self.current_direction == "top":
            if self._y > 0:
                self._y -= self._vector + self._speed
            else:
                self.current_direction = random.choice(["left", "bottom", "right"])
                self.last_change = now
        if self.current_direction == "right":
            if self._x < 640 - self.width:
                self._x += self._vector + self._speed
            else:
                self.current_direction = random.choice(["left", "top", "bottom"])
                self.last_change = now
        if self.current_direction == "bottom":
            if self._y < 480 - self.height:
                self._y += self._vector + self._speed
            else:
                self.current_direction = random.choice(["left", "top", "right"])
                self.last_change = now

    def calculate_monster_position(self, robot):
        is_pos_ok_x = False
        is_pos_ok_y = False

        if self._x in range(robot.x,robot.x+robot.robot_img.get_width()) or self._x + self.width in range(robot.x, robot.x + robot.robot_img.get_width()):
            is_pos_ok_x = True
        if self._y in range(robot.y,robot.y+robot.robot_img.get_height()) or self._y + self.height in range(robot.y, robot.y + robot.robot_img.get_height()):
            is_pos_ok_y = True

        if is_pos_ok_x and is_pos_ok_y and not robot.is_invincible:
            robot.is_invincible = True
            robot.last_time = pygame.time.get_ticks()
            lives.life_count -= 1
            self._status = "destroy"


    def fall(self):
        self._y += self._vector + self._speed
        if self._y == 480 - self.height:
            self._status = "destroy"

    def shoot(self, shoot_list):
        now = time.time()
        if now - self.last_change >= random.randint(2,5 ):
            new_shoot = Shoot(self.x + self.width// 2, self.y+self.height+1, 2, random.randint(0,2), "exists", (255, 255, 255), "ghost")    
            shoot_list.append(new_shoot)
            self.last_change = now

class Lives:
    def __init__(self):
        self.life_count = 5
        self.text = "Lives: "
        self.color = (255, 0, 0)

def create_coins(list_coins):
    if random.randint(1, 33) == 1:
        random_x = random.randint(0, 590)
        random_speed = random.randint(0,2)
        list_coins.append(Coin(random_x, 0, 1,random_speed,"falling"))

def create_monsters(list_monsters, rate):
    spawn_rate_random = random.randint(1, rate)
    if  spawn_rate_random == 1:
        random_monster = random.randint(1,3)
        random_x = random.randint(0, 590)
        if random_monster == 1:
            random_speed = random.randint(0,3)
            # Monster from above that goes down (Bombs)
            list_monsters.append(Monster(random_x, 0, 1, random_speed,"alive","bombs"))
        elif random_monster == 2:
            # Monster that moves randomly
            random_speed = random.randint(0,2)
            random_y = random.randint(50, 300)
            list_monsters.append(Monster(random_x, random_y, 1, random_speed, "alive", "random"))
        elif random_monster == 3:
            # Monster that shoots
            list_monsters.append(Monster(random_x, 0, 0, 0, "alive", "sniper"))

def update_and_draw_coin(coins, window, points, robot, rate):
    for coin in coins[:]:
        coin.update_y()
        coin.calculate_coin_position(robot)
        if coin._status == "gathered":
            coins.remove(coin)
            points.update_points(1)
            if rate > 10:
                rate -= 1
        if coin._status == "destroy":
            coins.remove(coin)
        window.blit(coin.coin_img, (coin.x, coin.y))
    return rate

def update_and_draw_shoots(shoots, window, target, points):
    for shoot in shoots[:]:
        shoot.touches_something(target, points)
        y = shoot.y
        if y < 0 or y > 480 or shoot._status == "destroy":
            shoots.remove(shoot)
        text_shoot = game_font.render(shoot.text, True, shoot.color)
        window.blit(text_shoot, (shoot._x, y))

def update_and_draw_monsters(monsters, window, points):
    for monster in monsters[:]:
        if monster.monster_type == "random":
            monster.random_move()
        if monster.monster_type == "bombs":
            monster.fall()
        if monster.monster_type == "sniper":
            monster.shoot(list_shoots)
        monster.calculate_monster_position(robot)
        if monster._status == "destroy":
            monsters.remove(monster)
        window.blit(monster.monster_img, (monster._x, monster._y))

def show_welcome_menu(window, font):
    title = font.render("Coins and Ghosts", True, (255, 255, 0))
    instructions = [
        "Goal: Collect coins to gain points.",
        "Avoid the ghosts or their lasers.",
        "SPACE to shoot.",
        "Arrows to move and jump",
        "Press ENTER to start !"
    ]
    window.blit(title, (60, 50))
    for i, line in enumerate(instructions):
        text = font.render(line, True, (255, 255, 255))
        window.blit(text, (40, 120 + i * 35))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False

def show_game_over_screen(window, font, p:Points):
    window.fill((0, 0, 40))
    game_over_text = [
        "Game Over!",
        f"You scored {p.points} points"
        ]
    for i, text in enumerate(game_over_text):
        game_over_txt = font.render(text, True, (255, 255, 255))
        window.blit(game_over_txt, (100, 180+(i*35)))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False

pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Coins and Ghosts')
clock = pygame.time.Clock()
game_font = pygame.font.SysFont("Arial", 24)
rate = 400

robot = Robot(200, 390, 1, 1, "walk")
text_points = Points()
lives = Lives()
list_coins = []
list_shoots = []
list_monsters = []

show_welcome_menu(window, game_font)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    robot.move(keys)
    robot.jump(keys)
    robot.shoot(keys, list_shoots)
    robot.apply_gravity()
    blink = True
    if robot.is_invincible:
        if (pygame.time.get_ticks() // 100) % 2 == 0:
            blink = False

    window.fill((0, 0, 40))

    create_coins(list_coins)
    create_monsters(list_monsters, rate)

    rate = update_and_draw_coin(list_coins,window, text_points, robot, rate)
    update_and_draw_shoots(list_shoots, window, list_coins, text_points)
    update_and_draw_shoots(list_shoots, window, list_monsters, text_points)
    update_and_draw_shoots(list_shoots, window, robot, text_points)
    update_and_draw_monsters(list_monsters, window, text_points)

    # Invincibility timer: 2 seconds after being hit
    if robot.is_invincible and pygame.time.get_ticks() - robot.last_time > 500:
        robot.is_invincible = False
    if not robot.is_invincible or blink:
        window.blit(robot.robot_img, (robot.x, robot._y))



    text = game_font.render(f"{text_points.text}{text_points._points}", True, text_points.color)
    lives_txt = game_font.render(f"{lives.text}{lives.life_count}", True, lives.color)
    window.blit(text, (525, 5))
    window.blit(lives_txt, (425, 5))    

    pygame.display.flip()
    clock.tick(60)

    if lives.life_count == 0:
        show_game_over_screen(window, game_font, text_points)
        break