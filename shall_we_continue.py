# Write your solution here
print("hi")
continue_conv = True
while continue_conv:
    answer = input("Shall we continue?")
    if answer == "no":
        print("okay then")
        continue_conv = False
    else:
        print("hi")