# Write your solution here
def row_correct(sudoku: list, row_no: int):
    list_of_row_nb = []
    for cell in sudoku[row_no]:
        if cell > 0 and cell < 10:
            if cell in list_of_row_nb:
                return False
            else:
                list_of_row_nb.append(cell)
    return True