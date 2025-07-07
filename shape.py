# Copy here code of line function from previous exercise and use it in your solution
def line(nb, char):
    if len(char) > 0:
        print(char[0] * nb)
    else:
        print("*" * nb)

def shape(sh1_nb, sh1_chr, sh2_nb, sh2_chr):
    if sh1_nb > 0:
        idx = 1
        while idx <= sh1_nb:
            line(idx, sh1_chr)
            idx+=1
    
    if sh2_nb > 0:
        idx = 0
        while idx < sh2_nb:
            line(sh1_nb, sh2_chr)
            idx +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")