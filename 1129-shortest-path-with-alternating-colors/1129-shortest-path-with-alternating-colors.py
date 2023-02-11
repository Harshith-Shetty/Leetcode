class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[], []] for i in range(n)]
        for startNode, endNode in redEdges: 
            graph[startNode][0].append(endNode)
        for startNode, endNode in blueEdges: 
            graph[startNode][1].append(endNode)
        res = [[0, 0]] + [[inf, inf] for i in range(n - 1)]
        bfsQueue = [[0, 0], [0, 1]]
        for node, color in bfsQueue:
            for neighbor in graph[node][color]:
                if res[neighbor][color] == inf:
                    res[neighbor][color] = res[node][1 - color] + 1
                    bfsQueue.append([neighbor, 1 - color])
        return [minPath if minPath < inf else -1 for minPath in map(min, res)]
    