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


student_info = input("Student information: ")
exercise_info = input("Exercises completed: ")

students_data = get_data(student_info)
exercise_data = get_data(exercise_info)

dict_total_pts = {}
for key, values in exercise_data.items():
    total_pts = 0
    for points in values:
        total_pts += int(points)

    dict_total_pts[key] = total_pts

for key, value in dict_total_pts.items():
    print(f"{' '.join(students_data[key])} {value}")