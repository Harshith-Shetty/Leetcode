class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start = None  # to store starting point
        count = 0  
        for i in range(m):
            for j in range(n):
                count += grid[i][j] == 0
                if not start and grid[i][j] == 1:
                    start = (i, j)
        def backtrack(i: int, j: int) -> int:
            nonlocal count
            result = 0
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 0:
                        grid[x][y] = -1
                        count -= 1
                        result += backtrack(x, y)
                        grid[x][y] = 0
                        count += 1
                    elif grid[x][y] == 2:
                        result += count == 0
            return result
        return backtrack(start[0], start[1])