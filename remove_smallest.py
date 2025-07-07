# Write your solution here
def remove_smallest(numbers: list):
    smallest_number = numbers[0]
    
    for i in numbers:
        if i < smallest_number:
            smallest_number = i
    numbers.remove(smallest_number)
    

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)