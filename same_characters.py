# Write your solution here
def same_chars(string, nb_1, nb_2):
    try:
        if string[nb_1] == string[nb_2]:
            return True
        else:
            return False
    except:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))