#Problem 4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
#Answer: 906609

num = 0
for x in reversed(range(100,999)):
    for i in reversed(range(100,999)):
        num_test = str(x*i)
        if len(num_test) == 6:
            if num_test[:3] == num_test[:2:-1]:
                if (x*i) > num:
                    num = x*i
    else:
        continue
print(num)
