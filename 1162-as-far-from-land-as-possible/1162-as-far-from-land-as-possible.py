class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        dir = [(-1,0), (0,-1), (1,0), (0,1)]
        queue = []
        for i  in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    
        rows=len(grid)
        cols = len(grid[0])
                    
        if len(queue) == 0 or len(queue) == rows*cols:
            return -1
        dist = 0
        while queue:
            dist +=1
            for i in range(len(queue)):
                x,y = queue.pop(0)
                for dx,dy in dir:
                    if x+dx<0 or y+dy<0 or x+dx>=rows or y+dy>=cols or grid[x+dx][y+dy]>=1:
                        continue
                    grid[x+dx][y+dy] = dist
                    queue.append((x+dx,y+dy))
        return dist-1