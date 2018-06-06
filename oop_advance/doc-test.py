#!usr/bin/env/python3
# -*- coding: utf-8 -*-
# created_at: 2018/6/5

__author__ = 'IAPYANG'


def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    ?
    >>> fact(-1)
    ?
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()



