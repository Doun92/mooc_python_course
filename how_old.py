# Write your solution here
from datetime import datetime, timedelta

day = input("Date: ")
month = input("Month: ")
year = input("Year: ")

new_millenium = datetime(1999,12,31)

difference = new_millenium - datetime(int(year), int(month), int(day))

if difference.days > 0:
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")