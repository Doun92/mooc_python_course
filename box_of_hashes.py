# Copy here code of line function from previous exercise
def line(nb, char):
    if len(char) > 0:
        print(char[0] * nb)
    else:
        print("*" * nb)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    idx = 0
    while idx < height:
        line(10, "#")
        idx += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
