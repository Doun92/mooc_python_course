# Write your solution here
def older_people(people: list, year: int):
    temp_dict = {}

    for person in people:
        temp_dict[person[0]] = person[1]

    older_people = []
    for key, value in temp_dict.items():
        if value < year:
            older_people.append(key)
    
    return older_people
    

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)