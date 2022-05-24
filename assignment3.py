#!/usr/bin/python

########################
#      Dictionaries
#      Name : Collins Murimi
#      Date : 24/5/2022
#########################

 # Write a program that gets user input and adds Ksh.10000 to her account if she is between 25-30 years 
  
age = input("Enter age")   
acc_bal = 0        

if (int(age) > 25) and (int(age) < 30):
    acc_bal = acc_bal + 1000
    print("Confirmed you have received Ksh.10000")
else:
    print("Sorry no money for you")



