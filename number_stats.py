# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        result = 0
        for number in self.numbers:
            result += number
        return result

    def average(self):
        result = 0
        for number in self.numbers:
            result += number

        try:
            div_solution = result/len(self.numbers)
            return div_solution
        except:
            return "Impossible to divide by zéro"


stats = NumberStats()
evennum = NumberStats()
oddnumb = NumberStats()

while True:
    numb = int(input("Please type in integer numbers: "))
    if numb == -1:
        break
    else:
        if numb % 2 == 0:
            evennum.add_number(numb)
        else:
            oddnumb.add_number(numb)

        stats.add_number(numb)
print(f"Sum of numbers: {stats.get_sum()}")
print(f"Sum of even numbers: {evennum.get_sum()}")
print(f"Sum of odd numbers: {oddnumb.get_sum()}")
print(f"Mean of numbers: {stats.average()}")