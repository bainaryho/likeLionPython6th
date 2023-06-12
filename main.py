class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return "the engine is running!"

class Car(Vehicle):
    def start_engine(self):
        return super().start_engine() + "It's a engine"

my_car = Car('도요타','Corolla',2020)

print(my_car.start_engine()) #the engine is running!It's a engine