class Car:
    wheels = 4

    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    # Method
    def drive(self):
        return f"the {self.model} is moving"

    def stop(self):
        return f'the {self.model} is stop'


my_car = Car(make='Kia', color='Blue', model='Morning')

print(my_car.make)

print(my_car.drive())
print(my_car.stop())
