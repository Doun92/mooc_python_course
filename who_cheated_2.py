# Write your solution here
import csv
import datetime

def count_points(exam: dict):
    points = 0
    for v in exam.values():
        points += int(v)     

    return points   

def cheaters():
    with open("start_times.csv") as start_time:
        users_dict = {}

        start_time_reader = csv.reader(start_time, delimiter=';')
        for row in start_time_reader:
            this_date = datetime.datetime.strptime(row[1], '%H:%M')
            start_time = this_date.time()
            end_time = this_date + datetime.timedelta(hours=3)
            users_dict[row[0]] = [start_time, end_time.time()]

    # print(users_dict)

    list_cheaters = []
    for k,v in users_dict.items():
        with open("submissions.csv") as submission:
            submission_reader = csv.reader(submission, delimiter=';')
            for row in submission_reader:
                if row[0] == k:
                    end_time = datetime.datetime.strptime(v[-1].isoformat(), '%H:%M:%S').time()
                    end_exercice = datetime.datetime.strptime(row[-1], '%H:%M').time()
                    # print(type(end_time))
                    # print(type(end_exercice))
                    if end_exercice > end_time:
                        # print(k)
                        if k not in list_cheaters:
                            list_cheaters.append(k)
    return list_cheaters

def final_points():
    final_grade = {}

    with open("start_times.csv") as start_time:
        users_dict = {}

        start_time_reader = csv.reader(start_time, delimiter=';')
        for row in start_time_reader:
            this_date = datetime.datetime.strptime(row[1], '%H:%M')
            start_time = this_date.time()
            end_time = this_date + datetime.timedelta(hours=3)
            users_dict[row[0]] = [start_time, end_time.time()]

    for k,v in users_dict.items():
        points = 0
        with open("submissions.csv") as submission:
            submission_reader = csv.reader(submission, delimiter=';')
            exercices_done = {}
            for row in submission_reader:
                if row[0] == k:
                    # Check the exercice time
                    end_time = datetime.datetime.strptime(v[-1].isoformat(), '%H:%M:%S').time()
                    end_exercice = datetime.datetime.strptime(row[-1], '%H:%M').time()
                    if end_exercice > end_time:
                        points += 0
                    else:
                        # Add the exercice to the ones already done.
                        if row[1] in exercices_done:
                            if int(row[2]) > int(exercices_done[row[1]]):
                                exercices_done[row[1]] = row[2]
                    #if there is no duplicate
                    if row[1] not in exercices_done:
                        exercices_done[row[1]] = row[2]

            total_points = count_points(exercices_done)
            final_grade[k] = total_points

    return final_grade
if __name__ == "__main__":
    # print(cheaters())
    print(final_points())