# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    unit = Fraction(1,amount)
    return [unit]*amount

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print(fractionate(5))