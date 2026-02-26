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

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         top, bottom = 0, len(matrix) - 1
#         left, right = 0, len(matrix[0]) - 1

#         res = []

#         while top <= bottom and left <= right:
#             for j in range(left, right + 1):
#                 res.append(matrix[top][j])
#             top += 1

#             for i in range(top, bottom + 1):
#                 res.append(matrix[i][right])
#             right -= 1

#             # 3) bottom row
#             if top <= bottom:
#                 for j in range(right, left - 1, -1):
#                     res.append(matrix[bottom][j])
#                 bottom -= 1

#             # 4) left col
#             if left <= right:
#                 for i in range(bottom, top - 1, -1):
#                     res.append(matrix[i][left])
#                 left += 1

#         return res 




"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to 
its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel 
around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, 
it is guaranteed to be unique.

 

Example 1:
==========
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.


Example 2:
==========
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""


# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         total_tank = 0
#         current_tank = 0
#         start = 0
#         for i in range(len(gas)):
#             total_tank += gas[i] - cost[i]
#             current_tank += gas[i] - cost[i]
#             if current_tank < 0:
#                 start = i + 1
#                 current_tank = 0
        
#         if total_tank < 0:
#             return -1
#         else:
#             return start




"""
You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, 
all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. 
After each query, you need to find the number of colors among the balls.

Return an array result of length n, where result[i] denotes the number of colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color.

 

Example 1:

Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]

Output: [1,2,2,3]

Explanation:



After query 0, ball 1 has color 4.
After query 1, ball 1 has color 4, and ball 2 has color 5.
After query 2, ball 1 has color 3, and ball 2 has color 5.
After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.
Example 2:

Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]

Output: [1,2,2,3,4]
"""


# class Solution:
#     def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
#         ballColor = {}  # maps ball -> color
#         colorCount = {}  # maps color -> count of balls with that color
#         result = []

#         for x, y in queries:
#             # If ball x already has a color, remove it from that color's count
#             if x in ballColor:
#                 oldColor = ballColor[x]
#                 colorCount[oldColor] -= 1
#                 if colorCount[oldColor] == 0:
#                     del colorCount[oldColor]
            
#             # Assign new color to ball x
#             ballColor[x] = y
#             colorCount[y] = colorCount.get(y, 0) + 1
            
#             # Number of distinct colors = size of colorCount
#             result.append(len(colorCount))
        
        

"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
"""


# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         if not mat or not mat[0]:
#             return []
    
#         m, n = len(mat), len(mat[0])
#         result = []

#         for d in range(m + n - 1):
#             diagonal = []

#             # Start row
#             r = 0 if d < n else d - n + 1
#             c = d if d < n else n - 1

#             while r < m and c >= 0:
#                 diagonal.append(mat[r][c])
#                 r += 1
#                 c -= 1

#             if d % 2 == 0:
#                 result.extend(diagonal[::-1])
#             else:
#                 result.extend(diagonal)

#         return result



# if __name__ == '__main__':
#     mat = [[1,2,3],[4,5,6],[7,8,9]]


#     print(Solution().findDiagonalOrder(mat))




# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

# def insertionSort1(n, arr):
#     # The last element is the "key" we need to insert into the
#     # sorted subarray arr[0..n-2]. We shift elements to the right
#     # one by one and print the array after each shift. Finally we
#     # place the key in its correct position and print the array one
#     # last time (as required by the problem).
    
#     key = arr[n-1]
#     i = n - 2
#     # shift elements greater than key to the right
#     while i >= 0 and arr[i] > key:
#         arr[i+1] = arr[i]
#         print(" ".join(str(x) for x in arr))
#         i -= 1
#     # place key in its final spot
#     arr[i+1] = key
#     print(" ".join(str(x) for x in arr))



"""
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

 

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
"""


# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # for i in range(len(heights)):
        #     for j in range(len(heights)-i-1):
        #         if heights[j] < heights[j+1]:
        #             names[j], names[j+1] = names[j+1], names[j]
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        # print(names)




"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements 
that do not appear in arr2 should be placed at the end of arr1 in ascending order.


Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
"""


# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         pass








if __name__ == '__main__':
    arr1 = [4, 1, 3, 9, 7]

    # names = ["Alice","Bob","Bob"]
    # heights = [155,185,150]

    Solution().selectionSort(arr1)