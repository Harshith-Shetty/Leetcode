class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = defaultdict(set)
        stack = []
        visited = set()

        for i, j in edges:
            d[i].add(j)
            d[j].add(i)
            
        visited.add(source)
        stack.append(source)

        while stack:
            node = stack.pop(0)
            if node == destination: 
                return True

            for x in d[node]:
                if x not in visited:
                    visited.add(x)
                    stack.append(x)
        return False
        