class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        column = len(matrix[0])
        new_matrix = []
        for x in range(row):
            row_list = []
            for y in range (column):
                row_list.append(1)
            new_matrix.append(row_list)
        for i in range (row):
            for j in range (column):
                if(matrix[i][j] == 0):
                    new_matrix[i][j] = 0
        for i in range (row):
            for j in range (column):
                if(new_matrix[i][j] == 0):
                    for z in range (row):
                        matrix[z][j] = 0
                    for w in range (column):
                        matrix[i][w] = 0
        return matrix
                    
        