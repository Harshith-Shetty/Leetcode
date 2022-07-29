class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if(target<matrix[0][0] or target > matrix[-1][-1]):
            return False
        for x in range(len(matrix)):
            if(target <= matrix[x][-1]):
                for y in range(len(matrix[0])):
                    if(target == matrix[x][y]):
                        return True
        return False
        