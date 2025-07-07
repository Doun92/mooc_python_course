# Write your solution here
def transpose(matrix: list):
    new_matrix = []
    for i, row in enumerate(matrix):
        new_row = []
        for j, column in enumerate(matrix[i]):
            new_row.append(matrix[j][i])
        new_matrix.append(new_row)
    matrix.clear()
    matrix.extend(new_matrix)    


if __name__ == "__main__":
    transpose([[1,2,3],[4,5,6],[7,8,9]])
    transpose([[1,2],[1,2]])