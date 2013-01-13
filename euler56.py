#!/usr/bin/python
#-*- coding: utf-8 -*-

"""Powerful digit sum
Problem 56
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b  100, what is the maximum digital sum?"""


def sum_digits(number):
    return sum([int(i) for i in str(number)])


max = 0

for i in range(10,100):
    for j in range(10,100):
        if sum_digits(pow(i,j)) > max:
            max = sum_digits(pow(i,j))
print max

