# Write your solution here
w = int(input("Width: "))
h = int(input("Height: "))

idx = 0
hash_str = "#"

while idx < h:
    print(hash_str * w)
    idx +=1