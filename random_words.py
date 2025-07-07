# Write your solution here:
from random import randint

def word_generator(characters: str, length: int, amount: int):
    idx = 0
    char_to_list= list(characters)
    
    while idx < amount:
        temp_list = []
        while len(temp_list) < length:
            char = char_to_list[randint(0,len(char_to_list)-1)]
            temp_list.append(char) 
        yield "".join(temp_list)
        idx += 1
    

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)