class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class wheel:
    def __init__(self, size):
        self.size = size


class Car:
    def __init__(self, model, horsepower, wheel_size):
        self.model = model
        self.engine = Engine(horsepower)
        self.wheels = [wheel(wheel_size) for _ in range(4)]

    def display_info(self):
        print(f"Car Model: {self.model}")
        print(f"Engine Horsepower: {self.engine.horsepower}")
        print(f"Wheel Size: {self.wheels[0].size}")


car = Car("Sedan", 150, 16)

car.display_info()
