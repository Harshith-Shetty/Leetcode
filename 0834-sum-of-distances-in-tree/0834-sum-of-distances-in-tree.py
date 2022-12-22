class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        d = {i:[1, 0] for i in range(n)}
        def dfs(root, prev):
            for x in g[root]:
                if  x!= prev:
                    dfs(x, root)
                    d[root][0] += d[x][0]
                    d[root][1] += (d[x][0] + d[x][1])
        def dfs2(root, prev):
            for x in g[root]:
                if x != prev:
                    d[x][1] = d[root][1] - d[x][0] + (n-d[x][0])
                    dfs2(x, root)
        dfs(0, -1)
        dfs2(0, -1)
        res = []
        for key in d:
            res.append(d[key][1])
        return res
        