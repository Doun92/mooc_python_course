# Write your solution here
input_str = input("Please type in a string: ")

star_str = "*"

if len(input_str) < 20:
    nb_to_add = 20 - len(input_str)
    print(star_str * nb_to_add + input_str)
else:
    print(input_str)