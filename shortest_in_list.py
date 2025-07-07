# Write your solution here
def shortest(l):
    shortest_word = l[0]
    
    for w in l:
        if len(w) < len(shortest_word) and shortest_word != "":
            shortest_word = w
    return shortest_word