#!/usr/bin/python

########################
#      Classes
#      Name : Collins Murimi
#      Date : 18/5/2022
#########################

class person:
    def __init__(self,_name,_age):
        self.name=_name
        self.age=_age

    def sayHi(self): 
        print('Hello my name is '+self.name ,'and I am '+self.age + 'years old')
person1 = person('Bob',str(16))
person1.sayHi()

person2 = person('Sam',str(21))
person2.sayHi()


class Vehicle:
    def __init__(self,_max_speed,_mileage):   
        self.max_speed=_max_speed
        self.mileage=_mileage
    def sayHi(self):
        print('Vehicle has a speed of' + str(self.max_speed) + 'km/h and a mileage of' + str(self.mileage) + 'miles')
Toyota = Vehicle(100,25000)
Mercedes = Vehicle(150,6000)
Audi = Vehicle(200,78200)
Audi.sayHi()