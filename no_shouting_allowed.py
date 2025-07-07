# Write your solution here
def no_shouting(sentence : list):
    no_shout_list = []

    for word in sentence:
        if word.isupper() == False:
            no_shout_list.append(word)

    return no_shout_list