# write your solution here
input_from_usr = input("Write text: ")


marked_sentence = ""
with open("wordlist.txt") as wordlist:
    data = wordlist.readlines()
    for word in input_from_usr.split(" "):
        if f"{word.lower()}\n" not in data:
            word = f"*{word}*"
        marked_sentence += f"{word} "

print(marked_sentence[:-1])