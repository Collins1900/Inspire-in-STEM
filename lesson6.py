#!/usr/bin/python



# Learning about lists
motocycles_owner = "Mojo Jojo"
plate_number = ['H1234','Y1234','S1234']
motocycles = ['honda', 'yamaha', 'suzuki']
#accessing list using index
#print(motocycles)
#motocycles[1] = "Bugatti"#changing element in a list
#print("I love" + str(motocycles[1]))
#adding element in a list
#motocycles.append('Bugatti','Yamaha')#append Item into a list
#print(motocycles[0],[1],[2])
#print(plate_number[0])
#print(motocycles[0],plate_number[0])
print(motocycles[0],plate_number[0])
print(motocycles[1],plate_number[1])
print(motocycles[2],plate_number[2])
#deleting an item from a list
#del motocycles[2] #deleting an item from a list
#print(motocycles)

popped_motocycles = motocycles.pop()
#print(motocycles) 
#task print a statement
#My name is Mojo Jojo and I own a motocycle plate number
print(f"My name is {motocycles_owner} and I own a {motocycles[0]} plate number{plate_number[0]}")

#removing an item from a list 
#motocycles.remove('honda')
#print(motocycles)



