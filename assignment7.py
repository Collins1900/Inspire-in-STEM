#!/usr/bin/python

########################
#      Program to write a number in reverse
#      Name : Collins Murimi
#      Date : 1/6/2022
#########################

num = int(input("enter number "))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))