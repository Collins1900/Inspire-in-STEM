#!/usr/bin/python
 
 #####for loop#####
#print(range(0,20))

#for number in range(0,10):
    #print(number)

#for number in range(0,10):
    #print(number%2)
for number in range(0,10):
    if(number%2==0):
       print(number)

#sum of all odd numbers between 0 and 50
sum = 0
for number in range(0,50):
    sum = sum + number
#print(sum)

#sum of all even numbers between 0 and 50
sum = 0
for number in range(0,50):
    sum = sum + number
#print(sum)

#
sum_nums = 0
prod_nums = 1
sum
for number in range(0,20):
    if (number %2 == 0):
        sum_nums = sum_nums + number
#print(sum_nums)

#product of odd numbers between 0 and 50
for number in range(0,50):
    if (number %2 == 1): #odd numbers
        prod_nums = prod_nums + number
print(prod_nums)


num = 0
while num<10:
    #print(num)
    num = num + 1

num = 10
while num<20:
    #print(num)
    num = num + 2

    num = 10 
    while num < 10:
        if(num % 2 == 0):
          print(num)
        num = num + 1
