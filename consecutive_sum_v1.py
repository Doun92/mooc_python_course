# Write your solution here
limit = int(input("Limit: "))

total = 0
nb = 0

while total < limit:
    nb +=1
    total += nb
print(total)