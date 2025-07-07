# Write your solution here
nb = int(input("Please type in a number: "))

left_nb = 1

while nb > 0:
    while left_nb <= nb:
        idx = 1
        while idx <= nb:
            print(f"{left_nb} x {idx} = {left_nb * idx}")
            idx += 1
        left_nb +=1
    nb -= 1