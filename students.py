#!/usr/bin/python

########################
#      
#      Name : Collins Murimi
#      Date : 7/6/2022
#########################

from unicodedata import name


class student:
    def__init__(self,name,hobby,year_of_birth):
        self.name=name
        self.hobby=hobby
        self.year_of_birth=year_of_birth
    def greet_student(self):
        print("Hello from " + self.name)