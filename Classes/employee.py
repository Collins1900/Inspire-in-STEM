# Classes

class employee:
    def __init__(self,_name,_salary):
        self.name=_name
        self.salary=_salary
    def sayHi(self):
        print('Hello my name is' +str(self.name) +'and I earn' +str(self.salary) +'as my salary')
employee1 =employee ('John',str(1000000))
employee1.sayHi()

