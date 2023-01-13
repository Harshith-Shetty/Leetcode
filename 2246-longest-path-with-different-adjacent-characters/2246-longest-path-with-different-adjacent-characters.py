class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        g = defaultdict(list)
        for i, u in enumerate(parent):
            g[u].append(i)
        self.ans = 0
        
        def dfs(root):
            a1 = a2 = 0
            for v in g[root]:
                if s[v] == s[root]:
                    dfs(v)
                    continue
                curr = dfs(v)
                if curr >= a1:
                    a2 = a1
                    a1 = curr
                elif curr >= a2:
                    a2 = curr
            self.ans = max(self.ans, a1 + a2 + 1)
            return a1 + 1
        dfs(0)        
        return self.ans