# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    with open(f"src//{filename}", "r", encoding="utf-8") as file:
        # all_words = [w.lower() for w in file.read().split()]
        all_words = [w for w in file.read().split()]
        all_words = [word.replace(",", "").replace(".", "") if "," in word or "." in word else word for word in all_words]

        t = {}
        for w in all_words:
            if w not in t:
                t[w] = 1
            else:
                t[w] += 1

        for k, v in t.items():
            print(k)
            print(v)
        
        return {k:v for k,v in t.items() if v >= lower_limit}

if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))
