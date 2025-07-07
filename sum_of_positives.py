# Write your solution here
def sum_of_positives(l):
    result = 0
    
    for i in l:
        if i < 0:
            pass
        else:
            result += i

    return result