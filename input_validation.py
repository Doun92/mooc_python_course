from math import sqrt
# Write your solution here
continue_maths = True

while continue_maths:
    nb = int(input("Please type in a number: "))
    if nb < 0:
        print("Invalid number")
    elif nb == 0:
        print("Exiting...")
        continue_maths = False
    else:
        print(sqrt(nb))