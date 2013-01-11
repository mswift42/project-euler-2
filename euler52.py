#!/usr/bin/python
#-*- coding: utf-8 -*-

"""Permuted multiples
Problem 52
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits."""



def get_sorted(number):
    return sorted([int(i) for i in str(number)])

x = 1

while True:
    if get_sorted(x) == get_sorted(2*x) == get_sorted(3*x) == get_sorted(4*x) == get_sorted(5*x) == get_sorted(6*x):
        print x
        break
    x +=1 









