# Write your solution here
def count_matching_elements(my_matrix:list, element:int):
    nb_of_matches = 0
    for row in my_matrix:
        for i in row:
            if element == i:
                nb_of_matches +=1
    return nb_of_matches

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))