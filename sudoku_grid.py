# Write your solution here
def check_cell(set_of_nine: list):
    # print(set_of_nine)
    repeated_number = []
    for nb in set_of_nine:
        if nb > 0:
            if nb in repeated_number:
                return False
            else:
                repeated_number.append(nb)
    return True

def sudoku_grid_correct(sudoku: list):
    # Checking rows
    for row in sudoku:
        row_checked = check_cell(row)
        if row_checked == False:
            return False
    
    # Checking columns
    for i in range(9):
        col = []
        for row in sudoku:
            col.append(row[i])
        col_checked = check_cell(col)
        if col_checked == False:
            return False

    # Checking square
    list_of_indexes = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for index in list_of_indexes:
        grid = []
        for row in sudoku[index[0]:index[0]+3]:
            for cell in row[index[1]:index[1]+3]:
                grid.append(cell)
        grid_checked = check_cell(grid)
        if grid_checked == False:
            return False
    
    print(f"row_checked = {row_checked}")
    print(f"col_checked = {col_checked}")
    print(f"grid_checked = {grid_checked}")

    return True
    # if row_checked == True and col_checked == True and grid_checked == True:
    #     return True
    # else:
    #     return False


if __name__ == "__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    # sudoku2 = [
    #     [2, 6, 7, 8, 3, 9, 5, 0, 4],
    #     [9, 0, 3, 5, 1, 0, 6, 0, 0],
    #     [0, 5, 1, 6, 0, 0, 8, 3, 9],
    #     [5, 1, 9, 0, 4, 6, 3, 2, 8],
    #     [8, 0, 2, 1, 0, 5, 7, 0, 6],
    #     [6, 7, 4, 3, 2, 0, 0, 0, 5],
    #     [0, 0, 0, 4, 5, 7, 2, 6, 3],
    #     [3, 2, 0, 0, 8, 0, 0, 5, 7],
    #     [7, 4, 5, 0, 0, 3, 9, 0, 1]
    # ]

    # print(sudoku_grid_correct(sudoku2))

    # sudoku = [
    #     [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
    #     [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
    #     [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
    #     [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
    #     [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
    #     [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
    #     [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
    #     [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
    #     [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
    # ]
    # sudoku_grid_correct(sudoku)