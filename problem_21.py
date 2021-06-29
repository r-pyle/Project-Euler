import numpy

am_list = []
num = 220

while num < 221:
    sum_num = 0
    sum_num_2 = 0
    if num not in am_list:
        for i in range(1,num):
            if num % i == 0:
                sum_num += i
        for x in range(1,sum_num):
            if sum_num % x == 0:
                sum_num_2 += x
        if num == sum_num_2:
            am_list.append(num)
            am_list.append(sum_num)
        num+=1

print(numpy.sum(am_list))
