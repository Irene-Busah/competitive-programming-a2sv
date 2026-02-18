"""
Practicing 2D arrays in Competitive Programming

| Pattern            | Formula           |
| ------------------ | ----------------- |
| Main diagonal      | i == j            |
| Secondary diagonal | i + j == n - 1    |
| Same main diagonal | i - j == constant |
| Same anti diagonal | i + j == constant |
| 1D → row           | (k-1)//m          |
| 1D → col           | (k-1)%m           |
| 2D → 1D            | i*m + j           |

The interceptor
"""

from operator import le
from traceback import print_tb
from typing import List


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]


# for i in range(len(matrix[0])):
#     for j in range(len(matrix)):
#         if i == j:
#             # print('Main Diagonal')
#             print(matrix[i][j])
#             # print()


# for i in range(len(matrix[0])):
#     for j in range(len(matrix)):
#         if i + j == len(matrix)-1:
#             # print('Anti-Diagonal')
#             print(matrix[i][j])


# for i in range(len(matrix[0])):
#     for j in range(len(matrix)):
#         if i - j == 1:
#             print(matrix[i][j])


# k = 6
# row = 0
# col = 0
# row = (k - 1) // len(matrix)
# col = (k - 1) % len(matrix)
# print((row, col))



"""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, 
switching the matrix's row and column indices.

Example 1:

Input: matrix = [
                    [1,2,3], = (0,0) (1, 0) (2, 0)
                               (0,1) (1, 1) (1, 2)
                               (0,2) (1, 2) (2, 2)
                    [4,5,6],
                    [7,8,9]
            ]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],
                [4,5,6]]
Output: [[1,4],[2,5],[3,6]]
"""



class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])

        new_matrix = [[0]*n for _ in range(m)]
        print(new_matrix)
        
        for i in range(n):
            for j in range(m):
                new_matrix[j][i] = matrix[i][j]
        
        return new_matrix
                

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.

#         matrix = [[1,2,3],
#                   [4,5,6],
#                   [7,8,9]]


#         [
#         [1, 4, 7], 
#         [2, 5, 8], 
#         [3, 6, 9]
#         ]

#         [x][y] -> [y][n-x]
#         i = 0, j = 1
#         """
#         n = len(matrix)
#         for i in range(n):
#             for j in range(i+1, n):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        

#         for i in range(n):
#             left, right = 0, n-1
#             while left < right:
#                 matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]

#                 left += 1
#                 right -= 1

#         print(matrix)

# if __name__ == '__main__':
#     matrix = [[1,2,3],[4,5,6],[7,8,9]]

#     # Output: [[7,4,1],[8,5,2],[9,6,3]]

#     Solution().rotate(matrix)




"""
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) 
where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
 

Example 1:

Input: nums = [3,1,2,2,2,1,3], k = 2
Output: 4
Explanation:
There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.
Example 2:

Input: nums = [1,2,3,4], k = 1
Output: 0
Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the 
requirements.
"""



# class Solution:
#     def countPairs(self, nums: List[int], k: int) -> int:


#         # set the counter
#         count = 0

#         # going through array
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if i < j and nums[i] == nums[j] and (i * j) % k == 0:
#                     count += 1

#         return count




"""
You are given a 0-indexed 2D integer array nums. Initially, your score is 0. 
Perform the following operations until the matrix becomes empty:

From each row in the matrix, select the largest number and remove it. 
In the case of a tie, it does not matter which number is chosen.
Identify the highest number amongst all those removed in step 1. Add that number to your score.
Return the final score.

 

Example 1:
==========
Input: nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
Output: 15
Explanation: In the first operation, we remove 7, 6, 6, and 3. We then add 7 to our score. 
Next, we remove 2, 4, 5, and 2. We add 5 to our score. Lastly, we remove 1, 2, 3, and 1. 
We add 3 to our score. Thus, our final score is 7 + 5 + 3 = 15.


Example 2:
==========
Input: nums = [[1]]
Output: 1
Explanation: We remove 1 and add it to the answer. We return 1.
"""

# class Solution:
#     def matrixSum(self, nums: List[List[int]]) -> int:
#         # storing the score

#         removedItems = []
        
#         while nums[0]:
#             roundMax = []
#             for i in range(len(nums)):
#                 nums[i].sort()
#                 maxValue = nums[i].pop()

#                 roundMax.append(maxValue)

#             removedItems.append(max(roundMax))
            
#         print(sum(removedItems))




"""
Given an n x n binary matrix image, flip the image horizontally, then invert it, 
and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
 

Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
"""


# class Solution:
#     def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
#         # j = 0
#         # while j < len(image):
#         for i in range(len(image)):
#             image[i].reverse()

#         for i in range(len(image)):
#             for j in range(len(image[i])):
#                 if image[i][j] == 0:
#                     image[i][j] = 1
#                 else:
#                     image[i][j] = 0
#         print(image)



"""
Given an m x n matrix, return all elements of the matrix in spiral order.


Example 1:
===========
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]


Example 2:
==========
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        res = []

        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # 3) bottom row
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            # 4) left col
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res 
        



if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]


    print(Solution().spiralOrder(matrix))
