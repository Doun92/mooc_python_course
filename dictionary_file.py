# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    inpt = input("Function: ")

    if inpt == "1":
        inpt_fin = input("The word in Finnish: ")
        inpt_en =  input("The word in English: ")

        history = []
        with open("dictionary.txt", "r") as dict_file:
            for line in dict_file.readlines():
                history.append(line)

        if len(history) > 0:
            last_item = history[-1]

        with open("dictionary.txt", "w") as dict_file:
            for entry in history:
                dict_file.write(entry)
            dict_file.write(f"{inpt_fin} - {inpt_en}\n")
        print("Dictionary entry added")
    elif inpt == "2":
        answer = []
        with open("dictionary.txt", "r") as dict_file:
            search = input("Search term: ")
            for entry in dict_file.readlines():
                if search in entry:
                    answer.append(entry[:-1])
        
        for item in answer:
            print(item)

    elif inpt == "3":
        print("Bye!")
        break