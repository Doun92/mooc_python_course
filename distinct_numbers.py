# Write your solution here
def distinct_numbers(l):
    final_list = []

    for i in l:
        if i not in final_list:
            final_list.append(i)

    return sorted(final_list)