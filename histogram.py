# Write your solution here
def histogram(chars: str):
    groups = {}

    for char in chars:
        if char not in groups:
            groups[char] = 1
        else:
            groups[char] +=1
    # print(groups)

    for key, value in groups.items():
        col = "*"*value
        print(f"{key} {col}")

if __name__ == "__main__":
    histogram("abba")