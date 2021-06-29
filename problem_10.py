#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
#Answer: 142913828922

import numpy

prime_list = []

x = 2
while x < 2000000:
    for i in range(2,x):
        if (x%i) == 0:
            if x == i:
                continue
            else:
                break
    else:
        print(x)
        prime_list.append(x)
    x+=1

print(numpy.sum(prime_list))
