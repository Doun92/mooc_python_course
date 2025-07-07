# Copy here code of line function from previous exercise
def line(nb, char):
    if len(char) > 0:
        print(char[0] * nb)
    else:
        print("*" * nb)

def square(size, character):
    idx = 0
    while idx < size:
        line(size, character)
        idx += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")