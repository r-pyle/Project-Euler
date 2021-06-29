#Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#Answer: 232792560

x = 1

while x>0:
    for i in range(1,21):
        if (x%i) == 0:
            continue
        else:
            break
    else:
        print(x)
        break
    x+=1
