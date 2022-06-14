#!/usr/bin/python

########################
#      Password Generator
#      Name : Collins Murimi
#      Date : 5/6/2022
#########################

import random

print("Welcome to our password generator")
character = 'student@001'
num_password = int(input("how many passwords do you want to generate?"))
len_password = int(input("what is the lengh of your password"))
print("\n Here are your passwords")
for password in range (num_password):
    password = ''
    for c in range (len_password):
        password+= random.choice(character)
    print(password)
