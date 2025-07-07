# write your solution here
def get_data(source_file:str):
    """
    Returns a dict
    """
    data_dict = {}
    with open(source_file) as file:
        for row in file:
            row = row.replace("\n","")
            parts = row.split(";")
            # print(len(parts))
            i = 1
            data_list = []
            if parts[0] == "id":
                continue
            while i < len(parts):
                data_list.append(parts[i])
                i+=1
            # print(data_list)
            data_dict[parts[0]]= data_list     
    # print(data_dict)
    return data_dict

def get_sums(data_from_file: dict):
    """
    Returns a dict
    """

    points_from_examen = {}
    for key, values in data_from_file.items():
        total_pts = 0
        for points in values:
            total_pts += int(points)
        points_from_examen[key] = total_pts

    return points_from_examen

# if False:
student_info = input("Student information: ")
exercise_info = input("Exercises completed: ")
exam_info = input("Exam points: ")
# else:
#     student_info = "students1.csv"
#     exercise_info = "exercises1.csv"
#     exam_info = "exam_points1.csv"

students_data = get_data(student_info)
exercise_data = get_data(exercise_info)
exam_data = get_data(exam_info)

points_from_exercises = get_sums(exercise_data)


pts_from_ex = {}
for k, v in points_from_exercises.items():
    percentage = (v/40)*100
    pts_from_ex[k] = int(str(percentage/10)[0])

points_from_examen = get_sums(exam_data)

dict_grade = {}
for k1,v1 in pts_from_ex.items():
    for k2, v2 in points_from_examen.items():
        if k1 == k2:
            final_pts = v1+v2
            if final_pts < 15:
                grade = 0
            elif final_pts < 18:
                grade = 1
            elif final_pts < 21:
                grade = 2
            elif final_pts < 24:
                grade = 3
            elif final_pts < 28:
                grade = 4
            else:
                grade = 5
            dict_grade[k1] = grade

for key, value in dict_grade.items():
    print(f"{' '.join(students_data[key])} {value}")