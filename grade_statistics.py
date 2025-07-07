# Write your solution here
import math
def get_average(l):
    sum = 0
    for i in l:
        sum += i

    result = sum/len(l)
    return round(result,1)

def get_pass_percentage(l):
    sum = 0
    for i in l:
        if i > 0:
            sum += 1
    # print(len(l))
    result = (sum/len(l))*100
    return round(result,1)
    

def get_statistiques(list_of_results:list, list_points:list):
    # print(list_of_results)
    print("Statistics:")
    points_average = get_average(list_points)
    print(f"Points average: {points_average}")
    pass_percentage = get_pass_percentage(list_of_results)
    print(f"Pass percentage: {pass_percentage}")

    nb_5 = "5: "
    nb_4 = "4: "
    nb_3 = "3: "
    nb_2 = "2: "
    nb_1 = "1: "
    nb_0 = "0: "

    for i in list_of_results:
        if i == 5:
            nb_5 += "*"
        elif i == 4:
            nb_4 += "*"
        elif i == 3:
            nb_3 += "*" 
        elif i == 2:
            nb_2 += "*"
        elif i == 1:
            nb_1 += "*"
        elif i == 0:
            nb_0 += "*"
    print("Grade distribution:")
    print(nb_5)
    print(nb_4)
    print(nb_3)
    print(nb_2)
    print(nb_1)
    print(nb_0)

def get_grade(exam : list, exer : list):
    list_results = []
    list_grades = []

    for i, g in enumerate(exam):
        if g < 10:
            list_results.append(g+exer[i])
            list_grades.append(0)
        else:
            list_results.append(g+exer[i])
            if g+exer[i] < 14 :
                list_grades.append(0)
            elif g+exer[i] <= 17 :
                list_grades.append(1)
            elif g+exer[i] <= 20 :
                list_grades.append(2)
            elif g+exer[i] <= 23 :
                list_grades.append(3)
            elif g+exer[i] <= 27 :
                list_grades.append(4)
            elif g+exer[i] <= 30 :
                list_grades.append(5)

    get_statistiques(list_grades,list_results)

def get_exam_points(entries:list):
    list_exam_points = []
    for entry in entries:
        list_exam_points.append(int(entry.split()[0]))
    return list_exam_points

def get_exercices_points(entries: list):
    list_of_ex_points = []
    for entry in entries:
        exeercices_points = int(entry.split()[-1])
        ex_points = math.floor(exeercices_points/10)
        list_of_ex_points.append(ex_points)
    return list_of_ex_points

def ask_results():
    list_results = []
    while True:
        entry = input("Exam points and exercises completed: ")
        if entry == "":
            break
        else:
            list_results.append(entry)
        
    return list_results

# entry_by_teacher = ["10 85", "15 54", "20 0", "5 100", "11 45", "16 45"]
entry_by_teacher = ask_results()
exam_points = get_exam_points(entry_by_teacher)
exercices_points = get_exercices_points(entry_by_teacher)
get_grade(exam_points, exercices_points)
