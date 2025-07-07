# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self.__amount = self.__get_amount()

    def __str__(self):
        return f"{self.__amount} eur"

    def __eq__(self, another:"Money"):
        return self.__amount == another.__amount

    def __ne__(self, another:"Money"):
        return self.__amount != another.__amount

    def __lt__(self, another:"Money"):
        return self.__amount < another.__amount

    def __gt__(self, another:"Money"):
        return self.__amount > another.__amount

    def __add__(self, another:"Money"):
        new_amount = float(self.__amount) + float(another.__amount)
        new_euros, new_cents = str(new_amount).split(".")
        if len(new_cents) == 1:
            new_cents = new_cents+"0" 
        new_amount_money = Money(new_euros, new_cents)
        return new_amount_money

    def __sub__(self, another:"Money"):
        new_amount = float(self.__amount) - float(another.__amount)
        if new_amount < 0 :
            raise ValueError("a negative result is not allowed")
        else:
            new_euros, new_cents = str(new_amount).split(".")
            new_amount_money = Money(new_euros, new_cents)
            return new_amount_money

    def __get_amount(self):
        self.__amount = 0
        if int(self.__cents) < 10:
            self.__cents = f"0{str(self.__cents)}"
        self.__amount = int(self.__euros) + float(f"0.{self.__cents}")
        self.__amount = format(self.__amount, '.2f' )
        return self.__amount

if __name__ == "__main__":
    # e1 = Money(4, 10)
    # e2 = Money(2, 5)  # two euros and five cents

    # print(e1)
    # print(e2)

    # e1 = Money(4, 10)
    # e2 = Money(2, 5)
    # e3 = Money(4, 10)

    # print(e1)
    # print(e2)
    # print(e3)
    # print(e1 == e2)
    # print(e1 == e3)

    # e1 = Money(4, 10)
    # e2 = Money(2, 5)

    # print(e1 != e2)
    # print(e1 < e2)
    # print(e1 > e2)

    # e1 = Money(4, 5)
    # e2 = Money(2, 95)

    # e3 = e1 + e2
    # e4 = e1 - e2

    # print(e3)
    # print(e4)

    # e5 = e2-e1

    # print(e1)
    # e1.euros = 1000
    # print(e1)

    money1 = Money(15, 95)
    money2 = Money(15, 95)
    print(money1 + money2)