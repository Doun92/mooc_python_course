# Write your solution here
def read_input(request: str, min_value: int, max_value: int):
    while True:
        try:
            inpt = int(input(request))
            if inpt >= min_value and inpt <= max_value:
                return inpt
            else:
                print(f"You must type in an integer between {min_value} and {max_value}")
        except ValueError:
            print(f"You must type in an integer between {min_value} and {max_value}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)