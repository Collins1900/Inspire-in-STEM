#!/usr/bin/python

########################
#      Quadratic equations
#      Name : Collins Murimi
#      Date : 31/5/2022
#########################

import math

a = int(input("Enter the coefficient of first term(a)"))
b = int(input("Enter the coefficient of second term(b)"))
c = int(input("Constant(c)"))

def find_roots(a,b,c):
    y1 =(-b+math.sqrt((b**2) - (4*a*c))) / (2*a)
    y2 =(-b-math.sqrt((b**2) - (4*a*c))) / (2*a)
    print("The roots of the quadratic equation are :" ,y1,y2)
find_roots(a,b,c)

#w = math.sqrt((b**2)-(4*c*2))
#def look_roots(a,b,c):
    #y1 = (-b+w)/(2*a)
    #y2 = (-b-w)/(2*a)
    #print("the roots of quadratic equation are:",y1,y2)
#look_roots(a,b,c)
 