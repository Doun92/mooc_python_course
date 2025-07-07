# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(nbs: list):
    if len(nbs) % 5 != 0 :
        nbs.append(nbs[-1]+1)
        add_numbers_to_list(nbs)

if __name__ == "__main__":
    numbers = [1,3,4,5,10,11]
    add_numbers_to_list(numbers)
    print(numbers)