class Solution(object):
    def setZeroes(self, matrix):
        # optimized solution

        rows = len(matrix)
        cols = len(matrix[0])
        firstRowsZero = False
        firstColZero = False

        for c in range(cols):
            if(matrix[0][c] == 0):
                firstRowsZero = True
        
        for r in range(rows):
            if(matrix[r][0] == 0):
                firstColZero = True

        for i in range(1,rows):
            for j in range(1, cols):
                if(matrix[i][j] == 0):
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1,rows):
            for j in range(1, cols):
                if(matrix[0][j] == 0 or matrix[i][0] == 0 ):
                    matrix[i][j] = 0

        if(firstRowsZero):
            for c in range(cols):
                matrix[0][c] = 0

        if(firstColZero):
            for r in range(rows):
                matrix[r][0] = 0


        