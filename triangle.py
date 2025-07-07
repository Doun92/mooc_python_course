# Copy here code of line function from previous exercise
def line(nb, char):
    if len(char) > 0:
        print(char[0] * nb)
    else:
        print("*" * nb)

def triangle(size):
    # You should call function line here with proper parameters
    idx = 1
    while idx <= size:
        line(idx, "#")
        idx += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
