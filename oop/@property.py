class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"Width: {self._width:.1f}cm"

    @property
    def height(self):
        return f"Height: {self._height:.1f}cm"

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative.")
        self._width = value

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative.")
        self._height = value

    @width.deleter
    def width(self):
        del self._width
        print("Width attribute deleted.")

    @height.deleter
    def height(self):
        del self._height
        print("Height attribute deleted.")

    @property
    def area(self):
        return self._width * self._height


rectangle = Rectangle(5, 10)

print(rectangle.width)
print(rectangle.height)
print(rectangle.area)

del rectangle.width
del rectangle.height
