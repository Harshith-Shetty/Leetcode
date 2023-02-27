"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def is_same(grid, x, y, length):
            val = grid[x][y]
            for i in range(x, x+length):
                for j in range(y, y+length):
                    if val != grid[i][j]:
                        return False
            return True

        def solve(grid, x, y, length):
            if is_same(grid, x,y, length):
                return Node(grid[x][y], True)
            else:
                root = Node(None, False)
                root.topLeft = solve(grid, x, y, length//2)
                root.topRight = solve(grid, x, y+length//2, length//2)
                root.bottomLeft = solve(grid, x+length//2, y, length//2)
                root.bottomRight = solve(grid, x+length//2, y+length//2, length//2)
                return root
        return solve(grid, 0, 0, len(grid))