class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        matrix = [[1,2,3],[4,5,6],[7,8,9]]


        matrix[2][0]  
        matrix[2][1]
        matrix[2][2]
        """

        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        

        for i in range(n):
            left, right = 0, n-1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]

                left += 1
                right -= 1

        return matrix


        