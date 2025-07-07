# Write your solution here
def prime_numbers():
    idx = 2
    while True:
        for x in range(2,idx):
            if idx % x == 0:
                break
        else:
            yield idx
        idx += 1

if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))