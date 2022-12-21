class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def bfs(src):
            q = deque([src])
            color[src] = 0 
            while q:
                node = q.popleft()
                for ad in adj[node]:
                    if color[ad] == color[node]: 
                        return False
                    if color[ad] == -1:
                        color[ad] = 1 - color[node]
                        q.append(ad)
            
            return True
        
        adj = [[] for _ in range(n + 1)]
        for d in dislikes:
            adj[d[0]].append(d[1])
            adj[d[1]].append(d[0])
        
        color = [-1] * (n+1)
        for i in range(n+1):
            if color[i] == -1:
                if not bfs(i):
                    return False
        
        return True
                    
            
        