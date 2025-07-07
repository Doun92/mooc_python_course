# Write your solution here


while True:
    nb = int(input("Please type in a number: "))

    idx = nb

    factorisation = 1
    if nb <= 0:
        print("Thanks and bye!")
        break
    else:
        while idx > 0:
            factorisation = factorisation*idx
            idx -= 1
        print(f"The factorial of the number {nb} is {factorisation}")