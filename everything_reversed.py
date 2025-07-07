# Write your solution here
def reverse_word(word):
    new_word_in_list = []

    for char in word:
        new_word_in_list.insert(0, char)
    reversed_word = "".join(new_word_in_list)
    return reversed_word

def everything_reversed(words: list):
    reversed_list = []

    for word in words:
        reversed_word = reverse_word(word)
        reversed_list.insert(0, reversed_word)
    return reversed_list
