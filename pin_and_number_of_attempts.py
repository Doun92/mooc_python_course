nb_attempts = 0

while True:
    # Write your solution here
    answer = input("PIN: ")
    if answer != "4321":
        print("Wrong")
        nb_attempts += 1
    else:
        if nb_attempts == 0:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {nb_attempts+1} attempts")
        break