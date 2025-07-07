# Write your solution here
def store_personal_data(person: tuple):       
    from_file = []
    with open("people.csv", "r") as people_file:
        for line in people_file.readlines():
            from_file.append(line)                

    list_person = []
    for i in person:
        list_person.append(i)

    with open("people.csv", "w") as people_file:
        for f in from_file:
                people_file.write(f"{f}\n")
        people_file.write(f"{list_person[0]};{list_person[1]};{list_person[2]}")

if __name__ == "__main__":
    entry = ("Paul Paulson", 37, 175.5)
    store_personal_data(entry)