# Write your solution here
# Write your solution here
phone_book = {}
while True:
    cmd = input("command (1 search, 2 add, 3 quit): ")

    if cmd == "1":
        name = input("name: ")
        if name in phone_book:
            for nb in phone_book[name]:
                print(nb)
            # print(phone_book[name][-1])
        else:
            print("no number")
    elif cmd == "2":
        name = input("name: ")
        number = input("number: ")
        if name not in phone_book:
            phone_book[name] = [number]
        else:
            phone_book[name].append(number)

        print("ok!")

    elif cmd == "3":
        print("quitting...")
        break