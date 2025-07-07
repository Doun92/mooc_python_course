# Write your solution here
def palindromes(word):
    result = word == word[::-1]
    if result == True:
        print(f"{word} is a palindrome!")
        return True
    else:
        print("that wasn't a palindrome")
        return False

while True:
    input_word = input("Please type in a palindrome: ")
    is_palindrome = palindromes(input_word)
    if is_palindrome:
        break

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!