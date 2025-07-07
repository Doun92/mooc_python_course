# Write your solution here
import csv
import datetime

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

if __name__ == "__main__":
    print(cheaters())