"""Garage full of Classy Vehicles"""

class Vehicle:

    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4


    def drive(self):
        if self.gas > 0:
            self.gas -=1
            print('The {} {} goes VROOM!!'.format(self.color, self.manuf))

        else:
            print('The {} {} sputters out of gas'.format(self.color, self.manuf))


# class inheritance.
class Car(Vehicle):

    def radio(self):
        print("Rockiing to ITunes")

    def window(self):
        print('Fresh Air flowing in')

class Motorcycle(Vehicle):

    def helmet(self):
        print('helmet on .... safe now..')



my_car = Car('Blue', 'Mercedezs')

my_mc = Motorcycle('Kawasaki', 'Ninja')


for i in range(5):
    my_car.drive()

# methood override

class Ecar(Car):

    def drive(self):

        
        print('The {} {} goes shhhhhs!!'.format(self.color, self.manuf))




ele_car = Ecar('silver', 'Audi')

ele_car.drive()
ele_car.window()
ele_car.radio()
