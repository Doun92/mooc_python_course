# Write your solution here
grade = int(input("How many points [0-100]: "))
if grade > 100 or grade < 0:
    print("Grade: impossible!")
elif grade <= 49:
    print("Grade: fail")
elif grade <= 59:
    print("Grade: 1")
elif grade <= 69:
    print("Grade: 2")
elif grade <= 79:
    print("Grade: 3")
elif grade <= 89:
    print("Grade: 4")
elif grade <= 100:
    print("Grade: 5")