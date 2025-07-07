# Write your solution here
def oldest_person(people: list):
    temp_dict = {}

    for person in people:
        temp_dict[person[0]] = person[1]
    
    smallest_year = list(temp_dict.values())[0]
    # print(smallest_year)

    for key, value in temp_dict.items():
        if value < smallest_year:
            smallest_year = value
    

    oldest_person = list(temp_dict.keys())[list(temp_dict.values()).index(smallest_year)]
    return oldest_person

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))