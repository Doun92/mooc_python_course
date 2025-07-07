# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit ")
    inpt = input("Function: ")

    if inpt == "1":
        inpt = input("Diary entry: ")
       
        history = []
        with open("diary.txt", "r") as diary_file:
            for line in diary_file.readlines():
                history.append(line)                

        if len(history) > 0:
            last_item = history[-1]

        with open("diary.txt", "w") as diary_file:
            for entry in history:
                diary_file.write(f"{entry}\n")
            diary_file.write(inpt)

    elif inpt == "2":
        with open("diary.txt", "r") as diary_file:
            print("Entries:")
            print(diary_file.read())
    elif inpt == "0":
        print("Bye now!")
        break