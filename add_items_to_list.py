# Write your solution here
nb_items = int(input("How many items: "))

idx = 1

liste = []

while idx <= nb_items:
    entry = int(input(f"Item {idx}: "))

    liste.append(entry)

    idx +=1

print(liste)