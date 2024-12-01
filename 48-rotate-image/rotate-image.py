class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = list(zip(*mat))

        for i in range(len(mat)): mat[i] = matrix[i][::-1]