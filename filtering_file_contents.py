# Write your solution here
def add(calcul: str):
    n1, n2 = calcul.split("+")
    r = int(n1) + int(n2)
    return r

def substract(calcul: str):
    n1, n2 = calcul.split("-")
    r = int(n1) - int(n2)
    return r

def filter_solutions():
    liste_correct = []
    liste_incorrect = []
    with open("solutions.csv", "r") as solution_file:
        for row in solution_file.readlines():
            row = row.replace("\n","")
            name, calcul, answer = row.split(";")
            if "+" in calcul:
                r = add(calcul)
            elif "-" in calcul:
                r = substract(calcul)
            if r == int(answer):
                liste_correct.append(row)
            else:
                liste_incorrect.append(row)

    with open("correct.csv", "w") as correct_file:
        for row in liste_correct:
            correct_file.write(row+"\n")
    with open("incorrect.csv", "w") as incorrect_file:
        for row in liste_incorrect:
            incorrect_file.write(row+"\n")

    # print(liste_correct)
    # print(liste_incorrect)



if __name__ == "__main__":
    filter_solutions()