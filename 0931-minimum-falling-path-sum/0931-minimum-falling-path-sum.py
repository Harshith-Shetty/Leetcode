class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])-1):
                matrix[i][j] = matrix[i][j] + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
            
            matrix[i][0] = matrix[i][0] + min(matrix[i-1][0], matrix[i-1][1])
            matrix[i][-1] = matrix[i][-1] + min(matrix[i-1][-2], matrix[i-1][-1])
            
        return min(matrix[-1])
        