# Write your solution here
def invert(dictionary: dict):
    revert_dict  = {}

    for key, value in dictionary.items():
        revert_dict[value] = key

    # print(revert_dict)

    dictionary.clear()
    dictionary.update(revert_dict)

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)