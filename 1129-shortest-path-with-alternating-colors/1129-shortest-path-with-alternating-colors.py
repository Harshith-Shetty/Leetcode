class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        soln = [-1] * n
        for src, dst in redEdges:
            g[src].append((dst, 0))
        for src, dst in blueEdges:
            g[src].append((dst, 1))
        soln[0] = 0
        q = deque([(0, -1)])
        level = 0         
        visited = set()
        while q:
            levLen = len(q)
            for i in range(levLen):
                curr, color = q.popleft()
                if (curr, color) in visited:
                    continue
                visited.add((curr, color))
                if soln[curr] == -1:
                    soln[curr] = level
                for neigh, neighColor in g[curr]:
                    if color != neighColor:
                        q.append((neigh, neighColor))
            level += 1
        return soln