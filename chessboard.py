# Write your solution here
def chessboard(nb):
    idx = 0

    row = ""

    while idx < nb:
        i = 0
        while i < nb:
            if idx %2 == 0:
                if i %2 == 0:
                    row += "1"
                else:
                    row += "0"
            else:
                if i %2 == 0:
                    row += "0"
                else:
                    row += "1"
            # row += str(i)
            i +=1
        print(row)
        idx+=1
        row=""

# Testing the function
if __name__ == "__main__":
    chessboard(3)
