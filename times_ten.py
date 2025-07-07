# Write your solution here
def times_ten(start_index: int, end_index: int):
    diff = end_index - start_index
    i=0
    d = {}
    while i <= diff:
        d[start_index+i] = (start_index+i)*10
        i +=1

    return d

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)