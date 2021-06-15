class Square:
    def __init__(self):  # special method __init__
        self.sides = 4


square = Square()
print(square.sides)


class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand


# Note: you should not pass the self parameter explicitly, only the color parameter
car = Car("blue", "BMW")

print(car.color, car.brand)
