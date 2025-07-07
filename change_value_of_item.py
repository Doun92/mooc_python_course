# Write your solution here
liste = [1, 2, 3, 4, 5]
def change_value_of_item(ls):

    while True:
        index = int(input("Index: "))
        if index == -1:
            break
        else:
            new_value = int(input("New value: "))

            ls[index] = new_value

        print(ls)

change_value_of_item(liste)