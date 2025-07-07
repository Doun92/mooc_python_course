# Write your solution here
def most_common_character(arg:str):
    list_from_word = []
    for c in arg:
        list_from_word.append(c)

    most_common_char_nb = 0
    most_common_char = ""

    for i in list_from_word:
        # print(i)
        count = list_from_word.count(i)
        # print(count)
        if count > most_common_char_nb:
            most_common_char_nb = count
            most_common_char = i
            # print(most_common_char_nb)
            # print(most_common_char)
        else:
            pass
    # print(most_common_char)
    return most_common_char

# first_string = "abcdbde"
# most_common_character(first_string)