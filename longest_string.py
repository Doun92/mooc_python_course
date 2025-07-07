# Write your solution here
def longest(strings:list):
    longest_word = strings[0]
    for word in strings:
        if len(word)> len(longest_word):
            longest_word = word
    return longest_word

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))