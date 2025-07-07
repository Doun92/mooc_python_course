# Write your solution here
import datetime

filename = input("Filename: ")
starting_date = input("Starting date: ")
nb_days = int(input("How many days: "))


# Math with dates
date_in_list = starting_date.split(".")
delta = datetime.timedelta(days=nb_days)
date_zero = datetime.date(int(date_in_list[2]),int(date_in_list[1]),int(date_in_list[0]))
end_date =  date_zero + delta

# Create a dict with all the numbers and dates
results_dict = {}
print("Please type in screen time in minutes on each day (TV computer mobile): ")
day_index = date_zero
while day_index < end_date:
    day_row = datetime.datetime.strptime(str(day_index), '%Y-%m-%d').strftime('%d.%m.%Y')
    answr =input(f"Screen time {day_row}: ")
    to_list = answr.split(" ")
    results_dict[day_row] = "/".join(to_list)
    day_index = day_index + datetime.timedelta(days=1)

# Some date calcualtion and formating
time_period_end_date = datetime.datetime.strptime(str(end_date-datetime.timedelta(days=1)),'%Y-%m-%d').strftime('%d.%m.%Y')
# end_date = end_date.strftime('%d.%m.%Y')
starting_date = date_zero.strftime('%d.%m.%Y')


total_minutes = 0
i = 0
for liste in list(results_dict.values()):
    for number in liste.split("/"):
        total_minutes += int(number)
    i += 1

# Get the last key in the dict
keys = results_dict.keys()
last_key = [key for key in keys][-1]

average_minutes = total_minutes/i

with open(f"{filename}", "w") as date_file:
    if nb_days == 1:
        date_file.write(f"Time period: {starting_date}-{starting_date}")
    else:
        date_file.write(f"Time period: {starting_date}-{time_period_end_date}")
    date_file.write("\n")
    date_file.write(f"Total minutes: {total_minutes}")
    date_file.write("\n")
    date_file.write(f"Average minutes: {average_minutes}")
    date_file.write("\n")
    for k, v in results_dict.items():
        date_file.write(f"{k}: {v}")
        if k != last_key:
            date_file.write("\n")

print(f"Data stored in file {filename}")