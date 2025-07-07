# Write your solution here
def length_of_longest(l):
    list_of_len = []
    for w in l:
        list_of_len.append(len(w))
    
    return sorted(list_of_len)[-1]