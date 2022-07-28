class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for x in range(len(matrix)):
            for y in range(x, len(matrix[0]),1):
                matrix[x][y],matrix[y][x] = matrix[y][x],matrix[x][y]
        for i in range(len(matrix)):
            for j in range(0,int(len(matrix[0])/2),1):
                matrix[i][j],matrix[i][-1-j] = matrix[i][-1-j],matrix[i][j]
        return matrix
    
    
    
        