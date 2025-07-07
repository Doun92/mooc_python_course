# Write your solution here
from string import ascii_lowercase
import random

def generate_password(length: int):
    password = ""
    while len(password) < length:
        rand_num = random.randint(0,len(ascii_lowercase)-1)
        password += ascii_lowercase[rand_num]

    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))