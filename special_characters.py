# Write your solution here
import string

def separate_characters(my_string: str):
    letters = "".join(c for c in my_string if c in string.ascii_letters)
    punctuation = "".join(c for c in my_string if c in string.punctuation)
    others = "".join(c for c in my_string if c not in string.ascii_letters and c not in string.punctuation)
    
    return (letters, punctuation, others)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")