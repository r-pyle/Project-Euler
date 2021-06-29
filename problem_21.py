#Problem 21
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

#Answer: 31626

#Solution
import numpy as np

amicable_numbers = []

x = 6
while x < 10000:
    if x not in amicable_numbers:
        divisors_x = []
        i = 1
        while i < x:
            if x%i == 0:
                divisors_x.append(i)
            i += 1
        y = np.sum(divisors_x)
        divisors_y = []
        i = 1
        while i < y:
            if y%i == 0:
                divisors_y.append(i)
            i += 1
        z = np.sum(divisors_y)
        if x == z and x != y:
            print(x, y, z)
            amicable_numbers.append(x)
            amicable_numbers.append(y)
    x+=1
sum = np.sum(amicable_numbers)
print(sum)
