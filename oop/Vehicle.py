from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("The car is driving.")

    def stop(self):
        print("The car has stopped.")
        
class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motorcycle.")

    def stop(self):
        print("The motorcycle has stopped.")
        

# car=Car()
# car.go()
# car.stop()

motorcycle=Motorcycle()
motorcycle.go() 
motorcycle.stop()