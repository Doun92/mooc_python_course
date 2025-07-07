# Write your solution here
from random import choice
def words(n: int, beginning: str):
    with open("src\\words.txt") as txt_file:
        list_of_poss = [word.strip() for word in txt_file.readlines() if word.startswith(beginning)]
        # print(list_of_poss)

        if len(list_of_poss) < n:
            raise ValueError

        list_choices = []
        i=0
        while i < n:
            c = choice(list_of_poss)
            if c not in list_choices:
                list_choices.append(c)
                list_of_poss.remove(c)
            i+=1

        

        return list_choices
if __name__ == "__main__":
    # word_list = words(3, "ca")
    # for word in word_list:
    #     print(word)
    # test = words(500, 'car')
    # test = words(2, 'car')
    test = words(4, 'abs')
    print(test)
    print(len(test))