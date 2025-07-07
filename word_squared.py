# Write your solution here
def squared(string, nb):
    squarred_nb = nb * nb
    long_string = string * squarred_nb
    # print(long_string[:squarred_nb])
    # print(len(long_string))

    idx_zéro = 0
    idx = nb
    while idx <= len(long_string[:squarred_nb]):
        print(long_string[idx_zéro:idx])
        idx_zéro += nb
        idx += nb       


# Testing the function
if __name__ == "__main__":
    squared("ab", 3)
    # squared("aybabtu", 5)