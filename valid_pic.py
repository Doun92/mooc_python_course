# Write your solution here
import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False

    day = pic[0:2]
    month = pic[2:4]
    year = pic[4:6]
    if int(year) > 25:
        year = "19"+year
    elif int(year) == 00 and pic[6] in ["+","-"]:
        year = "19"+year
    else:
        year = "20"+year

    try:
        date = datetime.datetime(int(year),int(month),int(day))
        print(date)
    except:
        return False

    century_marker = pic[6]
    if century_marker in ["+", "-", "A"]:
        # if century_marker in ["+","-"] and int(year) > 1999:
        #     return False
        if century_marker == "A" and int(year) <2000:
            return False
        # pass
    else:
        return False

    control_caracter = pic[0:6] + pic[7:10]
    result_1 = int(int(control_caracter)/31)
    remainder = result_1*31
    result = int(control_caracter) - remainder
    control_letter = "0123456789ABCDEFHJKLMNPRSTUVWXY"[result]
    if control_letter != pic[-1]:
        return False

    return True
if __name__ == "__main__":
    # print(is_it_valid("230827-906F"))
    # print(is_it_valid("200614+561E"))
    print(is_it_valid("290200-1239"))