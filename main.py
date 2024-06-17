# class Human:
#     def __init__(self,name,dob,city_of_birth, sex):
#         self.name:str = name
#         self.dob: str = dob
#         self.city_of_birth: str = city_of_birth
#         self.sex: str = sex
#
#     def info(self):
#         print(self.name, self.dob, self.city_of_birth, self.sex)
#
# class Speels:
#     def __init__(self,name, damage, type_of_magic, active = False):
#         self.name:str = name
#         self.damage: int = damage
#         self.type_of_magic: str = type_of_magic
#         self.active = active
#
#     def attack(self):
#         print('*****', self.name.upper(), '*****')
#
#
# class Magician(Human): #в скобках класс который мы хотим наследовать
#     count = 0
#     def __init__(self, type, level, health, damage, name, dob, city_of_birth, sex):
#         super().__init__(name, dob, city_of_birth, sex) #обратились к родительскому классу с помощью super
#
#         self.type_of_spells: Speels = type
#         self.__level: int = level
#         self.health: int = health
#         self.damage: int = damage
#
#         Magician.count += 1
#
#     def healing(self, amount):
#         self.health += amount
#
#     def level_up(self):
#         self.__level += 1
#         self.health = self.__level * self.health
#         self.damage = self.__level * self.damage
#         print(f'LEVEL UP - {self.__level}')
#         print(f'HEALTH: {self.health}, DAMAGE: {self.damage}')
#
#     def level_info(self):
#         print(f'LEVEL INGO - {self.__level}')
#
# crystal_nova = Speels('crystal_nova', 110, 'Ice')
#
#
# crystal_maiden = Magician(type = crystal_nova, level = 15, health = 100, damage = 10, name = 'Crystal Maiden', dob = '18.05.2024', city_of_birth = 'Avalon', sex = 'F')
#
#
# crystal_maiden.level_up()
# crystal_maiden.info()
# crystal_maiden.type_of_spells.attack()
#
# class Vehicle:
#     def vehicle_method(self):
#         print("Vehicle class")
#
# class Car(Vehicle):
#     def car_method(self):
#         print("Car class")
#
# class Toyota(Car):
#     def toyota_method(self):
#         print("Toyota class")
#
# car_a = Toyota()
# car_a.vehicle_method()
