class Solution(object):
    def setZeroes(self, matrix):
        #Brute force:
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == 0):
                    rows.append(i)
                    cols.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i in rows or j in cols):
                    matrix[i][j] = 0
        