# Write your solution here
import math
input_str = input("Word: ")
# print(len(input_str))

frame = "*"*30
white_space = math.floor((30-2-len(input_str))/2)
# print(white_space)

if len(input_str) % 2 == 0:
    inner_frame = "*" + " "*white_space + input_str + " "*white_space + "*"
else:
    inner_frame = "*" + " "*white_space + input_str + " "*(white_space+1) + "*"

print(frame)
print(inner_frame)
print(frame)