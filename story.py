# Write your solution here
story = ""

last_word = ""

while True:
    word = input("Please type in a word: ")
    
    if word == "end":
        break
    elif word == last_word:
        break
    story += word + " "
    last_word = word

print(story)