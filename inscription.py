# Write your solution here
inpt = input("Whom should I sign this to: ")
place = input("Where shall I save it: ")

str_to_invit = f"Hi {inpt}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"

with open(place, "w") as inscription_file:
    inscription_file.write(str_to_invit)