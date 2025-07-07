# Write your solution here
def longest_series_of_neighbours(serie: list):
    max_length = 1
    current_length = 1

    for i in range(1, len(serie)):
        if abs(serie[i] - serie[i - 1]) == 1:
            current_length += 1
        else:
            current_length = 1 

        max_length = max(max_length, current_length)

    return max_length