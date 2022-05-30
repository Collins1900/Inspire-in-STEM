#!/usr/bin/python

#factorial
#method 1

n = input("enter number")
factorial = 1
if(int(n)<0):
    print("no factorial for negative number")
elif(int(n) == 0):
    print("factorial of 0 is equal to 1")
else:
    for n in range (1,int(n) + 1):
        factorial = factorial * int(n)
print("factorial of number is : " ,factorial)

#method 2

n = input("enter number")
factorial = 1
if(int(n)<0):
    print("no factorial for negative number")
elif(int(n) == 0):
    print("factorial for 0 is equal to 1")
else:
    for i in range (1,int(n) + 1):
        factorial = factorial * int(i)
print("factorial of number is : " , factorial)