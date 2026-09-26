class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        top = 0
        bottom = n-1

        # vertical swap
        while top < bottom:
            for i in range(n):
                matrix[top][i], matrix[bottom][i] = matrix[bottom][i],  matrix[top][i]
            top += 1
            bottom -= 1
        
        # matrix tranpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
