# class Car:
#     total_cars = 0

#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#         Car.total_cars += 1

#     def __str__(self):
#         return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

#     def start_engine(self, number):
#         print(f"Engine started! {number}")
#         Car.total_cars += 1

#     def get_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

# class ElectricBattery:
#     def __init__(self, battery_size):
#         self.battery_size = battery_size

#     def __str__(self):
#         return f"Battery size {self.battery_size}"

#     def check_bat_life(self, num):
#         print(f"{num/100} %")


# class ElectricCar(Car,ElectricBattery):
#     def __init__(self, brand, model, year, battery_size):
#         super().__init__(brand, model, year)
#         self.battery_size = battery_size

#     def __str__(self):
#         return f"{super().__str__()} Battery: {self.battery_size}"
#         # return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Battery: {self.battery_size}"

#     def display_battery_size(self):
#         print(f"Battery size: {self.battery_size} kwh")

#     def get_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Battery: {self.battery_size}")


# my_car = Car("Toyota","Camry",2020)
# my_electric_car = ElectricCar("Tesla", "X", 2022, 75)

# print(my_electric_car)









# # my_car.get_info()
# # my_electric_car.get_info()

# # print(my_electric_car)
# # my_electric_car.display_battery_size()





# class Dog:
#     def __init__(self, breed, color, age, gender):
#         self.breed = breed
#         self.color = color
#         self.age = age
#         self.gender = gender

#     def __str__(self):
#         return f"Breed: {self.breed}, Color: {self.color}, Age: {self.age}, Gender: {self.gender}"

# datetime

# first = "Giorgi"
# second = "Bitcamp"

# print(first + second)
from datetime import date

date_now = date.today()
birth_year = date.fromisoformat('2004-08-28')


print((date_now - birth_year).days)
