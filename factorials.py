# Write your solution here
def factorise(nb: int):
    list_nb = []

    i = 1
    while i <= nb:
        list_nb.append(i)
        i+=1
    
    result = 1
    for j in list_nb:
        result = result * j
    
    return result

def factorials(n: int):
    dict_factors = {}

    i = 1

    while i <= n:
        r = factorise(i)
        dict_factors[i] = r
        i+=1

    return dict_factors

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])