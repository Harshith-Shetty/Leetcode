class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            j = 0
            while (j<i):
                a = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = a
                j+=1

        for i in range(n):
            j = 0
            while (j< n/2):
                b = matrix[i][j]
                matrix[i][j] = matrix[i][n-j-1]
                matrix[i][n-j-1] = b
                j+=1