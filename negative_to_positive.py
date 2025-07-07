# Write your solution here
char = int(input("Please type in a positive integer: "))

ranged_list = range(char * -1, char+1)

for i in ranged_list:
    if i == 0:
        pass
    else:
        print(i)