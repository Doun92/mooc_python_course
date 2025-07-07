# Write your solution here
upper_limit = int(input("Upper limit: "))
base = int(input("Base: "))

lower_limit = 1

while lower_limit <= upper_limit:
    print(lower_limit)
    lower_limit = lower_limit*base