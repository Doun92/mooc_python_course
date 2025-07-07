# Write your solution here
import re

def is_dotw(my_string: str):
    search_regex = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"

    if re.search(search_regex, my_string):
        return True
    else:
        return False

def all_vowels(my_string):
    search_regex = "^[aeiou]+$"

    if re.search(search_regex, my_string):
        return True
    else:
        return False

def time_of_day(my_string: str):
    search_regex = "^(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"


    if re.search(search_regex, my_string):
        return True
    else:
        return False



if __name__ == "__main__":
    # print(is_dotw("Mon"))
    # print(is_dotw("Fri"))
    # print(is_dotw("Tui"))
    # print(all_vowels("eioueioieoieou"))
    # print(all_vowels("autoooo"))
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
    print(time_of_day("25:13:01"))  #False
    print(time_of_day("19:zz:04"))
