# Write your solution here
word = input("Please type in a string: ")
sub_str = input("Please type in a substring: ")

idx_1 = word.find(sub_str)

if sub_str in word:
    if sub_str in word[idx_1+len(sub_str):]:
        idx_2 = word[idx_1+len(sub_str):].find(sub_str)
        print(f"The second occurrence of the substring is at index {idx_2+idx_1+len(sub_str)}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")