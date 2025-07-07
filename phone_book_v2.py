
# Write your solution here:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address:str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)


    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        # numbers = self.__phonebook.get_entry(name)
        person = self.__phonebook.get_entry(name)

        if person == None:
            person = Person(name)
            print("number unknown") 
            print("address unknown")
        else:
            if len(person.numbers()) == 0:
                print("number unknown") 
            else:
                for number in person.numbers():
                    print(number)
            if person.address() == None:
                print("address unknown")
            else:
                print(person.address())
        


    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

class Person:
    def __init__(self, name):
        self._name = name
        self._numbers = []
        self._address = None

    def __str__(self):
        return f"{self._name}: {self._numbers}"

    # Comme il cherche avec des parenthèses, je ne dois pas mettre les @property et @variable.setter (d'ailleurs ils sont dans l'ordre inverse, également)
    # @name.setter
    def name(self, name):
        self._name = name
        
    # @property
    def name(self):
        return self._name

    def numbers(self, numbers):
        self._numbers = numbers

    def numbers(self):
        return self._numbers

    def add_number(self, number):
        self._numbers.append(number)
        return self

    def address(self, address):
        self._address = address

    def address(self):
        return self._address

    def add_address(self, address):
        self._address = address
        return self

# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

# if __name__ == "__main__":
#     person = Person("Eric")
#     print(person.name())
#     print(person.numbers())
#     print(person.address())
#     person.add_number("040-123456")
#     person.add_address("Mannerheimintie 10 Helsinki")
#     print(person.numbers())
#     print(person.address())

    # phonebook = PhoneBook()
    # phonebook.add_number("Eric", "02-123456")
    # print(phonebook.get_entry("Eric"))
    # print(phonebook.get_entry("Emily"))