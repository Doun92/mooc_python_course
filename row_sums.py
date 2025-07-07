# Write your solution here
def row_sums(my_matrix: list):
    for liste in my_matrix:
        value = 0
        for i in liste:
            value += i
        liste.append(value)

if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)