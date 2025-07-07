# Write your solution here
def line(nb, char):
    if len(char) > 0:
        print(char[0] * nb)
    else:
        print("*" * nb)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")