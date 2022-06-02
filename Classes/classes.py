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