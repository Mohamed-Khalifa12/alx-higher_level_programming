#!/usr/bin/python3
def weight_average(my_list=[]):
    num, den = 0, 0
    for li in my_list:
        num += li[0] * li[1]
        den += li[1]
    return num/den
