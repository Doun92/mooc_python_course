# Write your solution here
liste = []

idx = 1

while True:
    print(f"The list is now {liste}")

    r = input("a(d)d, (r)emove or e(x)it: ")

    if r == "d":
        liste.append(idx)
        idx += 1
    elif r == "r":
        liste.pop(-1)
        idx -= 1
    elif r == "x":
        print("Bye!")
        break
    else:
        pass