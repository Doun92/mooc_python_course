# Write your solution here
liste = []

while True:
    word = input("Word: ")

    if word in liste:
        print(f"You typed in {len(liste)} different words")
        break
    else:
        liste.append(word)