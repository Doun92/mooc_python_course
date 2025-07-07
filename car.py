# WRITE YOUR SOLUTION HERE:
class Car():
    def __init__(self):
        self.__amount_petrol = 0
        self.__km = 0

    def __str__(self):
        return f"Car: odometer reading {self.__km} km, petrol remaining {self.__amount_petrol} litres"

    def fill_up(self):
        self.__amount_petrol = 60

    def drive(self, km:int):
        if self.__amount_petrol - km >= 0:
            self.__km += km
            self.__amount_petrol = self.__amount_petrol - km
        else:
            self.__km += self.__amount_petrol
            self.__amount_petrol = 0


if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)