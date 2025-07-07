# write your solution here
def read_fruits():
    empty_dict = {}

    with open("fruits.csv") as file:
        for row in file:
            # print(row)
            parts = row.split(";")
            empty_dict[parts[0]] = float(parts[1])
    return empty_dict

if __name__ == "__main__":
    read_fruits()