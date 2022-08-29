class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        fresh_set=set()
        rotten = collections.deque()
        step = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y]==1:
                    fresh_set.add((x,y))
                elif grid[x][y]==2:
                    rotten.append([x,y,step])
        while rotten:
            x,y,step = rotten.popleft()
            for dx, dy in dirs:
                if 0<=x+dx<row and 0<=y+dy<col and grid[x+dx][y+dy] == 1:
                    grid[x+dx][y+dy]=2
                    fresh_set.remove((x+dx,y+dy))
                    rotten.append([x+dx,y+dy,step+1])
        return step if not fresh_set else -1