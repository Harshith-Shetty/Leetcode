class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        dict = {}
        for i in range(len(graph)):
            dict[i] = graph[i] 
        n = len(graph)
        arr = [(0, [0])] 
        output = []
        while arr:
            node, path = arr.pop()
            # check leaf
            if node == n - 1:
                output.append(path)
            for nei in dict[node]:
                arr.append((nei, path+[nei]))
        return output