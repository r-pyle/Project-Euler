#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#Answer: 6857

import math

x = 600851475143

large_num = 0
for i in reversed(range(2,int(round(math.sqrt(x),0))+1)):
    if (x%i) == 0:
        for y in range(2,i-1):
            if (i%y) == 0:
                break
        else:
            large_num = i
            break
    else:
        continue

print(large_num)
