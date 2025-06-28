class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    
    #build in __init__ function that executes when class is initiated, assigns the attribute
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    ##prints the attributes
    def describe_car(self):
        print(self.year)
        print(self.make)
        print(self.model)

new_car = Car(make="Toyota", model="Corolla", year=2020)
new_car.describe_car()


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
