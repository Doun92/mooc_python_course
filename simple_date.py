# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day:int, month:int, year:int):
        self.day = day
        self.month = month
        self.year = year
        self.date = self.set_date()

    def __str__(self):
        return self.date

    # ==
    def __eq__(self, another:"SimpleDate"):
        return self.date == another.date

    # !=
    def __ne__(self, another:"SimpleDate"):
        return self.date != another.date

    # <
    def __lt__(self, another:"SimpleDate"):
        if self.__ne__(another):
            if self.year == another.year:
                if self.month == another.month:
                    return self.day < another.day
                else:
                    return self.month < another.month
            else:
                return self.year < another.year

    # >
    def __gt__(self, another:"SimpleDate"):
        if self.__ne__(another):
            if self.year == another.year:
                if self.month == another.month:
                    return self.day > another.day
                else:
                    return self.month > another.month
            else:
                return self.year > another.year

    # +
    def __add__(self, day:int):
        index = 0
        new_day = int(self.day)
        new_month = int(self.month)
        new_year = int(self.year)
        while True:
            if index == day:
                break
            else:
                if new_day == 30:
                    if new_month == 12:
                        new_day = 1
                        new_month = 1
                        new_year += 1
                    else:
                        new_day = 1
                        new_month += 1
                else:
                    new_day += 1
                index += 1

        new_date = SimpleDate(new_day, new_month, new_year)
        return new_date

    # -
    def __sub__(self, another: "SimpleDate"):
        index = 0

        if self > another:
            temp_date = another
            while True:
                temp_date += 1
                index += 1

                if temp_date == self:
                    break

        elif self < another:
            temp_date = self
            while True:
                temp_date += 1
                index += 1

                if temp_date == another:
                    break
        else:
            return index
        
        return index
        

    def set_date(self):
        return f"{self.day}.{self.month}.{self.year}"



if __name__ == "__main__":
    sd1 = SimpleDate(5, 6, 1876)
    sd2 = SimpleDate(6, 6, 1876)
    print(sd1 < sd2)