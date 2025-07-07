# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people_in_room = []
        self.shortest_person = None

    def add(self, person: "Person"):
        "Adds the person given as an argument to the room."
        self.people_in_room.append(person)

    def is_empty(self):
        "Returns True or False depending on whether the room is empty."
        if len(self.people_in_room) == 0:
            return True
        else:
            return False

    def print_contents(self):
        "Prints out the contents of the list of persons in the room."

        max_weight = 0
        for p in self.people_in_room:
            max_weight += p.height

        print(f"There are {len(self.people_in_room)} in the room, and theur combined height is {max_weight} cm")

        for p in self.people_in_room:
            print(f"{p.name} ({p.height} cm)")

    def shortest(self):
        if len(self.people_in_room) == 0:
            return None
        else:
            list_heights = [p.height for p in self.people_in_room]
            min_height = min(list_heights)

            for p in self.people_in_room:
                if p.height == min_height:
                    if self.shortest_person == None:
                        self.shorest_person = p
                    return p

    def remove_shortest(self):
        if len(self.people_in_room) == 0:
            return None
        else:
            if self.shortest_person:
                pass
            else:
                self.shortest_person = self.shortest()

            removed_idx = self.people_in_room.index(self.shortest_person) 
            removed = self.people_in_room.pop(removed_idx)
            self.shortest_person = None
            return removed
        


if __name__ == "__main__":
    # room = Room()

    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Nina", 162))
    # room.add(Person("Ally", 166))
    # room.print_contents()

    # print()

    # removed = room.remove_shortest()
    # print(f"Removed from room: {removed.name}")

    # print()

    # room.print_contents()

    room = Room()
    test_cases = [("Grace", 180), ("Jan", 175), ("Lisa", 150), ("Paul", 204), ("Jana", 171), ("Ruth", 149)]

    tested = []
    persons = ""
    for test_case in test_cases:
        room.add(Person(test_case[0], test_case[1]))
        persons += f"\n{test_case[0]} ({test_case[1]} cm)"
        tested.append(test_case)
    prev_output = ""
    for i in range(len(test_cases)):
        val = room.remove_shortest()
        corr = min(tested, key = lambda x : x[1])
        
        tested.remove(corr)

        room.print_contents()
