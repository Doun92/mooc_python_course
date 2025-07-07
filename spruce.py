def row(total, nb):
    r = (total * " ") + (nb * "*")
    print(r)

# Write your solution here
def spruce(nb):
    print("a spruce!")

    idx = 0
    row_nb = 1

    total_spaces_static = nb-1
    total_spaces_dynamic = nb-1

    while idx < nb:
        row(total_spaces_dynamic, row_nb)
        row_nb += 2
        idx += 1
        total_spaces_dynamic -= 1
    row(total_spaces_static,1)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)