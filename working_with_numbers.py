# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")

numbers_of_nb = 0
addition_of_nb = 0
positive_numbers = 0
negative_numbers = 0

while True:
    nb = int(input("Number:"))
    addition_of_nb += nb
    print(f"Number: {nb}")
    if nb > 0:
        positive_numbers += 1
    elif nb < 0:
        negative_numbers += 1
    if nb == 0:
        break
    else:
        numbers_of_nb += 1
print(f"Numbers typed in {numbers_of_nb}")
print(f"The sum of the numbers is {addition_of_nb}")
print(f"The mean of the numbers is {addition_of_nb/numbers_of_nb}")
print(f"Positive numbers {positive_numbers}")
print(f"Negative numbers {negative_numbers}")