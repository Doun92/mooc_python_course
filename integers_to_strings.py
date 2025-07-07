# Write your solution here
def formatted(l):
    new_list = []
    for i in l:
        new_item = str(round(i, 2))
        if len(new_item)<4:
            new_item += "0"
            new_list.append(new_item)
        else:
            new_list.append(new_item)

    return new_list