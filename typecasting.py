import math
# Write your solution here
number = input("Please type in a number: ")
print(f"Integer part: {math.floor(float(number))}")
print(f"Decimal part: {float(number)%1}")