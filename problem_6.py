#Problem 6
#The sum of the squares of the first ten natural numbers is 385,
#The square of the sum of the first ten natural numbers is 3025,
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#Answer: 25164150

sum_of_sqr = 0
for x in range(1,101):
    sum_of_sqr += x**2

sqr_of_sum = 0
for x in range(1,101):
    sqr_of_sum += x
sqr_of_sum = sqr_of_sum**2

diff = sqr_of_sum - sum_of_sqr
print(diff)
