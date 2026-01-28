"""
Task
=====
The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n , print i^2.

Example
n = 3
The list of non-negative integers that are less than n = 3 is [0, 1, 2]. Print the square of each number on a separate line.
0
1
4

Input Format
=============
The first and only line contains the integer, n.

Constraints
============
1 <= n <= 20


Output Format
==============
Print n lines, one corresponding to each i
"""


def pow(n: int):
    """
    Returns the square of all the numbers less than n
    
    :param n: the input number
    :type n: int
    """

    if n < 0:
        pass

    for i in range(n):
        print(i**2)



if __name__ == '__main__':
    n = 5
    pow(n)

