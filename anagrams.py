# Write your solution here
def anagrams(first_str, sec_str):
    first_word = sorted(first_str)
    sec_word = sorted(sec_str)

    if first_word == sec_word:
        return True
    else:
        return False