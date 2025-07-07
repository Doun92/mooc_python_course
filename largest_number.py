# write your solution here
def largest():
    bigger_nb = 0
    with open("numbers.txt") as numbers_file:
        for line in numbers_file:
            if int(line) > bigger_nb:
                bigger_nb = int(line)

    return bigger_nb

if __name__ == "__main__":
    largest()