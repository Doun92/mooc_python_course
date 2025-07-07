word = input("Please type in a word: ")
character = input("Please type in a character: ")

idx_1 = word.find(character)

# If character is not found or not enough characters remain, print nothing
if idx_1 == -1 or idx_1 + 3 > len(word):
    print("")  # Or simply do nothing
else:
    print(word[idx_1:idx_1 + 3])