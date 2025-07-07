# Write your solution here
nb = int(input("Please type in a number: "))

idx = 1

while idx < nb:
    if idx % 2 == 0:
        # print("pair")
        print(idx-1)
    elif idx % 2 != 0:
        # print("impair")
        print(idx+1)
    idx += 1
if nb %2 != 0:
    print(nb)
else:
    print(nb-1)