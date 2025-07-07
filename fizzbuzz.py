# Write your solution here
nb = int(input("Number: "))
if (nb / 3) % 1 == 0 and (nb / 5) % 1 == 0:
    print("FizzBuzz")
elif (nb / 3) % 1 == 0:
    print("Fizz")
elif (nb / 5) % 1 == 0:
    print("Buzz")
