# # Write your solution here
# def get_data():
#     data_from_file = []
#     try:
#         with open("src\\words.txt", "r") as word_file:
#             data_from_file = word_file.readlines()
#     except:
#         with open("words.txt", "r") as word_file:
#             data_from_file = word_file.readlines()

#     data_in_list = []
#     for row in data_from_file:
#         row = row.replace("\n", "")
#         data_in_list.append(row)

#     return data_in_list

# def generate_combinations(s, index=0, results=None):
#     alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#     if results is None:
#         results = []

#     if index == len(s):
#         results.append("".join(s))
#         return 
    
#     if s[index] == '.': 
#         for letter in alphabet:
#             s[index] = letter
#             generate_combinations(s, index + 1, results)
#             s[index] = '.' 
#     else:
#         generate_combinations(s, index + 1, results) 

#     return results
    
# def get_all_possibilities(search_term: str):
#     dot_positions = []
#     for i, char in enumerate(search_term):
#         if char == ".":
#             dot_positions.append(i)

#     # possibilities = []
#     possibilities = generate_combinations(list(search_term))
#     # possibilities.append(new_item)

#     # print(possibilities)
#     return possibilities

# def search_with_dot(search_term: str, data: list):
#     len_search_term = len(search_term)

#     smaller_list = []
#     for word in data:
#         if len(word) == len_search_term:
#             smaller_list.append(word)

#     possibilities = get_all_possibilities(search_term)

#     results_list = []
#     for word in possibilities:
#         if word in data:
#             results_list.append(word)

#     return results_list

# def search_with_asterisk(search_term: str, data: list):
#     possibilities = []
#     if search_term[0] == "*":
#         for word in data:
#             if word.endswith(search_term[1:]):
#                 possibilities.append(word)

#     if search_term[-1] == "*":
#         for word in data:
#             if word.startswith(search_term[:-1]):
#                 possibilities.append(word)

#     return possibilities

# def find_words(search_term: str):
#     data = get_data()

#     if "." in search_term:
#         results_list = search_with_dot(search_term, data)
#     elif "*" in search_term:
#         results_list = search_with_asterisk(search_term, data)
#     else:
#         results_list = []
#         for word in data:
#             if search_term == word:
#                 results_list.append(word)

#     return results_list

# if __name__ == "__main__":
#     # print(find_words("zoo"))
#     # print(find_words("ca."))
#     # print(find_words("p.ng"))
#     print(find_words("c.d."))
#     # print(find_words("ca*"))
#     # print(find_words("*ane"))

import string

def get_data():
    """Reads words from a file and returns a sorted list of words."""
    try:
        with open("src/words.txt", "r") as word_file:
            words = [line.strip() for line in word_file]
    except FileNotFoundError:
        with open("words.txt", "r") as word_file:
            words = [line.strip() for line in word_file]

    return sorted(words)  # Ensure consistent order

def generate_combinations(s, index=0):
    """Generates all possible word combinations by replacing '.' with letters."""
    if index == len(s):
        return ["".join(s)]
    
    if s[index] == '.':
        results = []
        for letter in string.ascii_lowercase:
            s[index] = letter
            results.extend(generate_combinations(s[:], index + 1))
        s[index] = '.'  # Reset for backtracking
        return results
    
    return generate_combinations(s, index + 1)

def search_with_dot(search_term: str, data: list):
    """Finds words matching the search term with '.' wildcard."""
    possibilities = set(generate_combinations(list(search_term)))
    return sorted(word for word in data if word in possibilities)

def search_with_asterisk(search_term: str, data: list):
    """Finds words matching the search term with '*' wildcard at start or end."""
    if search_term.startswith("*"):
        results = [word for word in data if word.endswith(search_term[1:])]
    elif search_term.endswith("*"):
        results = [word for word in data if word.startswith(search_term[:-1])]
    else:
        results = []

    return sorted(results)

def find_words(search_term: str):
    """Finds words matching the search term using '.', '*', or exact match."""
    data = get_data()

    if "." in search_term:
        return search_with_dot(search_term, data)
    elif "*" in search_term:
        return search_with_asterisk(search_term, data)
    return [search_term] if search_term in data else []

# Example test cases
if __name__ == "__main__":
    print(find_words("c.d."))  # Expected sorted output matching the test cases
