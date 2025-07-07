# Write your solution here
from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    list_numbers = []

    while len(list_numbers) < amount:
        new_nb = randint(lower, upper)
        if new_nb not in list_numbers:
            list_numbers.append(new_nb)

    return sorted(list_numbers)

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)