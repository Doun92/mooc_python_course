# Write your solution here
def even_numbers(beginning: int, maximum: int):
    idx = beginning
    while idx <= maximum:
        if idx % 2 == 0:
            yield idx
            idx += 1
        else:
            idx += 1

if __name__ == "__main__":
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)

    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)