# Write your solution here
def define_numbers(nb: int):
    number_to_write = str(nb)
    # print(number_to_write)

    if number_to_write[-1] == "1":
        unit = "one"
    elif number_to_write[-1] == "2":
        unit = "two"
    elif number_to_write[-1] == "3":
        unit = "three"
    elif number_to_write[-1] == "4":
        unit = "four"
    elif number_to_write[-1] == "5":
        unit = "five"
    elif number_to_write[-1] == "6":
        unit = "six"
    elif number_to_write[-1] == "7":
        unit = "seven"
    elif number_to_write[-1] == "8":
        unit = "eight"
    elif number_to_write[-1] == "9":
        unit = "nine"

    if len(number_to_write) == 2:
        if number_to_write[0] == "2":
            dizaine = "twenty"
        elif number_to_write[0] == "3":
            dizaine = "thirty"
        elif number_to_write[0] == "4":
            dizaine = "forty"
        elif number_to_write[0] == "5":
            dizaine = "fifty"
        elif number_to_write[0] == "6":
            dizaine = "sixty"
        elif number_to_write[0] == "7":
            dizaine = "seventy"
        elif number_to_write[0] == "8":
            dizaine = "eighty"
        elif number_to_write[0] == "9":
            dizaine = "ninety"
    
    if number_to_write == "0":
        return "zero"
    elif number_to_write == "10":
        return "ten"
    elif number_to_write == "11":
        return "eleven"
    elif number_to_write == "12":
        return "twelve"
    elif number_to_write == "13":
        return "thirteen"
    elif number_to_write == "14":
        return "fourteen"
    elif number_to_write == "15":
        return "fifteen"
    elif number_to_write == "16":
        return "sixteen"
    elif number_to_write == "17":
        return "seventeen"
    elif number_to_write == "18":
        return "eighteen"
    elif number_to_write == "19":
        return "nineteen"
    
    if len(number_to_write) == 1:
        return unit
    else:
        if number_to_write[-1] == "0":
            return dizaine
        else:
            return f"{dizaine}-{unit}"

def dict_of_numbers():
    dict_nb = {}

    for i in range(100):
        # print(i)
        dict_nb[i] = define_numbers(int(i))

    # print(dict_nb)
    return dict_nb

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])