# Write your solution here
str_1 = input("Please type in string 1: ")
str_2 = input("Please type in string 2: ")

if len(str_1) > len(str_2):
    print(f"{str_1} is longer")
elif len(str_1) < len(str_2):
    print(f"{str_2} is longer")
else:
    print("The strings are equally long")