# Write your solution here
def list_sum(list_1, list_2):
    idx = 0

    sum_list = []

    while idx < len(list_1):
        sum_list.append(list_1[idx] + list_2[idx])
        idx += 1
    
    return sum_list