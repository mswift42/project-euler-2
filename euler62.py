#!/usr/bin/python
#-*- coding: utf-8 -*-

"""Cubic permutations
Problem 62

The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

cubedic = {}
def sortcube(n):
    return ''.join(sorted(str(n**3)))


for i in range(100,10000):
    if sortcube(i) in cubedic:
        cubedic[sortcube(i)].append(i)
    else:
        cubedic[sortcube(i)]=[i]

for i in cubedic:
    if len(cubedic[i])==5:
        smallest = min(cubedic[i])

print smallest ** 3

    





