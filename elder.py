# Write your solution here
print("Person 1:")
person_1 = input("Name: ")
age_1 = int(input("Age: "))
print("Person 2:")
person_2 = input("Name: ")
age_2 = int(input("Age: "))
if age_1 > age_2:
    print(f"The elder is {person_1}")
elif age_2 > age_1:
    print(f"The elder is {person_2}")
else:
    print(f"{person_1} and {person_2} are the same age")