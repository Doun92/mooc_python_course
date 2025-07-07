# Write your solution here
gift = int(input("Value of gift: "))
if gift < 5000:
    print("No tax!")
else:
    if gift >= 5000 and gift < 25000:
        result = 100 + (gift - 5000) * 0.08
    elif gift >= 25000 and gift < 55000:
        result = 1700 + (gift - 25000) * 0.1
    elif gift >= 55000 and gift < 200000:
        result = 4700 + (gift - 55000) * 0.12
    elif gift >= 200000 and gift < 1000000:
        result = 22100 + (gift - 200000) * 0.15
    elif gift >= 1000000:
        result = 142100 + (gift - 1000000) * 0.17
    print(f"Amount of tax: {result} euros")