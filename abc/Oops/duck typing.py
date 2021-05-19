#dynmaic typing - duck typing

#where the type or the class of an object is less important than the method it defines.

class Swift:
    def start(self):
        print("swift car starts")
    def accelerate(self):
        print("swift car accelerating functionality")
    def breaks(self):
        print("swift car break method")
    def stop(self):
        print("swift car stopping")

class Seltos:
    def start(self):
        print("seltos car starts")
    def accelerate(self):
        print("seltos car accelerating functionality")
    def breaks(self):
        print("seltos car break method")
    def stop(self):
        print("seltos car stopping")

class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.breaks()
        car.stop()
pe=Person()
sw=Swift()
pe.drive(sw)

#importance to functionality

