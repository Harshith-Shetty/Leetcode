class Solution(object):
    def setZeroes(self, matrix):
        #optimal solution
        # use the 1st row and 1st colum as our indicator array.
        cols0 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] ==0):
                    matrix[i][0] = 0

                    if(j!=0):
                        matrix[0][j] = 0
                    else:
                        cols0 = 0
        for i in range(1, len(matrix)):
            for j in range(1,len(matrix[0])):
                if (matrix[0][j] == 0 or matrix[i][0] == 0):
                    matrix[i][j] = 0
        
        if (matrix[0][0] == 0):
            for j in range(len(matrix[i])):
                matrix[0][j] = 0
        
        if cols0 == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
