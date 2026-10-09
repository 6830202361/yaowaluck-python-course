""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Vehicle info: \nBrand:{self.brand}, Model:{self.model}, Year: {self.year}"

class Car(Vehicle):

    def __init__(self, brand, model, year):
        number of (doors) :
        super() minite (brand, model, year)
        self.number_of_doors = number of doors

    def get_info(self):
        return f"Car info: \nBrand: {self.brand},
        Model: {self. mode134 Year: {self. year}, Number of doors: {self. number of doors}"
                
vehicle = Vehicle(“Toyota”, “Yaris”, “2025”)
print(vehicle.get_info0))

car = Car(“Honda”, “City”, “2020”, “5”)
print(car.get_info0))