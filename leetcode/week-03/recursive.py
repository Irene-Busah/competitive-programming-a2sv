from typing import List

"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
"""


# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 1 or n == 0:
#             return n
        
#         total = 0
#         for i in range(n):
#             total += i

#         return total


"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """

#         if len(s) == 0 or len(s) == 1:
#             return s

#         ans = self.reverseString(s[1:]) + [s[0]]

#         return ans



"""
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every 
subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and 
each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

 

Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        pass






if __name__ == '__main__':
    n = 1
    print(Solution().countGoodNumbers(n))

