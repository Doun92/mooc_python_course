# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self._name = name
        self._weight = weight

    def name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def weight(self):
        return self._weight
    
    def set_weight(self, weight):
        self._weight = weight

    def __str__(self):
        return f"{self._name} ({self._weight} kg)"

class Suitcase:
    def __init__(self, max_weight):
        self._max_weight = max_weight
        self._list_items = []

    def max_weight(self):
        return self._max_weight
    
    def set_max_weight(self, max_weight):
        self._max_weight = max_weight
    
    def __str__(self):
        max_weight = 0
        for i in self._list_items:
            max_weight += i.weight()

        if len(self._list_items) == 1:
            return f"{len(self._list_items)} item ({max_weight} kg)"
        else:
            return f"{len(self._list_items)} items ({max_weight} kg)"

    def add_item(self, item:"Item"):
        # print(item.weight())

        actual_weight = 0
        for i in self._list_items:
            actual_weight += i.weight()
        # print(f"actual_weight = {actual_weight}")

        if item.weight() + actual_weight <= self._max_weight:
            self._list_items.append(item)
        else:
            print("Too heavy")

        return self._list_items

    def print_items(self):
        for i in self._list_items:
            print(i)

    def weight(self):
        combined_weight = 0
        for i in self._list_items:
            combined_weight += i.weight()
        return combined_weight

    def heaviest_item(self):
        heaviest_weight = 0
        for i in self._list_items:
            if i.weight() > heaviest_weight:
                heaviest_weight = i.weight()
                heaviest_item = i
        return heaviest_item


class CargoHold:
    def __init__(self, max_weight):
        self.max_weight =  max_weight
        self._list_suitcases = []
    

    def __str__(self):
        actual_weight = 0
        for s in self._list_suitcases:
            actual_weight += s.weight()

        remaining_space = self.max_weight - actual_weight

        if len(self._list_suitcases) == 1:
            return f"{len(self._list_suitcases)} suitcase, space for {remaining_space} kg"
        else:
            return f"{len(self._list_suitcases)} suitcases, space for {remaining_space} kg"

    def add_suitcase(self, suitcase: "Suitcase"):
        actual_weight = 0
        for s in self._list_suitcases:
            actual_weight += s.weight()
        
        if actual_weight + suitcase.weight() <= self.max_weight:
            self._list_suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self._list_suitcases:
            suitcase.print_items()


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()