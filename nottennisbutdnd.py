import numpy as np
import random as random

#Problem: 
#In dnd your ability scores are determined by rolling four 6-sided dice and subtracting the smallest number. The aim here is to use different methods of determining the average score.


#1. Closed form solution

#Initialise matrix of all possible dice rolls, counter values (which will be used later) and a running average
A = np.zeros((1296, 4))
i1 = 1
i2 = 1
i3 = 1
i4 = 1

avg = 0

#Transforms the matrix in to one where every row represents a dice roll, starting with 1, 1, 1, 1, then 1, 1, 1, 2, etc., and ending with 6, 6, 6, 6.
#Each row has an equal probability of occuring and represents a discreet outcome. The "avg +=" in the for loop adds the contribution of the value of the roll in that row to the avg
#The values of i1, i2, i3 and i4 are then updated to be used by the next row.

for k in range(1296):

    A[k][3] = i1
    A[k][2] = i2
    A[k][1] = i3
    A[k][0] = i4

    avg += (A[k][3] + A[k][2] + A[k][1] + A[k][0] - A.min(1)[k]) /1296

    if i1 < 6:
        i1 += 1
    else:
        i1 = 1
        if i2 < 6:
            i2 += 1
        else:
            i2 = 1
            if i3 < 6:
                i3 += 1
            else:
                i3 = 1
                if i4 < 6:
                    i4 += 1

print(avg)


#2. Hacker statistics

total = 0
rolls = 10000

#Loop which rolls 4 dice "rolls" times, takes the sum of the 4 dice and discards the lowest one. Adds this number to the total

for m in range(rolls):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    d4 = random.randint(1, 6)
    stat = d1 + d2 + d3 + d4 - min(d1, d2, d3, d4)
    total += stat

#Takes the total of all the "rolls" dice rolls and then divices by the number of rolls to get the average
total = total/rolls

print(total)