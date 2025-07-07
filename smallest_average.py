# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    list_persons = [person1, person2, person3]

    person_with_smallest_result = ""
    smallest_result = 100

    # Average results calculation
    for person in list_persons:
        person_checked = ""
        result = 0
        for k,v in person.items():
            if type(v) == str:
                person_checked = v
            if type(v) == int:
                result += v
        if result < smallest_result:
            person_with_smallest_result = person_checked
            smallest_result = result

    print(f"smallest_result = {smallest_result}")
    for person in list_persons:
        r = 0
        p = ""
        # print(f"person = {person}")
        calc_list = []
        for v in person.values():
            if type(v) == str:
                p = v
            if type(v) == int:
                # r += v
                calc_list.append(v)
        for n in calc_list:
            r += n
        if r == smallest_result:
            # print(f"r = {r}")
            if p == person_with_smallest_result:
                return person
            

if __name__ == "__main__":
    # person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    # person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    # person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    # print(smallest_average(person1, person2, person3))

    person1 = {'name': 'Anna', "result1": 3,"result2": 3,"result3": 3}
    person2 = {'name': 'Anna', "result1": 5,"result2": 5,"result3": 5}
    person3 = {'name': 'Anna', "result1": 1,"result2": 1,"result3": 1}
    print(smallest_average(person1, person2, person3))