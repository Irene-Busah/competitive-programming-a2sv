"""
Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

Examples:
=========

Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]


Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
Output: true
Explanation: b[] is a subset of a[]


Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
Output: false
Explanation: b[] is not a subset of a[]
"""


#User function Template for python3

from sre_constants import CHCODES
from tabnanny import check
from collections import Counter


class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        """
        Docstring for isSubset
        
        :param a: input list
        :param b: input list
        """


        # first, if length of b > length of a, return false
        if len(b) > len(a):
            return False
        
        # APPROACH 1
        # count_a = Counter(a)
        # count_b = Counter(b)

        # print(count_b)

        # for num in count_b:
        #     if count_b[num] > count_a[num]:
        #         return False
        
        # return True

        # APPROACH 2
        counter_a = {}
        counter_b = {}

        for num in a:
            if num in counter_a.keys():
                counter_a[num] += 1
            else:
                counter_a[num] = 1

        for num in b:
            if num in counter_b.keys():
                counter_b[num] += 1
            else:
                counter_b[num] = 1
        
        for val in counter_b:
            if counter_b[val] > counter_a[val]:
                return False
        
        return True
    
    
if __name__ == '__main__':
    # a = [11, 7, 1, 13, 21, 3, 7, 3]
    # b = [11, 3, 7, 1, 7]

    # a = [10, 5, 2, 23, 19]
    # b = [19, 5, 3]

    a = [1, 2, 2]
    b = [1, 1]
    print(Solution().isSubset(a, b))
