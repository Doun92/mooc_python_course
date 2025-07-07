# Write your solution here
pass_1 = input("Password: ")
pass_2 = input("Repeat password: ")

while True:
    if pass_1 == pass_2:
        print("User account created!")
        break
    else:
        print("They do not match!")
        pass_2 = input("Repeat password: ")