# Write your solution here
def get_average_grades(db: dict, name: str):
    list_grades = []
    if name in db:
        for i in db[name]:
            list_grades.append(i[1])

    somme = 0
    for i in list_grades:
        somme += i
    average = somme/len(list_grades)
    return average


def add_student(db: dict, name: str):
    db[name]= []


def print_student(db: dict, name: str):
    message_from_db = ""

    if name in db:
        if len(db[name]) == 0:
            message_from_db = f"{name}:\n no completed courses"
        else:
            message_from_db = f"{name}:\n {len(db[name])} completed courses:\n"
            for i in db[name]:
                message_from_db += f"  {i[0]} {i[1]}\n"
            average = get_average_grades(db, name)
            message_from_db += f" average grade {average}"
    else:
        message_from_db = f"{name}: no such person in the database"

    print(message_from_db)


def add_course(db: dict, name: str, course: tuple):
    if name in db:
        if course[1] == 0:
            pass
        else:
            # control_dict[course[0]] = course[1]
            db[name].append(course)

    dict_courses = {}
    for course in db[name]:
        if course[0] in dict_courses.keys():
            if course[1] > dict_courses[course[0]]:
                dict_courses[course[0]] = course[1]
            else:
                pass
        else:
            dict_courses[course[0]] = course[1]

    res = list(dict_courses.items())

    db[name].clear()
    db[name].extend(res)


def summary(db:dict):
    list_students = []
    dict_student = {}
    dict_stu_nb_course = {}
    dict_stu_grades = {}

    for key, value in db.items():
        # print(key)
        list_students.append(key)
        dict_student[key] = value
        # print(len(value))
        # print(len(dict_student[key]))
        dict_stu_nb_course[key] = len(dict_student[key])


    for student in list_students:
        dict_stu_grades[student] = get_average_grades(db, student)

    print(f"students {len(list_students)}")
    print(f"most courses completed {max(dict_stu_nb_course.values())} {list(dict_stu_nb_course.keys())[list(dict_stu_nb_course.values()).index(max(dict_stu_nb_course.values()))]}")
    print(f"best average grade {max(dict_stu_grades.values())} {list(dict_stu_grades.keys())[list(dict_stu_grades.values()).index(max(dict_stu_grades.values()))]}")    

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    # print_student(students, "Eliza")
    # print_student(students, "Jack")
    # print_student(students, "Peter")
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)