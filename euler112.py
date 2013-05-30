#!/usr/bin/python3
""" I only added a python version of my lisp solution because I wanted to see
    how much slower it would be. Lisp: 6 sec, Python3 45 sec."""


def number_to_list(number):
    """Convert int to list of its digits"""
    return [int(i) for i in str(number)]

def is_increasing(lst):
    """Check if numbers in lst are increasing.
    >>> is_increasing([2,4,3])
    False
    >>> is_increasing([2,3,4])
    True
    """
    return lst == sorted(lst)

def is_decreasing(lst):
    """ Check if numbers in lst are decreasing.
    >>> is_decreasing([3,2,1])
    True
    >>> is_decreasing([4,3,5])
    False
    """
    return lst == sorted(lst, reverse=True)

def is_bouncy(lst):
    """Return if lst is neither in nor decreasing.
    >>> is_bouncy([2,4,3])
    True
    >>> is_bouncy([3,4,5])
    False
    >>> is_bouncy([3,2,1])
    False
    """
    if not is_increasing(lst) and not is_decreasing(lst):
        return True
    return False

def euler_112():
    """return number when ratio of bouncy to non-bouncy
       numbers is 99 %.
    """
    sumbouncy = 0
    i = 0
    while True:
        i += 1
        if is_bouncy(number_to_list(i)):
            sumbouncy += 1
        if (sumbouncy * 100) // i == 99:
            return i

print(euler_112())


if __name__ == '__main__':
    import doctest
    doctest.testmod()


    
