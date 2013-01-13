#!/usr/bin/python
#-*- coding: utf-8 -*-

"""Square root convergents
Problem 57
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?"""

from fractions import Fraction as fr

count = 0
x = fr(3,2) 
y = fr(7,5)
for i in range(3,1000):
    temp = y
    new_number = fr(x.numerator+y.numerator + y.numerator, x.denominator + 2*y.denominator)
    x = temp
    y = new_number
    if len(str(x.numerator)) > len(str(x.denominator)) :
        count +=1
print count
    
    


     
    
    
