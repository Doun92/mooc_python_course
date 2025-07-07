# Write your solution here
import difflib

input_from_usr = input("Write text: ")

list_of_errors = []

marked_sentence = ""
with open("wordlist.txt") as wordlist:
    data = wordlist.readlines()
    for word in input_from_usr.split(" "):
        if f"{word.lower()}\n" not in data:
            list_of_errors.append(word)
            word = f"*{word}*"
        marked_sentence += f"{word} "

clean_data = [x.rstrip() for x in data]

dict_corr = {}
for word in list_of_errors:
    list_corr = difflib.get_close_matches(word,clean_data)
    dict_corr[word] = list_corr

print(marked_sentence[:-1])
print("suggestions:")

for k, v in dict_corr.items():
    rigth_corr = ""
    for value in v:
        rigth_corr += f"{value}, "
    rigth_corr = rigth_corr.rstrip()

    print(f"{k}: {rigth_corr}")