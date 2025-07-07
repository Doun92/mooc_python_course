# Write your solution here
from math import floor
import string

def change_case(orig_string: str):
    return orig_string.swapcase()

def split_in_half(orig_string: str):
    cut_nb = floor(len(orig_string)/2)
    half_1 = orig_string[0:cut_nb]
    if len(orig_string)%2 == 0:
        half_2 = orig_string[(len(orig_string)-cut_nb):]
    else:    
        half_2 = orig_string[(len(orig_string)-cut_nb)-1:] 
    return half_1, half_2

def remove_special_characters(orig_string: str):
    result = ""
    string.punctuation += "§¤"
    for char in orig_string:
        if char not in string.punctuation:
            result += char
    return result

if __name__ == "__main__":
    my_string = "Well hello there!"
    # print(change_case(my_string))
    # print(split_in_half(my_string))¨
    print(remove_special_characters("Thi§ is a test test"))