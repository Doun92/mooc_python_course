# Write your solution here
layers = int(input("Layers: "))

size = 2 * layers - 1
square = []

for i in range(size):
    row = []
    for j in range(size):
        min_dist = min(i, j, size - 1 - i, size - 1 - j)
        letter = chr(ord('A') + (layers - 1 - min_dist))
        row.append(letter)
    square.append("".join(row))

print("\n".join(square))