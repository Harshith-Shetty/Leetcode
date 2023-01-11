class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
        
        def dfs(node, parent):
            
            res = 0
            
            for child in tree[node]:
                if child != parent:
                    res += dfs(child,node)
        
            if hasApple[node] and node != 0:
                hasApple[parent] = True
                return res+2
            return res
            
        return dfs(0,0)