import uuid

class ParkingLot:
    def __init__ (self, name, isAdmin = False):
        self.name = name
        self.isAdmin = isAdmin

class CarHandler(ParkingLot):
    def __init__(self, name):
        super.__init__(name)
        self.cars_in_lot = []

    def getCars(self, id, car_name, car_model):
        id = uuid.uuid1()
        car = Car(car_name, car_model, car_color, self)
        self.cars_in_lot.append(id, car)

class CarOwnner(ParkingLot):
    def __init__(self, name, car_name):
        super.__init__(name)
        self.car_name = car_name

class Car:
    def __init__(self, car_name, car_model, car_color, carOwnner):
        super.__init__(car_name)
        self.car_model = car_model
        self.car_color = car_color
        self.carOwnner = carOwnner