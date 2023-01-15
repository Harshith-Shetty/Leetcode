class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))
        n = len(vals)
        parents = list(range(n)); size = [1]*n
        def find(i): 
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]        
        goodPaths = n
        for a,b in edges:
            parent_a, parent_b = find(a), find(b)            
            if vals[parent_a] == vals[parent_b]:
                goodPaths += size[parent_a] * size[parent_b]
                parents[parent_a] = parent_b
                size[parent_b] += size[parent_a]
            elif vals[parent_a] > vals[parent_b]:
                parents[parent_b] = parent_a
            else:
                parents[parent_a] = parent_b
        return goodPaths