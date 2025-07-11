# Write your solution here!
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, w):
        super().__init__(width = w, height = w)

    def __str__(self):
        return f"square {self.width}x{self.width}"

    def area(self):
        area = super().area()
        return self.width*self.width


if __name__ == "__main__":
    square = Square(4)
    print(square)
    print("area:", square.area())