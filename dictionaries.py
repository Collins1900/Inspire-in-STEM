#!/usr/bin/python

########################
#      Dictionaries
#      Name : Collins Murimi
#      Date : 25/5/2022
#########################

#A dictionary is a collection of key,value pair
#syntax: dictionary = {'key':'value'}
colors = {'color':'red'}
vehicle = {'type' : 'toyota','plate_number':'KYZ45'}
#print(type(colors))

#Acessing values in a dictionary
#print vehicle type and plate number
#print(vehicle['type']) # You can acess value of an element using a key 
#print(vehicle['type'], vehicle['plate_number'])

person = {'name':'Johnson','address':'Naivasha','gender':'male','phone':'1234576'}
person['age'] = '21'
print(type[person])
print(person)

del person['phone']
print(person)

#Looping over dictionaries
for key,value in person.items():
    print(f"{key} : {value}")

#Using get to acess the value in a dictionary
print(person.get['phone'])

