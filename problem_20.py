#n! means n × (n − 1) × ... × 3 × 2 × 1

#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!
#Answer: 648

import numpy as np

x = 100

num_list = []

while x > 0:
    num_list.append(x)
    x -= 1

current_product = num_list[0]
for i in num_list[1:]:
    current_product = current_product * i

prod_list = [int(x) for x in str(current_product)]
print(np.sum(prod_list))



