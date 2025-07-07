# WRITE YOUR SOLUTION HERE:
def begin_with_vowel(words: list):
    return [v for v in words if v[0].lower() in ["a","e","i","o","u"]]

if __name__ == "__main__":
    word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
    for vowelled in begin_with_vowel(word_list):
        print(vowelled)