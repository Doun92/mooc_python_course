# Write your solution here
def mean(l):
    sum = 0
    for i in l:
        sum += i

    mean = sum / len(l)
    return mean

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)