#write a function which allows a user to input two integers
#generate 6 random numbers between these values and sorts them in order of highest to lowest
#print

import random

integer_1 = int(input("Enter your first integer: "))
integer_2 = int(input("Enter your second integer: "))

num_range = range(integer_1, integer_2)

for i in num_range:
    num_range2 = random.randint(integer_1, integer_2)
    print(num_range2)

