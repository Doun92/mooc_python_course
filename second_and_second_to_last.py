# Write your solution here
input_str = input("Please type in a string: ")
if input_str[1] == input_str[-2]:
    print(f"The second and the second to last characters are {input_str[1]}")
else:
    print("The second and the second to last characters are different")