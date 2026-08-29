class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.filled = is_filled

    def describe(self):
        print(f"Shape: Color={self.color}, Filled={self.filled}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius


class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side


class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height


circle = Circle("red", True, 5)
print(f"Circle: Color={circle.color}, Filled={circle.filled}, Radius={circle.radius}")

circle.describe()

square = Square("blue", False, 10)
print(f"Square: Color={square.color}, Filled={square.filled}, Side={square.side}")
square.describe()


triangle = Triangle("green", True, 8, 6)
print(f"Triangle: Color={triangle.color}, Filled={triangle.filled}, Base={triangle.base}, Height={triangle.height}")
triangle.describe()


