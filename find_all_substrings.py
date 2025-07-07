# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")

idx = word.find(character)

while True:

    if idx >= len(word):
        break

    if idx == -1:
        break
    else:
        if len(word[idx:idx + 3])<3:
            break
        else:
            if word[idx:idx + 3][0] == character:
                print(word[idx:idx + 3])
        idx +=1