# Write your solution here
souligner = "-"
while True:
    input_str = input("Please type in a string: ")

    if len(input_str) == 0:
        break
    else:
        print(input_str)
        print(souligner * len(input_str))