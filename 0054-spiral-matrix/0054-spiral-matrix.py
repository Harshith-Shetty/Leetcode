class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        result = []

        while(top <= bottom and left <= right):
            # move right
            for lr in range(left, right + 1):
                result.append(matrix[top][lr])
            top +=1
            
            # move bottom
            for tb in range(top, bottom + 1):
                result.append(matrix[tb][right])
            right -=1

            # move left
            if(top <= bottom):
                for rl in range(right, left - 1, -1):
                    result.append(matrix[bottom][rl])
                bottom -=1

            # move top
            if(left <= right):
                for bt in range(bottom,top - 1, -1):
                    result.append(matrix[bt][left])
                left +=1
        return result