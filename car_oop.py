class Car:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.meter_reading = 2000

    def desc(self):
        full_desc = f"{self.year} {self.make} {self.model}"
        return full_desc.title()

    def read_meter(self):
        print(f"car has {self.meter_reading} miles on it")    

    def update_meter(self,milage):
        if milage >= self.meter_reading:
            self.meter_reading = milage
        else:
            tamper = self.meter_reading - milage
            print(f"car has been tampered with {tamper} miles")

    def update_miles(self, miles):
        self.meter_reading += miles


class Battery:
    def __init__(self,battery_size=40):
        self.battery_size = battery_size

    def desc_bat(self):
        print(f"Battery Size : {self.battery_size}")

    def upgrade_bat(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print(f"{self.battery_size}")
        else:
            print(f"{self.battery_size}")

    def range(self):
        if self.battery_size == 40:
            return 150
        elif self.battery_size == 65:
            return 225
        elif self.battery_size == 100:
            return 300

class Ecar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def range(self):
        return self.battery.range()

    def refill_tank(self):
        print(f"E cars don't have tanks")

tesla = Ecar('Tesla', 'model s', 2019)
print(tesla.desc())

# used_car = Car('Nissan','Skyline R34 GTR', '2002')
# print(used_car.desc())
# used_car.update_meter(23500)
# used_car.read_meter()

# new_car = Car('Toyota', 'Supra', '2005')
# print(new_car.desc())
# new_car.update_meter(2000)
# new_car.read_meter()
tesla.battery.desc_bat()
tesla.battery.upgrade_bat()
print(f"Car range: {tesla.range()} miles")
tesla.refill_tank()