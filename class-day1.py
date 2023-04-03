# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self. age = age

#     def sit(self):
#         print(f"{self.name} is now sitting")

#     def roll_over(self):
#         print(f"{self.name} rolled over!")

# my_dog = Dog('regs', 2)
# my_dog.sit()
# my_dog.roll_over()
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")

# 2)
# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 100

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_descriptive_name(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

# my_used_car = Car('subaru', 'outback', 2016)
# print(my_used_car.get_descriptive_name)

# my_used_car.update_odometer(23_488)
# my_used_car.read_descriptive_name()

# my_used_car.increment_odometer(100)
# my_used_car.read_descriptive_name()




# Inheritance


# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 100

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_descriptive_name(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = 80
    
#     def descrip_battery(self):
#         print(self.battery_size)

# my_tesla = ElectricCar('tesla', 'model s', 2022)
# print(my_tesla.get_descriptive_name())
# my_tesla.descrip_battery()


