# Write your solution here
def new_person(name: str, age: int):
    """
        name is an empty string
        name contains less than two words
        name is longer than 40 characters
        age is a negative number
        age is greater than 150
    """

    if len(name) == 0:
        raise ValueError("The name is empty")
    elif " " not in name:
        raise ValueError("Please enter your full name")
    elif len(name) > 40:
        raise ValueError("The name is too long")

    if age < 0:
        raise ValueError("mpossible age")
    elif age > 150:
        raise ValueError("Too old")

    return (name, age)

if __name__ == "__main__":
    new_person("Daniel Escoval", 32)