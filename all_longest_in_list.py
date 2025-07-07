# Write your solution here
def all_the_longest(li):
    longest_word = li[0]

    # longest_list = []

    for word in li:
        if len(word) > len(longest_word):
            longest_word = word
    
    list_longest_words = []
    for word in li:
        if len(word) == len(longest_word):
            list_longest_words.append(word)

    return list_longest_words