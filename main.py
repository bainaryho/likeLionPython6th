class Engine:
    def start(self):
        return "Start"
    def stop(self):
        return "Stop"

class Wheels:
    def rotate(self):
        return "wheels are rotating"

#다중 상속
class Car(Engine, Wheels):
    pass

my_car = Car()
print(my_car.start())
print(my_car.rotate())