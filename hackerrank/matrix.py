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





if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    # matrix = [[1,2,3],[4,5,6]]

    print(Solution().transpose(matrix))
