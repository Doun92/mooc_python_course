# Write your solution here
def no_vowels(word: str):
        word = word.replace("a", "")
        word = word.replace("e", "")
        word = word.replace("i", "")
        word = word.replace("o", "")
        word = word.replace("u", "")
        # print(word)
        return word

# no_vowels("abcdefghijklmnopqrstuvwxyz")