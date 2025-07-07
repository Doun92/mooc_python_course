# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length:int):
        if length < 0:
            raise ValueError("The lenght needs to be higher than 0.")
        else:
            self.__length = length

    #Getter
    @property
    def length(self):
        if self.__length < 0:
            raise ValueError("The lenght needs to be higher than 0.")
        else:
            return self.__length

    #Setter
    @length.setter
    def length(self, length):
        if length < 0:
            raise ValueError("The lenght needs to be higher than 0.")
        else:
            self.__length = length
            return self.__length

if __name__ == "__main__":
    # the_wall = Recording(43)
    the_wall = Recording(-1)
    # print(the_wall.length)
    # the_wall.length = 44
    # print(the_wall.length)