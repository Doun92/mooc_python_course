# Write your solution here
import urllib.request
import json
import ssl
import math

def retrieve_all():
    url_courses = "https://studies.cs.helsinki.fi/stats-mock/api/courses"

    context = ssl._create_unverified_context()

    my_request = urllib.request.urlopen(url_courses)
    raw_content = my_request.read()
    page = json.loads(raw_content)

    liste_of_courses = []
    for course in page:
        if course["enabled"] == True:
            nb_exercice = 0
            for exercice in course["exercises"]:
                nb_exercice += exercice

            temp_tupple = (
                course["fullName"],
                course["name"],
                course["year"],
                nb_exercice
                )
            liste_of_courses.append(temp_tupple)

    return liste_of_courses


def retrieve_course(course_name: str):
    url_course = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request = urllib.request.urlopen(url_course)
    raw_content = my_request.read()
    page = json.loads(raw_content)

    number_weeks = len(page)

    print(page)

    number_students = 0
    total_hours = 0
    total_exercices = 0


    for k, v in page.items():
        if v['students'] > number_students:
            number_students = v['students']
        total_hours += v['hour_total']
        total_exercices += v['exercise_total']
        

    hours_average = total_hours/number_students
    exercises_average = total_exercices/number_students

    statistics = {
        'weeks': number_weeks,
        'students': number_students,
        'hours': total_hours,
        'hours_average': math.floor(hours_average),
        'exercises': total_exercices,
        'exercises_average': math.floor(exercises_average)
    }

    return statistics

if __name__ == "__main__":
    # retrieve_all()
    retrieve_course("docker2019")