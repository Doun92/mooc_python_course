# Write your solution here
import string
import random

def generate_strong_password(length: int, with_nb: bool, with_spec: bool):
    list_of_char = string.ascii_lowercase

    if with_nb:
         list_of_char +=  string.digits
    if  with_spec:
        list_of_char += "!?=+-()#"

    password = ""
    while len(password) < length:
        rand_num = random.randint(0,len(list_of_char)-1)
        password += list_of_char[rand_num]

    if with_nb:
        password = password.replace(password[random.randint(0,len(password)-1)],random.choice(string.digits))
    
    if with_spec:
        password = password.replace(password[random.randint(0,len(password)-1)],random.choice("!?=+-()#"))

    return password

if __name__ == "__main__":
    # for i in range(10):
    #     print(generate_strong_password(8, True, True))
    # print(generate_strong_password(5, False, False))
    # print(generate_strong_password(5, False, True))
    # print(generate_strong_password(5, True, False))
    # print(generate_strong_password(5, True, True))
    # print(generate_strong_password(2, False, False))
    # print(generate_strong_password(8, True, False))
    print(generate_strong_password(12, True, True))