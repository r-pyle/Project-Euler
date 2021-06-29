#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


#How many such routes are there through a 20×20 grid?
#Answer: 137846528820

from math import factorial

m = 20
n = 20

print(factorial(m+n)//factorial(m)//factorial(n))
