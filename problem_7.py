#Problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
#Answer: 104743

prime_list = []

x = 2

while len(prime_list) < 10001:
    for i in range(2,x):
        if (x%i) == 0:
            if (x/i) == 1:
                continue
            else:
                break
    else:
        prime_list.append(x)
    x+=1

print(prime_list[10000])
