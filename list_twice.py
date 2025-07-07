# Write your solution here
in_addition_order_list = []
smallest_to_greatest = []

while True:
    new_item = int(input("New item: "))

    if new_item == 0:
        print("Bye!")
        break
    else:
        in_addition_order_list.append(new_item)
        smallest_to_greatest.append(new_item)
        smallest_to_greatest = sorted(smallest_to_greatest)

        print(f"The list now: {in_addition_order_list}")
        print(f"The list in order: {smallest_to_greatest}")