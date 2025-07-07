# Write your solution here
nb_1 = int(input("Please type in the first number: "))
nb_2 = int(input("Please type in another number: "))
if nb_1 > nb_2:
    print(f"The greater number was: {nb_1}")
elif nb_2 > nb_1:
    print(f"The greater number was: {nb_2}")
else:
    print("The numbers are equal!")