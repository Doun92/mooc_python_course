# Write your solution here
limit = int(input("Limit: "))

total = 0
total_str = ""
nb = 0

while total < limit:
    nb +=1
    total += nb
    if total == 1:
        total_str += f"{str(nb)}"
    else:    
        total_str += f" + {str(nb)}"
# print()
total_str += f" = {total}"
print(f"The consecutive sum: {total_str}")