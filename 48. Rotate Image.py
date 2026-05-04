# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ndim = len(matrix)

        for i in range(ndim):
            for j in range(i+1, ndim):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(ndim):
            matrix[i].reverse()
        return matrix