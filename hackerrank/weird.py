"""
Task
=====
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format
=============
A single line containing a positive integer, n.

Constraints
============
1 <= n <= 100

Output Format
================
Print Weird if the number is weird. Otherwise, print Not Weird.
"""



def determine_weird(n: int):
    
    if (n % 2 != 0) or ((n % 2 == 0) and (6<= n <= 20)):
        print("Weird")
    elif ((n % 2 == 0) and (n > 20)) or ((2<=n<=5) and (n % 2 == 0)):
        print("Not Weird")



if __name__ == '__main__':
    determine_weird(3)
    determine_weird(24)

