#!/usr/bin/python

########################
#      Functions
#      Name : Collins Murimi
#      Date : 31/5/2022
#########################

#Function is a block of code

#defining a function
def say_hello():
    print("Hello from JKUAT")
    x=4
    y=7
    z=x+y
    print(z)
say_hello()

def bark():
    print("dogs bark woof woof")
bark()

def moow():
    print("cows moow")
moow()

def neighs():
    print("horse neighs")
neighs()

def slithers():
    print("snake slithers")
slithers()

# Function parameters
#Function to add 2 numbers
#initializing the function
def add_numbers(x,y):
    sum_nums=x+y
    print("the sum of numbers:",sum_nums)
#calling the function
add_numbers(40,50)
add_numbers(100,400)
add_numbers(1,4)
# function to get product of 2 numbers
def prod_numbers(x,y):
    prod_numbers = x*y
    print("the product of numbers:",prod_numbers)
#calling the function
prod_numbers(5,4)
prod_numbers(100,100)
prod_numbers(1,4)