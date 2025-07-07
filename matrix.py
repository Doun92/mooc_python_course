# write your solution here
def matrix_sum():
    sum = 0
    with open("matrix.txt") as file:
        for row in file:
            row = row.replace("\n",",")
            row_parts = row.split(",")
            for nb in row_parts:
                if len(nb)>0:
                    sum += int(nb)
    return sum

def matrix_max():
    max_nb = 0
    with open("matrix.txt") as file:
        for row in file:
            row = row.replace("\n",",")
            row_parts = row.split(",")
            for nb in row_parts:
                if len(nb)>0:
                    if int(nb) > max_nb:
                        max_nb=int(nb)
    return max_nb

def row_sums():
    list_of_sum_rows = []
    with open("matrix.txt") as file:
        for row in file:
            result = 0
            row = row[:-1]
            row_parts = row.split(",") 
            for nb in row_parts:
                result += int(nb)  
            list_of_sum_rows.append(result)  

    return list_of_sum_rows
if __name__ == "__main__":
    row_sums()
    matrix_sum()
    matrix_max()