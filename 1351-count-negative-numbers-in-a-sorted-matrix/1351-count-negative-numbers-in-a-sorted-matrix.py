class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if(grid):
            m = len(grid)
            n = len(grid[0])
        else:
            return 0
        count = 0
        for x in range(m):
            for y in range(n):
                if(grid[x][y]<0):
                    count+=1
        return count
                
            